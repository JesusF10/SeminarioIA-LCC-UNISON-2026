"""
Este módulo proporciona acceso a los datos y mapeos de claves relacionados con los conjuntos de datos utilizados en el proyecto.
Incluye rutas a los datos sin procesar, así como mapeos para:
   - Códigos de municipios.
   - Códigos de distritos de desarrollo regional (DDR).
"""

from .codes import get_cycle_code as get_cycle_code
from .codes import get_ddr_code as get_ddr_code
from .codes import get_mod_code as get_mod_code
from .codes import get_mun_code as get_mun_code
from .codes import get_unit_code as get_unit_code
from .data import get_crop_data as get_crop_data
from .data import get_mun_coordinates as get_mun_coordinates
from .data import get_nasa_power_data as get_nasa_power_data
from .data import get_prod_data as get_prod_data
from .data import load_prod_file as load_prod_file
from .paths import DATA_DIR as DATA_DIR
from .paths import JSON_CODIFICACION as JSON_CODIFICACION
from .paths import PROCESSED_DIR as PROCESSED_DIR
from .paths import RAW_DATASETS as RAW_DATASETS
from .paths import RAW_DIR as RAW_DIR

__all__ = {
    "RAW_DATASETS",
    "DATA_DIR",
    "PROCESSED_DIR",
    "RAW_DIR",
    "get_mun_code",
    "get_mun_coordinates",
    "get_ddr_code",
    "get_cycle_code",
    "get_mod_code",
    "get_unit_code",
    "get_prod_data",
    "load_prod_file",
    "get_nasa_power_data",
    "get_crop_data",
    "JSON_CODIFICACION",
}
