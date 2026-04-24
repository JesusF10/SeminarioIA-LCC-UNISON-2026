import json
from pprint import pprint

from seminario_ia.datasets import PROCESSED_DIR

JSON_PATH = PROCESSED_DIR / "codificacion.json"


with open(JSON_PATH) as f:
    data = json.load(f)
    codes = data["codigos_municipios"]

    if codes.get("41", None) is None:
        codes["41"] = "Nacozari de García"

    pprint(codes)
