# Data

Este directorio centraliza todas las fuentes de datos necesarias para el
análisis de reconversión productiva en Sonora. Los datos se dividen en
estados de procesamiento: `raw` (originales) y `processed` (limpios).

## Estructura de Directorios

### 1. Datos Proporcionados (`data/raw/datos_proporcionados/`)

Información estratégica entregada por supervisores o consolidada por el equipo.
Origen: [INIFAP](https://www.gob.mx/inifap) / [FIRA](https://www.fira.gob.mx/).

```bash
datos_proporcionados/
├── PUS-TRIGO-2024-25-AMBAS-VAR-UNISON.xlsx # Permisos única siembra
├── manual-tecnico-cultivos-sonora-2024.csv  # Láminas/Costos (Consolidado)
├── reporte-repna-1.csv                      # Concesiones Agua (REPDA)
├── reporte-repna-2.csv                      # Concesiones Agua (REPDA)
└── tecnificacion-riego-invernadores_DDR_2021.xlsx # Infraestructura DDR
```

### 2. SIAP Producción Agrícola (`data/raw/siap-produccion-agricola/`)

Estadísticas oficiales del SIAP. Origen: [SIAP Datos Abiertos](https://nube.agricultura.gob.mx/datosAbiertos/Agricola.php).

```bash
siap-produccion-agricola/
├── municipal/
│   ├── cierre_agricola_sonora_2003..2024.csv # Series de tiempo Sonora
│   └── Diccionario_agricola_2003_a_2023.xlsx
├── nacional/
│   ├── Cierre_agricola_1980..2002.csv        # Referencia histórica Nac.
│   └── Diccionario_agricola_1980_a_2002.xlsx
└── no-seguimiento/                           # Cultivos emergentes
    ├── NoSeguimiento_cierre_agricola_2020..2021.csv
    └── NoSeguimiento_diccionario_agricola_2020_a_2021.xlsx
```

### 3. Datos Abiertos de Sonora (`data/raw/datos-abiertos/`)

Información gubernamental estatal. Origen: [Portal Datos Sonora](https://www.sonora.gob.mx/datos).

```bash
datos-abiertos/
├── agricultura/
│   └── datos/
│       └── Agricultura Sonora año 1999..2023.xlsx # Anuarios estatales
└── recursos-hidricos/
    └── datos/
        └── Datos hídricos 1941..2024.xlsx # Almacenamiento de presas
```

### 4. Datos de Sequía (`data/raw/datos-sequia/`)

Información geoespacial municipalizada. Origen: [Datos Abiertos Gob Mx](https://www.datos.gob.mx/dataset/?groups=agricultura&page=4).

```bash
datos-sequia/
├── impacto_sequia.shp  # Capa vectorial (ISAG)
└── impacto_sequia.shx, .dbf, .prj, .cpg # Archivos de soporte SIG
```

## Resumen de Fuentes Principales

| Dataset       | Periodo   | Origen                                                                | Variables Clave                   |
| :------------ | :-------- | :-------------------------------------------------------------------- | :-------------------------------- |
| **SIAP Mun.** | 2003-2024 | [SIAP](https://nube.agricultura.gob.mx/datosAbiertos/Agricola.php)    | Sembrada, Cosechada, PMR, Valor.  |
| **Hídricos**  | 1941-2024 | [Sonora](https://www.sonora.gob.mx/datos)                             | Almacenamiento (hm3), Fecha.      |
| **REPNA**     | Actual    | [SIAP](https://nube.agricultura.gob.mx/datosAbiertos/Agricola.php)    | Volumen Extracción (Sup/Sub).     |
| **Manual**    | 2024      | [INIFAP](https://www.gob.mx/inifap)                                   | Lámina (mm), Costo ($/ha), Ciclo. |
| **Sequía**    | Reciente  | [Gob.mx](https://www.datos.gob.mx/dataset/?groups=agricultura&page=4) | Impacto (ISAG), Geometría (SHP).  |

## Guía de Uso

1. **Unidades:** Superficie en Ha, producción en Ton, volúmenes en hm3,
   láminas en mm y costos en MXN.
2. **Cruce de Datos:** El campo de unión principal es `CVE_MUN` (Clave INEGI).
3. **Diccionarios:** Consultar archivos `Diccionario.csv` o `.xlsx`
   para definiciones exactas.
