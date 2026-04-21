import json
from pathlib import Path

from seminario_ia.datasets.data import JSON_DDRS_PATH, JSON_MUNICIPIOS_PATH

with open(JSON_MUNICIPIOS_PATH, encoding="utf-8") as f:
    data = json.load(f)
    CODIGO_MUNICIPIO = {int(k): v for k, v in data.items()}
    MUNICIPIO_CODIGO = {v: int(k) for k, v in data.items()}

with open(JSON_DDRS_PATH, encoding="utf-8") as f:
    data = json.load(f)
    CODIGO_DDR = {int(k): v for k, v in data.items()}
    DDR_CODIGO = {v: int(k) for k, v in data.items()}

with open(Path(__file__).parent / "mapa_ciclos.json", encoding="utf-8") as f:
    data = json.load(f)
    IDCICLO_CICLO = {int(k): v for k, v in data.items()}

if __name__ == "__main__":
    if IDCICLO_CICLO:
        print("Mapa de ciclos cargado correctamente:")
        for idciclo, ciclo in IDCICLO_CICLO.items():
            print(f"- ID {idciclo}: {ciclo}")
    print()
