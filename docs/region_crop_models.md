# Modelos de Datos: Region y Crop

## Descripción General

Las clases `Region` y `Crop` representan la estructura de regiones
geográficas con sus cultivos asociados, incluyendo información
fenológica y agronómica.

## Clase Crop

Representa un cultivo agrícola con sus características fenológicas
y coeficientes de cultivo (Kc) para cálculo de evapotranspiración.

### Atributos

| Atributo    | Tipo  | Descripción                              |
| ----------- | ----- | ---------------------------------------- |
| name        | str   | Nombre del cultivo                       |
| start_month | int   | Mes de inicio del ciclo (1-12)           |
| start_day   | int   | Día de inicio del ciclo (1-31)           |
| end_month   | int   | Mes de fin del ciclo (1-12)              |
| end_day     | int   | Día de fin del ciclo (1-31)              |
| kc_ini      | float | Coeficiente de cultivo en etapa inicial  |
| kc_mid      | float | Coeficiente de cultivo en etapa media    |
| kc_end      | float | Coeficiente de cultivo en etapa final    |
| durations   | tuple | Duraciones (días) de cada etapa (4 val.) |

### Propiedades

- `start_date`: Retorna tupla `(mes, día)` de inicio
- `end_date`: Retorna tupla `(mes, día)` de fin
- `kc`: Retorna diccionario con coeficientes `{ini, mid, end}`

### Ejemplo de Uso

```python
from seminario_ia.models import Crop

trigo = Crop(
    name="Trigo",
    start_month=10,
    start_day=30,
    end_month=4,
    end_day=19,
    kc_ini=0.3,
    kc_mid=1.15,
    kc_end=0.25,
    durations=(31, 47, 63, 31),
)

# Usar __str__() para salida legible
print(trigo)

# Usar __repr__() para debugging
print(repr(trigo))
```

### Salida de __str__()

La representación amigable muestra la información de forma
jerárquica y estructurada, con indentación clara.

### Salida de __repr__()

La representación compacta muestra todos los parámetros
separados por comas, útil para debugging y logs.

---

## Clase Region

Representa una región geográfica con información municipal
y los cultivos que se producen en ella.

### Atributos

| Atributo  | Tipo         | Descripción                  |
| --------- | ------------ | ---------------------------- |
| name      | str          | Nombre de la región          |
| latitude  | float        | Latitud geográfica           |
| longitude | float        | Longitud geográfica          |
| altitude  | float        | Altitud en metros            |
| crops     | list[Crop]   | Lista de cultivos (vacía     |
|           |              | por defecto)                 |

### Métodos

#### `add_crop(crop: Crop) -> None`

Agrega un cultivo a la región.

**Parámetros:**
- `crop`: Instancia de la clase `Crop`

**Ejemplo:**
```python
region.add_crop(trigo)
region.add_crop(maiz)
```

### Ejemplo de Uso Completo

```python
from seminario_ia.models import Crop, Region

# Crear cultivos
trigo = Crop(
    name="Trigo",
    start_month=10,
    start_day=30,
    end_month=4,
    end_day=19,
    kc_ini=0.3,
    kc_mid=1.15,
    kc_end=0.25,
    durations=(31, 47, 63, 31),
)

maiz = Crop(
    name="Maíz grano",
    start_month=5,
    start_day=1,
    end_month=10,
    end_day=15,
    kc_ini=0.5,
    kc_mid=1.2,
    kc_end=0.4,
    durations=(25, 40, 50, 35),
)

# Crear región
region = Region(
    name="San Ignacio Río Muerto",
    latitude=27.32498,
    longitude=-110.39104,
    altitude=7.0,
)

# Agregar cultivos
region.add_crop(trigo)
region.add_crop(maiz)

# Imprimir con __str__() para formato legible
print(region)
```

### Salida de __str__()

La representación produce una salida jerárquica con:
- Información de la región (nombre, coordenadas, altitud)
- Lista de cultivos con indentación en cascada
- Todos los detalles de cada cultivo apropiadamente indentados

Ejemplo:

```
Región: San Ignacio Río Muerto
  Latitud: 27.32498
  Longitud: -110.39104
  Altitud (m): 7.0
  Cultivos:
    Cultivo: Trigo
      Período: 10/30 - 04/19
      Coeficientes Kc:
        Inicial: 0.3
        Medio: 1.15
        Final: 0.25
      Duraciones por etapa:
        Inicial: 31 días
        Desarrollo: 47 días
        Medio: 63 días
        Maduración: 31 días
    Cultivo: Maíz grano
      Período: 05/01 - 10/15
      Coeficientes Kc:
        Inicial: 0.5
        Medio: 1.2
        Final: 0.4
      Duraciones por etapa:
        Inicial: 25 días
        Desarrollo: 40 días
        Medio: 50 días
        Maduración: 35 días
```

### Salida de __repr__()

Representación compacta para debugging:

```python
Region(name='San Ignacio Río Muerto', latitude=27.32498,
longitude=-110.39104, altitude=7.0, crops=[Crop(...), Crop(...)])
```

---

## Notas de Implementación

### Indentación en Cascada

La clase `Region` utiliza indentación en cascada para mostrar
sus cultivos de forma jerárquica:

1. **Nivel 0**: Nombre de la región (sin indentación)
2. **Nivel 1** (2 espacios): Atributos principales de la región
3. **Nivel 2** (4 espacios): Cada cultivo en la lista
4. **Nivel 3** (10 espacios): Propiedades de cada cultivo
5. **Nivel 4** (12 espacios): Detalles específicos

### Diferencia entre __str__() y __repr__()

| Aspecto        | __str__()          | __repr__()          |
| -------------- | ------------------ | ------------------- |
| Propósito      | Legibilidad humana | Debugging técnico   |
| Formato        | Multilinea         | Compacto            |
| Indentación    | Jerárquica         | Mínima              |
| Uso            | print(), reportes  | Consola, logging    |

---

## Validación

- `start_month`, `end_month`: 1-12
- `start_day`, `end_day`: 1-31
- `kc_ini`, `kc_mid`, `kc_end`: Valores positivos (típicamente 0-1.5)
- `durations`: Tupla de 4 enteros positivos (días de cada etapa)
- `latitude`, `longitude`, `altitude`: Floats (sin restricciones específicas)

---

## Integración con el Proyecto

Estas clases se integran con:

- **Datasets**: Datos de `get_prod_data()` pueden ser mapeados a
  instancias de `Crop`
- **Análisis**: Los atributos fenológicos permiten análisis de
  requerimientos hídricos
- **Visualización**: El formato `__str__()` es ideal para reportes
  y presentaciones

---

Última actualización: Enero 2024
Proyecto: Seminario IA - Reconversión Productiva LCC UNISON 2026
