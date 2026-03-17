#set page(
  width: 29.7cm,
  height: 21cm,
  margin: 1.5cm,
  fill: white,
)
#set text(
  font: "Nimbus Sans",
  size: 11pt,
  fill: rgb("#212121"),
)

#align(center)[
  #text(size: 24pt, weight: "bold")[Cronograma de Actividades 2026]
  #v(0.1cm)
  #text(size: 14pt, fill: rgb("#757575"))[    Reconversión de Cultivos en Sonora]
]

#v(1cm)

#let phase-row(phase, color, weeks, dates, goal, activities) = (
  table.cell(fill: color)[#text(weight: "bold")[#phase]],
  table.cell(fill: color)[#weeks],
  table.cell(fill: color)[#dates],
  table.cell(fill: color)[#text(style: "italic")[#goal]],
  table.cell(fill: color)[#activities],
)

#table(
  columns: (1.2fr, 0.8fr, 1.2fr, 1.8fr, 3fr),
  stroke: 0.5pt + rgb("#dddddd"),
  align: left + horizon,
  inset: 10pt,
  // Header
  table.header(
    [*Fase*], [*Semana*], [*Fechas*], [*Objetivo*], [*Actividades Sintetizadas*]
  ),

  // Fase 1
  ..phase-row(
    "F1: Exploración", rgb("#e3f2fd"),
    "1 - 2", "19 Feb - 04 Mar",
    "Entender el problema",
    "Zonificación, Cultivos, Lista"
  ),
  ..phase-row(
    "F1: Exploración", rgb("#e3f2fd"),
    "3", "05 Mar - 11 Mar",
    "Alternativas",
    "Alternativas, Fuentes, Datos"
  ),

  // Fase 2
  ..phase-row(
    "F2: Mercado", rgb("#e8f5e9"),
    "4", "12 Mar - 18 Mar",
    "Trabajo de Campo",
    "Contexto, Diagnóstico, Problemas"
  ),
  ..phase-row(
    "F2: Mercado", rgb("#e8f5e9"),
    "5", "19 Mar - 25 Mar",
    "Análisis de Mercado",
    "Mercado, Precios, Demanda"
  ),
  ..phase-row(
    "F2: Mercado", rgb("#e8f5e9"),
    "6 - 7", "26 Mar - 08 Abr",
    "Finanzas",
    "Costos, Rentabilidad, Equilibrio"
  ),

  // Fase 3
  ..phase-row(
    "F3: Viabilidad", rgb("#fff9c4"),
    "8 - 9", "09 Abr - 22 Abr",
    "Recurso Hídrico",
    "Agua, Riego, Disponibilidad"
  ),
  ..phase-row(
    "F3: Viabilidad", rgb("#fff9c4"),
    "10", "23 Abr - 29 Abr",
    "Planificación",
    "Calendario, Rotación"
  ),

  // Fase 4
  ..phase-row(
    "F4: Conclusión", rgb("#f5f5f5"),
    "11 - 12", "30 Abr - 13 May",
    "Cierre",
    "Integración, Reporte, Visualización"
  ),
)

#v(1cm)
#align(right)[
  #text(size: 9pt, fill: rgb("#9e9e9e"))[Marzo 2026]
]
