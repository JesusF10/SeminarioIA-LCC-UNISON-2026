#import "@preview/fletcher:0.5.8" as fletcher: diagram, edge, node

#set page(
  width: 25.4cm,
  height: 14.29cm,
  margin: 1.5cm,
  fill: white,
)
#set text(
  font: "Nimbus Sans",
  size: 16pt,
  fill: rgb("#212121"),
)

// --- ESTILOS ---
#let title-slide(title, subtitle, date) = {
  align(center + horizon)[
    #text(size: 40pt, weight: "bold")[#title] \
    #v(0.5cm)
    #text(size: 24pt, fill: rgb("#616161"))[#subtitle] \
    #v(1cm)
    #text(size: 16pt, fill: rgb("#9e9e9e"))[#date]
  ]
}

#let slide(title, body) = {
  pagebreak(weak: true)
  v(0.05cm)
  text(size: 24pt, weight: "bold")[#title]
  v(0.05cm)
  line(length: 100%, stroke: 0.5pt + rgb("#eeeeee"))
  v(0.5cm)
  body
}

// --- INICIO DE LA PRESENTACIÓN ---

#title-slide(
  "Reconversión de Cultivos en Sonora",
  "Avances Fase 3: Análisis Hídrico y Huella Hídrica",
  "28 de Abril de 2026",
)

#slide("Objetivos de la Semana", [
  - *Consolidación Climática:* Datos diarios 2003-2024 para Sonora.
  - *Cálculo de Huella Hídrica:* Implementación del estándar FAO-56.
  - *Línea Base:* Cuantificación del impacto hídrico de cada cultivo (como prueba se utiliza el trigo).
  - *Estandarización:* Configuración técnica de 128 cultivos potenciales.
])

#slide("Actividades Realizadas", [
  - *Automatización Climática:* Scripts para descarga masiva de NASA POWER.
  - *Limpieza de Datos:* Estandarización de registros de producción de SIAP.
  - *Implementación Técnica:* Adaptación del método FAO-56 para Huella Hídrica.
  - *Documentación:* Definición de parámetros para 128 cultivos candidatos.
])

#slide("Resultados Clave", [
  - *Datos:* Base de datos meteorológica y agrícola unificada.
  - *Indicadores:* Cálculo exitoso de HH Azul y Verde para Sonora.
  - *Vinculación Geoespacial:* Integración de coordenadas y altitud en modelos.
  - *Línea Base:* Cuantificación de la dependencia del riego en cultivos actuales.
])

#slide("Infraestructura de Datos", [
  #v(0.5cm)
  #align(center)[
    #figure(
      diagram(
        node-defocus: 0.1,
        spacing: (1.5cm, 1.5cm),
        node((0, 0), [Región (GIS)], stroke: 1pt, fill: blue.lighten(95%), name: <reg>),
        node((2, 0), [Cultivo (FAO)], stroke: 1pt, fill: green.lighten(95%), name: <cult>),
        node((1, 1), [NASA POWER API], stroke: 1pt, fill: orange.lighten(95%), name: <nasa>),
        node((1, 2), [*Cálculo HH*], stroke: 2pt, fill: gray.lighten(90%), name: <proc>),
        edge(<reg>, <nasa>, "-|>"),
        edge(<cult>, <proc>, "-|>"),
        edge(<nasa>, <proc>, "-|>"),
      ),
      caption: [Flujo de Ingesta y Procesamiento Automatizado],
    )
  ]
])

#slide("Huella Hídrica: El Caso del Trigo", [
  #grid(
    columns: (1.2fr, 1fr),
    gutter: 1cm,
    [
      *Hallazgos en Cajeme (2019-2024):*
      - HH Total: ~1,770 m³/Ton.
      - *93% es Huella Azul (Riego).*
      - Alta vulnerabilidad ante posible escasez en presas.
      - Baja contribución de lluvia (HH Verde).
    ],
    align(center + horizon)[
      #image("prueba_analisis/huella_hidrica_Cajeme.png", width: 100%)
    ],
  )
])

#slide("Eficiencia Hídrica Municipal", [
  #grid(
    columns: (1fr, 1.2fr),
    gutter: 1cm,
    align(center + horizon)[
      #image("prueba_analisis/comparativa_hh_azul_municipios.png", width: 100%)
    ],
    [
      - Variaciones significativas entre municipios líderes.
      - *Objetivo:* Identificar zonas con ineficiencia hídrica relativa.
      - Base para la priorización de zonas de reconversión.
    ],
  )
])

#slide("Recomendación Sistémica", [
  #v(0.2cm)
  #align(center)[
    #figure(
      diagram(
        node-defocus: 0.2,
        spacing: (1cm, 0.8cm),
        node((-1, 0), [HH & ETo], stroke: 1pt, fill: blue.lighten(95%), name: <hh>),
        node((0, 0), [Mercado], stroke: 1pt, fill: green.lighten(95%), name: <econ>),
        node((1, 0), [FAO-56], stroke: 1pt, fill: orange.lighten(95%), name: <tech>),
        node((2, 0), [Sequía], stroke: 1pt, fill: red.lighten(95%), name: <risk>),
        node((0.5, 1), [REPNA], stroke: 1pt, fill: purple.lighten(95%), name: <repna>),
        node(
          (0.5, 2.5),
          [*Modelo de Recomendación*],
          shape: rect,
          stroke: 1.5pt,
          fill: gray.lighten(92%),
          inset: 10pt,
          name: <model>,
        ),
        node((0.5, 4), [Cultivos Óptimos], stroke: 1.5pt, fill: yellow.lighten(90%), name: <out>),
        edge(<hh>, <model>, "-|>"),
        edge(<econ>, <model>, "-|>"),
        edge(<tech>, <model>, "-|>"),
        edge(<risk>, <model>, "-|>"),
        edge(<repna>, <model>, "-|>"),
        edge(<model>, <out>, "-|>"),
      ),
      caption: [Ecuación para la Propuesta de Reconversión],
    )
  ]
])

#slide("Limitaciones y Retos", [
  - *Heterogeneidad de Datos:* Diferencias en unidades de medida municipales.
  - *Incertidumbre Técnica:* Estimaciones necesarias para cultivos poco comunes.
  - *Validación:* Requerimiento de contraste con datos de campo locales.
  - *Complejidad:* Integración de factores legales y de mercado (pendiente por ser evaluado).
])

#slide("Próximos Pasos", [
  - *Balance Oferta-Demanda:* Contraste HH vs Concesiones REPNA.
  - *Rentabilidad Hídrica:* Análisis de (\$ / m³) por cultivo.
  - *Alternativas:* Modelado de cultivos de bajo consumo.
  - *Riesgo:* Integración del impacto de la sequía.
])
