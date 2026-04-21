"""
Este módulo proporciona acceso a los datos y mapeos de claves relacionados con los conjuntos de datos utilizados en el proyecto.
Incluye rutas a los datos sin procesar, así como mapeos para:
   - Códigos de municipios.
   - Códigos de distritos de desarrollo regional (DDR).
"""

from seminario_ia.datasets.data import DATA_DIR as DATA_DIR
from seminario_ia.datasets.data import RAW_DATASETS as RAW_DATASETS
from seminario_ia.datasets.mapeo_claves import CODIGO_DDR as CODIGO_DDR
from seminario_ia.datasets.mapeo_claves import CODIGO_MUNICIPIO as CODIGO_MUNICIPIO
from seminario_ia.datasets.mapeo_claves import DDR_CODIGO as DDR_CODIGO
from seminario_ia.datasets.mapeo_claves import MUNICIPIO_CODIGO as MUNICIPIO_CODIGO

__all__ = {
    "RAW_DATASETS",
    "DATA_DIR",
    "CODIGO_MUNICIPIO",
    "MUNICIPIO_CODIGO",
    "CODIGO_DDR",
    "DDR_CODIGO",
}
