"""
Pipeline de procesamiento masivo para el análisis de huella hídrica municipal.
"""

import logging
from pathlib import Path

from seminario_ia.datasets import (
    get_ddr_code,
    get_nasa_power_data,
)
from seminario_ia.models import Crop, Region
from seminario_ia.utils import process_file_per_region_crop

import pandas as pd

# Configuración de logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Constantes
HEAT_THRESHOLD = 35.0
FROST_THRESHOLD = 5.0
OUTPUT_DIR = Path("data/processed/analisis_municipal")
YEARS_RANGE = "2010-2024"


def run_municipality_pipeline(
    region: Region, crops: dict[str, Crop], all_prod_data: pd.DataFrame, year_range: str
):
    """Procesa todos los cultivos para un municipio específico.

    Parámetros:
    - region: Region geográfica del municipio.
    - crops: Diccionario de cultivos disponibles.
    - all_prod_data: Datos de producción de todos los municipios.
    - year_range: Rango de años a procesar.

    Procesa cada cultivo y año, calculando las métricas de producción y clima.

    """

    mun_name = region.name

    # Cargar clima del municipio
    data_nasa = get_nasa_power_data(mun_name, year=YEARS_RANGE)
    if data_nasa.empty:
        logger.warning(f"Sin datos NASA POWER para {mun_name}")
        return

    results_list = []
    years_list = list(range(*map(int, year_range.split("-"))))

    for crop_name, crop_obj in crops.items():
        for year in years_list:
            # Filtramos producción para este municipio, cultivo y año
            prod_year = all_prod_data[
                (all_prod_data["Nommunicipio"] == mun_name)
                & (all_prod_data["Nomcultivo"] == crop_name)
                & (all_prod_data["Anio"] == year)
            ]

            if prod_year.empty:
                continue

            # Determinar fechas reales del ciclo
            # Si el cultivo termina en mes < inicio, significa que cruza el año
            start_dt = pd.Timestamp(
                year=year, month=crop_obj.start_month, day=crop_obj.start_day
            )
            if crop_obj.end_month < crop_obj.start_month:
                # Cruza el año. Si el año SIAP es el de cosecha, el inicio fue el año anterior.
                start_dt = start_dt - pd.DateOffset(years=1)
                end_dt = pd.Timestamp(
                    year=year, month=crop_obj.end_month, day=crop_obj.end_day
                )
            else:
                # Mismo año
                end_dt = pd.Timestamp(
                    year=year, month=crop_obj.end_month, day=crop_obj.end_day
                )

            # Filtramos clima para el rango del ciclo
            data_nasa_cycle = data_nasa[
                (data_nasa["Date"] >= start_dt) & (data_nasa["Date"] <= end_dt)
            ]

            if (
                data_nasa_cycle.empty or len(data_nasa_cycle) < 30
            ):  # Al menos un mes de datos
                # Intentar cargar datos extra
                if start_dt.year < 2010:
                    data_nasa_extra = get_nasa_power_data(mun_name, year=start_dt.year)
                    if not data_nasa_extra.empty:
                        data_nasa = (
                            pd.concat([data_nasa, data_nasa_extra])
                            .drop_duplicates()
                            .sort_values("Date")
                        )
                        data_nasa_cycle = data_nasa[
                            (data_nasa["Date"] >= start_dt)
                            & (data_nasa["Date"] <= end_dt)
                        ]

            if data_nasa_cycle.empty:
                logger.warning(
                    f"Sin clima para {mun_name} - {crop_name} - ciclo {start_dt.date()} a {end_dt.date()}"
                )
                continue

            # Procesar con el módulo de utils
            try:
                processed_daily = process_file_per_region_crop(
                    region, data_nasa_cycle, crop_obj, prod_year
                )
            except Exception as e:
                logger.error(f"Error procesando {mun_name} - {crop_name} - {year}: {e}")
                continue

            if processed_daily.empty:
                logger.warning(
                    f"Resultado vacío para {mun_name} - {crop_name} - {year}"
                )
                continue

            # Datos productivos
            rend = prod_year["Rendimiento"].iloc[0]
            sup_sem = prod_year["Sembrada"].iloc[0]
            sup_cos = prod_year["Cosechada"].iloc[0]
            vol_prod = prod_year["Volumenproduccion"].iloc[0]
            pmr = prod_year["PMR"].iloc[0]
            valor_prod = prod_year["Valorproduccion"].iloc[0]
            id_mun = int(prod_year["Idmunicipio"].iloc[0])
            id_ddr = int(prod_year["Idddr"].iloc[0])
            nom_ddr = get_ddr_code(id_ddr)

            # Estadísticas
            metrics = {
                # Datos region
                "Estado": "Sonora",
                "Municipio": mun_name,
                "IdMunicipio": id_mun,
                "DDR": nom_ddr,
                "IdDDR": id_ddr,
                "Cultivo": crop_name,
                "Anio": year,
                "AnioFin": year + 1,
                "Lat": region.latitude,
                "Lon": region.longitude,
                "Z_m": region.altitude,
                # ET0
                "ET0_total_mm": processed_daily["ET0"].sum(),
                "ET0_mean_mm_d": processed_daily["ET0"].mean(),
                "ET0_min_mm_d": processed_daily["ET0"].min(),
                "ET0_max_mm_d": processed_daily["ET0"].max(),
                # Tmean
                "Tmean_ciclo_mean_C": processed_daily["Tmean_"].mean(),
                "Tmean_ciclo_min_C": processed_daily["Tmean_"].min(),
                "Tmean_ciclo_max_C": processed_daily["Tmean_"].max(),
                # Tmax
                "Tmax_ciclo_mean_C": processed_daily["T_max"].mean(),
                "Tmax_ciclo_min_C": processed_daily["T_max"].min(),
                "Tmax_ciclo_max_C": processed_daily["T_max"].max(),
                # Tmin
                "Tmin_ciclo_mean_C": processed_daily["T_min"].mean(),
                "Tmin_ciclo_min_C": processed_daily["T_min"].min(),
                "Tmin_ciclo_max_C": processed_daily["T_min"].max(),
                # Humedad
                "RH_mean_pct": processed_daily["Rh"].mean(),
                "RH_min_pct": processed_daily["Rh"].min(),
                "RH_max_pct": processed_daily["Rh"].max(),
                # Radiación
                "Rs_mean_MJ_m2_d": processed_daily["Rs"].mean(),
                "Rs_min_MJ_m2_d": processed_daily["Rs"].min(),
                "Rs_max_MJ_m2_d": processed_daily["Rs"].max(),
                # Viento
                "Ws_mean_m_s": processed_daily["Ws"].mean(),
                "Ws_min_m_s": processed_daily["Ws"].min(),
                "Ws_max_m_s": processed_daily["Ws"].max(),
                # Precipitación
                "Ptot_total_mm": processed_daily["P_total"].sum(),
                "Ptot_mean_mm_d": processed_daily["P_total"].mean(),
                "Ptot_min_mm_d": processed_daily["P_total"].min(),
                "Ptot_max_mm_d": processed_daily["P_total"].max(),
                "Pef_total_mm": processed_daily["P_ef"].sum(),
                "Pef_mean_mm_d": processed_daily["P_ef"].mean(),
                "Pef_min_mm_d": processed_daily["P_ef"].min(),
                "Pef_max_mm_d": processed_daily["P_ef"].max(),
                # Radiación Neta
                "Rn_mean_MJ_m2_d": processed_daily["Rn_"].mean(),
                "Rn_min_MJ_m2_d": processed_daily["Rn_"].min(),
                "Rn_max_MJ_m2_d": processed_daily["Rn_"].max(),
                # Ratios y Días
                "ratio_Ptot_ET0": processed_daily["P_total"].sum()
                / processed_daily["ET0"].sum()
                if processed_daily["ET0"].sum() > 0
                else 0,
                "dias_lluvia_ge_1mm": (processed_daily["P_total"] >= 1.0).sum(),
                "dias_lluvia_ge_5mm": (processed_daily["P_total"] >= 5.0).sum(),
                "dias_estres_calor": (processed_daily["T_max"] >= HEAT_THRESHOLD).sum(),
                "dias_riesgo_helada": (
                    processed_daily["T_min"] <= FROST_THRESHOLD
                ).sum(),
                # Agua / ETc
                "ETc_total_mm": processed_daily["ETc"].sum(),
                "ETc_mean_mm_d": processed_daily["ETc"].mean(),
                "ETc_min_mm_d": processed_daily["ETc"].min(),
                "ETc_max_mm_d": processed_daily["ETc"].max(),
                "ETverde_total_mm": processed_daily["ET_v"].sum(),
                "ETverde_mean_mm_d": processed_daily["ET_v"].mean(),
                "ETverde_min_mm_d": processed_daily["ET_v"].min(),
                "ETverde_max_mm_d": processed_daily["ET_v"].max(),
                "ETazul_total_mm": processed_daily["ET_a"].sum(),
                "ETazul_mean_mm_d": processed_daily["ET_a"].mean(),
                "ETazul_min_mm_d": processed_daily["ET_a"].min(),
                "ETazul_max_mm_d": processed_daily["ET_a"].max(),
                "UACverde_m3_ha": processed_daily["UAC_v"].iloc[0],
                "UACazul_m3_ha": processed_daily["UAC_a"].iloc[0],
                "UACtotal_m3_ha": processed_daily["UAC_v"].iloc[0]
                + processed_daily["UAC_a"].iloc[0],
                "deficit_hidrico_mm": processed_daily["ETc"].sum()
                - processed_daily["P_ef"].sum(),
                "frac_verde": processed_daily["ET_v"].sum()
                / processed_daily["ETc"].sum()
                if processed_daily["ETc"].sum() > 0
                else 0,
                "frac_azul": processed_daily["ET_a"].sum()
                / processed_daily["ETc"].sum()
                if processed_daily["ETc"].sum() > 0
                else 0,
                # Productivos
                "Rend_t_ha": rend,
                "SupSembradaTotal_ha": sup_sem,
                "SupCosechadaTotal_ha": sup_cos,
                "VolumenTotal_t": vol_prod,
                "PMR": pmr,
                "Valorproduccion": valor_prod,
                # HH
                "HHverde_m3_ton": processed_daily["HH_v"].iloc[0],
                "HHazul_m3_ton": processed_daily["HH_a"].iloc[0],
                "HHtotal_m3_ton": processed_daily["HH_v"].iloc[0]
                + processed_daily["HH_a"].iloc[0],
            }
            results_list.append(metrics)

    if results_list:
        df_final = pd.DataFrame(results_list)
        safe_name = mun_name.replace(" ", "_")
        output_path = OUTPUT_DIR / f"{safe_name}_{year_range.replace('-', '_')}.csv"
        df_final.to_csv(output_path, index=False, encoding="utf-8")
        logger.info(f"Guardado: {output_path}")


def consolidate_results():
    """Consolida todos los archivos municipales en uno solo."""
    all_files = list(OUTPUT_DIR.glob("*.csv"))
    if not all_files:
        logger.error("No hay archivos para consolidar.")
        return

    logger.info(f"Consolidando {len(all_files)} archivos...")
    df_master = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)

    master_path = Path("data/processed/analisis_municipal_sonora_2010_2024.csv")
    df_master.to_csv(master_path, index=False, encoding="utf-8")
    logger.info(f"Maestro guardado en: {master_path}")


if __name__ == "__main__":
    print()
