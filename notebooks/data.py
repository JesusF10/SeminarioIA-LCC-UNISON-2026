# %% Importar dependencias
from pathlib import Path

# import geopandas as gpd
import pandas as pd

DATA_DIR = Path("../data").resolve()
SEQUIA_DIR = DATA_DIR / "raw" / "impacto-sequia"
DATOS_ABIERTOS_SONORA_DIR = DATA_DIR / "raw" / "datos-abiertos"
DATOS_SIAP = DATA_DIR / "raw" / "siap-produccion-agricola"


# %% Cargar datos

for i in Path(DATOS_SIAP / "nacional").glob("*.csv"):
    df = pd.read_csv(i, encoding="latin-1")
    sonora = df[df["Idestado"] == 26]
    nombre = i.stem.lower().split("_")
    nombre = "_".join(nombre + ["sonora"])
    sonora.to_csv(
        DATOS_SIAP / "nacional" / nombre / ".csv", index=False, encoding="latin-1"
    )

# nacional = pd.read_csv(DATOS_SIAP / "nacional" / )

# %% Filtrar datos
distritos_riego = agricultura["NDDR"].unique().tolist()

# %%
#
