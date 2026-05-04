# Guía de Uso: get_prod_data

## Descripción General

La función `get_prod_data` permite cargar y consolidar datos de producción
agrícola del Servicio de Información Agroalimentaria y Pesquera (SIAP) para
múltiples años. Trabaja exclusivamente con datos a nivel **municipal** de
Sonora (2003-2024).

## Firma de la Función

```python
def get_prod_data(
    years: tuple[int, int] | str | int,
    loc_name: str | Region = "all",
    crop_name: str | Crop = "all",
) -> pd.DataFrame
```

## Parámetros

### years (requerido)

Especifica los años de producción a cargar. Acepta los siguientes formatos:

- **tuple[int, int]**: Rango de años (ambos extremos inclusivos)
  - Ejemplo: `(2010, 2015)` carga 2010, 2011, 2012, 2013, 2014, 2015

- **str**:
  - Rango en formato estricto "YYYY-YYYY" (sin espacios)
    - Ejemplo: `"2010-2015"` carga 2010 hasta 2015
  - Año único como string
    - Ejemplo: `"2020"` carga solo 2020

- **int**: Un único año
  - Ejemplo: `2020` carga solo 2020

**Nota**: No se aceptan listas de años sueltos (ej. `[2010, 2015, 2020]`).
Para cargar años no consecutivos, haga múltiples llamadas.

### loc_name (opcional)

Filtra datos por municipio.

- **Valor por defecto**: `"all"`
- **Tipo**: `str | Region`

Opciones:

- `"all"`: Retorna datos de todos los municipios (sin filtrar)
- `str`: Nombre del municipio (ej. `"Hermosillo"`, `"Cajeme"`)
- `Region`: Objeto Region del módulo `seminario_ia.models`

**Importante**: No se aceptan códigos numéricos de municipio. Use siempre
el nombre o un objeto `Region`.

### crop_name (opcional)

Filtra datos por cultivo.

- **Valor por defecto**: `"all"`
- **Tipo**: `str | Crop`

Opciones:

- `"all"`: Retorna datos de todos los cultivos (sin filtrar)
- `str`: Nombre del cultivo (ej. `"Trigo grano"`, `"Maíz grano"`)
- `Crop`: Objeto Crop del módulo `seminario_ia.models`

**Importante**: No se aceptan códigos numéricos de cultivo. Use siempre
el nombre o un objeto `Crop`.

## Valor de Retorno

**Tipo**: `pd.DataFrame`

Retorna un DataFrame consolidado con los datos de producción agrícola. Si no
se encuentran archivos para los años especificados, o si los parámetros son
inválidos, retorna un DataFrame vacío.

### Estructura de Datos

#### Datos Municipales

Columnas disponibles:

| Columna           | Tipo  | Descripción                            |
| ----------------- | ----- | -------------------------------------- |
| Anio              | int   | Año de producción                      |
| Idddr             | int   | Código del DDR                         |
| Idmunicipio       | int   | Código del municipio (1-72)            |
| Nommunicipio      | str   | Nombre del municipio                   |
| Idciclo           | int   | Código del ciclo agrícola (1-5)        |
| Idmodalidad       | int   | Código de modalidad (1=Riego, 2=Temp.) |
| Idcultivo         | int   | Código del cultivo                     |
| Nomcultivo        | str   | Nombre del cultivo                     |
| Sembrada          | float | Superficie sembrada (hectáreas)        |
| Cosechada         | float | Superficie cosechada (hectáreas)       |
| Siniestrada       | float | Superficie siniestrada (hectáreas)     |
| Volumenproduccion | float | Volumen de producción                  |
| Rendimiento       | float | Rendimiento (ton/ha)                   |
| PMR               | float | Precio Medio Rural ($/ton)             |
| Valorproduccion   | float | Valor de la producción (miles de $)    |

## Ejemplos de Uso

### Ejemplo 1: Cargar un año específico

```python
from seminario_ia.datasets import get_prod_data

# Cargar datos de Sonora para 2020
df = get_prod_data(years=2020)

print(f"Registros cargados: {len(df)}")
print(f"Municipios únicos: {df['Nommunicipio'].nunique()}")
```

### Ejemplo 2: Cargar rango de años (tupla)

```python
# Cargar datos de 2015 a 2020
df = get_prod_data(years=(2015, 2020))

print(f"Años incluidos: {sorted(df['Anio'].unique())}")
```

### Ejemplo 3: Cargar rango de años (string)

```python
# Equivalente usando string en formato estricto "YYYY-YYYY"
df = get_prod_data(years="2015-2020")

print(f"Años incluidos: {sorted(df['Anio'].unique())}")
```

### Ejemplo 4: Filtrar por municipio (nombre)

```python
# Usar nombre de municipio
df_hmo = get_prod_data(
    years=(2015, 2020),
    loc_name="Hermosillo",
)

print(f"Registros de Hermosillo: {len(df_hmo)}")
print(f"Cultivos en Hermosillo: {df_hmo['Nomcultivo'].nunique()}")
```

### Ejemplo 5: Filtrar por municipio (objeto Region)

```python
from seminario_ia.datasets import get_prod_data, get_mun_coordinates
from seminario_ia.models import Region

# Obtener coordenadas del municipio
coords = get_mun_coordinates("Cajeme")
if not coords.empty:
    row = coords.iloc[0]
    region = Region(
        name="Cajeme",
        latitude=row["lat"],
        longitude=row["lon"],
        altitude=row["z_m"],
    )

    df = get_prod_data(
        years=(2018, 2023),
        loc_name=region,
    )

    print(f"Registros de Cajeme: {len(df)}")
```

### Ejemplo 6: Análisis por cultivo

```python
# Cargar datos recientes de Hermosillo
df = get_prod_data(
    years=(2018, 2023),
    loc_name="Hermosillo",
)

# Analizar principales cultivos
top_cultivos = df.groupby('Nomcultivo').agg({
    'Volumenproduccion': 'sum',
    'Valorproduccion': 'sum',
    'Cosechada': 'sum'
}).sort_values('Valorproduccion', ascending=False).head(10)

print(top_cultivos)
```

### Ejemplo 7: Filtrar por cultivo específico

```python
# Cargar datos de trigo para múltiples años
df_trigo = get_prod_data(
    years=(2018, 2023),
    crop_name="Trigo grano",
)

print(f"Municipios productores de trigo: {df_trigo['Nommunicipio'].nunique()}")
print(f"Producción total de trigo: {df_trigo['Volumenproduccion'].sum()}")
```

### Ejemplo 8: Filtrar por cultivo y municipio

```python
# Analizar producción de trigo en Hermosillo
df = get_prod_data(
    years=(2015, 2023),
    loc_name="Hermosillo",
    crop_name="Trigo grano",
)

# Ver evolución temporal
evolucion = df.groupby('Anio')['Volumenproduccion'].sum()
print(evolucion)
```

### Ejemplo 9: Usar objeto Crop para filtrar

```python
from seminario_ia.datasets import get_prod_data, get_crop_data

# Obtener objeto Crop
trigo = get_crop_data("Trigo grano")

# Usar objeto Crop como filtro
df = get_prod_data(
    years=2020,
    crop_name=trigo,
)

print(f"Registros de trigo: {len(df)}")
```

### Ejemplo 10: Comparación temporal

```python
# Cargar datos de dos periodos
df_2003_2008 = get_prod_data(years=(2003, 2008))
df_2018_2023 = get_prod_data(years=(2018, 2023))

# Comparar producción total
prod_temprana = df_2003_2008['Volumenproduccion'].sum()
prod_reciente = df_2018_2023['Volumenproduccion'].sum()

cambio = ((prod_reciente - prod_temprana) / prod_temprana) * 100
print(f"Cambio en producción: {cambio:.2f}%")
```

## Manejo de Archivos Faltantes

La función es robusta ante archivos faltantes. Si algún año especificado no
tiene archivo correspondiente, ese año se omite silenciosamente y se
continúa con los demás.

```python
# Si 2014 no existe, cargará 2013, 2015, 2016
df = get_prod_data(years=(2013, 2016))

# Verificar qué años se cargaron realmente
print(f"Años disponibles: {sorted(df['Anio'].unique())}")
```

Si ningún año tiene archivo, retorna un DataFrame vacío:

```python
df = get_prod_data(years=9999)
print(df.empty)  # True
```

## Parámetros Inválidos

La función retorna un DataFrame vacío cuando los parámetros son inválidos:

```python
# Lista de años (no soportado)
df = get_prod_data(years=[2010, 2015, 2020])
print(df.empty)  # True

# Código numérico de municipio (no soportado)
df = get_prod_data(years=2020, loc_name=30)
print(df.empty)  # True

# Código numérico de cultivo (no soportado)
df = get_prod_data(years=2020, crop_name=9050000)
print(df.empty)  # True

# Rango con espacios (formato inválido)
df = get_prod_data(years="2015 - 2020")
print(df.empty)  # True
```

## Notas Técnicas

### Ubicación de Archivos

Los archivos se cargan desde:

```
data/processed/siap_produccion/
└── sonora/          # Datos municipales (2003-2024)
    └── cierre_agricola_sonora_YYYY.csv
```

### Convenciones de Nomenclatura

- Archivos municipales: `cierre_agricola_sonora_YYYY.csv`

La función usa glob patterns para buscar archivos que contengan el año, por
lo que es flexible a variaciones menores en el nombre.

### Rendimiento

Para cargar múltiples años, la función:

1. Lee cada archivo CSV individualmente
2. Los concatena usando `pd.concat()`
3. Filtra por municipio y cultivo si se especifican

Para grandes rangos de años, considere:

- Filtrar por municipio para reducir memoria
- Seleccionar columnas específicas después de cargar
- Procesar en lotes si trabaja con el rango completo

## Funciones Relacionadas

- `load_prod_file(year)`: Función auxiliar que carga un solo año
- `get_mun_code()`: Obtiene códigos de municipios
- `get_mun_coordinates()`: Obtiene coordenadas de municipios
- `get_crop_data(name)`: Obtiene información de cultivos (objeto Crop)
- `get_cycle_code()`: Obtiene códigos de ciclos agrícolas
- `get_mod_code()`: Obtiene códigos de modalidades

## Referencia Rápida

```python
# Un año
df = get_prod_data(2020)

# Rango con tupla
df = get_prod_data((2015, 2020))

# Rango con string (formato estricto)
df = get_prod_data("2015-2020")

# Municipio específico (por nombre)
df = get_prod_data((2015, 2020), loc_name="Hermosillo")

# Cultivo específico (por nombre)
df = get_prod_data((2015, 2020), crop_name="Trigo grano")

# Municipio y cultivo específicos
df = get_prod_data(
    (2015, 2020),
    loc_name="Hermosillo",
    crop_name="Trigo grano",
)

# Usando objeto Region
from seminario_ia.models import Region
region = Region(name="Cajeme", latitude=..., longitude=..., altitude=...)
df = get_prod_data((2015, 2020), loc_name=region)

# Usando objeto Crop
from seminario_ia.datasets import get_crop_data
trigo = get_crop_data("Trigo grano")
df = get_prod_data((2015, 2020), crop_name=trigo)
```

---
