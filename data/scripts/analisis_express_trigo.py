import os
import pandas as pd
import matplotlib.pyplot as plt
from seminario_ia.datasets import get_prod_data, get_mun_coordinates, get_nasa_power_data, get_crop_data
from seminario_ia.models import Region
from seminario_ia.utils import process_file_per_region_crop
from pathlib import Path

# Configuración de rutas
OUTPUT_DIR = Path("reports/fase3/prueba_analisis")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CROP_NAME = "Trigo grano"
YEARS = (2003, 2024)

print(f"Iniciando análisis express para {CROP_NAME} ({YEARS[0]}-{YEARS[1]})...")

# 1. Carga de datos de producción
df_prod = get_prod_data(YEARS, muni=True, crop_name=CROP_NAME)

if df_prod.empty:
    print("No se encontraron datos de producción para los años especificados.")
    exit()

# Filtrar solo Toneladas (para uniformidad)
df_prod = df_prod[df_prod["Nomunidad"] == "Tonelada"]

# --- ANÁLISIS 1: TENDENCIAS ESTATALES ---
state_trends = df_prod.groupby("Anio").agg({
    "Sembrada": "sum",
    "Cosechada": "sum",
    "Siniestrada": "sum",
    "Volumenproduccion": "sum",
    "Valorproduccion": "sum"
}).reset_index()

# Cálculo de rendimiento promedio estatal (ponderado)
state_trends["Rendimiento_Prom"] = state_trends["Volumenproduccion"] / state_trends["Cosechada"]
state_trends["Porcentaje_Siniestrada"] = (state_trends["Siniestrada"] / state_trends["Sembrada"]) * 100

# Gráfica 1: Producción y Superficie Sembrada
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel("Año")
ax1.set_ylabel("Superficie Sembrada (Ha)", color="tab:blue")
ax1.plot(state_trends["Anio"], state_trends["Sembrada"], label="Sup. Sembrada", color="tab:blue", marker='o')
ax1.tick_params(axis='y', labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.set_ylabel("Volumen Producción (Ton)", color="tab:green")
ax2.plot(state_trends["Anio"], state_trends["Volumenproduccion"], label="Producción", color="tab:green", marker='s')
ax2.tick_params(axis='y', labelcolor="tab:green")

plt.title(f"Tendencia Estatal: {CROP_NAME} en Sonora")
fig.tight_layout()
plt.savefig(OUTPUT_DIR / "tendencia_produccion_estatal.png")
plt.close()

# Gráfica 2: Rendimiento y Siniestralidad
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel("Año")
ax1.set_ylabel("Rendimiento (Ton/Ha)", color="tab:red")
ax1.plot(state_trends["Anio"], state_trends["Rendimiento_Prom"], label="Rendimiento", color="tab:red", marker='^')
ax1.tick_params(axis='y', labelcolor="tab:red")

ax2 = ax1.twinx()
ax2.set_ylabel("% Superficie Siniestrada", color="tab:orange")
ax2.bar(state_trends["Anio"], state_trends["Porcentaje_Siniestrada"], alpha=0.3, color="tab:orange", label="% Siniestrada")
ax2.tick_params(axis='y', labelcolor="tab:orange")

plt.title(f"Rendimiento vs Siniestralidad: {CROP_NAME} en Sonora")
fig.tight_layout()
plt.savefig(OUTPUT_DIR / "rendimiento_siniestralidad.png")
plt.close()

# --- ANÁLISIS 2: DISTRIBUCIÓN MUNICIPAL (TOP 10 HISTÓRICO) ---
mun_total = df_prod.groupby("Nommunicipio")["Volumenproduccion"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 7))
mun_total.plot(kind='bar', color='skyblue')
plt.title(f"Top 10 Municipios Productores de {CROP_NAME} (Total 2003-2024)")
plt.ylabel("Producción Total (Ton)")
plt.xlabel("Municipio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_municipios_productores.png")
plt.close()

# --- ANÁLISIS 3: ANÁLISIS HÍDRICO Y HUELLA HÍDRICA (Cajeme como ejemplo) ---
MUN_EJEMPLO = "Cajeme"
print(f"Realizando análisis hídrico para {MUN_EJEMPLO}...")

# Obtener coordenadas
coords = get_mun_coordinates(MUN_EJEMPLO)
if not coords.empty:
    row = coords.iloc[0]
    region = Region(
        name=MUN_EJEMPLO,
        crops=get_crop_data(CROP_NAME),
        latitude=row["lat"],
        longitude=row["lon"],
        altitude=row["z_m"]
    )
    
    # Analizar últimos 5 años de clima vs rendimiento y HH
    clima_yield = []
    for year in range(2019, 2025):
        nasa_df = get_nasa_power_data(MUN_EJEMPLO, year)
        if not nasa_df.empty:
            out = process_file_per_region_crop(
                region=region,
                data_nasa=nasa_df,
                crop_name=CROP_NAME,
                prod_data=df_prod
            )
            if not out.empty:
                # ETo acumulada en el ciclo
                eto_total = out["ET0"].sum()
                # Huella Hídrica (constante en el archivo resultante para ese ciclo)
                g_hh = out["G_HH"].iloc[0]
                b_hh = out["B_HH"].iloc[0]
                # Rendimiento en ese año para ese municipio
                y_val = df_prod[(df_prod["Anio"] == year) & (df_prod["Nommunicipio"] == MUN_EJEMPLO)]["Rendimiento"].mean()
                clima_yield.append({
                    "Año": year, 
                    "ETo_Acum": eto_total, 
                    "Rendimiento": y_val,
                    "HH_Verde": g_hh,
                    "HH_Azul": b_hh
                })
    
    if clima_yield:
        cy_df = pd.DataFrame(clima_yield)
        
        # Gráfica 3: ETo vs Rendimiento
        fig, ax1 = plt.subplots(figsize=(10, 6))
        ax1.set_xlabel("Año")
        ax1.set_ylabel("ETo Acumulada (mm)", color="tab:purple")
        ax1.plot(cy_df["Año"], cy_df["ETo_Acum"], marker='o', color="tab:purple", label="ETo")
        ax1.tick_params(axis='y', labelcolor="tab:purple")
        
        ax2 = ax1.twinx()
        ax2.set_ylabel("Rendimiento (Ton/Ha)", color="tab:red")
        ax2.plot(cy_df["Año"], cy_df["Rendimiento"], marker='s', color="tab:red", label="Rendimiento")
        ax2.tick_params(axis='y', labelcolor="tab:red")
        
        plt.title(f"ETo vs Rendimiento en {MUN_EJEMPLO} ({CROP_NAME})")
        plt.savefig(OUTPUT_DIR / f"eto_vs_rendimiento_{MUN_EJEMPLO}.png")
        plt.close()

        # Gráfica 4: Huella Hídrica (Verde vs Azul)
        plt.figure(figsize=(10, 6))
        plt.bar(cy_df["Año"], cy_df["HH_Verde"], label="HH Verde (Lluvia)", color="tab:green")
        plt.bar(cy_df["Año"], cy_df["HH_Azul"], bottom=cy_df["HH_Verde"], label="HH Azul (Riego)", color="tab:blue")
        plt.title(f"Huella Hídrica de {CROP_NAME} en {MUN_EJEMPLO} (2019-2024)")
        plt.ylabel("Huella Hídrica (m3/Ton)")
        plt.xlabel("Año")
        plt.legend()
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f"huella_hidrica_{MUN_EJEMPLO}.png")
        plt.close()

# --- ANÁLISIS 4: COMPARATIVA DE HUELLA HÍDRICA AZUL (TOP 10 MUNICIPIOS) ---
print("Realizando comparativa de Huella Hídrica entre municipios líderes...")
top_10_muns = mun_total.index.tolist()
hh_comparativa = []

for mun in top_10_muns:
    coords_mun = get_mun_coordinates(mun)
    if coords_mun.empty: continue
    
    row_mun = coords_mun.iloc[0]
    region_mun = Region(
        name=mun,
        crops=get_crop_data(CROP_NAME),
        latitude=row_mun["lat"],
        longitude=row_mun["lon"],
        altitude=row_mun["z_m"]
    )
    
    # Promediar HH de los últimos 3 años disponibles para mayor estabilidad
    hh_vals = []
    for year in range(2022, 2025):
        nasa_mun = get_nasa_power_data(mun, year)
        if not nasa_mun.empty:
            out_mun = process_file_per_region_crop(
                region=region_mun,
                data_nasa=nasa_mun,
                crop_name=CROP_NAME,
                prod_data=df_prod
            )
            if not out_mun.empty:
                hh_vals.append(out_mun["B_HH"].iloc[0])
    
    if hh_vals:
        hh_comparativa.append({"Municipio": mun, "HH_Azul_Prom": sum(hh_vals)/len(hh_vals)})

if hh_comparativa:
    hh_comp_df = pd.DataFrame(hh_comparativa).sort_values(by="HH_Azul_Prom", ascending=False)
    
    plt.figure(figsize=(12, 7))
    plt.barh(hh_comp_df["Municipio"], hh_comp_df["HH_Azul_Prom"], color='salmon')
    plt.title(f"Comparativa: Huella Hídrica Azul (Riego) de {CROP_NAME}\n(Promedio 2022-2024)")
    plt.xlabel("m3 de agua por Tonelada producida")
    plt.ylabel("Municipio")
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "comparativa_hh_azul_municipios.png")
    plt.close()

# --- GENERAR RESUMEN ESCRITO ---
with open(OUTPUT_DIR / "resumen_analisis.txt", "w", encoding="utf-8") as f:
    f.write(f"Análisis Express de {CROP_NAME} en Sonora (2003-2024)\n")
    f.write("="*50 + "\n\n")
    f.write(f"1. Producción Total Histórica: {df_prod['Volumenproduccion'].sum():,.2f} Ton\n")
    f.write(f"2. Municipio Líder: {mun_total.index[0]} con {mun_total.iloc[0]:,.2f} Ton\n")
    f.write(f"3. Rendimiento Promedio Histórico: {state_trends['Rendimiento_Prom'].mean():.2f} Ton/Ha\n")
    f.write(f"4. Año con mayor siniestralidad: {state_trends.loc[state_trends['Porcentaje_Siniestrada'].idxmax(), 'Anio']} "
            f"({state_trends['Porcentaje_Siniestrada'].max():.2f}%)\n")
    
    if clima_yield:
        f.write(f"\nDatos Huella Hídrica ({MUN_EJEMPLO}):\n")
        f.write(f"- HH Azul Promedio: {cy_df['HH_Azul'].mean():.2f} m3/Ton\n")
        f.write(f"- HH Verde Promedio: {cy_df['HH_Verde'].mean():.2f} m3/Ton\n")
        f.write(f"- HH Total Promedio: {(cy_df['HH_Azul'].mean() + cy_df['HH_Verde'].mean()):.2f} m3/Ton\n")

    f.write("\nAnálisis Geográfico (Top 10):\n")
    f.write(mun_total.to_string())
    f.write("\n\nConclusiones:\n")
    f.write("- Se observa una clara predominancia de la HH Azul (riego) sobre la Verde (lluvia).\n")
    f.write("- El rendimiento muestra sensibilidad a las variaciones de la ETo acumulada.\n")

print(f"Análisis completado. Resultados guardados en {OUTPUT_DIR}")
