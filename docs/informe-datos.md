---
title: "Informe de datos recolectados - Fase 1"
author: "Reconversión de Cultivos en Sonora"
date: \today
geometry: margin=0.8in
fontsize: 10pt
lang: es
header-includes:
  - \newcommand{\pandocbounded}[1]{#1}
---

# Reporte de Análisis de Datos Recabados (Fase 1)

Este informe presenta un análisis detallado de los datos recopilados durante las primeras tres semanas del proyecto de reconversión de cultivos en el estado de Sonora. El objetivo principal es identificar la información disponible, su significado técnico y su alineación con las metas planteadas en el cronograma de la Fase 1.

## 1. Contexto del Proyecto

El proyecto busca alternativas de cultivos para Sonora que optimicen el uso de recursos hídricos y mejoren la rentabilidad de los agricultores, enfrentando los retos de las condiciones climáticas desérticas e históricas sequías del estado.

## 2. Inventario Detallado de Datos (`data/raw`)

A continuación se detalla el contenido y la relevancia de cada una de las fuentes de datos identificadas en el directorio raíz de datos crudos.

### 2.1. Datos Proporcionados (`datos_proporcionados/`)

Esta carpeta contiene archivos específicos de alta relevancia estratégica para el análisis actual del trigo y la infraestructura hídrica.

- **`PUS-TRIGO-2024-25-AMBAS-VAR-UNISON.xlsx`**:
  - **Contenido:** Detalle de los Permisos de Única Siembra para el ciclo actual. Incluye campos como `VARIEDAD`, `SUPERFICIE`, `FUENTE_RIEGO` (Pozo, Gravedad), `TIPO_RIEGO` e incluso el nivel de `TECNOLOGIA` aplicado.
  - **Relevancia:** Es la "línea base" para entender qué se está sembrando hoy mismo, bajo qué condiciones tecnológicas y con qué fuentes de agua.
- **`tecnificacion-riego-invernadores_DDR_2021.xlsx`**:
  - **Contenido:** Estadísticas de hectáreas bajo riego tecnificado comparadas con el total de superficie en operación por Distrito de Desarrollo Rural.
  - **Relevancia:** Permite identificar qué distritos (como Caborca o Hermosillo) están más avanzados en eficiencia hídrica y cuáles requieren mayor intervención.
- **`reporte-repna-1.csv` y `reporte-repna-2.csv`**:
  - **Contenido:** Listado de concesiones del Registro Público de Derechos de Agua. Detalla el `Titular`, el `Uso` (filtrado para Agrícola) y los volúmenes anuales permitidos de extracción de aguas `Superficiales` y `Subterráneas`.
  - **Relevancia:** Crucial para cruzar la demanda teórica de los cultivos con la oferta legal de agua permitida en cada zona.

### 2.2. SIAP - Producción Agrícola (`siap-produccion-agricola/`)

Es la fuente más extensa de series temporales sobre producción.

- **`municipal/`**:
  - **Contenido:** Cierres agrícolas de Sonora de 2003 a 2024. Variables: `Sembrada`, `Cosechada`, `Siniestrada`, `Volumenproduccion`, `Rendimiento`, `Preciomediorural` (PMR) y `Valorproduccion`.
  - **Relevancia:** Permite realizar análisis de tendencias de 20 años para identificar qué cultivos han sido rentables y cuáles han sufrido más siniestros por clima o falta de agua.
- **`nacional/`**:
  - **Contenido:** Datos históricos de 1980 a 2002 a nivel nacional.
  - **Relevancia:** Sirve de referencia histórica para entender cambios de largo plazo en la vocación agrícola de Sonora tras la implementación de tratados comerciales o cambios climáticos.
- **`no-seguimiento/`**:
  - **Contenido:** Datos de cultivos que no tienen un seguimiento estadístico regular.
  - **Relevancia:** Útil para identificar cultivos "nicho" o emergentes que podrían ser candidatos a la reconversión pero que no aparecen en las estadísticas principales.

### 2.3. Datos Abiertos de Sonora (`datos-abiertos/`)

Información proveniente directamente del portal del gobierno estatal.

- **`agricultura/`**:
  - **Contenido:** Anuarios de 1999 a 2023. Aunque similares al SIAP, estos datos a menudo incluyen detalles específicos de la administración estatal y validaciones locales.
  - **Relevancia:** Validación cruzada con los datos federales del SIAP para asegurar la integridad de la información.
- **`recursos-hidricos/`**:
  - **Contenido:** Datos de almacenamiento de presas desde 1941. Variables principales: `Clave` (de la presa), `Fecha` y `Almacenamiento (hm3)`.
  - **Relevancia:** Permite correlacionar los ciclos de sequía con la reducción en la superficie sembrada de cultivos de alto consumo (como el trigo o la alfalfa).

### 2.4. Datos de Sequía (`datos-sequia/`)

- **Contenido:** Archivos vectoriales (Shapefiles) del "Mapa de Impacto de la sequía sobre la actividad agrícola".
- **Relevancia:** Al estar georeferenciados a nivel municipal, permiten realizar análisis espaciales para identificar qué municipios están en "zonas críticas" donde la reconversión no es opcional, sino urgente.

---

## 3. Análisis Técnico de Variables Principales

| Categoría          | Variable           | Tipo     | Significado Técnico                               |
| :----------------- | :----------------- | :------- | :------------------------------------------------ |
| **Identificación** | `Nomddr` / `NDDR`  | Texto    | Distrito de Desarrollo Rural (Gestión).           |
|                    | `Nommunicipio`     | Texto    | Unidad político-administrativa del cultivo.       |
| **Producción**     | `Sembrada`         | Numérico | Hectáreas comprometidas al inicio del ciclo.      |
|                    | `Siniestrada`      | Numérico | Hectáreas perdidas (indicador de riesgo).         |
|                    | `Rendimiento`      | Numérico | Toneladas por hectárea (indicador de eficiencia). |
| **Económicos**     | `Preciomediorural` | Numérico | Ingreso bruto por tonelada para el agricultor.    |
|                    | `Valorproduccion`  | Numérico | Impacto económico total del cultivo.              |
| **Hídricos**       | `Almacenamiento`   | Numérico | Disponibilidad de agua en presas (hm3).           |
|                    | `Vol. Extracción`  | Numérico | Capacidad legal de uso de agua (m3).              |

---
