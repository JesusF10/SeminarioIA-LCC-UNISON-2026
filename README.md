# SeminarioIA-LCC-UNISON-2026

Repositorio para la clase de Seminario de Inteligencia Artificial para la Licenciatura en
Ciencias de la Computación de la Universidad de Sonora.

## Introducción

Las principales actividades económicas primarias realizadas en el estado de Sonora incluyen
a la Agricultura, Ganadería, Pesca y Minería. Con respecto a la primera, actualmente una
gran cantidad de agua es utilizada por los agricultores para su trabajo en los campos.

El estado de Sonora presenta condiciones climáticas desérticas, e históricamente ha
enfrentado varias sequías. Es por esto que es necesario enfocarnos en el problema de la
utilización óptima de sus recursos hídricos.

De los diferentes cultivos que se cosechan en el estado hay algunos que destacan por su
necesidad de grandes cantidades de agua. Con este trabajo se intenta encontrar alternativas
más viables para los cultivos actuales. Es decir, alternativas que optimicen el uso del
agua y, a su vez, la rentabilidad de los mismos. Con el análisis efectuado, se busca apoyar
a los agricultores de Sonora con dichas alternativas.

## Objetivo General

> Conversión de los cultivos de Sonora por otros que optimicen el uso del agua y su
> rentabilidad, en apoyo a los agricultores.

## Contenido del repositorio

```bash
SeminarioIA-LCC-UNISON-2026/
├── data/
│   ├── raw/            # Datos originales
│   ├── processed/      # Datos limpios listos para modelar
├── docs/               # Documentos, PDFs a leer, referencias bibliográficas, etc.
├── notebooks/          # Jupyter Notebooks para exploración y pruebas rápidas
├── src/                # Código fuente (scripts .py)
│   ├── extraction/     # Scripts para leer fuentes y cargar datos
│   ├── analysis/       # Lógica de análisis de datos
│   └── visualization/  # Generación de gráficas
├── reports/            # Borradores del informe final
├── .gitignore          # Gitignore
└── README.md           # Explicación del proyecto
```

## Metodología

### FASE 1. EXPLORACIÓN Y DIAGNÓSTICO.

Entendimiento general de la agricultura en Sonora y recopilación de información relevante de
fuentes oficiales.

### FASE 2. ANÁLISIS DE MERCADO Y RENTABILIDAD.

Recopilación de datos pertinentes para la propuesta de optimización en rentabilidad y
sostenibilidad en cultivos de Sonora, con enfoque en los recursos hídricos utilizados.

### FASE 3. ANÁLISIS TÉCNICO Y VIABILIDAD.

Análisis técnico exhaustivo de los datos recopilados, realizando estimaciones y clasificaciones
con prioridad en la viabilidad, rentabilidad y disponibilidad, entre otros factores.

### FASE 4. CONCLUSIÓN Y RECOMENDACIÓN.

Consolidación de los datos de Mercado, Rentabilidad y Viabilidad Técnica/Agua y la elaboración
del informe final.

## Cronograma (Fase Actual)

### FASE 1: EXPLORACIÓN Y DIAGNÓSTICO

| Semana     | Fechas         | Objetivo de la Semana                | Actividades Clave                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------- | -------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Semana 1-2 | 19 Feb - 4 Mar | Entender el problema y el territorio | • **Zonificación:** Identificar los distritos de riego/temporal de Sonora. Conseguir mapas básicos.<br>• **Cultivo actual:** Investigar a fondo el trigo y otros cultivos en el estado: ¿dónde se siembra?, ¿qué variedades?, ¿cómo es el ciclo (siembra-cosecha)?<br>• **Primer contacto:** Hacer una lista de posibles fuentes de datos confiables y extracción de información (SIAT, INIFAP, SADER).                                                                                                                                                                                                     |
| Semana 3   | 5 Mar - 11 Mar | Investigación de alternativas        | • **Lluvia de ideas:** Basados en la búsqueda de información de los cultivos en Sonora, buscar otras opciones como sorgo, frijol, variantes del trigo, o cultivos forrajeros, además de considerar otros cultivos de regiones con condiciones similares a las del estado (canola, cártamo, girasol, maíz, hortalizas).<br>• **Filtro rápido:** Para cada cultivo, investigar: ciclo, requerimientos de agua (mm por ciclo), temperatura ideal, y si se ha cultivado antes en la región.<br>• **Fuentes clave:** Buscar páginas confiables con datos abiertos de instituciones (SIAT, INIFAP, SADER, AOANS). |

## Datos

Revisar `data/raw` para los datos obtenidos.

```
data/raw
├── datos-abiertos
│   ├── agricultura
│   │   └── datos
│   └── recursos-hidricos
│       └── datos
├── datos_proporcionados
├── datos-sequia
└── siap-produccion-agricola
    ├── municipal
    ├── nacional
    └── no-seguimiento
```

### Espacio Compartido Multiusos

Para facilitar la colaboración, se ha creado un espacio compartido en Google Drive
para subir archivos, compartir documentos y mantener un registro de las actividades del proyecto.

[**Carpeta de Drive**](https://drive.google.com/drive/folders/1uUxQb10JEHVp5kOcSslYLTTxHoU8rSpx?usp=drive_link)

## Development

Para trabajar en el proyecto, se recomienda seguir la estructura de carpetas propuesta.
Para cada fase del proyecto, se pueden crear scripts específicos en la carpeta `src`
para la extracción, análisis y visualización de datos.

### Herramientas recomendadas

- **Python** 3.10 o superior
- [**UV**](https://docs.astral.sh/uv/) para gestión de dependencias y entornos virtuales.
- Jupyter Notebooks para exploración y análisis rápido.
- Librerías: pandas, numpy, matplotlib, etc.

Nota: las librerías específicas pueden variar según las necesidades del análisis,
pero se recomienda mantener un entorno de desarrollo organizado y documentado.

Se adjunta un archivo `pyproject.toml` con la configuración del proyecto y las
dependencias necesarias para facilitar la instalación y gestión del entorno de desarrollo.

```bash

...
dependencies = [
    "numpy>=1.21.0",
    "pandas>=1.3.0",
    "matplotlib>=3.4.0",
    "PyYAML>=6.0",
    "tqdm>=4.60.0",
    "pydantic>=2.12.4",
    "openpyxl>=3.1.5",
    "polars>=1.38.1",
]

[dependency-groups]
dev = [
    "ruff>=0.1.0",
    "pre-commit>=2.15.0",
    "ty>=0.0.6",
]

[project.optional-dependencies]
jupyter = [
    "jupyter>=1.0.0",
    "ipykernel>=6.0.0",
    "ipywidgets>=7.6.0",
]
...

```

### Uso de UV

#### Para instalar dependencias

Para instalar las dependencias del proyecto, se puede usar el siguiente comando:

```bash
uv sync --no-dev
```

Para instalar las dependencias de desarrollo, se puede usar:

```bash
uv sync --dev
```

Para instalar las dependencias opcionales para Jupyter, se puede usar:

```bash
uv sync --extra jupyter
```

Para instalar todas las dependencias (incluyendo desarrollo y opcionales), se puede usar:

```bash
uv sync --dev --extra jupyter
```

o

```bash
uv sync --all
```

#### Para correr un script

Para ejecutar un script específico, se puede usar el siguiente comando:

```bash
uv run python mi_script.py
```

Para utilizar `Ruff`:

```bash
uv run ruff check src/ # Revisa el código en la carpeta src
```

### Workflow sugerido

#### Obtener el repositorio

- **Fork** del repositorio para trabajar en tu propia copia.
- Clonar tu fork localmente.
  Por ejemplo, con SSH (depende de cómo tengas configurado tu acceso a GitHub):

```bash
git clone git@github.com:JesusF10/SeminarioIA-LCC-UNISON-2026.git
```

- Pueden trabajar con la rama principal (`main`).

#### Guardar y actualizar cambios

- Realizar cambios en tu entorno local.

```bash
git add . # Agrega los archivos modificados al staging
```

- Hacer commit de los cambios con un mensaje descriptivo.

```bash
git commit -m "Descripción de los cambios realizados"
```

- Subir los cambios a tu fork en GitHub.

```bash
git push origin main
```

- En GitHub, crear un Pull Request desde tu fork hacia el repositorio original
  para que los cambios sean revisados e integrados.

## Src

> Código fuente a utilizar

## Notebooks

> Notebooks correspondientes

## Referencias

- [Plan de trabajo](docs/PlanDeTrabajo.pdf)
- [Presentación Reconversión Productiva (18 de Febrero de 2026)](docs/Presentaciom-DEyT-Reconversion-productiva_18FEB2026.pdf)
- [Datos Abiertos](https://www.sonora.gob.mx/datos/)
- [Anuario Estadístico de la Producción Agrícola (SIAP)](https://nube.agricultura.gob.mx/cierre_agricola/)
- [FIRA - Agrocostos (Costos de Producción 2024-2025)](https://www.fira.gob.mx/InfraestructuraWeb/AnexosStatico.jsp?IdAnexo=7372)
- [INIFAP - Paquetes Tecnológicos y Requerimientos Hídricos](https://www.gob.mx/inifap)
- [CONAGUA - Almacenamiento de Presas](https://www.gob.mx/conagua)
