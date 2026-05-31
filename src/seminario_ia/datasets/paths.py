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
SEQUIA_DIR = RAW_DIR / "datos-sequia"
SIAP_DIR = RAW_DIR / "siap-produccion-agricola"
PROPORCIONADOS_DIR = RAW_DIR / "datos_proporcionados"
DATOS_CONAGUA = RAW_DIR / "conagua"

# Diccionario de datasets en raw
RAW_DATASETS: dict[str, Path] = {
    "datos-sequia": SEQUIA_DIR,
    "siap-produccion-agricola": SIAP_DIR,
    "datos_proporcionados": PROPORCIONADOS_DIR,
    "conagua": DATOS_CONAGUA,
}

# Rutas a archivos procesados
COORDINATES_CSV = PROCESSED_DIR / "SonoraLatLongAlt.csv"
JSON_CODIFICACION = CONFIG_DATA_DIR / "codificacion.json"
NASA_POWER_DATA = PROCESSED_DIR / "nasa_power"
PRODUCCION_SIAP = PROCESSED_DIR / "siap_produccion" / "municipal"
PROD_SONORA_DIR = PROCESSED_DIR / "siap_produccion" / "sonora"
