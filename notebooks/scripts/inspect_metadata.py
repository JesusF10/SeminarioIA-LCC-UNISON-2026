import geopandas as gpd
import pandas as pd
import os

def inspect_technical_metadata():
    report = []
    
    # 1. Inspección de Shapefile de Sequía
    shp_path = "data/raw/datos-sequia/impacto_sequia.shp"
    if os.path.exists(shp_path):
        gdf = gpd.read_file(shp_path)
        report.append("--- SHAPEFILE SEQUIA ---")
        report.append(f"Columnas: {', '.join(gdf.columns.tolist())}")
        report.append(f"CRS (Proyección): {gdf.crs}")
    
    # 2. Inspección de Diccionario SIAP (Excel)
    dic_siap = "data/raw/siap-produccion-agricola/municipal/Diccionario_agricola_2003_a_2023.xlsx"
    if os.path.exists(dic_siap):
        df_dic = pd.read_excel(dic_siap)
        report.append("\n--- DICCIONARIO SIAP ---")
        # Mostrar solo los nombres de columnas presentes
        report.append(f"Variables SIAP: {', '.join(df_dic.iloc[:, 0].dropna().astype(str).tolist()[:15])}")
    
    # 3. Inspección de Catálogo hídrico
    cat_hidro = "data/raw/datos-abiertos/recursos-hidricos/Catalogo.xlsx"
    if os.path.exists(cat_hidro):
        df_cat = pd.read_excel(cat_hidro)
        report.append("\n--- CATALOGO HIDRICO ---")
        report.append(f"Columnas hidricas: {', '.join(df_cat.columns.tolist())}")

    with open("notebooks/scripts/metadata_audit.txt", "w") as f:
        f.write("\n".join(report))

if __name__ == "__main__":
    inspect_technical_metadata()
