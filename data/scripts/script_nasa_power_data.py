from seminario_ia.datasets import PROCESSED_DIR
from seminario_ia.utils import request_nasa_power_data

import pandas as pd

coords = pd.read_csv(PROCESSED_DIR / "SonoraLatLongAlt.csv")

PATH_TO_SAVE_DATA = PROCESSED_DIR / "nasa_power"
PATH_TO_SAVE_DATA.mkdir(parents=True, exist_ok=True)

INIT_YEAR = 2003
FINAL_YEAR = 2024

for row in coords.itertuples():
    index, entidad, municipio, lat, lon, z_m = row
    for year in range(INIT_YEAR, FINAL_YEAR + 1, 1):
        filename = f"data_{municipio}_{year}.csv"
        start_date = f"{str(year)}0101"
        end_date = f"{str(year)}1231"
        data = request_nasa_power_data(municipio, lat, lon, start_date, end_date)
        if data is None:
            print(
                f"Error al obtener datos para el municipio {municipio} en el año {year}."
            )
            break
        data.to_csv(PATH_TO_SAVE_DATA / filename, index=False)
