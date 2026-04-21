#set page(
  paper: "a4",
  margin: 2.5cm,
)
#set text(
  font: "Nimbus Sans",
  size: 11pt,
)

// Estilos de encabezados
#show heading.where(level: 1): it => [
  #set text(size: 18pt, weight: "bold")
  #v(1cm)
  #it
  #v(0.5cm)
]

#show heading.where(level: 2): it => [
  #set text(size: 14pt, weight: "bold", fill: rgb("#2c3e50"))
  #v(0.5cm)
  #it
  #v(0.3cm)
]

// Portada
#align(center + horizon)[
  #text(size: 24pt, weight: "bold")[Informe Detallado de Avances: Fase 2] \
  #v(0.5cm)
  #text(size: 18pt, fill: gray)[Análisis de Mercado y Rentabilidad para la Reconversión] \
  #v(1.5cm)
  #text(size: 14pt)[Seminario de IA - LCC UNISON] \
  #text(size: 12pt, fill: gray)[Abril 2026]
]

#pagebreak()

= 1. Introducción y Propósito del Informe

Este documento constituye la extensión detallada de la presentación de avances de la *Fase 2*. Su objetivo es documentar la lógica de procesamiento, las fuentes de datos validadas y la estructura del modelo de reconversión que se está implementando para el estado de Sonora.

= 2. Gestión Integral de Datos

Tras un proceso de auditoría de datos, se ha definido el inventario final de fuentes que alimentarán el modelo.

== 2.1 Descarte y Depuración
Se determinó el descarte de los datasets de _Datos Abiertos de Sonora_ y _SIACON_ debido a que su información ya se encuentra contenida de forma más robusta y estandarizada en el *SIAP*. Este paso reduce el ruido estadístico y evita duplicidades en el análisis.

== 2.2 Incorporación de Nuevas Fuentes
Se han integrado conjuntos de datos críticos para la dimensión económica y legal:
- *CONAGUA:* Estadística agrícola por cultivo y distrito, incluyendo superficies regadas y volúmenes de agua en Distritos de Riego (DR).
- *SADER:* Precios de Garantía, fundamentales para entender los subsidios en granos básicos y leche.
- *REPDA/REPNA:* Registro de derechos legales de extracción (superficial y pozos), esencial para la Fase 3 de viabilidad hídrica.

= 3. Análisis de Mercado Regional

El análisis de mercado no se limita a precios, sino que busca entender la dinámica sistémica de la comercialización en Sonora:

- *Dinámica de Oferta:* Identificación de cultivos con *sobreoferta crónica* (como el trigo) que genera almacenamiento forzado y caída de rentabilidad.
- *Sustitución de Importaciones:* Cruce de datos de comercio exterior para identificar cultivos que México importa masivamente y que Sonora tiene potencial de producir con alta eficiencia.
- *Estructura de Compradores:* Análisis de la relevancia de PyMES, grandes empresas y la dinámica de los cultivos forrajeros para el sector ganadero local.

= 4. Especificación del Modelo de Reconversión

El modelo se estructura bajo una arquitectura de procesamiento de tres capas: Entrada, Procesamiento y Salida.

== 4.1 Capa de Entrada: Variables y Dimensiones
Se han recolectado y normalizado las siguientes dimensiones de análisis:
- *Territorial:* DDR (Distritos de Desarrollo Rural) y Municipios.
- *Productiva:* Lista de cultivos, producción histórica y superficie sembrada/cosechada.
- *Hídrica:* Uso de agua, métodos de riego y volúmenes concesionados.
- *Infraestructura:* Grado de tecnificación del riego.
- *Económica:* Precios medios rurales, canales de mercado y costos operativos.
- *Climatica:* Registros de siniestralidad por eventos climáticos.

== 4.2 Capa de Procesamiento: Lógica y Metas
El motor de procesamiento integra factores internos y externos:
- *Análisis de Subsidios:* Impacto de los Precios de Garantía en la decisión del productor.
- *Requerimientos Técnicos:* Cruce de necesidades edafoclimáticas de los cultivos candidatos.

*Metas del Procesamiento:*
1. *Optimización del uso del agua:* Minimizar el requerimiento hídrico total de la región.
2. *Rentabilidad Garantizada:* Asegurar un beneficio económico neto superior o igual al cultivo actual para el productor.

== 4.3 Capa de Salida: Resultados Esperados
El modelo generará tres productos principales:
1. *Lista de Cultivos Candidatos:* Alternativas con alto potencial de rentabilidad y bajo impacto hídrico.
2. *Lista de Cultivos "Problema":* Identificación de especies críticas por su ineficiencia hídrica o rentabilidad negativa bajo precios actuales.
3. *Configuración de Reconversión:* Propuesta de distribución espacial y porcentual de los nuevos cultivos recomendados.

= 5. Marco Metodológico de Evaluación (Scoring)

El modelo de scoring integra variables cuantitativas actuales con validaciones cualitativas y proyecciones de viabilidad técnica. A continuación, se desglosan los criterios por dimensión estratégica, clasificándolos según su estado de obtención:

== 5.1 Dimensión Hídrica (Núcleo de la Reconversión)
- *Eficiencia Hídrica Relativa (Fase 2):* Toneladas producidas por milímetro de agua aplicado.
- *Ahorro de Lámina Bruta (Fase 2):* Diferencia porcentual en mm de agua respecto al trigo.
- *Presión sobre Acuíferos y Presas (Fase 3):* Multiplicador de riesgo basado en el déficit hídrico del municipio o distrito de riego.
- *Huella Hídrica Económica (Fase 3):* Valor monetario generado por cada metro cúbico de agua consumido (\$ /m³).

== 5.2 Dimensión Económica y de Rentabilidad
- *ROI Proyectado (Fase 2 - Refinando):* Retorno de inversión considerando costos FIRA 2024 y PMR histórico.
- *Margen de Seguridad (Fase 2 - Pendiente):* Proximidad del precio de mercado al punto de equilibrio (PMR mínimo).
- *Vulnerabilidad por Subsidios (Emilio):* Dependencia del cultivo de los Precios de Garantía de SADER.
- *Costo de Transición (Fase 3):* Inversión inicial necesaria en infraestructura o maquinaria específica.

== 5.3 Dimensión de Mercado y Comercialización
- *Diversificación de Compradores (Emilio):* Puntuación basada en la cantidad de canales de venta (industria, exportación, local).
- *Índice de Sustitución de Importaciones (Fase 2):* Prioridad a cultivos con alta demanda nacional insatisfecha.
- *Volatilidad del Precio (Fase 2):* Estabilidad del PMR en los últimos 10 años (análisis de varianza).
- *Riesgo de Sobreoferta Regional (Emilio):* Identificación de saturación de mercado en la zona de influencia.

== 5.4 Dimensión Técnico-Ambiental
- *Resiliencia Climática (Fase 2):* Tasa histórica de siniestralidad por eventos climáticos extremos en Sonora.
- *Afinidad Edafológica (Fase 3):* Compatibilidad del tipo de suelo municipal con el cultivo propuesto.
- *Ventaja de Ventana Estacional (Fase 3):* Sincronía del ciclo de cosecha con precios altos internacionales.
- *Requerimiento de Tecnificación (Fase 2):* Nivel de infraestructura necesaria (riego por goteo, malla sombra, etc.).

== 5.5 Ponderación del Scoring Multicriteria

Para la Fase 2, se aplica la siguiente distribución de pesos:

#table(
  columns: (2fr, 1fr, 3fr),
  align: (left, center, left),
  stroke: 0.5pt + gray,
  [*Criterio*], [*Peso*], [*Justificación*],
  [Eficiencia Hídrica], [35%], [Optimización hídrica como núcleo del Seminario IA.],
  [ROI (Rentabilidad)], [30%], [Incentivo económico para la adopción de la reconversión.],
  [Estabilidad de Precios], [15%], [Mitigación del riesgo de volatilidad de mercado.],
  [Resiliencia Climática], [10%], [Adaptación a la realidad de sequía del estado.],
  [Potencial de Mercado], [10%], [Aseguramiento de la demanda y canales de venta.],
)

= 6. Conclusión de Avances y Próximos Pasos

La Fase 2 se encuentra en su etapa de validación de costos utilizando los tabuladores de *FIRA 2024-2025*.
El siguiente hito es la generación del *Top 5 de Cultivos Recomendados*, los cuales serán sometidos a pruebas de estrés
en escenarios de sequía extrema para garantizar que la propuesta de reconversión sea resiliente a largo plazo.
