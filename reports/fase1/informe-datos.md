# Reporte de Análisis de Datos Recabados (Fase 1)

Este informe presenta un análisis detallado de los datos recopilados durante
la Fase 1 (Exploración y Diagnóstico) del proyecto de reconversión de cultivos
en el estado de Sonora. El objetivo es identificar la información disponible
y su alineación con las metas planteadas en el cronograma.

## 1. Contexto del Proyecto

El proyecto busca alternativas de cultivos para Sonora que optimicen el uso
de recursos hídricos y mejoren la rentabilidad de los agricultores,
enfrentando los retos de las condiciones climáticas desérticas e históricas
sequías del estado.

## 2. Inventario Detallado de Datos (`data/raw`)

### 2.1. Datos Proporcionados (`datos_proporcionados/`)

Esta carpeta contiene archivos estratégicos para el análisis actual.

- **`manual-tecnico-cultivos-sonora-2024.csv` (NUEVO):**
  - **Contenido:** Parámetros técnicos para 22 cultivos clave (Granos,
    Hortalizas, Frutales y Perennes).
  - **Relevancia:** Datos de láminas de riego (mm), costos de producción ($/ha)
    y rendimientos. Habilita el análisis comparativo de ahorro hídrico.
- **`PUS-TRIGO-2024-25-AMBAS-VAR-UNISON.xlsx`:**
  - **Contenido:** Permisos de Única Siembra del ciclo actual. Incluye
    `VARIEDAD`, `SUPERFICIE`, `FUENTE_RIEGO` y `TECNOLOGIA`.
- **`tecnificacion-riego-invernadores_DDR_2021.xlsx`:**
  - **Contenido:** Estadísticas de riego tecnificado por Distrito de
    Desarrollo Rural (DDR).
- **`reporte-repna-1.csv` y `reporte-repna-2.csv`:**
  - **Contenido:** Listado de concesiones del Registro Público de Derechos de
    Agua. Detalla volúmenes permitidos de extracción.

### 2.2. SIAP - Producción Agrícola (`siap-produccion-agricola/`)

Es la fuente más extensa de series temporales sobre producción.

- **`municipal/`**:
  - **Contenido:** Cierres agrícolas de Sonora de 2003 a 2024. Variables:
    `Sembrada`, `Cosechada`, `Siniestrada`, `PMR` (Precio Medio Rural) y
    `Valorproduccion`.
- **`nacional/`**:
  - **Contenido:** Datos históricos de 1980 a 2002 a nivel nacional.
- **`no-seguimiento/`**:
  - **Contenido:** Datos de cultivos que no tienen un seguimiento estadístico
    regular (cultivos nicho o emergentes).

### 2.3. Datos Abiertos de Sonora (`datos-abiertos/`)

Información proveniente directamente del portal del gobierno estatal.

- **`agricultura/`**:
  - **Contenido:** Anuarios estatales de 1999 a 2023.
- **`recursos-hidricos/`**:
  - **Contenido:** Datos de almacenamiento de presas desde 1941 (hm3).

### 2.4. Datos de Sequía (`datos-sequia/`)

- **Contenido:** Shapefiles del impacto de la sequía a nivel municipal.
  Contiene el Índice de Severidad de Sequía Agrícola (ISAG).

## 3. Análisis Técnico de Variables Principales

| Categoría          | Variable      | Significado Técnico                            |
| :----------------- | :------------ | :--------------------------------------------- |
| **Identificación** | `CVE_MUN`     | Clave única municipal para cruce de datos.     |
| **Hídricos**       | `Lámina (mm)` | Consumo de agua por ciclo (Requerimiento).     |
| **Producción**     | `Rendimiento` | Toneladas por hectárea (Eficiencia).           |
| **Económicos**     | `PMR`         | Ingreso bruto por tonelada para el agricultor. |
| **Riesgo**         | `Siniestrada` | Indicador de resiliencia climática.            |

---

_Reporte finalizado en Marzo 2026_
