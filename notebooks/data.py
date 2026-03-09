# %% Importar dependencias
from pathlib import Path

import geopandas as gpd

DATA_DIR = Path("../data").resolve()
SEQUIA_DIR = DATA_DIR / "raw" / "impacto-sequia"

# %% Cargar datos
gdf = gpd.read_file(SEQUIA_DIR / "impacto_sequia.shp")

# %% Filtrar datos
print(gdf.columns)

# %%
