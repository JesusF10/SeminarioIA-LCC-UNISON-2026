# Notebooks

Aquí se encuentran los Jupyter Notebooks utilizados para la exploración de datos, análisis preliminares y
pruebas rápidas relacionadas con el proyecto. Estos notebooks contienen código, visualizaciones y anotaciones
que documentan el proceso de investigación y análisis llevado a cabo durante las diferentes fases del proyecto.

## Directorio de Datos:

Para facilitar la organización y el acceso a los datos, se recomienda mantener una estructura clara dentro del directorio `data/`, diferenciando entre datos crudos (`raw/`) y datos procesados (`processed

Para ello, se encuentra el script.py `data.py`, que contiene la variable `DATASET`, la cual es
la ruta al dataset que se utilizará en el proyecto.

```python
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
```
