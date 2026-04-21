#set page(
  width: 25.4cm,
  height: 14.29cm,
  margin: 1.5cm,
  fill: white,
)
#set text(
  font: "Nimbus Sans",
  size: 15pt,
  fill: rgb("#212121"),
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

// --- INICIO DE LA PRESENTACIÓN ---

#title-slide(
  "Reconversión de Cultivos en Sonora",
  "Reporte de Avances: \nFase 1 \nExploración",
  "",
  "Marzo 2026"
)

#slide("Objetivos", [

  - *Zonificación:* Identificación de niveles de división.
  #v(1cm)
  - *Línea Base:* Análisis de cultivos actuales.
    #v(1cm)
  - *Fuentes Clave:* Consolidación de repositorios de datos oficiales.
    #v(1cm)
  - *Alternativas:* Investigación de posibles cultivos candidatos.
])

#slide("Actividades", [
  #set text(size: 15pt)
  #v(0.2cm)
  #table(
    columns: (1.2fr, 2.5fr),
    stroke: (y, x) => if y == 0 { (bottom: 0.7pt + black) } else { none },
    inset: 10pt,
    fill: (x, y) => if y > 0 and calc.even(y) { rgb("#f9f9f9") },
    [*Actividad*], [*Descripción Clave*],
    [Fuentes Clave], [Lista de fuentes.],
    [Zonificación], [Distritos de riego.],
    [Cultivo Actual], [Cultivos, ciclos y tecnología.],
    [Alternativas], [Cultivos alternativos.],
    [Zonas de interés], [Zonas similares a Sonora.]
  )
])

#slide("Fuentes", [
  - Secretaría de Agricultura, Ganadería, Recursos Hidráulicos, Pesca y Acuacultura (*SAGARHPA*)
      #v(0.5cm)
  - Servicio de Información Agroalimentaria y Pesquera (*SIAP*)
      #v(0.5cm)
  - Comisión Nacional del Agua (*CONAGUA*)
      #v(0.5cm)
  - Secretaría de Agricultura y Desarrollo Rural (*SADER*)
      #v(0.5cm)
  - Registro Público de Derechos Agrarios (*REPDA*)
      #v(0.5cm)
  - Datos Abiertos de Sonora (_datos.sonora.gob.mx_)
      #v(0.5cm)
  - Sistema de Información Agroalimentaria de Consulta (*SIACON*)
])

#slide("Zonificación: Niveles de División", [
  El territorio se clasifica en tres niveles con propósitos distintos:

  #set text(size: 14pt)
  #table(
    columns: (1fr, 1fr, 2.5fr),
    stroke: (y, x) => if y == 0 { (bottom: 0.7pt + black) } else { none },
    inset: 8pt,
    fill: (x, y) => if y > 0 and calc.even(y) { rgb("#f9f9f9") },
    [*Nivel*], [*Organización*], [*Datos Asociados*],
    [Municipio], [Política], [Producción SIAP, ISAG (Sequía), REPNA.],
    [DDR], [SADER], [Agregación estadística, Tecnificación regional.],
    [DR], [CONAGUA], [Infraestructura hidráulica, Presas, Canales.],
  )
  #v(0.2cm)
  - Se identificaron los 13 Distritos de Desarrollo Rural (DDR) en Sonora.
])

#slide("Zonificación: Distritos de Desarrollo Rural (DDR)", [
  Se identifican los siguientes Distritos de Desarrollo Rural (DDR):
  #table(
      columns: (1fr, 2fr, 1fr, 2fr),
      stroke: none,
      fill: (x, y) => if y == 0 { rgb("#f5f5f5") },
      [*Código*], [*Nombre*], [*Código*], [*Nombre*],
      [139], [Caborca], [145], [Mazatán],
      [140], [Magdalena], [146], [Sahuaripa],
      [141], [Agua Prieta], [147], [Guaymas],
      [142], [Ures], [148], [Cajeme],
      [143], [Moctezuma], [149], [Navojoa],
      [144], [Hermosillo], [193], [San Luis Río Colorado]
  )

])

#slide("Zonificación: Análisis Territorial", [
  Para las fases posteriores, se ha definido la siguiente jerarquía técnica:

  - *Unidad Base: Municipio.* Es la clave (`CVE_MUN`) que permite la
    conectividad entre los datasets heterogéneos recolectados.
  - *Agregación: DDR.* Se utilizarán los 13 Distritos de Desarrollo Rural
    como nivel de agrupación administrativa para reportes y política agrícola.
  - *Contexto: Distrito de Riego (DR).* Se integra como capa de
    infraestructura para entender la procedencia del agua (superficial).
])



#slide("Inventario de Datos Técnicos", [
  #set text(size: 14pt)
  #v(0.2cm)
  #table(
    columns: (1.2fr, 2fr, 2.5fr),
    stroke: (y, x) => if y == 0 { (bottom: 0.7pt + black) } else { none },
    inset: 10pt,
    fill: (x, y) => if y > 0 and calc.even(y) { rgb("#f9f9f9") },
    [*Fuente*], [*Dataset*], [*Variables y Cobertura*],
    [SIAP], [Cierres Agrícolas], [Sembrada, PMR, Valor. (Sonora 2003-24)],
    [Sonora], [Anuarios Edo.], [Superficie, Prod, Rend. (1999-2023)],
    [INIFAP], [Manual Técnico], [Láminas (mm), Costos, Ciclo. (2024)],
    [REPNA], [Concesiones Agua], [Volúmenes, Uso, Fuente. (Actual)],
    [Presas], [Recursos Hídricos], [Almacenamiento (hm3), Fecha. (1941-24)],
    [Sequía], [Mapas Impacto], [Índice ISAG, Geometría. (Mun. Sonora)],
  )
])


#slide("SIAP: Producción Agrícola", [
  - *Series Temporales:* 20+ años de historia productiva en Sonora.
  #v(0.5cm)
  - *Siniestralidad:* Permite identificar años de crisis climática por municipio.
  #v(0.5cm)
  - *Económicos:* PMR para calcular la rentabilidad bruta histórica.
  #v(0.5cm)
  - *Ciclos:* Diferenciación clara entre cultivos OI y PV.

  #v(0.5cm)
  *No Seguimiento:* Información sobre cultivos emergentes y no seguidos.

  #v(1cm)
  #set text(size: 11pt, fill: gray)
  *PMR*: Precio Medio Rural, indicador de referencia para el valor de producción
])


#slide("Datos Abiertos Sonora: Agricultura y Recursos Hídricos", [
  - *Validación:* Comparativa de anuarios estatales vs federales (SIAP).
  #v(1cm)
  - *Memoria Hídrica:* Histórico de almacenamiento de presas desde 1941.
  #v(1cm)
  - *Capacidad:* Datos de almacenamiento máximo operativo (NAMO) y volúmenes
    muertos por presa en el estado.

])


#slide("Manual Técnico", [
  - *Consumo Hídrico:* Parámetros de láminas de riego (mm) para 22 cultivos.
  - *Viabilidad Económica:* Costos de producción actualizados (\$ / Ha).
  - *Benchmarking:* Habilita la comparación directa entre el cultivo actual
    y alternativas potenciales en términos de eficiencia.
  #v(1cm)
    *Datos:*
    - `cultivo`
    - `tipo`
    - `lamina_riego_mm`
    - `costo_prod`
    - `ciclo`
    - `rendimiento`
])


#slide("REPNA: Concesiones Agua", [
  - *Títulos:* Identificación de concesionarios y volúmenes legales.
  #v(1cm)
  - *Fuentes:* Diferenciación entre aguas superficiales y subterráneas (pozos).
  #v(1cm)
  - *Análisis Espacial:* Vinculación de demanda hídrica teórica vs oferta legal
    por municipio y DDR.
])


#slide("SADER: Impacto Sequía", [
  - Índice de Severidad de Sequía Agrícola.
  - Identificador municipal para vinculación con cierres del SIAP.
  - *SP_O-I / SP_P-V:* Superficie siniestrada reportada geográficamente.

  #v(0.2cm)
  #align(center)[
    #image("images/sequia-mapa.png", width: 25%)
  ]

    #v(1fr)
    #set text(size: 9pt, fill: gray)
    *Nota:* Visualización y procesamiento de capas realizado mediante el software
    *QGIS Desktop*.
  ])


#slide("Cultivos más recientes", [
  Basado en el Cierre Agrícola 2023-2024, Sonora mantiene una producción
  diversificada con predominio de granos y cultivos de exportación:

  #grid(
    columns: (1fr, 1fr),
    gutter: 1cm,
    [
      *Líderes en Superficie (Ha):*
      - Trigo Grano (OI)
      - Alfalfa (Perenne)
      - Maíz Grano (OI/PV)
      - Espárrago (Hortaliza)
      - Algodón (Industrial)
    ],
    [
      *Líderes en Valor (\$):*
      - Uva de Mesa
      - Nogal Pecanero
      - Tomate Rojo
      - Trigo Grano
      - Garbanzo Grano
    ]
  )

])



#slide("Regiones de Interés", [
  #set text(size: 11pt)
  #v(0.1cm)
  #table(
    columns: (1.2fr, 1fr, 2.5fr, 1.5fr),
    stroke: (y, x) => if y == 0 { (bottom: 0.7pt + black) } else { none },
    inset: 8pt,
    fill: (x, y) => if y > 0 and calc.even(y) { rgb("#f9f9f9") },
    [*Región / País*], [*Clima*], [*Factor de Similitud*], [*Variables*],
    [Valle Imperial, EE.UU.], [BWh], [Cuenca Colorado y dependencia riego.],
    [hm3, Acre-feet],
    [Murcia/Almería, España], [BSh], [Gestión escasez y tecnificación líder.],
    [Validación riego],
    [Murray-Darling, Aus.], [Semiárido], [Variabilidad y mercados de agua.],
    [Siniestrada],
    [Punjab/Sindh, Pak.], [Semiárido], [Granos a gran escala y estrés hídrico.],
    [Rendimiento],
    [Valle Central, Chile], [Árido], [Exportación frutales alto valor.],
    [Valorprod (PMR)],
    [Al-Jouf, Arabia S.], [Árido], [Reconversión de trigo a olivo.],
    [m3 Extracción],
        [Estepa Sur, Ucrania], [Semiárido], [Producción masiva y canales extensos.],
        [SHP / Mun.],
      )
      #v(0.2cm)
      #set text(size: 9pt, fill: gray)
      *BWh:* Clima desértico cálido, *BSh:* Clima semiárido cálido
    ])


#slide("Forma de Trabajo", [
  Se ha establecido un ecosistema digital para garantizar la reproducibilidad
  y la colaboración eficiente del equipo:

  - *Uso de Git y GitHub:* Control de versiones y colaboración remota.
  - *Repositorio de Datos:* Estructurado en `data/raw` y `data/processed`.
  - *Herramientas:* Python (`Polars` para datos masivos, `GeoPandas` para SIG),
    `uv` para entornos virtuales y `Typst` para documentación.
  - *Espacio Compartido (Drive):* Repositorio colaborativo para toma de notas,
    material de lectura, lista de pendientes y documentos administrativos.
  - *Dominio de conocimiento:* Redacción de glosario y documentación técnica.
])

#slide("Conclusiones Fase 1", [
  1. *Aprendizaje del Dominio:* Contexto agrícola sonorense.
  #v(1cm)
  2. *Inventario de Datos:* Repositorio con 20+ años
     de historia productiva e hídrica.
    #v(1cm)
  3. *Estructura de trabajo:* Repositorio de datos, herramientas, espacio compartido.
  #v(1cm)
  4. *Exploración de Datos:* Exploración superficial de fuentes de datos.
])

#slide("Próximos Pasos: Fase 2", [
  *Análisis de Mercado y Rentabilidad*
  - Evaluación de la demanda de cultivos.
  #v(0.5cm)
  - Modelado de costos de producción e ingresos proyectados.
  #v(0.5cm)
  - Análisis de la cadena de suministro en Sonora.
])
