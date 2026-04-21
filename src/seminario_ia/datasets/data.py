# %% Importar librerias y datos
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR.parent.parent / "data"
RAW_DIR = Path("../data/raw").resolve()
SEQUIA_DIR = RAW_DIR / "impacto-sequia"
DATOS_ABIERTOS_SONORA_DIR = RAW_DIR / "datos-abiertos"
SIAP_DIR = RAW_DIR / "siap-produccion-agricola"
SIACON_DIR = RAW_DIR / "siacon"
PROPORCIONADOS_DIR = RAW_DIR / "datos_proporcionados"
DATOS_CONAGUA = RAW_DIR / "conagua"

JSON_MUNICIPIOS_PATH = BASE_DIR / "mapa_municipios.json"
JSON_DDRS_PATH = BASE_DIR / "mapa_ddr.json"


RAW_DATASETS: dict[str, Path] = {
    "impacto-sequia": SEQUIA_DIR,
    "datos-abiertos": DATOS_ABIERTOS_SONORA_DIR,
    "siap-produccion-agricola": SIAP_DIR,
    "siacon": SIACON_DIR,
    "datos_proporcionados": PROPORCIONADOS_DIR,
    "conagua": DATOS_CONAGUA,
}

if __name__ == "__main__":
    for dataset_name, dataset_path in RAW_DATASETS.items():
        print(f"Cargando dataset: {dataset_name}")
        print(f"Ruta del dataset: {dataset_path}")
