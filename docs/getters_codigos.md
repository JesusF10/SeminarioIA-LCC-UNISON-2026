# Guía de Uso: Getters de Códigos

## Descripción General

El módulo `seminario_ia.datasets` proporciona funciones getter para acceder a
las codificaciones utilizadas en los datos agrícolas de Sonora. Estas funciones
permiten **tres modos de operación**:

1. **Sin argumentos** → Retorna el diccionario completo de códigos
2. **Con código (int)** → Retorna el nombre correspondiente
3. **Con nombre (str)** → Retorna el código correspondiente

## Funciones Disponibles

### `get_mun_code(input=None)`

Obtiene códigos y nombres de municipios de Sonora (72 municipios).

**Parámetros:**

- `input: str | int | None` - Código, nombre o None (por defecto)

**Retorna:**

- `dict` si `input=None` - Diccionario completo `{código: nombre}`
- `str` si se pasa un código (int) - Nombre del municipio
- `int` si se pasa un nombre (str) - Código del municipio
- `None` si no se encuentra

**Ejemplos:**

```python
from seminario_ia.datasets import get_mun_code

# Obtener todos los municipios
todos = get_mun_code()  # {'01': 'Aconchi', '02': 'Agua Prieta', ...}

# Buscar por código
nombre = get_mun_code(30)  # 'Hermosillo'

# Buscar por nombre
codigo = get_mun_code('Hermosillo')  # 30
```

---

### `get_cycle_code(input=None)`

Obtiene códigos y nombres de ciclos agrícolas (5 ciclos).

**Parámetros:**

- `input: str | int | None` - Código, nombre o None (por defecto)

**Retorna:**

- `dict` si `input=None` - Diccionario completo
- `str` si se pasa un código (int) - Nombre del ciclo
- `int` si se pasa un nombre (str) - Código del ciclo
- `None` si no se encuentra

**Ejemplos:**

```python
from seminario_ia.datasets import get_cycle_code

# Obtener todos los ciclos
todos = get_cycle_code()
# {'1': 'Ciclo Primavera-Verano', '2': 'Ciclo Otoño-Invierno', ...}

# Buscar por código
nombre = get_cycle_code(1)  # 'Ciclo Primavera-Verano'

# Buscar por nombre
codigo = get_cycle_code('Ciclo Perennes')  # 3
```

---

### `get_ddr_code(input=None)`

Obtiene códigos y nombres de Distritos de Desarrollo Rural (12 DDRs).

**Parámetros:**

- `input: str | int | None` - Código, nombre o None (por defecto)

**Retorna:**

- `dict` si `input=None` - Diccionario completo
- `str` si se pasa un código (int) - Nombre del DDR
- `int` si se pasa un nombre (str) - Código del DDR
- `None` si no se encuentra

**Ejemplos:**

```python
from seminario_ia.datasets import get_ddr_code

# Obtener todos los DDRs
todos = get_ddr_code()  # {'149': 'Navojoa', '140': 'Magdalena', ...}

# Buscar por código
nombre = get_ddr_code(144)  # 'Hermosillo'

# Buscar por nombre
codigo = get_ddr_code('Guaymas')  # 147
```

---

### `get_mod_code(input=None)`

Obtiene códigos y nombres de modalidades de producción (2 modalidades).

**Parámetros:**

- `input: str | int | None` - Código, nombre o None (por defecto)

**Retorna:**

- `dict` si `input=None` - Diccionario completo
- `str` si se pasa un código (int) - Nombre de la modalidad
- `int` si se pasa un nombre (str) - Código de la modalidad
- `None` si no se encuentra

**Ejemplos:**

```python
from seminario_ia.datasets import get_mod_code

# Obtener todas las modalidades
todos = get_mod_code()  # {'1': 'Riego', '2': 'Temporal'}

# Buscar por código
nombre = get_mod_code(1)  # 'Riego'

# Buscar por nombre
codigo = get_mod_code('Temporal')  # 2
```

---

### `get_unit_code(input=None)`

Obtiene códigos y nombres de unidades de medida (4 unidades).

**Parámetros:**

- `input: str | int | None` - Código, nombre o None (por defecto)

**Retorna:**

- `dict` si `input=None` - Diccionario completo
- `str` si se pasa un código (int) - Nombre de la unidad
- `int` si se pasa un nombre (str) - Código de la unidad
- `None` si no se encuentra

**Ejemplos:**

```python
from seminario_ia.datasets import get_unit_code

# Obtener todas las unidades
todos = get_unit_code()
# {'200201': 'Tonelada', '200205': 'Manojo', ...}

# Buscar por código
nombre = get_unit_code(200201)  # 'Tonelada'

# Buscar por nombre
codigo = get_unit_code('Tonelada')  # 200201
```

---

## Patrones de Uso Comunes

### 1. Validar si un municipio existe

```python
municipio = "Hermosillo"
codigo = get_mun_code(municipio)

if codigo is not None:
    print(f"✓ Municipio válido: {municipio} (código {codigo})")
else:
    print(f"✗ Municipio no encontrado: {municipio}")
```

### 2. Iterar sobre todos los municipios

```python
for codigo, nombre in get_mun_code().items():
    print(f"Procesando {codigo}: {nombre}")
    # ... lógica de análisis ...
```

### 3. Crear mapeos inversos

```python
# Mapeo código → nombre
mun_por_codigo = get_mun_code()

# Mapeo nombre → código
mun_por_nombre = {v: int(k) for k, v in mun_por_codigo.items()}
```

### 4. Filtrar datos por región

```python
import pandas as pd

# Obtener códigos de municipios de interés
hermosillo = get_mun_code("Hermosillo")
caborca = get_mun_code("Caborca")

# Filtrar DataFrame
df_region = df[df['CVE_MUN'].isin([hermosillo, caborca])]
```

---

## Manejo de Errores

Todas las funciones retornan `None` cuando no encuentran el código o nombre:

```python
# Códigos inexistentes
get_mun_code(999)  # → None
get_cycle_code(99)  # → None

# Nombres inexistentes
get_mun_code("NoExiste")  # → None
get_ddr_code("Inexistente")  # → None
```

**Recomendación:** Siempre validar el resultado antes de usarlo:

```python
resultado = get_mun_code(codigo_usuario)
if resultado is None:
    raise ValueError(f"Municipio no válido: {codigo_usuario}")
```

---

## Notas Técnicas

### Fuente de Datos

Todos los códigos se cargan desde el archivo JSON de codificación:

```
data/config/codificacion.json
```

Este archivo contiene los mapeos oficiales utilizados en los datasets de SIAP.

### Estructura del Módulo

```
src/seminario_ia/datasets/
├── __init__.py        # Exporta todas las funciones
├── codes.py           # Implementación de getters
├── paths.py           # Definiciones de rutas
└── data.py            # Operaciones con datos
```

---

## Script de Ejemplo

Un script completo de demostración está disponible en:

```
notebooks/ejemplo_codigos.py
```

Ejecutar con:

```bash
uv run python notebooks/ejemplo_codigos.py
```

---

## Referencia Rápida

| Función          | Total | Ejemplo Código | Ejemplo Nombre         |
| ---------------- | ----- | -------------- | ---------------------- |
| `get_mun_code`   | 72    | `30`           | `"Hermosillo"`         |
| `get_cycle_code` | 5     | `1`            | `"Ciclo Primavera-V."` |
| `get_ddr_code`   | 12    | `144`          | `"Hermosillo"`         |
| `get_mod_code`   | 2     | `1`            | `"Riego"`              |
| `get_unit_code`  | 4     | `200201`       | `"Tonelada"`           |

---

**Última actualización:** Enero 2024  
**Proyecto:** Seminario de IA - Reconversión de Cultivos
