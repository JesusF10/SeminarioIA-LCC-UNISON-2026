# Datos Raw

## Fuentes de datos

- [Datos Abiertos Sonora](https://www.sonora.gob.mx/datos)
- [SIAP - Servicio de Información Agroalimentaria y Pesquera](https://nube.agricultura.gob.mx/datosAbiertos/Agricola.php)
- [Datos Abiertos Gob Mx (Sequía)](https://www.datos.gob.mx/dataset/?groups=agricultura&page=4)
- [INIFAP / FIRA (Manual Técnico 2024)](https://www.gob.mx/inifap)
- Datos proporcionados por los supervisores del proyecto (Tecnificación de
  Riego, Trigo 2024-25)

## Lista de datos obtenidos

#### Datos Proporcionados

Se encuentran en el directorio `datos_proporcionados`.

- **Datos REPNA (Concesiones Agua)**

```bash
reporte-repna-1.csv
reporte-repna-2.csv
```

- **Datos de la Tecnificación de Riego**

```bash
tecnificacion-riego-invernadores_DDR_2021.xlsx
```

- **Datos Trigo 2024-25**

```bash
PUS-TRIGO-2024-25-AMBAS-VAR-UNISON.xlsx
```

- **Manual Técnico de Cultivos 2024 (NUEVO)**

```bash
manual-tecnico-cultivos-sonora-2024.csv # Láminas de riego, costos y ciclos
```

#### Datos SIAP

Se encuentran en el directorio `siap-produccion-agricola`.

- **Datos Municipales (de Sonora)**

```bash
municipal
├── cierre_agricola_sonora_2003.csv
├── cierre_agricola_sonora_2004.csv
...
├── cierre_agricola_sonora_2024.csv
└── Diccionario_agricola_2003_a_2023.xlsx
```

- **Datos Nacionales**

```bash
nacional
├── Cierre_agricola_1980.csv
├── Cierre_agricola_1981.csv
...
├── Cierre_agricola_2001.csv
├── Cierre_agricola_2002.csv
└── Diccionario_agricola_1980_a_2002.xlsx
```

- **Datos No Seguimiento**

```bash
no-seguimiento
├── NoSeguimiento_cierre_agricola_2020.csv
├── NoSeguimiento_cierre_agricola_2021.csv
└── NoSeguimiento_diccionario_agricola_2020_a_2021.xlsx
```

#### Datos Abiertos de Sonora

Se encuentran en el directorio `datos-abiertos`.

- **Recursos hídricos**

```bash
recursos-hidricos
├── Catalogo.xlsx
├── datos
│   ├── Datos hídricos 1941-1949.xlsx
│   ├── Datos hídricos 1950-1959.xlsx
│   ├── Datos hídricos 1970-1979.xlsx
│   ├── Datos hídricos 1980-1989.xlsx
│   ├── Datos hídricos 1990-1999.xlsx
│   ├── Datos hídricos 2000-2009.xlsx
│   ├── Datos hídricos 2010-2019.xlsx
│   └── Datos hídricos 2020-2024.xlsx
└── Diccionario.csv
```

- **Agricultura**

```bash
agricultura
├── Catalogo.xlsx
├── datos
│   ├── Agricultura Sonora año 1999.xlsx
│   ├── Agricultura Sonora año 2000.xlsx
│   ├── Agricultura Sonora año 2001.xlsx
│   ├── Agricultura Sonora año 2002.xlsx
│   ├── Agricultura Sonora año 2003.xlsx
│   ├── Agricultura Sonora año 2004.xlsx
│   ├── Agricultura Sonora año 2005.xlsx
│   ├── Agricultura Sonora año 2006.xlsx
│   ├── Agricultura Sonora año 2007.xlsx
│   ├── Agricultura Sonora año 2008.xlsx
│   ├── Agricultura Sonora año 2009.xlsx
│   ├── Agricultura Sonora año 2010.xlsx
│   ├── Agricultura Sonora año 2011.xlsx
│   ├── Agricultura Sonora año 2012.xlsx
│   ├── Agricultura Sonora año 2013.xlsx
│   ├── Agricultura Sonora año 2014.xlsx
│   ├── Agricultura Sonora año 2015.xlsx
│   ├── Agricultura Sonora año 2016.xlsx
│   ├── Agricultura Sonora año 2017.xlsx
│   ├── Agricultura Sonora año 2018.xlsx
│   ├── Agricultura Sonora año 2019.xlsx
│   ├── Agricultura Sonora año 2020.xlsx
│   ├── Agricultura Sonora año 2021.xlsx
│   ├── Agricultura Sonora año 2022.xlsx
│   └── Agricultura Sonora año 2023.xlsx
└── Diccionario.csv
```

#### Datos Sequía (Georeferenciados)

Se encuentran en el directorio `datos-sequia`.

Corresponden a la base de datos denominada "Mapa de Impacto de la sequía sobre
la actividad agrícola", la cual se encuentra georeferenciada a nivel de
municipio.

**Nota:**

- Los datos se encuentran en formato Shapefile (SIG).
- Se requiere software como [QGIS](https://qgis.org/) para su visualización.

```bash
datos-sequia
├── impacto_sequia.cpg
├── impacto_sequia.dbf
├── impacto_sequia.prj
├── impacto_sequia.shp  # Capa de Índice ISAG
└── impacto_sequia.shx
```
