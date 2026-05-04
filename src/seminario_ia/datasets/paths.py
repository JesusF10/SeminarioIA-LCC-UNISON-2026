"""
Rutas a los datasets y directorios utilizados en el proyecto.

Este módulo centraliza todas las definiciones de rutas para evitar
dependencias circulares entre módulos.
"""

from pathlib import Path

# Rutas base del proyecto
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR.parent.parent.parent / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"
CONFIG_DATA_DIR = DATA_DIR / "config"

# Rutas a datasets específicos en el directorio raw
SEQUIA_DIR = RAW_DIR / "impacto-sequia"
DATOS_ABIERTOS_SONORA_DIR = RAW_DIR / "datos-abiertos"
SIAP_DIR = RAW_DIR / "siap-produccion-agricola"
SIACON_DIR = RAW_DIR / "siacon"
PROPORCIONADOS_DIR = RAW_DIR / "datos_proporcionados"
DATOS_CONAGUA = RAW_DIR / "conagua"

# Diccionario de datasets en raw
RAW_DATASETS: dict[str, Path] = {
    "impacto-sequia": SEQUIA_DIR,
    "datos-abiertos": DATOS_ABIERTOS_SONORA_DIR,
    "siap-produccion-agricola": SIAP_DIR,
    "siacon": SIACON_DIR,
    "datos_proporcionados": PROPORCIONADOS_DIR,
    "conagua": DATOS_CONAGUA,
}

# Rutas a archivos procesados
COORDINATES_CSV = PROCESSED_DIR / "SonoraLatLongAlt.csv"
JSON_CODIFICACION = CONFIG_DATA_DIR / "codificacion.json"
NASA_POWER_FILES = PROCESSED_DIR / "nasa_power"
