#import "@preview/fletcher:0.5.5" as fletcher: diagram, edge, node

#set page(
  paper: "us-letter",
  margin: (x: 2cm, y: 2.5cm),
)

#set text(
  font: "Nimbus Sans",
  size: 11pt,
)

// --- ENCABEZADO ---
#align(center)[
  #text(size: 18pt, weight: "bold")[Reporte de Avances Semanal] \
  #v(0.2cm)
  #text(size: 14pt)[Proyecto: Reconversión de Cultivos en el estado de Sonora] \
  #v(0.2cm)
  #text(size: 12pt, fill: rgb("#616161"))[Periodo: Fase 3] \
  #v(0.2cm)
  #text(size: 11pt)[28 de Abril de 2026]
]

#v(1cm)

// --- INTEGRANTES ---

#align(center)[
  #text(size: 12pt, weight: "bold")[Integrantes del Equipo]
]

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  align(center)[
    \
    Jesús Flores Lacarra \
    Michell Berenice Altamirano Ocejo
  ],
  align(center)[
    \
    Orlando López Roque \
    Sebastián Rodríguez Serrano
  ],
)

#v(1.5cm)

// --- RESUMEN ---
#heading(level: 1)[Resumen]
#v(0.5cm)

Durante la presente semana, los esfuerzos se han centrado en la consolidación y
limpieza de los conjuntos de datos y archivos de configuración técnica fundamentales para el
análisis hídrico y climático a nivel municipal. Se automatizó la extracción de datos
meteorológicos históricos utilizando la API de NASA POWER para múltiples
municipios, y se avanzó en la depuración de las series temporales de
producción agrícola del SIAP. Estos datos son la base para el posterior
cálculo de la evapotranspiración de referencia (ETo) y el modelado de los
requerimientos hídricos de los cultivos candidatos.

#v(1cm)

// --- ACTIVIDADES REALIZADAS ---
#heading(level: 1)[Actividades Realizadas]
#v(0.5cm)

Durante este periodo, el equipo se enfocó en las siguientes tareas técnicas:

- *Automatización de descarga climática:* Se desarrollaron scripts en Python para
  interactuar con la API de NASA POWER, permitiendo la descarga masiva de
  variables meteorológicas (radiación solar, temperatura, humedad relativa y
  velocidad del viento) para todos los municipios de Sonora desde 2003 hasta 2024.
- *Limpieza de datos de producción:* Se implementaron rutinas de limpieza para
  los registros históricos del SIAP de producción agrícola (2003-2024), resolviendo inconsistencias en
  la nomenclatura municipal y estandarizando los formatos para su cruce con
  capas hídricas.
- *Cálculo de Evapotranspiración (ETo):* Adaptación de la implementación del método
  FAO-56 Penman-Monteith en libreta interactiva proporcionada por el Lic. Manuel Alberto Valenzuela Arce
  para estimar la demanda hídrica atmosférica del trigo (trigo grano) en todos los municipios, para
  poder ser replicado en cualquier cultivo que cuente con su ficha técnica respectiva.
  Además, se realizó creación de módulos de código reutilizables para su aplicación en municipios
  específicos o regiones.
- *Configuración de información técnica para modelado:* Se estructuraron los archivos de
  configuración técnica necesarios para la ejecución de modelos hidrológicos y
  de balance hídrico, incluyendo la definición de parámetros específicos para
  cada municipio (latitud, longitud, altitud) y cultivo candidato (constantes de crecimiento,
  calendarios, nombre, duraciones) dentro de los registros de la SIAP.
- *Redacción de documentación técnica:* Se documentaron detalladamente las metodologías utilizadas
  para el cálculo de ETo, con el fin de garantizar la reproducibilidad y
  facilitar la transferencia de conocimientos dentro del equipo.

#v(1cm)

// --- RESULTADOS  ---
#heading(level: 1)[Resultados]
#v(0.5cm)

Los hitos alcanzados durante esta semana reflejan un avance significativo en la
capacidad de análisis hídrico-agrícola del proyecto:

- *Repositorio climático municipal y configuración técnica:* Consolidación de un repositorio con
  registros diarios para cada municipio del estado desde 2003 hasta 2024. Este dataset ya
  incluye las variables necesarias para el método FAO-56 (Radiación, Temp,
  Viento, Humedad). Además, se generaron archivos de configuración técnica para cada municipio y cultivo candidato, lo que
  permitirá la ejecución de modelos hidrológicos y de balance hídrico en fases posteriores.

  - *Configuración por municipio:* Cada municipio cuenta con un archivo de configuración que incluye su latitud, longitud y altitud,
    lo que es esencial para la precisión de los cálculos de ETo y modelado hidrológico, ya que se obtienen los datos climáticos
    específicos para cada ubicación geográfica.

  - *Configuración por cultivo:* Para cada cultivo candidato (en total 128 cultivos registrados), se definieron parámetros técnicos como
    constantes de crecimiento, calendarios de desarrollo y duraciones, lo que facilitará la aplicación de modelos específicos para cada tipo de cultivo.

    Para ejemplo, para el cultivo de trigo grano, se establecieron los parámetros técnicos necesarios para modelar su demanda hídrica, lo que permitirá
    realizar análisis específicos de estrés hídrico y requerimientos de riego para este cultivo en los municipios donde se cultiva.


    #text(size: 11pt, weight: "bold")[Ejemplo de Configuración Técnica para Trigo Grano]
    #table(
      columns: (auto, 1fr),
      // 'auto' ajusta el ancho al texto, '1fr' ocupa el resto
      inset: 10pt,
      // Espaciado interno para que no se vea apretado
      align: horizon,
      // Alinea el texto verticalmente al centro

      // Definición del encabezado
      table.header([*Parámetros Técnicos*], [*Valores*]),

      // Contenido de las filas (se ponen una tras otra)
      [Calendario de Desarrollo], [Start: 10/30 --- End: 04/19],

      [Duración por Fase],
      [
        - 31 días (Inicial)
        - 47 días (Desarrollo)
        - 63 días (Madurez)
        - 31 días (Final)
      ],

      [Constantes de Crecimiento (Kc)],
      [
        0.30 (Inicial), 1.15 (Desarrollo), 0.25 (Madurez)
      ],
    )

    === Fuente de los Datos Técnicos

    Los parámetros de configuración para los cultivos se derivaron de las
    siguientes fuentes:

    - *Duraciones y Coeficientes:* Obtenidos de los Cuadros 11 y 12 del
      documento *FAO-56 (2006)*, considerando las condiciones de clima árido
      y semiárido propias de Sonora.
    - *Fenología Derivada:* Las fechas de cosecha fueron calculadas sumando la
      duración total de las cuatro etapas fenológicas a la fecha de siembra
      representativa.
    - *Cultivos con Valores Aproximados:* Para cultivos no listados en el
      FAO-56 (ej. Agave, Jojoba, Pitahaya, Stevia), se utilizaron valores de
      cultivos agronómicamente cercanos o grupos genéricos (suculentas,
      arbustos desérticos, hortalizas de hoja pequeña).

    #block(inset: (left: 10pt), stroke: (left: 1pt + gray))[
      #set text(size: 9pt, style: "italic")
      *Referencia:* Allen, R.G., et al. (2006). Evapotranspiración del cultivo.
      Estudio FAO Riego y Drenaje No. 56. FAO, Roma. ISBN 92-5-304219-2.
    ]

    #v(0.5cm)
  Con todo lo anterior, se establece la base para el flujo de analisis hídrico-agrícola, permitiendo la integración de datos climáticos
  con información técnica de cultivos para modelar la demanda hídrica y el balance hídrico en fases posteriores, como lo muestra
  la siguiente figura:

  #figure(
    diagram(
      node-defocus: 0.1,
      spacing: (1.5cm, 2cm),
      node((0, 0), [Definición de Región\ (Lat, Lon, Alt)], stroke: 1pt, fill: blue.lighten(90%), name: <reg>),
      node((2, 0), [Parámetros Cultivo\ (Kc, Duración, Rend)], stroke: 1pt, fill: green.lighten(90%), name: <cult>),
      node((1, 1), [NASA POWER API], stroke: 1pt, fill: orange.lighten(90%), name: <nasa>),
      node((1, 2), [Procesamiento ETo / HH], stroke: 2pt, fill: gray.lighten(90%), name: <proc>),
      node((1, 3), [Reporte / Dataset ML], stroke: 1pt, fill: red.lighten(90%), name: <out>),

      edge(<reg>, <nasa>, [Consulta], "-|>"),

      // Arista con curva desde cultivo para evitar traslape
      edge(<cult>, <proc>, "-|>", bend: 40deg),

      // Arista recta desde NASA
      edge(<nasa>, <proc>, [Datos Diarios\ (T, RH, Rs, u2, P)], "-|>"),

      edge(<proc>, <out>, "-|>"),
    ),
    caption: [Flujo de Ingesta y Origen de Datos],
  )

#v(1cm)


- *Modelo de Demanda Hídrica (ETo):* Se obtuvo una curva de ETo diaria
  validada para múltiples municipios. Este resultado permite cuantificar el
  estrés hídrico atmosférico en puntos específicos del estado de Sonora.
- *Infraestructura de Datos:* El sistema de archivos ahora permite la ingesta
  directa de nuevos municipios mediante el script de automatización, reduciendo
  drásticamente el tiempo de preparación de datos para futuras fases.

=== Modelo de Calculo de la Huella Hídrica
Con los datos de ETo y la producción agrícola, se estableció un modelo para calcular la Huella Hídrica (HH) de los cultivos, desglosada en sus
componentes Azul (riego), Verde (precipitación) y Gris (contaminación).

Este proceso se puede observar en el siguiente diagrama:

#v(1cm)
#figure(
  diagram(
    node-defocus: 0.1,
    spacing: (1.5cm, 1cm),
    node((0, 0), [Datos Clima], name: <clima>),
    node((0, 1), [Cálculo $E T_o$\ (Penman-Monteith)], stroke: 1pt, name: <eto>),
    node((2, 1), [Curva $K_c$], name: <kc>),
    node((1, 2), [$E T_c = E T_o dot K_c$], stroke: 2pt, name: <etc>),
    node((0, 2), [Precipitación ($P$)], name: <p>),
    node((0, 3), [$P_"ef"$ (FAO Simple)], name: <pef>),

    edge(<clima>, <eto>, "-|>"),
    edge(<eto>, <etc>, "-|>"),
    edge(<kc>, <etc>, "-|>"),
    edge(<p>, <pef>, "-|>"),

    node((1, 4), [$E T_"Verde"$ / $E T_"Azul"$], stroke: 1pt, name: <va>),
    edge(<etc>, <va>, "-|>"),
    edge(<pef>, <va>, "-|>"),

    node((1, 5), [$U A C$ ($m^3/h a$)], name: <uac>),
    node((2, 6), [Rendimiento], name: <rend>),
    node((1, 7), [Huella Hídrica ($m^3/t$)], stroke: 2pt, fill: red.lighten(95%), name: <hh>),

    edge(<va>, <uac>, [Suma Ciclo], "-|>"),
    edge(<uac>, <hh>, "-|>"),
    edge(<rend>, <hh>, "-|>"),
  ),
  caption: [Proceso Secuencial de Cálculo de Huella Hídrica],
)


#v(0.5cm)
#heading(level: 2)[Ejemplo de Análisis de Huella Hídrica (Trigo Grano)]
#v(0.3cm)

Se realizó un análisis de ejemplo de la Huella Hídrica del cultivo de trigo grano en el municipio de Cajeme,
utilizando los datos de producción agrícola y las estimaciones de ETo obtenidas. Los resultados muestran:

- *Predominancia de la Huella Azul:* En el municipio de Cajeme, el análisis
  de los últimos ciclos (2019-2024) muestra que la Huella Hídrica Azul
  (riego) representa aproximadamente el 93% de la huella total (~1,646
  m³/Ton). Esto evidencia el alto costo hídrico ambiental de mantener este
  cultivo en zonas áridas. La estrategia a seguir es comparar esta huella total del trigo
  con la de cultivos alternativos para evaluar su viabilidad en términos de sostenibilidad hídrica.

#v(0.5cm)
#figure(
  image("prueba_analisis/huella_hidrica_Cajeme.png", width: 90%),
  caption: [Composición de HH en Cajeme (2019-2024)],
)

- *Comparativa de Eficiencia:* La disparidad en la Huella Azul entre los
  principales municipios productores permite identificar regiones de
  ineficiencia relativa. Estas métricas son fundamentales para la Fase 3, ya
  que sirven como línea base para comparar la viabilidad de cultivos
  alternativos con menor requerimiento de riego.

#figure(
  image("prueba_analisis/comparativa_hh_azul_municipios.png", width: 90%),
  caption: [Eficiencia Hídrica Azul por Municipio],
)

- *Lista de Municipios Productivos:* También se identificaron los municipios con mayor producción de trigo grano,
  lo que permitirá focalizar los análisis de estrés hídrico y modelado en estas zonas críticas.

#figure(
  image("prueba_analisis/top_municipios_productores.png", width: 100%),
  caption: [Principales Municipios Productores de Trigo Grano],
)

#heading(level: 1)[Limitaciones y Retos]
#v(0.5cm)
A pesar de los avances significativos, se identificaron algunas limitaciones y retos que el equipo deberá abordar en las siguientes fases:
- *Heterogeneidad en las unidades de medición de producción agrícola*, lo que requiere una estandarización cuidadosa para garantizar
  la comparabilidad de los datos.
- La *falta de datos específicos para ciertos cultivos* alternativos, lo que obliga a utilizar aproximaciones basadas en cultivos similares,
  introduciendo incertidumbre en los análisis.
- La necesidad de *validar los modelos de balance hídrico* con datos de campo o estudios previos, para asegurar la precisión y relevancia de los resultados obtenidos.

#heading(level: 1)[Próximos Pasos]
#v(0.5cm)
En la siguiente semana, el equipo se enfocará en:
- *Expansión del Análisis de Huella Hídrica:* Aplicar la metodología de cálculo de ETo y Huella Hídrica a otros cultivos candidatos, para generar un panorama comparativo de su sostenibilidad hídrica en los municipios de Sonora.
- *Modelado de Balance Hídrico:* Integrar los datos climáticos y técnicos para desarrollar modelos de balance hídrico que permitan simular escenarios de estrés hídrico y evaluar la viabilidad de cultivos alternativos bajo diferentes condiciones climáticas.
- *Optimización de la Infraestructura de Datos:* Continuar mejorando los scripts de automatización para facilitar la actualización y mantenimiento de los conjuntos de datos, así como la generación de reportes técnicos para la toma de decisiones.
- *Documentación y Transferencia de Conocimientos:* Seguir documentando detalladamente las metodologías y resultados obtenidos, para garantizar la reproducibilidad y facilitar la transferencia de conocimientos dentro del equipo y hacia los stakeholders involucrados en la gestión hídrica agrícola en Sonora.
- *Resolver las limitaciones identificadas*, como la estandarización de unidades de producción y la búsqueda de datos técnicos para cultivos alternativos, para mejorar la precisión y relevancia de los análisis futuros.

=== Planteamiento del modelo de reconversión de cultivos
Con la base de datos climáticos y técnicos ya estructurada, se plantea el desarrollo de un modelo de reconversión de cultivos que permita evaluar la viabilidad de diferentes opciones agrícolas en función de su demanda hídrica y su impacto en la Huella Hídrica. Este modelo
integrará los datos de ETo y de la Huella Hídrica, los parámetros técnicos de los cultivos y las métricas de producción para generar recomendaciones informadas sobre qué cultivos podrían ser más sostenibles en cada municipio, considerando tanto la eficiencia hídrica como la rentabilidad agrícola.

Esto se puede visualizar en el siguiente diagrama de convergencia, donde se integran las diferentes fuentes de información para alimentar un modelo central que genere recomendaciones de reconversión productiva.

#figure(
  diagram(
    node-defocus: 0.2,
    spacing: (1.5cm, 2cm),

    // Entradas en una fila superior
    node((-1, 0), [Huella Hídrica \ & ETo], stroke: 1pt, fill: blue.lighten(95%), name: <hh>),
    node((0, 0), [Valor de \ Producción], stroke: 1pt, fill: green.lighten(95%), name: <econ>),
    node((1, 0), [Parámetros \ Cultivos], stroke: 1pt, fill: orange.lighten(95%), name: <tech>),
    node((2, 0), [Impacto \ Sequía], stroke: 1pt, fill: red.lighten(95%), name: <risk>),

    // Entrada adicional debajo de la fila
    node((0.5, 1), [Disponibilidad Legal \ (REPNA / Agua)], stroke: 1pt, fill: purple.lighten(95%), name: <repna>),

    // MODELO CENTRAL DE CONVERGENCIA - CORREGIDO A RECTÁNGULO
    node(
      (0.5, 2.5),
      [*Modelo de Recomendación \ de Reconversión*],
      shape: rect,
      stroke: 1.5pt,
      fill: gray.lighten(92%),
      inset: 10pt,
      name: <model>,
    ),

    // Salida final
    node((0.5, 4), [Priorización de Zonas \ y Cultivos Óptimos], stroke: 1.5pt, fill: yellow.lighten(90%), name: <out>),

    // CONEXIONES DE CONVERGENCIA
    edge(<hh>, <model>, "-|>", bend: 15deg),
    edge(<econ>, <model>, "-|>"),
    edge(<tech>, <model>, "-|>"),
    edge(<risk>, <model>, "-|>", bend: -15deg),
    edge(<repna>, <model>, "-|>"),

    edge(<model>, <out>, "-|>", stroke: 2pt),
  ),
  caption: [Modelo sistémico para la propuesta de reconversión productiva],
)

#v(1cm)

Además, se plantea la incorporación de un módulo de análisis de escenarios que permita simular el impacto de diferentes estrategias de manejo hídrico (como riego eficiente, uso de cultivos resistentes a la sequía, etc.) en la Huella Hídrica y en la producción agrícola, para apoyar la toma de decisiones en la gestión del agua en el sector agrícola de Sonora.
Se tomará en cuenta el impacto de la sequía y el cambio climático en la disponibilidad de agua, para asegurar que las recomendaciones generadas por el modelo sean resilientes a las condiciones futuras del clima y del recurso hídrico en la región.
