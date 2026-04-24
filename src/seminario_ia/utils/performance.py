"""
Funciones para calcular la curva de Kc diaria, Pef diario, rendimiento, UAC y HH.
"""

import numpy as np
import pandas as pd


def daily_kc_curve(
    fechas_idx: pd.DatetimeIndex,
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


def pef_simple_fao_per_day(ptot_series_mm: pd.Series) -> pd.Series:
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


# ----------------------------------------------------------------------------------
# def rendimiento_por_archivo(df: pd.DataFrame, region: str) -> float:
#    """
#    Obtiene el rendimiento (ton/ha) para el/los años presentes en el archivo.
#    - Si hay varios años, usa el promedio simple de los disponibles en prod_df
#      para ese municipio y cultivo (Trigo grano).
#    - Si no hay coincidencias, devuelve NaN.
#    """
#    years = sorted(set(int(y) for y in pd.Series(df["YEAR"]).dropna().unique()))
#    rend_vals = []
#    for y in years:
#        sel = prod_df[
#            (prod_df["Anio"] == y) &
#            (prod_df["Nommunicipio"] == region) &
#            (prod_df["Nomcultivo"] == "Trigo grano")
#        ]
#        if not sel.empty:
#            vals = sel["Rend_t_ha"].astype(float).tolist()
#            rend_vals.extend(vals)
#    if rend_vals:
#        return float(np.mean(rend_vals))
#    return float("nan")
# ----------------------------------------------------------------------------------


def performance_per_file(
    df: pd.DataFrame, region: str, prod_df: pd.DataFrame, crop: str
) -> float:
    """
    Obtiene el rendimiento (ton/ha) para el/los años presentes en el archivo
    usando la tabla de producción municipal (prod_df).

    - Para cada año presente en df["YEAR"], busca en prod_df filas con:
        Anio == YEAR,
        Nommunicipio == region,
        Nomcultivo == crop.
    - Si encuentra varios registros, promedia Rend_t_ha.
    - Si no encuentra nada para ningún año, devuelve NaN y avisa.

    Parametros:
    - df: DataFrame del ciclo actual, usado solo para extraer los años presentes.
    - region: Nombre del municipio/región para buscar en prod_df.
    - prod_df: DataFrame con la producción municipal, que debe contener las columnas:
        - Anio: Año calendario (int).
        - Nommunicipio: Nombre del municipio (str).
        - Nomcultivo: Nombre del cultivo (str).
        - Rend_t_ha: Rendimiento en toneladas por hectárea (float).
    - crop: Nombre del cultivo a buscar en prod_df (ej. "Trigo grano").

    Regresa:
    - Rendimiento promedio (ton/ha) para los años encontrados en df, o NaN si no se encuentra
    ningún dato en prod_df para esos años y región.
    """
    # Años presentes en el archivo de clima (ej. 2010 y 2011 para un ciclo 2010–2011)
    years = pd.to_numeric(df["YEAR"], errors="coerce").dropna().astype(int).unique()
    years = sorted(years)

    rend_vals = []

    for y in years:
        sel = prod_df[
            (prod_df["Anio"] == y)
            & (prod_df["Nommunicipio"].astype(str).str.strip() == region)
            & (prod_df["Nomcultivo"] == crop)
        ]

        if sel.empty:
            print(
                f"[Rendimiento] No hay dato de Rend_t_ha en prod_df para region='{region}', año={y}."
            )
            continue

        # Si hay varias filas, promediamos el rendimiento
        r_mean = float(sel["Rend_t_ha"].astype(float).mean())
        rend_vals.append(r_mean)

    if rend_vals:
        # Promedio simple de los años encontrados en este archivo
        return float(np.mean(rend_vals))

    print(
        f"[Rendimiento] Archivo de región '{region}' (años {years}) "
        "sin rendimiento disponible en prod_df. HH se pondrá como NaN."
    )
    return float("nan")


def calculate_wf_uac(
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


def decades_per_cycle(idx: pd.DatetimeIndex) -> pd.Series:
    """
    Calcula las décadas relativas al ciclo (no calendario) a partir de un índice de fechas.
    Cada década corresponde a un bloque de 10 días consecutivos, comenzando desde el inicio del
    ciclo (día 1-10 = década 1, día 11-20 = década 2, etc.). El resultado es una Serie con el
    mismo índice que idx y valores enteros indicando la década correspondiente a cada fecha.

    Parametros:
        - idx: Índice de fechas (pd.DatetimeIndex) para el ciclo completo.

    Regresa:
        - pd.Series de enteros indicando la década relativa al ciclo para cada fecha en idx.
    """
    n = len(idx)
    dec = np.ceil((np.arange(1, n + 1)) / 10.0).astype(int)
    return pd.Series(dec, index=idx, name="decada_")
