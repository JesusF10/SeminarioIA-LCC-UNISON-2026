# SeminarioIA-LCC-UNISON-2026

Repositorio para la clase de Seminario de Inteligencia Artificial para la Licenciatura en Ciencias de la Computación de la Universidad de Sonora.

## Introducción

Las principales actividades económicas primarias realizadas en el estado de Sonora incluyen a la Agricultura, Ganadería, Pesca y Minería. Con respecto a la primera, actualmente una gran cantidad de agua es utilizada por los agricultores para su trabajo en los campos.

El estado de Sonora presenta condiciones climáticas desérticas, e históricamente ha enfrentado varias sequías. Es por esto que es necesario enfocarnos en el problema de la utilización óptima de sus recursos hídricos.

De los diferentes cultivos que se cosechan en el estado hay algunos que destacan por su necesidad de grandes cantidades de agua. Con este trabajo se intenta encontrar alternativas más viables para los cultivos actuales. Es decir, alternativas que optimicen el uso del agua y, a su vez, la rentabilidad de los mismos. Con el análisis efectuado, se busca apoyar a los agricultores de Sonora con dichas alternativas.

## Objetivo General

> Conversión de los cultivos de Sonora por otros que optimicen el uso del agua y su rentabilidad, en apoyo a los agricultores.

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

Entendimiento general de la agricultura en Sonora y recopilación de información relevante de fuentes oficiales.

### FASE 2. ANÁLISIS DE MERCADO Y RENTABILIDAD.

Recopilación de datos pertinentes para la propuesta de optimización en rentabilidad y sostenibilidad en cultivos de Sonora, con enfoque en los recursos hídricos utilizados.

### FASE 3. ANÁLISIS TÉCNICO Y VIABILIDAD.

Análisis técnico exhaustivo de los datos recopilados, realizando estimaciones y clasificaciones con prioridad en la viabilidad, rentabilidad y disponibilidad, entre otros factores.

### FASE 4. CONCLUSIÓN Y RECOMENDACIÓN.

Consolidación de los datos de Mercado, Rentabilidad y Viabilidad Técnica/Agua y la elaboración del informe final.

## Cronograma (Fase Actual)

### FASE 1: EXPLORACIÓN Y DIAGNÓSTICO

| Semana     | Fechas         | Objetivo de la Semana                | Actividades Clave                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------- | -------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Semana 1-2 | 19 Feb - 4 Mar | Entender el problema y el territorio | • **Zonificación:** Identificar los distritos de riego/temporal de Sonora. Conseguir mapas básicos.<br>• **Cultivo actual:** Investigar a fondo el trigo y otros cultivos en el estado: ¿dónde se siembra?, ¿qué variedades?, ¿cómo es el ciclo (siembra-cosecha)?<br>• **Primer contacto:** Hacer una lista de posibles fuentes de datos confiables y extracción de información (SIAT, INIFAP, SADER).                                                                                                                                                                                                     |
| Semana 3   | 5 Mar - 11 Mar | Investigación de alternativas        | • **Lluvia de ideas:** Basados en la búsqueda de información de los cultivos en Sonora, buscar otras opciones como sorgo, frijol, variantes del trigo, o cultivos forrajeros, además de considerar otros cultivos de regiones con condiciones similares a las del estado (canola, cártamo, girasol, maíz, hortalizas).<br>• **Filtro rápido:** Para cada cultivo, investigar: ciclo, requerimientos de agua (mm por ciclo), temperatura ideal, y si se ha cultivado antes en la región.<br>• **Fuentes clave:** Buscar páginas confiables con datos abiertos de instituciones (SIAT, INIFAP, SADER, AOANS). |

## Data

Revisar `data/raw` para los datos obtenidos.

```
data/raw
├── datos-abiertos
│   ├── agricultura
│   │   └── datos
│   └── recursos-hidricos
│       └── datos
└── datos_proporcionados
```

## Src

> Código fuente a utilizar

## Notebooks

> Notebooks correspondientes

## Referencias

- [Plan de trabajo](docs/PlanDeTrabajo.pdf)
- [Presentación Reconversión Productiva (18 de Febrero de 2026)](docs/Presentaciom-DEyT-Reconversion-productiva_18FEB2026.pdf)
- [Datos Abiertos](https://www.sonora.gob.mx/datos/)
- [Anuario Estadístico de la Producción Agrícola](https://nube.agricultura.gob.mx/cierre_agricola/)
