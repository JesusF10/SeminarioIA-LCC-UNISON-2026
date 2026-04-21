#set page(
  width: 25.4cm,
  height: 14.29cm,
  margin: 1.5cm,
  fill: white,
)
#set text(
  font: "Nimbus Sans",
  size: 15pt,
)

// Estilos para títulos y subtítulos
#let title-slide(title, subtitle, author, date) = {
  align(center + horizon)[
    #text(size: 40pt, weight: "bold")[#title] \
    #v(0.5cm)
    #text(size: 24pt, fill: rgb("#616161"))[#subtitle] \
    #v(1cm)
    #text(size: 18pt)[#author] \
    #text(size: 16pt, fill: rgb("#9e9e9e"))[#date]
  ]
}

#let slide(title, body) = {
  pagebreak(weak: true)
  v(0.05cm)
  text(size: 20pt, weight: "bold")[#title]
  v(0.05cm)
  line(length: 100%, stroke: 0.5pt + rgb("#eeeeee"))
  v(0.05cm)
  body
}

// Bloque de diagrama
#let box-node(content, fill-color: rgb("#e3f2fd")) = {
  rect(
    fill: fill-color,
    stroke: 0.5pt + gray,
    radius: 4pt,
    width: 6cm,
    height: 1.8cm,
    inset: 8pt,
    align(center + horizon, text(size: 12pt, weight: "bold", content)),
  )
}

// --- INICIO DE LA PRESENTACIÓN ---

#title-slide(
  "Reconversión de Cultivos en Sonora",
  "Reporte de Avances",
  "Seminario IA - LCC UNISON",
  "Abril 2026",
)

#slide("Datos", [

  - *Descarte:* Se eliminaron los _Datos Abiertos de Sonora_ y los datos obtenidos de la plataforma de _SIACON_ (redundantes con *SIAP*).
  #v(0.5cm)
  - *Nuevas Fuentes:*
    - *CONAGUA (3 nuevos datasets):*
      - Estadística agrícola por Cultivo y Distrito.
      - Superficies Regadas y Volúmenes: Datos de Uso de agua en DR.
    - *SADER (1 nuevo dataset):*
      - Precios de Garantía: Precios oficiales de apoyo para granos y leche.
    - *REPDA/REPNA*: Derechos legales de extracción (superficial y pozos).
])

#slide("Mercado", [
  Se está realizando una consulta técnica para la valoración de la realidad regional:

  - *Sobreoferta vs. Déficit*: Identificar cultivos con almacenamiento forzado vs. oportunidades de mercado insatisfechas.
  - *Comercio Exterior*: Cruce con los mayores importadores de México para proponer sustitución de importaciones desde Sonora.
  - *Estructura de Compradores:* Relevancia de PyMES, Grandes Empresas y Centrales de Abastos.
  - *Cultivos Forrajeros:* Dinámicas de compra, nutrición y almacenaje (mercado ganadero).
])

#slide("Modelo de Reconversión", [
  #v(2.5cm)
  #align(center)[
    #grid(
      columns: (1fr, 0.5fr, 1fr, 0.5fr, 1fr),
      align: horizon,
      box-node("ENTRADA", fill-color: rgb("#f5f5f5")),
      text(size: 30pt, fill: gray)[$arrow.r$],
      box-node("MODELO", fill-color: rgb("#bbdefb")),
      text(size: 30pt, fill: gray)[$arrow.r$],
      box-node("SALIDA", fill-color: rgb("#c8e6c9")),
    )
  ]
])

#slide("Modelo: Especificación de Entrada", [
  Variables y dimensiones recolectadas para el análisis:

  #columns(2, gutter: 1cm)[
    - *DDR:* Distritos de Desarrollo Rural.
    - *Cultivos:* Lista de cultivos.
    - *Producción:* Tonelajes históricos.
    - *Superficie:* Hectáreas sembradas.
    - *Agua:* Uso y concesiones.

    #colbreak()

    - *Riego:* Métodos y volúmenes.
    - *Tecnificación:* Grado de infraestructura.
    - *Mercado:* Precios y canales.
    - *Clima:* Condiciones climáticas.
  ]
])

#slide("Modelo: Procesamiento", [
  Factores internos:

  - *Subsidios:* Impacto de Precios de Garantía.
  - *Cultivos:* Cruce de requerimientos técnicos.
  - *Mercado General:* Dinámicas de oferta y demanda nacional.

  #v(1cm)
  *Metas del Modelo:*
  #rect(fill: rgb("#e1f5fe"), stroke: 0.5pt + rgb("#01579b"), inset: 15pt, radius: 5pt)[
    1. *Optimizar el uso del agua:* Minimizar el requerimiento hídrico.
    2. *Rentabilidad:* Asegurar el beneficio económico del productor.
  ]
])

#slide("Modelo: Especificación de Salida", [
  El modelo plantea tres resultados para la reconversión:

  - *Lista de Cultivos Candidatos:*
  Alternativas con alto potencial.

  #v(0.5cm)
  - *Lista de Cultivos "Problema":*
  Especies críticas por alto consumo o baja rentabilidad actual.

  #v(0.5cm)
  - *Posible Configuración de Reconversión:*
  Propuesta de distribución de cultivos.
])
