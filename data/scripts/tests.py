from seminario_ia.datasets import RAW_DATASETS

import geopandas as gpd

path = RAW_DATASETS.get("datos-sequia", None)

assert path is not None, "datos-sequia not found in RAW_DATASETS"

assert len(list(path.glob("*.shp"))) > 0, (
    "No shapefiles found in impacto Sequia dataset"
)

filename = list(path.glob("*.shp"))[0]

df = gpd.read_file(filename)

df = df[df["Entidad"] == "Sonora"]

print(len(df))


print(df.columns)
