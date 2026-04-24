# Script para limpieza de datos de produccion de la SIAP en Sonora de 2003 a 2024.
from pprint import pprint

from seminario_ia.datasets import PROCESSED_DIR, RAW_DATASETS

import pandas as pd

siap = RAW_DATASETS["siap-produccion-agricola"]
municipal = siap / "municipal"
nacional = siap / "nacional"
files_municipal = municipal.glob("*.csv")
files_nacional = nacional.glob("*.csv")

cols_to_keep_municipal = [
    "Anio",
    "Idddr",
    "Idmunicipio",
    "Nommunicipio",
    "Idciclo",
    "Nommodalidad",
    "Nomunidad",
    "Nomcultivo",
    "Sembrada",
    "Cosechada",
    "Siniestrada",
    "Volumenproduccion",
    "Rendimiento",
    "PMR",
    "Valorproduccion",
]

cools_to_keep_nacional = [
    "Anio",
    "Idestado",
    "Nomestado",
    "Idciclo",
    "Nommodalidad",
    "Nomunidad",
    "Nomcultivo",
    "Cosechada",
    "Siniestrada",
    "Volumenproduccion",
    "Rendimiento",
    "PMR",
    "Valorproduccion",
]

new_path_muni = PROCESSED_DIR / "siap_produccion" / "sonora"
if new_path_muni.exists():
    print(f"El directorio {new_path_muni} ya existe. Se eliminará su contenido.")
    for file in new_path_muni.glob("*.csv"):
        file.unlink()
new_path_muni.mkdir(parents=True, exist_ok=True)

new_path_nacional = PROCESSED_DIR / "siap_produccion" / "nacional"
if new_path_nacional.exists():
    print(f"El directorio {new_path_nacional} ya existe. Se eliminará su contenido.")
    for file in new_path_nacional.glob("*.csv"):
        file.unlink()
new_path_nacional.mkdir(parents=True, exist_ok=True)

pprint("Columnas a conservar (en municipal):")
pprint(cols_to_keep_municipal)

for file in files_municipal:
    # pprint(file.name)
    df = pd.read_csv(file)
    df.rename(columns={"Preciomediorural": "PMR", "Precio": "PMR"}, inplace=True)
    df = df[cols_to_keep_municipal]
    null_values = df.isnull().sum()

    if null_values.any():
        print(f"Valores nulos encontrados en {file.name}:")
        print(null_values[null_values > 0])
        print(f"Total de registros: {len(df)}")
        print(df[df.isnull().any(axis=1)])

    if new_path_muni / file.name in new_path_muni.glob("*.csv"):
        print(f"Archivo {file.name} ya existe en destino. Se sobrescribirá.")
    df.to_csv(new_path_muni / file.name, index=False, mode="w")


pprint("Columnas a conservar (en nacional):")
pprint(cools_to_keep_nacional)

for file in files_nacional:
    # print(file.name)
    df = pd.read_csv(file, encoding="latin-1")
    df.rename(
        columns={
            "Preciomediorural": "PMR",
            "Precio": "PMR",
            "NomcultivoSembrada": "Nomcultivo",
        },
        inplace=True,
    )
    df = df[cools_to_keep_nacional]

    # df = df.dropna()

    null_values = df.isnull().sum()

    if null_values.any():
        print(f"Valores nulos encontrados en {file.name}:")
        print(null_values[null_values > 0])
        print(f"Total de registros: {len(df)}")
        df = df.dropna()
        print(f"Registros después de eliminar nulos: {len(df)}")

    df.to_csv(new_path_nacional / file.name, index=False)
