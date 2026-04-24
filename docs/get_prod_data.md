# Guía de Uso: get_prod_data

## Descripción General

La función `get_prod_data` permite cargar y consolidar datos de producción
agrícola del Servicio de Información Agroalimentaria y Pesquera (SIAP) para
múltiples años. Soporta dos niveles de agregación:

- **Municipal**: Datos de producción agrícola de Sonora por municipio
  (2003-2024)
- **Nacional**: Datos de producción agrícola por estado a nivel nacional
  (1980-2002)

## Firma de la Función

```python
def get_prod_data(
    years: tuple[int, int] | str | list[int],
    loc_name: str | int = "all",
    crop_name: str | int = "all",
    muni: bool = False,
) -> pd.DataFrame
```

## Parámetros

### years (requerido)

Especifica los años de producción a cargar. Acepta múltiples formatos:

- **tuple[int, int]**: Rango de años (ambos extremos inclusivos)
  - Ejemplo: `(2010, 2015)` carga 2010, 2011, 2012, 2013, 2014, 2015

- **str**: Rango en formato "año_inicio-año_fin"
  - Ejemplo: `"2010-2015"` carga 2010 hasta 2015

- **list[int]**: Lista explícita de años
  - Ejemplo: `[2010, 2012, 2015]` carga solo esos tres años

- **int**: Un único año
  - Ejemplo: `2020` carga solo 2020

### loc_name (opcional)

Filtra datos por ubicación. Solo aplica cuando `muni=True`.

- **Valor por defecto**: `"all"`
- **Tipo**: `str | int`

Opciones:

- `"all"`: Retorna datos de todos los municipios (sin filtrar)
- `int`: Código del municipio (ej. `30` para Hermosillo)
- `str`: Nombre del municipio (ej. `"Hermosillo"`)

**Nota**: Este parámetro se ignora cuando `muni=False` (datos nacionales).

### crop_name (opcional)

Filtra datos por cultivo. Aplica tanto para datos municipales como nacionales.

- **Valor por defecto**: `"all"`
- **Tipo**: `str | int`

Opciones:

- `"all"`: Retorna datos de todos los cultivos (sin filtrar)
- `int`: Código del cultivo (ej. `9050000` para Trigo grano)
- `str`: Nombre del cultivo (ej. `"Trigo grano"`)

### muni (opcional)

Determina el nivel de agregación de los datos.

- **Valor por defecto**: `False`
- **Tipo**: `bool`

Opciones:

- `True`: Carga datos municipales de Sonora (2003-2024)
- `False`: Carga datos nacionales por estado (1980-2002)

## Valor de Retorno

**Tipo**: `pd.DataFrame`

Retorna un DataFrame consolidado con los datos de producción agrícola. Si no
se encuentran archivos para los años especificados, retorna un DataFrame
vacío.

### Estructura de Datos

#### Datos Municipales (muni=True)

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

#### Datos Nacionales (muni=False)

Columnas disponibles:

| Columna           | Tipo  | Descripción                         |
| ----------------- | ----- | ----------------------------------- |
| Anio              | int   | Año de producción                   |
| Idestado          | int   | Código del estado                   |
| Nomestado         | str   | Nombre del estado                   |
| Idciclo           | int   | Código del ciclo agrícola           |
| Idmodalidad       | int   | Código de modalidad                 |
| Idcultivo         | int   | Código del cultivo                  |
| Nomcultivo        | str   | Nombre del cultivo                  |
| Cosechada         | float | Superficie cosechada (hectáreas)    |
| Siniestrada       | float | Superficie siniestrada (hectáreas)  |
| Volumenproduccion | float | Volumen de producción               |
| Rendimiento       | float | Rendimiento (ton/ha)                |
| PMR               | float | Precio Medio Rural ($/ton)          |
| Valorproduccion   | float | Valor de la producción (miles de $) |

## Ejemplos de Uso

### Ejemplo 1: Cargar un año específico (municipal)

```python
from seminario_ia.datasets import get_prod_data

# Cargar datos de Sonora para 2020
df = get_prod_data(years=2020, muni=True)

print(f"Registros cargados: {len(df)}")
print(f"Municipios únicos: {df['Nommunicipio'].nunique()}")
```

### Ejemplo 2: Cargar rango de años (municipal)

```python
# Cargar datos de 2015 a 2020 (tupla)
df = get_prod_data(years=(2015, 2020), muni=True)

# Equivalente usando string
df = get_prod_data(years="2015-2020", muni=True)

print(f"Años incluidos: {sorted(df['Anio'].unique())}")
```

### Ejemplo 3: Cargar años específicos no consecutivos

```python
# Cargar solo 2010, 2015 y 2020
df = get_prod_data(years=[2010, 2015, 2020], muni=True)

print(df.groupby('Anio')['Volumenproduccion'].sum())
```

### Ejemplo 4: Filtrar por municipio

```python
# Opción 1: Usar código de municipio
df_hmo = get_prod_data(
    years=(2015, 2020),
    loc_name=30,  # Código de Hermosillo
    muni=True
)

# Opción 2: Usar nombre de municipio
df_hmo = get_prod_data(
    years=(2015, 2020),
    loc_name="Hermosillo",
    muni=True
)

print(f"Registros de Hermosillo: {len(df_hmo)}")
print(f"Cultivos en Hermosillo: {df_hmo['Nomcultivo'].nunique()}")
```

### Ejemplo 5: Datos nacionales históricos

```python
# Cargar datos nacionales de 1980 a 1990
df_nacional = get_prod_data(years=(1980, 1990), muni=False)

# Filtrar solo Sonora (código 26)
df_sonora = df_nacional[df_nacional['Idestado'] == 26]

print(f"Producción de Sonora 1980-1990:")
print(df_sonora.groupby('Anio')['Valorproduccion'].sum())
```

### Ejemplo 6: Análisis por cultivo

```python
# Cargar datos recientes de Hermosillo
df = get_prod_data(
    years=(2018, 2023),
    loc_name="Hermosillo",
    muni=True
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
    muni=True
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
    muni=True
)

# Ver evolución temporal
evolucion = df.groupby('Anio')['Volumenproduccion'].sum()
print(evolucion)
```

### Ejemplo 9: Usar código de cultivo

```python
# Opción 1: Usar código numérico del cultivo
df = get_prod_data(
    years=2020,
    crop_name=9050000,  # Código de Trigo grano
    muni=True
)

# Opción 2: Equivalente con nombre
df = get_prod_data(
    years=2020,
    crop_name="Trigo grano",
    muni=True
)
```

### Ejemplo 10: Comparación temporal

```python
# Cargar datos de dos periodos
df_2003_2008 = get_prod_data(years=(2003, 2008), muni=True)
df_2018_2023 = get_prod_data(years=(2018, 2023), muni=True)

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
df = get_prod_data(years=[2013, 2014, 2015, 2016], muni=True)

# Verificar qué años se cargaron realmente
print(f"Años disponibles: {sorted(df['Anio'].unique())}")
```

Si ningún año tiene archivo, retorna un DataFrame vacío:

```python
df = get_prod_data(years=9999, muni=True)
print(df.empty)  # True
```

## Notas Técnicas

### Ubicación de Archivos

Los archivos se cargan desde:

```
data/processed/siap_produccion/
├── sonora/          # Datos municipales (2003-2024)
│   └── cierre_agricola_sonora_YYYY.csv
└── nacional/        # Datos nacionales (1980-2002)
    └── Cierre_agricola_YYYY.csv
```

### Convenciones de Nomenclatura

- Archivos municipales: `cierre_agricola_sonora_YYYY.csv`
- Archivos nacionales: `Cierre_agricola_YYYY.csv`

La función usa glob patterns para buscar archivos que contengan el año, por
lo que es flexible a variaciones menores en el nombre.

### Rendimiento

Para cargar múltiples años, la función:

1. Lee cada archivo CSV individualmente
2. Los concatena usando `pd.concat()`
3. Filtra por municipio si se especifica

Para grandes rangos de años, considere:

- Filtrar por municipio para reducir memoria
- Seleccionar columnas específicas después de cargar
- Procesar en lotes si trabaja con el rango completo

## Funciones Relacionadas

- `load_prod_file(year, muni)`: Función auxiliar que carga un solo año
- `get_mun_code()`: Obtiene códigos de municipios
- `get_cycle_code()`: Obtiene códigos de ciclos agrícolas
- `get_mod_code()`: Obtiene códigos de modalidades

## Referencia Rápida

```python
# Municipal: un año
df = get_prod_data(2020, muni=True)

# Municipal: rango
df = get_prod_data((2015, 2020), muni=True)

# Municipal: municipio específico
df = get_prod_data((2015, 2020), loc_name="Hermosillo", muni=True)

# Cultivo específico
df = get_prod_data((2015, 2020), crop_name="Trigo grano", muni=True)

# Municipio y cultivo específicos
df = get_prod_data(
    (2015, 2020),
    loc_name="Hermosillo",
    crop_name="Trigo grano",
    muni=True
)

# Nacional: histórico
df = get_prod_data((1980, 2000), muni=False)

# Nacional con cultivo específico
df = get_prod_data((1980, 2000), crop_name="Trigo grano", muni=False)

# Lista de años no consecutivos
df = get_prod_data([2010, 2015, 2020], muni=True)
```

---
