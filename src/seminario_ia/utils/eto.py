"""
Funciones para calcular la evapotranspiración de referencia (ETo) usando el método de Penman-Monteith según FAO-56.
Incluye funciones para:
- Presión de vapor de saturación y pendiente.
- Presión atmosférica y constante psicrométrica.
- Radiación extraterrestre, cielo despejado y neta.
- Cálculo de ETo diario con G=0 (flujo del calor del suelo a 0).

Se ha vectorizado el cálculo utilizando NumPy para mejorar el rendimiento con arrays de datos.
"""

import numpy as np

# === Constantes FAO-56 ===

# Coef. de reflexión de la superficie de referencia (césped)
ALBEDO = 0.23

# Constante de Stefan-Boltzmann [MJ K^-4 m^-2 día^-1]
SIGMA = 4.903e-9

# Presión atmosférica estándar a nivel del mar [kPa]
P0_kPa = 101.3

# Temperatura estándar de referencia (20 °C en Kelvin)
T0_K = 293.0

# Constante solar [MJ m^-2 min^-1]
GSC = 0.0820


# --- Funciones ---
def es_kpa(t_c: float | np.ndarray) -> float | np.ndarray:
    """
    Calcula la presión de vapor de saturación (kPa) a partir de la temperatura en °C
    usando la fórmula de Tetens (FAO-56 Eq. 11).

    Parámetros:
        t_c: Temperatura del aire [°C].

    Regresa:
        Presión de vapor de saturación [kPa].
    """
    return 0.6108 * np.exp((17.27 * t_c) / (t_c + 237.3))


def delta_kpa_per_c(t_c: float | np.ndarray) -> float | np.ndarray:
    """
    Calcula la pendiente de la curva de saturación (kPa/°C) a partir de la temperatura en °C
    usando la fórmula derivada de Tetens (FAO-56 Eq. 13).

    Parámetros:
        t_c: Temperatura de aire [°C].

    Regresa:
        Pendiente de la curva de saturación [kPa/°C].
    """
    e = es_kpa(t_c)
    return 4098.0 * e / ((t_c + 237.3) ** 2)


# --- Presión y constante psicrométrica ---
def atm_pressure_kpa(z_m: float | np.ndarray) -> float | np.ndarray:
    """
    Calcula la presión atmosférica (kPa) a partir de la altitud en metros usando la
    fórmula de barometría (FAO-56 Eq. 7).

    Temperatura estándar de referencia (20 °C) se asume para el cálculo.

    Parámetros:
        z_m: Elevación sobre el nivel del mar [m].

    Regresa:
        Presión atmosférica [kPa].
    """
    return 101.3 * ((293.0 - 0.0065 * z_m) / 293.0) ** 5.26


def psychrometric_constant_kpa_per_c(p_kpa: float | np.ndarray) -> float | np.ndarray:
    """
    Calcula la constante psicrométrica (kPa/°C) a partir de la presión atmosférica en kPa
    usando la fórmula de FAO-56 (Eq. 8).

    Parámetros:
        p_kpa: Presión atmosférica [kPa].

    Regresa:
        Un valor de la constante psicrométrica [kPa/°C].
    """
    cl = 2.45  # Calor latente de vaporización [MJ/kg]
    cp = 1.013e-3  # Calor específico del aire [MJ/kg/°C]
    epsilon = 0.622  # Cociente del peso molecular vapor de agua / aire seco
    return (cp * p_kpa) / (epsilon * cl)


def extraterrestrial_radiation_mj_m2d(
    lat_deg: float | np.ndarray, doy: int | np.ndarray
) -> float | np.ndarray:
    """
    Calcula la radiación extraterrestre (Ra) en MJ/m²/día a partir de la latitud en grados y
    el día del año usando las fórmulas de FAO-56 (Eqs. 21–25).

    Parámetros:
        lat_deg: Latitud en grados.
        doy: Día del año (1-365/366).

    Regresa:
        Valor de la radiación de la radiación extraterrestre [MJ/m²/día].
    """
    phi = np.radians(lat_deg)
    dr = 1.0 + 0.033 * np.cos(2.0 * np.pi / 365.0 * doy)
    delta = 0.409 * np.sin(2.0 * np.pi / 365.0 * doy - 1.39)
    ws = np.arccos(-np.tan(phi) * np.tan(delta))
    ra = (
        (24.0 * 60.0 / np.pi)
        * GSC
        * dr
        * (ws * np.sin(phi) * np.sin(delta) + np.cos(phi) * np.cos(delta) * np.sin(ws))
    )
    return ra


def clear_sky_radiation_rso_fao56(
    lat_deg: float | np.ndarray, doy: int | np.ndarray, z_m: float | np.ndarray
) -> float | np.ndarray:
    """
    Calcula la radiación de cielo despejado (Rso) en MJ/m²/día a partir de la latitud,
    día del año y altitud usando la fórmula de FAO-56 (Eq. 37).

    FAO-56 - Cielo despejado: (0.75 + 2e-5*z) * Ra.

    Parametros:
        lat_deg: Latitud en grados.
        doy: Día del año (1-365/366).
        z_m: Altitud [m].

    Regresa:
        Valor de la radiación de cielo despejado [MJ/m²/día].
    """
    ra = extraterrestrial_radiation_mj_m2d(lat_deg, doy)
    return (0.75 + 2e-5 * z_m) * ra


def net_shortwave_rns(
    rs_mjm2d: float | np.ndarray, albedo: float = ALBEDO
) -> float | np.ndarray:
    """
    Calcula la radiación neta de onda corta (Rns) en MJ/m²/día a partir de la radiación solar global
    y el albedo usando la fórmula de FAO-56 (Eq. 38).

    Rns [MJ m-2 d-1] — (1 - albedo) * Rs (FAO-56).

    Parametros:
        rs_mjm2d: Radiación solar global [MJ/m²/día].
        albedo: Coeficiente de reflexión de la superficie (por defecto 0.23 para césped).

    Regresa:
        Valor de la radiación neta de onda corta [MJ/m²/día].
    """
    return (1.0 - albedo) * rs_mjm2d


def net_longwave_rnl_fao56(
    tmax_c: float | np.ndarray,
    tmin_c: float | np.ndarray,
    ea_kpa: float | np.ndarray,
    rs_mjm2d: float | np.ndarray,
    rso_mjm2d: float | np.ndarray,
) -> float | np.ndarray:
    """
    Calcula la radiación neta de onda larga (Rnl) en MJ/m²/día a partir de las temperaturas máxima
    y mínima, la presión de vapor actual, la radiación solar global y la radiación de cielo despejado
    usando la fórmula de FAO-56 (Eq. 39).

    Parametros:
        tmax_c: Temperatura máxima absoluta en un periodo de 24h del aire [°C].
        tmin_c: Temperatura mínima absoluta en un periodo de 24h del aire [°C].
        ea_kpa: Presión de vapor real [kPa].
        rs_mjm2d: Radiación solar media o calculada [MJ/m²/día].
        rso_mjm2d: Radiación solar de cielo despejado [MJ/m²/día].

    Regresa:
        Valor de la radiación neta de onda larga [MJ/m²/día] calculada según FAO-56.
    """
    tmaxk, tmink = tmax_c + 273.16, tmin_c + 273.16
    t4 = (tmaxk**4 + tmink**4) / 2.0

    # Radiacion relativa de onda corta (Rs/Rso)
    # rsrso = 0.0 if rso_mjm2d <= 0.0 else max(0.0, min(rs_mjm2d / rso_mjm2d, 1.0))
    # Vectorized logic:
    rsrso = np.where(rso_mjm2d <= 0.0, 0.0, np.clip(rs_mjm2d / rso_mjm2d, 0.0, 1.0))

    fcloud = 1.35 * rsrso - 0.35
    return SIGMA * t4 * (0.34 - 0.14 * np.sqrt(np.maximum(ea_kpa, 0.0))) * fcloud


# --- Penman-Monteith con G=0 a escala diaria ---
def eto_fao56_mm(
    tmax: float | np.ndarray,
    tmin: float | np.ndarray,
    rh_pct: float | np.ndarray,
    u2_ms: float | np.ndarray,
    rs_mjm2d: float | np.ndarray,
    lat_deg: float | np.ndarray,
    z_m: float | np.ndarray,
    doy: int | np.ndarray,
    g_mjm2d: float | np.ndarray = 0.0,
) -> dict:
    """
    Regresa un diccionario con los componentes intermedios y el resultado final de
    la evapotranspiración de referencia (ETo) en mm/día usando el método de Penman-Monteith según FAO-56.

    ETo [mm/día] — FAO-56 Penman-Monteith (Eq. 6) diario (G=0 por defecto).
    - Usa es, ea (de T y HR)
    - delta(Tmean), gamma(z)
    - Rn = Rns - Rnl (Rnl FAO-56 Eq. 39)

    Parametros:
        - tmax, tmin: Temperaturas máxima y mínima en °C.
        - rh_pct: Humedad relativa promedio en %.
        - u2_ms: Velocidad del viento a 2 m en m/s.
        - rs_mjm2d: Radiación solar global en MJ/m²/día.
        - lat_deg: Latitud en grados.
        - z_m: Altitud en metros.
        - doy: Día del año (1-365/366).
        - g_mjm2d: Flujo de calor del suelo en MJ/m²/d

    Regresa:
    Un diccionario con:
        - Tmean_: Temperatura media (°C).
        - es_: Presión de vapor de saturación (kPa).
        - ea_: Presión de vapor real (kPa).
        - delta_: Pendiente de la curva de saturación (kPa/°C).
        - P_: Presión atmosférica (kPa).
        - gamma_: Constante psicrométrica (kPa/°C).
        - Rso_: Radiación extraterrestre (MJ/m²/día).
        - Rns_: Radiación neta de onda corta (MJ/m²/día).
        - Rnl_: Radiación neta de onda larga (MJ/m²/día).
        - Rn_: Radiación neta total (MJ/m²/día).
        - ET0: Evapotranspiración de referencia (mm/día).
    """
    tmean = (tmax + tmin) / 2.0
    es = (es_kpa(tmax) + es_kpa(tmin)) / 2.0
    ea = es * (rh_pct / 100.0)
    delta = delta_kpa_per_c(tmean)
    p = atm_pressure_kpa(z_m)
    gamma = psychrometric_constant_kpa_per_c(p)

    # ===================== Versión FAO-56 ========================
    # Rso = clear_sky_radiation_Rso_FAO56(lat_deg, doy, z_m)
    # =============================================================

    # ===================== Versión "UAMEX" =======================
    rso = extraterrestrial_radiation_mj_m2d(
        lat_deg, doy
    )  # ← aquí va Ra cuando uses la versión "equipo"

    rns = net_shortwave_rns(rs_mjm2d=rs_mjm2d, albedo=ALBEDO)
    rnl = net_longwave_rnl_fao56(tmax, tmin, ea, rs_mjm2d, rso)
    rn = rns - rnl
    num = 0.408 * delta * (rn - g_mjm2d) + gamma * (900.0 / (tmean + 273.0)) * u2_ms * (
        es - ea
    )
    den = delta + gamma * (1.0 + 0.34 * u2_ms)
    eto = np.maximum(0.0, num / den)
    return {
        "Tmean_": tmean,
        "es_": es,
        "ea_": ea,
        "delta_": delta,
        "P_": p,
        "gamma_": gamma,
        "Rso_": rso,
        "Rns_": rns,
        "Rnl_": rnl,
        "Rn_": rn,
        "ET0": eto,
    }
