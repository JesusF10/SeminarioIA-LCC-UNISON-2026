# %% Cargar datasets y librerias
from ..datasets import RAW_DATASETS

import polars as pd

print("Datasets disponibles:")
for dataset_name, dataset_path in RAW_DATASETS.items():
    print(f"- {dataset_name}: {dataset_path}")
dataset_name = "siap-produccion-agricola"
dataset_dir = RAW_DATASETS[dataset_name]
print()


print(f"Cargando dataset: {dataset_name} desde {dataset_dir}")
files = list(dataset_dir.glob("municipal/*.csv"))
if not files:
    print(f"No se encontraron archivos CSV en {dataset_dir / 'municipal'}")
    df = None
else:
    print(f"Archivos encontrados en {dataset_dir / 'municipal'}:")

print(f"- {files[0]}")
df = pd.read_csv(files[0])
columns = df.columns
for file in files[1:]:
    # print(f"- {file}")
    f = pd.read_csv(file, ignore_errors=True)
    f.columns = columns
    df = pd.concat([df, f])

print(df.height)
print(df.columns)
# df = df.drop(columns_to_remove, strict=True)
print(df.head())
# print(columns[0])
# for col in zip(*columns, strict=True):
#    print(col)
# %% Eliminar columnas no deseadas
columns_to_remove = [
    "",
    "Idestado",
    "Nomestado",
    "Idcader",
    "Nomcader",
    "Nommunicipio",
    "Nomddr",
]

IDCICLO_CICLO = {}
