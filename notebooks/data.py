# %% Importar dependencias
from pathlib import Path

# import geopandas as gpd
import pandas as pd
from jedi.inference.value.dynamic_arrays import DictModification

DATA_DIR = Path("../data").resolve()
SEQUIA_DIR = DATA_DIR / "raw" / "impacto-sequia"
DATOS_ABIERTOS_SONORA_DIR = DATA_DIR / "raw" / "datos-abiertos"
DATOS_SIAP = DATA_DIR / "raw" / "siap-produccion-agricola"


# %% Cargar datos

agricultura = pd.read_excel(
    DATOS_ABIERTOS_SONORA_DIR
    / "agricultura"
    / "datos"
    / "Agricultura Sonora año 2023.xlsx"
)

diccionario = pd.read_excel(
    DATOS_SIAP / "municipal" / "Diccionario_agricola_2003_a_2023.xlsx"
)

# nacional = pd.read_csv(DATOS_SIAP / "nacional" / )

# %% Filtrar datos
# distritos_riego = agricultura["NDDR"].unique().tolist()
#

print(diccionario.dropna(axis=0))


# %%
