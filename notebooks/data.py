from pathlib import Path

DATA_DIR = Path("../data").resolve()
SEQUIA_DIR = DATA_DIR / "raw" / "impacto-sequia"
DATOS_ABIERTOS_SONORA_DIR = DATA_DIR / "raw" / "datos-abiertos"
SIAP_DIR = DATA_DIR / "raw" / "siap-produccion-agricola"
SIACON_DIR = DATA_DIR / "raw" / "siacon"
PROPORCIONADOS_DIR = DATA_DIR / "raw" / "datos_proporcionados"

DATASETS = {
    "raw": {
        "impacto-sequia": SEQUIA_DIR,
        "datos-abiertos": DATOS_ABIERTOS_SONORA_DIR,
        "siap-produccion-agricola": SIAP_DIR,
        "siacon": SIACON_DIR,
        "datos_proporcionados": PROPORCIONADOS_DIR,
    },
    "processed": {},
}
