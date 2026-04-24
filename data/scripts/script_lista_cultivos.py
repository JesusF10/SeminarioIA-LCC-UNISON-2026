# Script para obtener todos los cultivos producidos que tienen registro en la SIAP en Sonora de 2003 a 2024.
# import json
from pprint import pprint

from seminario_ia.datasets import RAW_DATASETS

import pandas as pd

siap = RAW_DATASETS["siap-produccion-agricola"]

municipal = siap / "municipal"

files = list(municipal.glob("*.csv"))

df = pd.read_csv(files[0])

for file in files:
    df = pd.concat([df, pd.read_csv(file)], ignore_index=True)

# pprint(sorted(df["Nomcultivo"].astype(str).unique()))
# pprint(df[["Idmodalidad", "Nommodalidad"]].value_counts())

unidades = df[["Idunidadmedida", "Nomunidad"]].value_counts()


codigos_unidades = {}

for row in unidades.index:
    codigos_unidades[row[0]] = row[1]

pprint(codigos_unidades)
print()

pprint(df[["Nomunidad"]].value_counts())

# with open("codigos_unidades.json", "w", encoding="utf-8") as f:
#    json.dump(codigos_unidades, f, ensure_ascii=False, indent=4)
