#set page(
  paper: "a4",
  margin: 2cm,
)
#set text(
  font: "Nimbus Sans",
  size: 10pt,
)

#align(center)[
  #text(size: 16pt, weight: "bold")[
    Marco Analítico Fase 2: Análisis de Rentabilidad
  ] \
  #text(size: 11pt, fill: gray)[
    Seminario IA 2026 - Reconversión de Cultivos en Sonora
  ] \
  #text(size: 9pt, fill: gray, style: "italic")[
    Documento de Trabajo - Semana 6 Fase 2 - Marzo 2026
  ]
]

#v(0.5cm)
#line(length: 100%, stroke: 0.5pt + gray)
#v(0.5cm)

= 1. Contexto y Propósito

== 1.1 Resumen de Pendientes de la Reunión

Durante la reunión del equipo se identificaron los siguientes 
pendientes para avanzar en la Fase 2 (Análisis de Mercado y 
Rentabilidad):

*Tareas Operativas:*
- Preparar preguntas para Emilio (enlace con SAGARPHA)
- Preprocesamiento de datos (formatos, columnas, nulos, duplicados)
- Elaborar lista de tareas detallada para Fase 2

*Objetivos de la Fase 2 (según cronograma):*
- Responder: "¿Qué ha funcionado antes?", "¿Qué compradores hay?", 
  "¿Cuál es el principal problema del agua?"
- Destino de cosecha: identificar compradores por tipo (industria, 
  exportación, mercado local, forraje)
- Precios históricos: análisis de PMR mediante SNIIM
- Demanda: identificar oportunidades de mercado
- Costos de producción: consultar INIFAP, SADER y FIRA
- Punto de equilibrio: calcular viabilidad económica por cultivo

== 1.2 La Pregunta Clave de Lic. Paloma

Durante la discusión de las preguntas propuestas, Lic. Paloma 
planteó una observación metodológica crítica:

#quote(block: true)[
  _"Me preguntaría el por qué estamos considerando cada una de esas 
  preguntas. ¿Qué pretendemos lograr con la respuesta?"_
  
  _"Por ejemplo, ¿por qué nos interesa saber quién compra? ¿Qué 
  haremos si identificamos que una empresa consume mucho de cierto 
  cultivo?"_
]

Esta pregunta es fundamental para mantener el rigor metodológico 
del proyecto: *cada dato recopilado debe tener un objetivo analítico 
claro y una conexión directa con el objetivo de reconversión*.

== 1.3 Objetivo de Este Documento

Proporcionar un marco analítico estructurado que:

1. Evalúe críticamente las preguntas propuestas
2. Reformule las preguntas con objetivos explícitos
3. Establezca el flujo metodológico: Dato → Variable → Decisión
4. Defina el plan de preprocesamiento de datos actuales
5. Liste tareas concretas y priorizadas para Fase 2
6. Trace el roadmap completo del análisis de rentabilidad

#pagebreak()

= 2. Evaluación Crítica de Preguntas Propuestas

== 2.1 Clasificación por Utilidad Analítica

Las preguntas propuestas se clasifican según su conexión directa 
con el objetivo de reconversión productiva:

#table(
  columns: (1fr, 2fr, 1fr),
  align: (center, left, center),
  table.header(
    [*Categoría*], [*Criterio*], [*Prioridad*]
  ),
  [✅ Estratégicas], 
  [Identifica oportunidades directas de sustitución de cultivos],
  [Alta],
  
  [⚠️ Tácticas], 
  [Requiere justificación adicional del uso analítico],
  [Media],
  
  [⚠️ Operativas], 
  [Muy granular para Fase 2, postergar a Fase 3 o 4],
  [Baja]
)

== 2.2 Análisis Individual de Preguntas

=== Pregunta 1: Cultivos con Sobreoferta vs. Déficit

#quote(block: true)[
  _"¿Qué otros cultivos se almacenan a causa de exceso de oferta 
  (como el trigo)? ¿Qué cultivos se quedan cortos en oferta?"_
]

*Clasificación:* ✅ Estratégica (Alta Prioridad)

*Justificación Analítica:*
- Identifica cultivos a *EVITAR* (sobreoferta = bajo PMR = menor 
  rentabilidad)
- Identifica cultivos *OBJETIVO* (déficit = oportunidad de mercado)
- Conexión directa con rentabilidad del agricultor

*Uso en Modelo:*
- Variable: `Riesgo_Comercial` (categórica: Alto/Medio/Bajo)
- Cálculo: Si cultivo tiene sobreoferta crónica → Riesgo Alto
- Impacto en scoring: Penalización en cultivos con exceso de oferta

*Acción Concreta:*
Cruzar datos de almacenamiento/inventarios con series de PMR del 
SIAP (2015-2024). Un PMR decreciente + aumento de superficie 
sembrada = señal de sobreoferta.

=== Pregunta 2: Importaciones de Cultivos a México

#quote(block: true)[
  _"¿Cuáles son los mayores importadores de cultivos de México?"_
]

*Clasificación:* ✅ Estratégica (Alta Prioridad)

*Justificación Analítica:*
- Identifica cultivos con *demanda garantizada*
- Oportunidad de *sustitución de importaciones*
- Reduce dependencia externa en productos que Sonora puede producir

*Uso en Modelo:*
- Variable: `Potencial_Mercado` (numérica: volumen de demanda 
  insatisfecha)
- Cálculo: [Importaciones MX - Producción Nacional] / Importaciones
- Impacto en scoring: Bonus para cultivos con alto potencial de 
  mercado

*Acción Concreta:*
Consultar datos de comercio exterior (SE/INEGI) para identificar 
cultivos importados en volumen significativo. Cruzar con 
`manual-tecnico-cultivos-sonora-2024.csv` para evaluar viabilidad 
técnica en Sonora.

*Fuentes:*
- Sistema de Información Arancelaria Vía Internet (SIAVI)
- Balanza Comercial Agropecuaria (SADER/SIAP)

=== Pregunta 3: PyMES y Empresas Compradoras

#quote(block: true)[
  _"¿Qué PyMES o Empresas más grandes compran tales cultivos, y en 
  qué cantidad?"_
]

*Clasificación:* ⚠️ Táctica (Prioridad Media)

*Riesgo Identificado:*
Demasiado granular para Fase 2. Puede llevar a recopilación de 
datos sin utilidad analítica clara.

*Reformulación Sugerida:*
Cambiar enfoque de "¿Quién compra?" a "¿Cuánta diversificación 
de compradores existe?"

*Justificación Analítica (Reformulada):*
- Un cultivo con múltiples canales (industria + exportación + 
  mercado local) tiene *menor riesgo comercial*
- Dependencia de 2-3 empresas = vulnerabilidad de ingresos para 
  el agricultor

*Uso en Modelo:*
- Variable: `Diversificacion_Mercado` (categórica: Alta/Media/Baja)
- Cálculo: Número de tipos de compradores (industria, exportación, 
  abastos, forraje)
- Impacto en scoring: Mayor diversificación = menor riesgo = mayor 
  puntaje

*Acción Concreta:*
NO recopilar lista de empresas específicas. En su lugar, consultar 
con Emilio: "Para cada cultivo candidato, ¿cuántos tipos de 
compradores existen?"

=== Pregunta 4: Centrales de Abastos

#quote(block: true)[
  _"¿Existe lista de centrales de abastos? ¿Hay datos de volumen 
  comprado/vendido?"_
]

*Clasificación:* ⚠️ Operativa (Baja Prioridad)

*Recomendación:* Postergar a Fase 3 (Viabilidad) o Fase 4 
(Implementación)

*Justificación:*
- Demasiado operativo para análisis de rentabilidad
- Solo relevante si se identifica un cuello de botella logístico
- No impacta directamente el scoring de cultivos alternativos

*Condición para Rescatar:*
Si el análisis de Fase 2 identifica que la logística de distribución 
es un factor limitante para ciertos cultivos, entonces reevaluar en 
Fase 3.

#pagebreak()

= 3. Preguntas Reformuladas con Objetivos Analíticos

Esta sección presenta las preguntas para Emilio con su objetivo 
analítico explícito, uso en el modelo y variables resultantes.

== 3.1 Identificación de Oportunidades de Mercado

*Pregunta para Emilio:*

#quote(block: true)[
  "¿Qué cultivos en Sonora tienen sobreoferta crónica (como el 
  ejemplo del trigo almacenado) y cuáles tienen demanda insatisfecha 
  o déficit de producción?"
]

*Objetivo Analítico:*
- Identificar cultivos a *EVITAR* (sobreoferta = bajo PMR)
- Identificar cultivos *OBJETIVO* (déficit = oportunidad)

*Uso en Modelo:*
- Variable generada: `Riesgo_Comercial`
- Tipo: Categórica {Alto, Medio, Bajo}
- Cálculo:
  - Alto: Cultivo con sobreoferta documentada
  - Bajo: Cultivo con déficit o demanda creciente
  - Medio: Equilibrio oferta-demanda

*Validación Cuantitativa:*
Cruzar respuesta cualitativa de Emilio con series de PMR del SIAP 
(2015-2024). Una tendencia decreciente en PMR confirma sobreoferta.

#v(0.3cm)
#rect(
  fill: rgb("#e8f4f8"),
  width: 100%,
  inset: 8pt,
  radius: 4pt
)[
  *Nota Metodológica:* Si Emilio menciona un cultivo con déficit, 
  verificar que sea técnicamente viable en Sonora consultando 
  `manual-tecnico-cultivos-sonora-2024.csv` (lámina de riego, 
  temperatura, ciclo).
]

== 3.2 Análisis de Sustitución de Importaciones

*Pregunta para Emilio:*

#quote(block: true)[
  "¿Qué cultivos importa México en grandes volúmenes que sean 
  técnicamente viables de producir en Sonora? ¿Conoce casos de 
  éxito de sustitución de importaciones en la región?"
]

*Objetivo Analítico:*
- Identificar cultivos con *demanda garantizada* a nivel nacional
- Priorizar cultivos con menor consumo hídrico que el trigo
- Aprovechar infraestructura y conocimiento local existente

*Uso en Modelo:*
- Variable generada: `Potencial_Mercado`
- Tipo: Numérica (0-100%)
- Cálculo:
  - Potencial = [Importaciones_MX - Producción_Nacional] / 
    Importaciones_MX × 100

*Datos Complementarios Necesarios:*
- Balanza comercial agropecuaria (SADER/SIAP)
- Cruce con láminas de riego de `manual-tecnico-cultivos`
- Verificar si el cultivo ya se produce en algún municipio de Sonora 
  (SIAP municipal 2003-2024)

*Ejemplo de Aplicación:*
Si México importa 500,000 ton de cultivo X, y la producción nacional 
es 200,000 ton, el potencial de mercado es: (500k - 200k)/500k = 60%

== 3.3 Estructura y Diversificación del Mercado

*Pregunta para Emilio:*

#quote(block: true)[
  "Para los cultivos candidatos (listado específico), ¿el mercado 
  está concentrado en pocas empresas o hay múltiples canales de 
  venta? ¿Qué tipos de compradores existen: industria procesadora, 
  exportación, mercado de abastos, forraje local?"
]

*Objetivo Analítico:*
- Evaluar *riesgo de dependencia* de pocos compradores
- Identificar cultivos con *estabilidad comercial*
- Priorizar cultivos con múltiples opciones de venta

*Uso en Modelo:*
- Variable generada: `Diversificacion_Mercado`
- Tipo: Categórica {Alta, Media, Baja}
- Cálculo:
  - Alta: 3+ tipos de compradores
  - Media: 2 tipos de compradores
  - Baja: 1 tipo de comprador (monopsonio)

*Lógica de Scoring:*
Mayor diversificación = menor riesgo comercial = mayor puntaje en 
el modelo de recomendación.

#v(0.3cm)
#rect(
  fill: rgb("#fff4e6"),
  width: 100%,
  inset: 8pt,
  radius: 4pt
)[
  *Importante:* NO necesitamos nombres de empresas específicas. 
  Solo necesitamos saber cuántos *tipos* de compradores existen 
  para cada cultivo.
]

== 3.4 Series Históricas de Precios (SNIIM)

*Pregunta para Emilio:*

#quote(block: true)[
  "¿Tienen acceso a series completas de Precio Medio Rural (PMR) 
  por cultivo y región para los últimos 10 años (2015-2025)? ¿O 
  debemos consultar directamente SNIIM?"
]

*Objetivo Analítico:*
- Calcular *volatilidad de precios* (riesgo económico)
- Identificar *tendencias* alcistas o bajistas
- Estimar *ingreso esperado* y su variabilidad

*Uso en Modelo:*
- Variable generada: `Volatilidad_PMR`
- Tipo: Numérica (coeficiente de variación)
- Cálculo:
  - CV = σ(PMR) / μ(PMR) × 100%
  - Donde σ = desviación estándar, μ = media

*Interpretación:*
- CV < 15%: Precio estable (bajo riesgo)
- CV 15-30%: Volatilidad moderada
- CV > 30%: Alta volatilidad (alto riesgo económico)

*Fuente Alternativa:*
Si Emilio no tiene los datos, consultar directamente:
- SNIIM: Sistema Nacional de Información e Integración de Mercados
- SIAP: Anuario Estadístico (columna `Preciomediorural`)

#pagebreak()

= 4. Marco Metodológico

== 4.1 Flujo: Dato → Variable → Decisión

El análisis de rentabilidad sigue un flujo estructurado que conecta 
cada dato recopilado con una variable analítica y, finalmente, con 
la decisión de reconversión.

#align(center)[
  #table(
    columns: (1.5fr, 2fr, 2fr),
    align: (left, left, left),
    table.header(
      [*Dato Recopilado*], 
      [*Variable Analítica*], 
      [*Decisión de Reconversión*]
    ),
    
    [Cultivo X tiene\ndeficit de oferta],
    [`Potencial_Mercado`\n= ALTO],
    [Si además consume\nmenos agua que trigo\n→ CANDIDATO PRIORITARIO],
    
    [PMR con tendencia\nalcista (2015-2024)],
    [`Tendencia_Precio`\n= Positiva],
    [Mayor rentabilidad\nesperada\n→ Aumentar puntaje],
    
    [Mercado dominado\npor 1-2 empresas],
    [`Diversificacion`\n= BAJA],
    [Riesgo comercial alto\n→ Penalización en scoring],
    
    [Lámina de riego:\n600 mm vs. 800 mm\n(trigo)],
    [`Eficiencia_Hidrica`\n= +25%],
    [Ahorro de agua\nsignificativo\n→ Priorizar],
    
    [Tasa siniestralidad:\n< 5% histórica],
    [`Resiliencia_Climatica`\n= ALTA],
    [Menor riesgo de\npérdida\n→ Aumentar puntaje]
  )
]

== 4.2 Tabla de Variables Analíticas Clave

#table(
  columns: (2fr, 2fr, 2.5fr, 1fr),
  align: (left, left, left, center),
  table.header(
    [*Variable*],
    [*Fuente de Datos*],
    [*Fórmula / Cálculo*],
    [*Tipo*]
  ),
  
  [`Eficiencia_Hidrica`],
  [Manual técnico\n2024],
  [Rendimiento (t/ha) /\nLámina (mm)],
  [Num.],
  
  [`ROI_Preliminar`],
  [Manual técnico\n+ SIAP],
  [(PMR × Rend. - Costo) /\nCosto × 100%],
  [Num.],
  
  [`Volatilidad_PMR`],
  [SIAP 2003-2024],
  [σ(PMR) / μ(PMR) × 100%],
  [Num.],
  
  [`Potencial_Mercado`],
  [Importaciones +\nSIAP],
  [(Demanda - Oferta) /\nDemanda × 100%],
  [Num.],
  
  [`Riesgo_Comercial`],
  [Entrevista Emilio\n+ PMR histórico],
  [Categórica basada en\nsobreoferta/déficit],
  [Cat.],
  
  [`Diversificacion`],
  [Entrevista Emilio],
  [Núm. tipos compradores\n(1-4+)],
  [Cat.],
  
  [`Resiliencia_Climatica`],
  [SIAP municipal\n2003-2024],
  [% Siniestrada / Sembrada\n(histórico 10 años)],
  [Num.],
  
  [`Tendencia_Precio`],
  [SIAP 2015-2024],
  [Pendiente regresión\nlineal PMR(t)],
  [Num.]
)

#v(0.3cm)
#rect(
  fill: rgb("#f0f0f0"),
  width: 100%,
  inset: 8pt,
  radius: 4pt
)[
  *Nota:* Todas las variables numéricas serán normalizadas (0-100) 
  para el scoring final. Las variables categóricas se convertirán 
  a puntajes: Alto=100, Medio=50, Bajo=0.
]

== 4.3 Conexión con Objetivo de Reconversión

El objetivo central del proyecto es:

#quote(block: true)[
  _"Conversión de los cultivos de Sonora por otros que optimicen 
  el uso del agua y su rentabilidad, en apoyo a los agricultores."_
]

Las variables analíticas se conectan directamente con este objetivo:

*Optimización del uso del agua:*
- `Eficiencia_Hidrica` (directa)
- `Resiliencia_Climatica` (adaptación a sequía)

*Optimización de rentabilidad:*
- `ROI_Preliminar` (directa)
- `Potencial_Mercado` (oportunidad comercial)
- `Volatilidad_PMR` (riesgo económico)
- `Diversificacion` (estabilidad de ingresos)

*Apoyo a agricultores:*
- Minimizar `Riesgo_Comercial` (evitar sobreoferta)
- Maximizar `Tendencia_Precio` (ingreso futuro)
- Alta `Diversificacion` (opciones de venta)

#pagebreak()

= 5. Plan de Preprocesamiento

== 5.1 Prioridad 1: Manual Técnico de Cultivos (2024)

*Archivo:* 
`data/raw/datos_proporcionados/manual-tecnico-cultivos-sonora-2024.csv`

*Contenido:* Parámetros técnicos para 22 cultivos (láminas de riego, 
costos, rendimientos).

=== Tareas de Preprocesamiento

*T1.1: Análisis Exploratorio (EDA)*
```python
import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv('data/raw/datos_proporcionados/
                  manual-tecnico-cultivos-sonora-2024.csv')

# Explorar estructura
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Identificar columnas clave
columnas_clave = ['cultivo', 'lamina_riego_mm', 
                  'costo_prod_mxn_ha', 'rendimiento_t_ha']
```

*T1.2: Cálculo de Eficiencia Hídrica*
```python
# Eficiencia: toneladas producidas por mm de agua
df['eficiencia_hidrica'] = (
    df['rendimiento_t_ha'] / df['lamina_riego_mm']
)

# Comparar con trigo como referencia
trigo_base = df[df['cultivo'] == 'Trigo'].iloc[0]
df['ahorro_vs_trigo_pct'] = (
    (trigo_base['lamina_riego_mm'] - df['lamina_riego_mm']) 
    / trigo_base['lamina_riego_mm'] * 100
)

# Ordenar por eficiencia
df_eficientes = df.sort_values('eficiencia_hidrica', 
                                ascending=False)
print(df_eficientes[['cultivo', 'eficiencia_hidrica', 
                      'ahorro_vs_trigo_pct']].head(10))
```

*T1.3: Cálculo de ROI Preliminar*
```python
# Nota: Necesitamos PMR para calcular ingreso
# Por ahora, calculamos costo por tonelada producida
df['costo_por_ton'] = (
    df['costo_prod_mxn_ha'] / df['rendimiento_t_ha']
)

# ROI se calculará después con datos de PMR del SIAP
```

*Entregable:*
- Notebook: `notebooks/fase2_01_analisis_manual_tecnico.ipynb`
- Dataset procesado: 
  `data/processed/cultivos_con_eficiencia_hidrica.csv`

== 5.2 Prioridad 2: SIAP Municipal (2003-2024)

*Archivo(s):* `data/raw/siap-produccion-agricola/municipal/*.csv`

*Contenido:* Series temporales de producción, superficie, PMR y 
valor de producción para Sonora.

=== Tareas de Preprocesamiento

*T2.1: Consolidación de Archivos Anuales*
```python
import glob
import pandas as pd

# Cargar todos los archivos CSV municipales
archivos = glob.glob('data/raw/siap-produccion-agricola/
                      municipal/*.csv')
df_siap = pd.concat([pd.read_csv(f) for f in archivos], 
                     ignore_index=True)

# Filtrar solo Sonora (por si hay otros estados)
df_sonora = df_siap[df_siap['Nomentidad'] == 'Sonora']

print(f"Total registros: {len(df_sonora)}")
print(f"Años: {df_sonora['Anio'].min()} - 
              {df_sonora['Anio'].max()}")
print(f"Cultivos únicos: {df_sonora['Nomcultivo'].nunique()}")
```

*T2.2: Análisis de Volatilidad de PMR*
```python
# Filtrar últimos 10 años para análisis de volatilidad
df_reciente = df_sonora[df_sonora['Anio'] >= 2015]

# Calcular estadísticas de PMR por cultivo
volatilidad = df_reciente.groupby('Nomcultivo').agg({
    'Preciomediorural': ['mean', 'std', 'count']
}).reset_index()

volatilidad.columns = ['cultivo', 'pmr_mean', 'pmr_std', 
                       'n_obs']
volatilidad['cv_pct'] = (
    volatilidad['pmr_std'] / volatilidad['pmr_mean'] * 100
)

# Clasificar volatilidad
volatilidad['volatilidad_cat'] = pd.cut(
    volatilidad['cv_pct'],
    bins=[0, 15, 30, 100],
    labels=['Baja', 'Moderada', 'Alta']
)
```

*T2.3: Tendencias de Superficie Sembrada*
```python
from scipy.stats import linregress

def calcular_tendencia(grupo):
    x = grupo['Anio'].values
    y = grupo['Sembrada'].values
    if len(x) < 5:  # Mínimo 5 años para tendencia
        return np.nan
    slope, _, _, _, _ = linregress(x, y)
    return slope

# Calcular tendencia por cultivo
tendencias = df_reciente.groupby('Nomcultivo').apply(
    calcular_tendencia
).reset_index(name='tendencia_superficie_ha_anio')

# Identificar cultivos en expansión vs. contracción
tendencias['tendencia_cat'] = pd.cut(
    tendencias['tendencia_superficie_ha_anio'],
    bins=[-np.inf, -100, 100, np.inf],
    labels=['Decreciente', 'Estable', 'Creciente']
)
```

*T2.4: Tasa de Siniestralidad*
```python
# Calcular % de superficie siniestrada por cultivo
df_siniestralidad = df_reciente.groupby('Nomcultivo').apply(
    lambda g: (g['Siniestrada'].sum() / 
               g['Sembrada'].sum() * 100)
).reset_index(name='tasa_siniestralidad_pct')

# Clasificar resiliencia climática
df_siniestralidad['resiliencia'] = pd.cut(
    df_siniestralidad['tasa_siniestralidad_pct'],
    bins=[0, 5, 15, 100],
    labels=['Alta', 'Media', 'Baja']
)
```

*Entregable:*
- Notebook: `notebooks/fase2_02_analisis_siap_municipal.ipynb`
- Datasets procesados:
  - `data/processed/volatilidad_pmr_por_cultivo.csv`
  - `data/processed/tendencias_superficie_por_cultivo.csv`
  - `data/processed/siniestralidad_por_cultivo.csv`

== 5.3 Prioridad 3: Integración y Scoring Preliminar

*T3.1: Cruce de Datasets*
```python
# Unir manual técnico con análisis de SIAP
df_integrado = pd.merge(
    df_eficientes,
    volatilidad[['cultivo', 'pmr_mean', 'cv_pct', 
                 'volatilidad_cat']],
    on='cultivo',
    how='inner'
)

df_integrado = pd.merge(
    df_integrado,
    tendencias[['Nomcultivo', 'tendencia_cat']],
    left_on='cultivo',
    right_on='Nomcultivo',
    how='left'
)

df_integrado = pd.merge(
    df_integrado,
    df_siniestralidad[['Nomcultivo', 'resiliencia']],
    left_on='cultivo',
    right_on='Nomcultivo',
    how='left'
)
```

*T3.2: Cálculo de ROI con PMR*
```python
# Ahora podemos calcular ROI completo
df_integrado['ingreso_bruto_ha'] = (
    df_integrado['rendimiento_t_ha'] * 
    df_integrado['pmr_mean']
)

df_integrado['roi_pct'] = (
    (df_integrado['ingreso_bruto_ha'] - 
     df_integrado['costo_prod_mxn_ha']) /
    df_integrado['costo_prod_mxn_ha'] * 100
)
```

*T3.3: Scoring Multicriteria Preliminar*
```python
# Normalizar variables numéricas (0-100)
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 100))
df_integrado['score_eficiencia'] = scaler.fit_transform(
    df_integrado[['eficiencia_hidrica']]
)
df_integrado['score_roi'] = scaler.fit_transform(
    df_integrado[['roi_pct']]
)

# Convertir volatilidad a score (inverso: baja vol = alto score)
df_integrado['score_volatilidad'] = 100 - scaler.fit_transform(
    df_integrado[['cv_pct']]
)

# Score compuesto (pesos ajustables)
pesos = {
    'eficiencia': 0.35,  # Uso del agua (prioridad)
    'roi': 0.30,         # Rentabilidad
    'volatilidad': 0.20, # Estabilidad
    'resiliencia': 0.15  # Adaptación climática
}

# Convertir resiliencia categórica a numérica
resiliencia_map = {'Alta': 100, 'Media': 50, 'Baja': 0}
df_integrado['score_resiliencia'] = (
    df_integrado['resiliencia'].map(resiliencia_map)
)

# Calcular score final
df_integrado['score_final'] = (
    df_integrado['score_eficiencia'] * pesos['eficiencia'] +
    df_integrado['score_roi'] * pesos['roi'] +
    df_integrado['score_volatilidad'] * pesos['volatilidad'] +
    df_integrado['score_resiliencia'] * pesos['resiliencia']
)

# Ordenar por score
top_candidatos = df_integrado.sort_values('score_final', 
                                           ascending=False)
print(top_candidatos[['cultivo', 'score_final', 
                       'eficiencia_hidrica', 'roi_pct']].head(10))
```

*Entregable:*
- Notebook: `notebooks/fase2_03_scoring_preliminar.ipynb`
- Dataset final: `data/processed/cultivos_scoring_fase2.csv`
- Visualización: Top 10 cultivos candidatos con radar chart

#pagebreak()

= 6. Lista de Tareas Fase 2

== Semana 6 (26-31 Marzo): Preprocesamiento y Análisis de Datos

#table(
  columns: (0.5fr, 2fr, 1fr, 1fr),
  align: (center, left, left, center),
  table.header([*ID*], [*Tarea*], [*Responsable*], [*Tiempo*]),
  
  [T6.1],
  [Análisis exploratorio `manual-tecnico-cultivos-sonora-2024.csv`],
  [TBD],
  [2h],
  
  [T6.2],
  [Cálculo de eficiencia hídrica por cultivo],
  [TBD],
  [1h],
  
  [T6.3],
  [Consolidación archivos SIAP municipal (2003-2024)],
  [TBD],
  [2h],
  
  [T6.4],
  [Análisis de volatilidad de PMR (últimos 10 años)],
  [TBD],
  [3h],
  
  [T6.5],
  [Cálculo de tendencias de superficie sembrada],
  [TBD],
  [2h],
  
  [T6.6],
  [Análisis de tasa de siniestralidad por cultivo],
  [TBD],
  [2h],
  
  [T6.7],
  [Integración de datasets y cálculo de ROI],
  [TBD],
  [3h],
  
  [T6.8],
  [Scoring preliminar multicriteria],
  [TBD],
  [2h],
  
  [T6.9],
  [Preparar preguntas reformuladas para Emilio],
  [TBD],
  [1h],
)

*Total estimado:* ~18 horas de trabajo técnico

*Dependencias:*
- T6.2 depende de T6.1
- T6.4, T6.5, T6.6 dependen de T6.3
- T6.7 depende de T6.2, T6.4, T6.5, T6.6
- T6.8 depende de T6.7

*Entregables de Semana 6:*
- [ ] 3 notebooks de análisis (EDA, SIAP, Scoring)
- [ ] 5 datasets procesados en `data/processed/`
- [ ] Documento de preguntas para Emilio (este documento)
- [ ] Top 10 cultivos candidatos preliminares

== Semana 7 (1-8 Abril): Análisis de Rentabilidad y Validación

#table(
  columns: (0.5fr, 2fr, 1fr, 1fr),
  align: (center, left, left, center),
  table.header([*ID*], [*Tarea*], [*Responsable*], [*Tiempo*]),
  
  [T7.1],
  [Reunión con Emilio (respuestas a preguntas reformuladas)],
  [Equipo],
  [2h],
  
  [T7.2],
  [Incorporar variables cualitativas (riesgo comercial, 
   diversificación)],
  [TBD],
  [2h],
  
  [T7.3],
  [Consultar datos de importaciones (SIAVI/SADER)],
  [TBD],
  [3h],
  
  [T7.4],
  [Calcular potencial de mercado por cultivo],
  [TBD],
  [2h],
  
  [T7.5],
  [Análisis de punto de equilibrio (costos FIRA)],
  [TBD],
  [4h],
  
  [T7.6],
  [Refinamiento de scoring con todas las variables],
  [TBD],
  [3h],
  
  [T7.7],
  [Análisis de sensibilidad (escenarios optimista/pesimista)],
  [TBD],
  [3h],
  
  [T7.8],
  [Visualizaciones para reporte (dashboards, mapas)],
  [TBD],
  [4h],
  
  [T7.9],
  [Redacción de informe de Fase 2],
  [Equipo],
  [6h],
)

*Total estimado:* ~29 horas de trabajo técnico

*Entregables de Semana 7:*
- [ ] Scoring final con todas las variables
- [ ] Top 5 cultivos recomendados para reconversión
- [ ] Análisis de punto de equilibrio por cultivo
- [ ] Dashboard interactivo (opcional, si hay tiempo)
- [ ] Informe ejecutivo Fase 2 (5-10 páginas)

#pagebreak()

= 7. Roadmap del Análisis de Rentabilidad

Este roadmap describe el flujo completo desde los datos procesados 
hasta la recomendación final de cultivos alternativos.

== Paso 1: Scoring Multicriteria (T6.8, T7.6)

*Objetivo:* Clasificar cultivos candidatos mediante un sistema de 
puntuación que integre múltiples criterios.

*Criterios y Pesos (Propuesta Inicial):*

#table(
  columns: (2fr, 1fr, 3fr),
  align: (left, center, left),
  table.header([*Criterio*], [*Peso*], [*Justificación*]),
  
  [Eficiencia Hídrica],
  [35%],
  [Objetivo central: optimizar uso del agua],
  
  [ROI (Rentabilidad)],
  [30%],
  [Viabilidad económica para el agricultor],
  
  [Estabilidad (Volatilidad PMR)],
  [15%],
  [Reducir riesgo de ingresos],
  
  [Resiliencia Climática],
  [10%],
  [Adaptación a sequías],
  
  [Potencial de Mercado],
  [10%],
  [Oportunidad comercial],
)

*Fórmula del Score:*
#align(center)[
  $"Score" = sum_(i=1)^n w_i dot "Variable"_i$
]

Donde todas las variables están normalizadas (0-100) y $w_i$ son 
los pesos.

*Nota:* Los pesos son ajustables según retroalimentación de Emilio 
y asesores del proyecto.

== Paso 2: Análisis de Punto de Equilibrio (T7.5)

*Objetivo:* Determinar el precio mínimo de venta necesario para 
cubrir costos de producción.

*Datos Necesarios:*
- Costos de producción (FIRA Agrocostos 2024-2025)
- Rendimiento esperado (manual técnico + SIAP histórico)
- PMR histórico (SIAP 2015-2024)

*Cálculo:*

#align(center)[
  $"PMR mínimo" = "Costo producción ($/ha)" / "Rendimiento (t/ha)"$
]

*Análisis:*
- Comparar PMR mínimo con PMR histórico promedio
- Si PMR promedio > PMR mínimo × 1.2 → Margen de seguridad adecuado
- Si PMR promedio < PMR mínimo × 1.1 → Riesgo de pérdidas

*Entregable:*
Tabla de punto de equilibrio para Top 10 cultivos candidatos.

== Paso 3: Análisis de Escenarios (T7.7)

*Objetivo:* Evaluar la robustez de las recomendaciones ante cambios 
en variables clave.

*Escenarios a Modelar:*

#table(
  columns: (1.5fr, 2fr, 2fr),
  align: (left, left, left),
  table.header(
    [*Escenario*],
    [*Supuestos*],
    [*Impacto en Score*]
  ),
  
  [Base],
  [Valores promedio históricos (2015-2024)],
  [Score calculado en Paso 1],
  
  [Optimista],
  [PMR +15%, rendimiento +10%, disponibilidad hídrica normal],
  [Recalcular ROI y score],
  
  [Pesimista],
  [PMR -15%, rendimiento -10%, sequía (agua -20%)],
  [Evaluar qué cultivos mantienen viabilidad],
  
  [Sequía Extrema],
  [Disponibilidad hídrica -40% (como 2020-2021)],
  [Test de resiliencia: ¿sigue siendo viable?]
)

*Análisis de Sensibilidad:*
- Variar precio ±20%
- Variar rendimiento ±15%
- Variar costo de agua (electricidad para bombeo) ±25%

*Entregable:*
Matriz de sensibilidad que muestre qué cultivos son robustos ante 
variaciones.

== Paso 4: Selección Final y Recomendación (T7.9)

*Objetivo:* Identificar Top 5 cultivos alternativos con mayor 
potencial de reconversión.

*Criterios de Selección Final:*

1. *Score ≥ 70 puntos* (en escala 0-100)
2. *ROI > 20%* en escenario base
3. *Punto de equilibrio alcanzable* (PMR histórico > PMR mínimo × 1.2)
4. *Resiliencia en escenario pesimista* (ROI > 0%)
5. *Viabilidad técnica confirmada* (ya se cultiva en Sonora o 
   región similar)

*Formato de Recomendación:*

Para cada cultivo en el Top 5, proporcionar:
- Ficha técnica (lámina, ciclo, rendimiento esperado)
- Análisis económico (costos, ingresos esperados, ROI)
- Evaluación de riesgos (comercial, climático, operativo)
- Requerimientos de implementación (semilla, tecnología, 
  capacitación)
- Comparación directa con trigo (ahorro de agua, diferencial de 
  rentabilidad)

*Entregable Final:*
Informe ejecutivo (8-12 páginas) con:
- Resumen ejecutivo (1 página)
- Metodología (2 páginas)
- Resultados: Top 5 cultivos con fichas detalladas (5 páginas)
- Análisis de riesgos y recomendaciones (2 páginas)
- Anexos: tablas de datos, gráficas, scripts

#pagebreak()

= 8. Respuesta a Lic. Paloma

Retomando la pregunta clave planteada al inicio:

#quote(block: true)[
  _"¿Por qué nos interesa saber quién compra? ¿Qué haremos con esa 
  información?"_
]

== Respuesta Metodológica

Nos interesa el *tipo* y *diversificación* de compradores, no 
necesariamente empresas específicas por nombre.

*Razón 1: Evaluación de Riesgo Comercial*

Un cultivo con múltiples canales de venta (industria procesadora + 
exportación + mercado local + forraje) tiene *menor riesgo comercial* 
que uno dependiente de 2-3 empresas compradoras.

*Ejemplo:*
- Cultivo A: Solo 2 empresas compran el 90% de la producción
  → Si una empresa cierra o reduce compras, el agricultor pierde 
  mercado
- Cultivo B: 4 tipos de compradores (industria, exportación, 
  abastos, forraje)
  → Si un canal falla, existen alternativas de venta

*Razón 2: Estabilidad de Ingresos*

La diversificación de compradores se traduce en *seguridad económica* 
para el agricultor al hacer la reconversión. No queremos recomendar 
un cultivo con excelente rentabilidad teórica pero con riesgo de 
monopsonio (un solo comprador que controla el precio).

*Razón 3: Conecta con el Objetivo del Proyecto*

El proyecto busca "apoyar a los agricultores de Sonora". Parte de 
ese apoyo es *minimizar el riesgo económico* al recomendar cultivos 
con mercados estables y diversificados.

== Acción Concreta con la Información

*NO haremos:*
- Contactar empresas específicas
- Negociar contratos de compra
- Crear un directorio de compradores

*SÍ haremos:*
- Asignar una variable `Diversificacion_Mercado` en el modelo de 
  scoring
- Penalizar cultivos con mercados concentrados (monopsonio)
- Priorizar cultivos con múltiples opciones de venta
- Incluir en el informe final una sección de "Riesgos Comerciales" 
  para cada cultivo recomendado

*Ejemplo de Uso en Informe Final:*

#quote(block: true)[
  "Cultivo Recomendado: Garbanzo"
  
  *Análisis de Mercado:* El garbanzo en Sonora tiene 4 canales 
  de venta principales: (1) exportación a Medio Oriente, (2) industria 
  nacional de alimentos procesados, (3) mercado de abastos regional, 
  y (4) semilla certificada. Esta diversificación reduce el riesgo 
  comercial frente a cultivos como el trigo, donde el 70% de la 
  producción depende de pocas empresas harineras.
  
  *Riesgo Comercial:* BAJO (diversificación alta)
]

#v(0.5cm)
#line(length: 100%, stroke: 0.5pt + gray)
#v(0.3cm)

#align(center)[
  #text(size: 9pt, style: "italic", fill: gray)[
    Documento generado para reunión de avance - Semana 6 Fase 2\
    Seminario IA 2026 - LCC UNISON\
    Marzo 2026
  ]
]
