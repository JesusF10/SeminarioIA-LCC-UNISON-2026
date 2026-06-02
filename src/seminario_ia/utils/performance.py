"""
Funciones para calcular la curva de Kc diaria, Pef diario, rendimiento, UAC y HH.
"""

from seminario_ia.models import Crop, Region

from .eto import eto_fao56_mm

import numpy as np
import pandas as pd


def daily_kc_curve(
    fechas_idx: pd.Index,
    kc_ini: float,
    kc_mid: float,
    kc_end: float,
    dur,  # (d_ini, d_des, d_mid, d_fin)
    endpoint_rampas: bool = True,  # se mantiene por compatibilidad, no se usa
) -> pd.Series:
    """
    Calcula la curva de Kc diaria a partir de los parámetros dados.

    Versión con ASIGNACIÓN POR FASE (sin rampas):
      - Inicio: kc_ini (constante)
      - Desarrollo: kc_mid (constante)  ← se permiten saltos
      - Media: kc_mid (constante)
      - Final: kc_end (constante)

    Parámetros:
    - fechas_idx: Índice de fechas para el ciclo completo.
    - kc_ini: Kc al inicio del ciclo (constante).
    - kc_mid: Kc en la fase media del ciclo (constante).
    - kc_end: Kc al final del ciclo (constante).
    - dur: Tupla con la duración (en días) de cada fase: (d_ini, d_des, d_mid, d_fin).
    - endpoint_rampas: Si True, se generan rampas lineales entre fases; si False, se asignan
        valores constantes por fase con saltos entre ellas.

    Regresa:
    - Serie de Kc diario con el mismo índice que fechas_idx.
    """
    d_ini, d_des, d_mid, d_fin = dur
    n = len(fechas_idx)

    kc_ini_arr = np.full(d_ini, kc_ini)
    kc_des_arr = np.full(d_des, kc_mid)  # salto kc_ini -> kc_mid
    kc_mid_arr = np.full(d_mid, kc_mid)
    kc_fin_arr = np.full(d_fin, kc_end)  # salto kc_mid -> kc_end

    kc_full = np.concatenate([kc_ini_arr, kc_des_arr, kc_mid_arr, kc_fin_arr])

    # Ajuste a la longitud disponible
    if len(kc_full) >= n:
        kc_full = kc_full[:n]
    else:
        kc_full = np.concatenate([kc_full, np.full(n - len(kc_full), kc_end)])

    return pd.Series(kc_full, index=fechas_idx, name="Kc_")


def calculate_daily_simple_efp(ptot_series_mm: pd.Series) -> pd.Series:
    """
    Calcula el Pef diario a partir de la precipitación total (Ptotal) usando una regla simple basada en FAO-56:
        FAO simple: Pef = f * Ptotal.
        f = 0.8 si Ptotal < 250 mm; f = 0.6 si no.
        Se aplica el mismo factor f a cada día.

    Parámetros:
        - ptot_series_mm: Serie de precipitación total (mm) por día.

    Regresa:
        - Serie de Pef diario (mm) con el mismo índice que ptot_series_mm.
    """
    ptotal = ptot_series_mm.fillna(0).sum()
    f = 0.8 if ptotal < 250.0 else 0.6
    return ptot_series_mm.fillna(0) * f  # Pef_ diario


def calculate_performance_per_file(
    df: pd.DataFrame, region: str, prod_df: pd.DataFrame, crop: str
) -> dict[int, float]:
    """
    Obtiene un diccionario {año: rendimiento_ton_ha} para los años presentes
    en el archivo usando la tabla de producción municipal (prod_df).
    """
    years = df["Date"].dt.year.unique()
    rend_map = {}

    for y in years:
        sel = prod_df[
            (prod_df["Anio"] == y)
            & (prod_df["Nommunicipio"].astype(str).str.strip() == region)
            & (prod_df["Nomcultivo"] == crop)
        ]

        if not sel.empty:
            r_mean = float(sel["Rendimiento"].astype(float).mean())
            rend_map[y] = r_mean

    return rend_map


def calculate_wf_wc(
    green_et_series_mm: pd.Series,
    blue_et_series_mm: pd.Series,
    performance_ton_ha: float,
) -> dict:
    """
    Calcula:
      - ETverde_total_mm, ETazul_total_mm
      - UACverde_m3_ha, UACazul_m3_ha
      - HHverde_m3_ton, HHazul_m3_ton
    Convenciones:
      - 1 mm sobre 1 ha = 10 m3  => UAC = sum(ET) * 10
      - HH = UAC / rendimiento(ton/ha)
    Si no hay rendimiento válido (>0), HH = NaN.

    Parametros:
        - green_et_series_mm: Serie de ET verde diario (mm).
        - blue_et_series_mm: Serie de ET azul diario (mm).
        - performance_ton_ha: Rendimiento en toneladas por hectárea (ton/ha).

    Regresa:
        Diccionario con las métricas calculadas:
        {
            "ETverde_total_mm": ...,
            "ETazul_total_mm": ...,
            "UACverde_m3_ha": ...,
            "UACazul_m3_ha": ...,
            "HHverde_m3_ton": ...,
            "HHazul_m3_ton": ...,
        }
    """
    total_green_et_mm = float(pd.Series(green_et_series_mm).fillna(0).sum())
    total_blue_et_mm = float(pd.Series(blue_et_series_mm).fillna(0).sum())

    green_uac_m3_ha = total_green_et_mm * 10.0
    blue_uac_m3_ha = total_blue_et_mm * 10.0

    if (performance_ton_ha is not None) and (performance_ton_ha > 0):
        green_wf_m3_ton = green_uac_m3_ha / performance_ton_ha
        blue_wf_m3_ton = blue_uac_m3_ha / performance_ton_ha
        # HH =  UAC / rendimiento(ton/ha)
    else:
        green_wf_m3_ton = float("nan")
        blue_wf_m3_ton = float("nan")

    return {
        "ETverde_total_mm": total_green_et_mm,
        "ETazul_total_mm": total_blue_et_mm,
        "UACverde_m3_ha": green_uac_m3_ha,
        "UACazul_m3_ha": blue_uac_m3_ha,
        "HHverde_m3_ton": green_wf_m3_ton,
        "HHazul_m3_ton": blue_wf_m3_ton,
    }


def calculate_decades_per_cycle(idx: pd.Index) -> pd.Series:
    """
    Calcula las décadas relativas al ciclo (no calendario) a partir de un índice de fechas.
    Cada década corresponde a un bloque de 10 días consecutivos, comenzando desde el inicio del
    ciclo (día 1-10 = década 1, día 11-20 = década 2, etc.). El resultado es una Serie con el
    mismo índice que idx y valores enteros indicando la década correspondiente a cada fecha.

    Parametros:
        - idx: Índice de fechas o posiciones (pd.Index) para el ciclo completo.

    Regresa:
        - pd.Series de enteros indicando la década relativa al ciclo para cada fecha en idx.
    """
    n = len(idx)
    dec = np.ceil((np.arange(1, n + 1)) / 10.0).astype(int)
    return pd.Series(dec, index=idx, name="decada_")


def process_file_per_region_crop(
    region: Region,
    data_nasa: pd.DataFrame,
    crop_name: str | Crop,
    prod_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Procesa un archivo de datos de Nasa para una región y cultivo específicos, calculando
    el rendimiento y agregando las estadísticas de ET0 y UAC/HH por década.

    Parámetros:
        - region: Región geográfica (Region).
        - data_nasa: Datos de Nasa para la región (pd.DataFrame).
        - crop_name: Nombre del cultivo (str) o objeto Crop.
        - prod_data: Datos de producción (pd.DataFrame).

    Regresa:
        - pd.DataFrame con las estadísticas de rendimiento y ET0/UAC/HH por década.
    """

    # Obtener informacion del cultivo:
    if isinstance(crop_name, str):
        from seminario_ia.datasets import get_crop_data

        crop_obj = get_crop_data(crop_name)
    else:
        crop_obj = crop_name
        crop_name = crop_obj.name

    assert isinstance(crop_obj, Crop), "No se procesa un solo cultivo, sino varios."

    kc = crop_obj.kc
    dur = crop_obj.durations

    # --- Rendimiento (ton/ha) del ciclo ---
    if prod_data.empty:
        return pd.DataFrame()
    rend = float(prod_data["Rendimiento"].astype(float).mean())

    # Fechas y orden
    dates = data_nasa["Date"]

    # Kc Diario (indice consistente con data_nasa)
    daily_kc = daily_kc_curve(
        data_nasa.index, kc_ini=kc["ini"], kc_mid=kc["mid"], kc_end=kc["end"], dur=dur
    )

    # Cálculo de ETo vectorizado
    eto_results = eto_fao56_mm(
        tmax=data_nasa["T_max"].values,
        tmin=data_nasa["T_min"].values,
        rh_pct=data_nasa["Rh"].values,
        u2_ms=data_nasa["Ws"].values,
        rs_mjm2d=data_nasa["Rs"].values,
        lat_deg=region.latitude,
        z_m=region.altitude,
        doy=data_nasa["Date"].dt.dayofyear.values,
    )

    eto_df = pd.DataFrame(eto_results, index=data_nasa.index)

    # --- Pef (FAO simple sobre el ciclo) ---
    efp_series = calculate_daily_simple_efp(data_nasa["P_total"])
    efp_series.index = data_nasa.index

    # Decadas del ciclo (1..ceil(n/10)) con índice consistente ---
    decades_series = calculate_decades_per_cycle(data_nasa.index)

    # --- ETc, ET verde/azul (todo con el mismo índice) ---
    et0 = eto_df["ET0"]
    etc = et0 * daily_kc

    green_et = np.minimum(etc, efp_series)
    blue_et = np.maximum(etc - efp_series, 0.0)

    # Preparar salida
    out = pd.concat([data_nasa, eto_df], axis=1)
    out = out.loc[:, ~out.columns.duplicated()]

    out["P_ef"] = efp_series
    out["Decada"] = decades_series
    out["ETc"] = etc
    out["ET_v"] = green_et
    out["ET_a"] = blue_et

    # Calcular HH y UAC para el ciclo completo
    summary = calculate_wf_wc(green_et, blue_et, rend)

    out["UAC_v"] = summary["UACverde_m3_ha"]
    out["UAC_a"] = summary["UACazul_m3_ha"]
    out["HH_v"] = summary["HHverde_m3_ton"]
    out["HH_a"] = summary["HHazul_m3_ton"]

    # Columnas finales deseadas
    keep_cols = [
        "Date", "T_max", "T_min", "Rs", "Rh", "Ws", "P_total",
        "Tmean_", "Rn_", "ET0", "P_ef", "Decada", "ETc",
        "ET_v", "ET_a", "UAC_v", "UAC_a", "HH_v", "HH_a"
    ]
    
    # Asegurar que solo devolvemos las columnas que existen y queremos
    out = out[[c for c in keep_cols if c in out.columns]]
    
    return out
