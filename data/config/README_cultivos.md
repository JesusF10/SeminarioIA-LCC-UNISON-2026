# Archivo de Configuración de Cultivos (`cultivos.json`)

## Descripción

Este archivo contiene los parámetros agronómicos e hídricos de los 128 cultivos registrados en el sistema. Es utilizado para el cálculo de evapotranspiración del cultivo (ETc) mediante el método de coeficiente único de cultivo (Kc) descrito en la metodología FAO Penman-Monteith.

---

## Estructura del archivo

Cada entrada del JSON representa un cultivo con la siguiente estructura:

```json
"Nombre del cultivo": {
  "calendario": {
    "start_mmdd": ["mes", "dia"],
    "end_mmdd":   ["mes", "dia"]
  },
  "dur": ["etapa_ini", "etapa_des", "etapa_med", "etapa_fin"],
  "kc": {
    "ini": "valor",
    "mid": "valor",
    "end": "valor"
  }
}
```

### Descripción de campos

| Campo        | Descripción                                                                       |
| ------------ | --------------------------------------------------------------------------------- |
| `start_mmdd` | Fecha de siembra en formato [mes, día]                                            |
| `end_mmdd`   | Fecha de cosecha en formato [mes, día]                                            |
| `dur`        | Duración en días de cada etapa fenológica: [inicial, desarrollo, mediados, final] |
| `kc.ini`     | Coeficiente de cultivo en etapa inicial                                           |
| `kc.mid`     | Coeficiente de cultivo en etapa de mediados de temporada                          |
| `kc.end`     | Coeficiente de cultivo en etapa final                                             |

---

## Fuente de los datos

### Duraciones de etapas (`dur`)

Obtenidas del **Cuadro 11** del documento FAO-56 _"Evapotranspiración del cultivo — Guías para la determinación de los requerimientos de agua de los cultivos"_ (FAO Estudio Riego y Drenaje No. 56, Roma 2006), páginas 104–108.

### Coeficientes de cultivo (`kc`)

Obtenidos del **Cuadro 12** del mismo documento FAO-56, páginas 110–114.

### Fecha de siembra (`start_mmdd`)

Obtenida de la columna "Fecha de Siembra" del **Cuadro 11** del FAO-56, considerando las fechas representativas para clima árido/semiárido, correspondiente a las condiciones de la región de Sonora, México.

### Fecha de cosecha (`end_mmdd`)

La fecha de cosecha **no aparece explícitamente** en los Cuadros 11 y 12 del FAO-56. Fue calculada de forma derivada sumando la duración total del ciclo (suma de las cuatro etapas fenológicas) a la fecha de siembra indicada en el Cuadro 11, considerando fechas típicas para clima árido/semiárido representativo de la región de Sonora. Este valor debe ser validado con datos locales reales.

---

## Cultivos con valores aproximados

Los siguientes cultivos no aparecen directamente en el FAO-56 o no cuentan con datos suficientes en los Cuadros 11 y 12. Sus valores fueron estimados a partir del cultivo o grupo más cercano agronómicamente.

Agave y Maguey pulquero utilizan valores de piña, ya que ambos son plantas suculentas de ciclo muy largo con baja transpiración y comportamiento hídrico similar. Jojoba y Sábila se basaron en promedios de arbustos y suculentas desérticas respectivamente, dado que son cultivos nativos del desierto sonorense sin referencia directa en FAO-56. Pitahaya usó valores estimados para cactáceas, al ser una planta suculenta de comportamiento hídrico parecido al agave. Stevia se aproximó con los valores de menta, por tratarse de un cultivo de hoja perenne con ciclos y manejo del agua similares. Nopal forrajero y Nopalitos se basaron en los mismos valores del agave al pertenecer a la misma familia de cactáceas. Kale se trató como crucífera del mismo grupo que brócoli y coliflor, ya que el FAO-56 no lo incluye por ser un cultivo que ganó popularidad comercial después de la publicación del documento en 2006. Mano de León, Quelite, Rapini, Napa, Shop suey y Eneldo se aproximaron con valores del grupo genérico de hortalizas de hoja pequeña del FAO-56, al ser cultivos de nicho o de uso regional sin entrada propia en el documento. Margarita, Zempoalxochitl y Semilla de flores usaron valores de flores ornamentales genéricas. Granada, Higo, Persimonio, Membrillo, Chabacano y Ciruela se basaron en los valores de drupas y frutales caducifolios del Cuadro 12, que los agrupa bajo una misma categoría. Arándano usó valores similares a la uva por compartir un ciclo productivo parecido como fruto de arbusto. Las variantes forrajeras, secas y achicaladas de maíz, trigo, sorgo y cebada utilizaron los mismos valores base del cultivo principal, ajustando únicamente el Kc final cuando la cosecha ocurre en verde en lugar de seco. Las semillas de papa, soya, girasol, trigo y cilantro comparten los valores del cultivo base ya que el proceso fisiológico y los requerimientos hídricos son los mismos. Finalmente, las entradas Varios, Frutales varios y Hortalizas usan promedios representativos de su grupo, al ser categorías genéricas que por definición no tienen un cultivo específico de referencia.

---

## Referencia bibliográfica

Allen, R.G., Pereira, L.S., Raes, D., Smith, M. (2006). _Evapotranspiración del cultivo — Guías para la determinación de los requerimientos de agua de los cultivos_. Estudio FAO Riego y Drenaje No. 56. FAO, Roma. ISBN 92-5-304219-2.
