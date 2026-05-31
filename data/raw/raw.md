# Datos Raw

## Fuentes de datos

- [SIAP - Servicio de Información Agroalimentaria y Pesquera](https://nube.agricultura.gob.mx/datosAbiertos/Agricola.php)
- [Datos Abiertos Gob Mx (Sequía)](https://www.datos.gob.mx/dataset/?groups=agricultura&page=4)
- [INIFAP / FIRA (Manual Técnico 2024)](https://www.gob.mx/inifap)
- Datos proporcionados por los supervisores del proyecto (Tecnificación de Riego, Trigo 2024-25)

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
