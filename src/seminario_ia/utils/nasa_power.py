"""
Modulo para obtener datos de la API de NASA POWER
"""

__author__ = "Jesus Flores Lacarra"

from datetime import datetime

import pandas as pd
import requests

# Parámetros por defecto para obtener datos de la API de NASA POWER
DEFAULT_PARAMS = [
    "ALLSKY_SFC_SW_DWN",
    "ALLSKY_SFC_LW_DWN",
    "PRECTOTCORR",
    "WS2M",
    "T2M_MAX",
    "T2M_MIN",
    "RH2M",
]


URL = "https://power.larc.nasa.gov/api/temporal/daily/point"


def get_nasa_power_data(
    loc_name: str,
    lat: float,
    lon: float,
    start_date: str | datetime,
    end_date: str | datetime,
    columns=DEFAULT_PARAMS,
) -> pd.DataFrame | None:
    """
    Recupera datos diarios de la API de NASA POWER para una ubicación y rango de fechas específicos.
    """

    if isinstance(start_date, datetime):
        start_date = start_date.strftime("%Y%m%d")
    if isinstance(end_date, datetime):
        end_date = end_date.strftime("%Y%m%d")

    params = {
        "parameters": ",".join(columns),  # Parámetros a solicitar
        "community": "AG",  # Comunidad agrícola
        "longitude": lon,  # Longitud de la ubicación
        "latitude": lat,  # Latitud de la ubicación
        "start": start_date,  # Fecha de inicio (YYYYMMDD)
        "end": end_date,  # Fecha de fin (YYYYMMDD)
        "format": "JSON",  # Formato de respuesta
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        rh_values = data["properties"]["parameter"]
        df = pd.DataFrame(rh_values)
        df.index.name = "DATE"
        return df.reset_index()
    else:
        print(f"Error al obtener datos de NASA POWER: {response.status_code}")
        return None


if __name__ == "__main__":
    # Ejemplo de uso
    loc_name = "Hermosillo"
    lat, lon = 29.094821, -110.969220
    # lat = 29.0
    # lon = 111.0
    start_date = "20240101"
    end_date = "20241231"

    df_nasa_power = get_nasa_power_data(loc_name, lat, lon, start_date, end_date)
    if df_nasa_power is not None:
        print(df_nasa_power.head())
    print()
