#import "@preview/tablex:0.0.8": cellx, tablex

#set page(
  paper: "us-letter",
  margin: (x: 1in, y: 1in),
)

#set text(
  size: 11pt,
  lang: "es",
)

#set par(
  justify: true,
  leading: 0.65em,
)

#align(center)[
  #text(size: 18pt, weight: "bold")[Reporte de Situación Hídrica] \
  #text(size: 12pt)[Mayo 2026]
]

#v(1cm)

= Situación Hídrica en Sonora

Para proponer una reconversión productiva en Sonora, es fundamental analizar la
situación hídrica bajo un enfoque sistémico. Este diagnóstico va desde la
evolución temporal de largo plazo hasta la oferta natural pluvial, los riesgos
térmicos extremos, la demanda fisiológica de los cultivos y la extracción real.

== Evolución Temporal de la Sequía en Sonora (2003-2026)

Este análisis retrospectivo evalúa la severidad de la sequía a nivel municipal
en las últimas dos décadas, clasificando la afectación del territorio según las
categorías oficiales del Monitor de Sequía.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/evolucion_sequia_historica.png",
      width: 90%,
    ),
    caption: [Evolución de la Sequía en Sonora (2003-2026)],
  )
]

La gráfica de área apilada revela que la sequía en Sonora no es un fenómeno
aislado, sino una condición crónica. Se observan picos críticos en 2011-2012,
2020-2021 y un repunte sumamente severo a partir de 2023, donde casi el 90% del
territorio estatal ha experimentado algún grado de sequía. La persistencia de
las categorías "Extrema (D3)" y "Excepcional (D4)" demuestra que depender de
cultivos perennes o de ciclos largos expone al productor a una alta probabilidad
de pérdida total debido al agotamiento de fuentes de agua superficial y al
descenso de los niveles estáticos de los acuíferos.

== Tendencia de Precipitación y Temperatura Promedio (2010-2023)

Analizar las tendencias climáticas agregadas permite identificar si la escasez
de agua se ve agravada por variaciones de temperatura que eléven la demanda
evapotranspirativa del entorno.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/tendencia_climatica_anual.png",
      width: 80%,
    ),
    caption: [Tendencia de Precipitación y Temperatura en Sonora (2010-2023)],
  )
]

Los registros históricos climatológicos muestran una tendencia decreciente en la
precipitación media anual acumulada, acompañada de un aumento sostenido en la
temperatura promedio de los ciclos agrícolas. Este calentamiento intensifica la
evapotranspiración de referencia ($E T_o$), lo que incrementa de forma directa
las láminas de riego requeridas por los cultivos para evitar el estrés
hídrico. La brecha creciente entre la oferta pluvial decreciente y la demanda
térmica ascendente hace indispensable transicionar hacia cultivos xerófitos o
hortalizas de ciclo corto altamente eficientes.


== Eficiencia de la Lluvia: Precipitación Total vs. Precipitación Efectiva

No toda la lluvia que cae es aprovechada por los cultivos. Este análisis estima
la precipitación efectiva ($P_("ef")$), que es la porción de agua pluvial que
logra infiltrarse y almacenarse en la zona radicular, excluyendo las pérdidas
por escorrentía superficial rápida o percolación profunda.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/eficiencia_lluvia_municipios.png",
      width: 80%,
    ),
    caption: [Comparativa de Lluvia Total vs. Lluvia Efectiva por Municipio],
  )
]

La comparativa revela que en municipios de la región de la sierra y sur de
Sonora (como Álamos, Yécora o Quiriego), la brecha entre la lluvia total y la
efectiva es muy amplia debido a la alta intensidad de eventos torrenciales.
Mucha agua se pierde por escurrimiento rápido debido a la topografía accidentada
y a la baja capacidad de retención de humedad de los suelos agrícolas. Este
resultado justifica que en zonas con baja eficiencia de lluvia se implemente
infraestructura de retención hídrica, labranza de conservación y cultivos de
ciclo corto que coincidan con la ventana de mayor humedad efectiva.

== Distribución de Días de Lluvia Significativa en el Ciclo

Este indicador muestra el número promedio de días en los que se registran
precipitaciones iguales o mayores a 1 mm y 5 mm, permitiendo contrastar lluvias
de distribución constante contra eventos aislados y torrenciales del monzón.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/dias_lluvia_municipios.png",
      width: 80%,
    ),
    caption: [Días Promedio de Lluvia Significativa por Municipio],
  )
]

Los datos confirman que, a pesar de que algunos municipios registran acumulados
pluviales aparentemente aceptables, la distribución temporal es sumamente errática,
concentrando la mayor cantidad de días con lluvia significativa ($\ge 5$ mm) en
un periodo menor a 15 días del año. La prolongada ausencia de lluvias constantes
significa que los cultivos de ciclo largo experimentarán largos meses de sequía
intermedia si no cuentan con riego de auxilio, fundamentando la necesidad de
introducir cultivos tolerantes a sequías intermitentes o sistemas de riego por
goteo que estabilicen el abasto de agua en el suelo.

== Impacto por Sequía Acumulada Municipal (ISAG) por Ciclo

El Índice de Impacto por Sequía Acumulada Georeferenciada (ISAG) evalúa el
riesgo de afectación sobre la actividad agrícola municipal distinguiendo entre los
ciclos productivos Primavera-Verano (P-V) y Otoño-Invierno (O-I).

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  align(center)[
    #figure(
      image("../../reports/fase3/prueba_analisis/images/mapa_isag_primavera-verano.png", width: 90%),
      caption: [ISAG Ciclo Primavera-Verano (P-V)],
    )
  ],
  align(center)[
    #figure(
      image("../../reports/fase3/prueba_analisis/images/mapa_isag_otoño-invierno.png", width: 90%),
      caption: [ISAG Ciclo Otoño-Invierno (O-I)],
    )
  ],
)

La distribución geográfica del ISAG demuestra que el ciclo Primavera-Verano
concentra una vulnerabilidad extrema casi generalizada en todo el estado, debido
al incremento en las temperaturas veraniegas y la alta evaporación previa al
monzón. En el ciclo Otoño-Invierno, el impacto es menor y se concentra en el
norte y altiplano. Para la reconversión productiva, este análisis determina que
las restricciones son más severas en el ciclo P-V, donde se debe sustituir de
inmediato el maíz por sorgo forrajero o suspender siembras de alta demanda en
áreas clasificadas con vulnerabilidad "Alta".




== Estrés Agroclimático por Temperaturas Extremas

Este indicador evalúa la cantidad de días promedio anuales en que los cultivos
se ven expuestos a temperaturas extremas, ya sea por estrés térmico por calor
o riesgo de daño físico por heladas.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/estres_termico_municipios.png",
      width: 80%,
    ),
    caption: [Días Promedio de Estrés por Calor y Riesgo de Helada],
  )
]

Los resultados muestran una clara segmentación térmica en Sonora: los municipios de
la sierra alta experimentan un elevado número de días con temperaturas bajo cero
(riesgo de helada), limitando el establecimiento de perennes sensibles como cítricos.
Por su parte, los municipios desérticos y costeros registran más de 90 días de
estrés por calor extremo por ciclo, lo cual inhibe la polinización y viabilidad
de diversas hortalizas durante el verano. Este análisis justifica la necesidad de
seleccionar variedades de cultivos alternativos adaptados genéticamente a estos
umbrales térmicos específicos.

== Distribución Espacial de Temperaturas por Municipio

Para consolidar la zonificación térmica del estado, se generaron mapas de la
distribución geográfica de las temperaturas media, máxima y mínima registradas:

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  align(center)[
    #figure(
      image(
        "../../reports/fase3/prueba_analisis/images/mapa_temperatura_media.png",
        width: 95%,
      ),
      caption: [Temperatura Media Promedio del Ciclo],
    )
  ],
  align(center)[
    #figure(
      image(
        "../../reports/fase3/prueba_analisis/images/mapa_temperatura_maxima.png",
        width: 95%,
      ),
      caption: [Temperatura Máxima Promedio del Ciclo],
    )
  ],
)

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/mapa_temperatura_minima.png",
      width: 70%,
    ),
    caption: [Temperatura Mínima Promedio del Ciclo],
  )
]

Los tres mapas de temperatura muestran un patrón constante donde la altitud de la
Sierra Madre Occidental amortigua las temperaturas máximas pero intensifica las
mínimas estacionales, mientras que la llanura costera y el desierto noroccidental
actúan como ollas de calor extremo. Esta cartografía sirve de base técnica para
la exclusión de cultivos alternativos que no toleren temperaturas superiores a
40 °C en su etapa de floración o requieran horas-frío específicas para romper
dormancia.

== Láminas Técnicas de Riego por Cultivo (INIFAP/FIRA)

Los requerimientos hídricos teóricos (láminas netas recomendadas) para los
cultivos tradicionales y potenciales se presentan en la siguiente tabla de
referencia agronómica:

#align(center)[
  #table(
    columns: (auto, 1fr, 1fr, 1fr),
    align: (left, center, center, center),
    [*Cultivo*], [*Tipo*], [*Lámina (mm)*], [*Ciclo (Días)*],
    [Alfalfa], [Forraje (Perenne)], [1,650], [365],
    [Nogal Pecanero], [Frutal (Perenne)], [1,350], [365],
    [Dátil], [Frutal (Perenne)], [1,850], [365],
    [Maíz Grano], [Grano], [800], [150],
    [Trigo Grano], [Grano], [650], [160],
    [Tomate Rojo], [Hortaliza], [725], [140],
    [Garbanzo Grano], [Leguminosa], [375], [150],
  )
]

La tabla evidencia la gran brecha en el consumo de agua: cultivos perennes como la
alfalfa, el nogal y el dátil demandan láminas anuales acumuladas de más de 1,350 mm
a 1,850 mm. Al permanecer todo el año en el campo, consumen agua de forma continua,
incluso en los meses de sequía más severa. Por otro lado, granos como el trigo y el
maíz requieren láminas sustanciales de 650 a 800 mm pero en periodos más acotados.
Las alternativas como el garbanzo (375 mm) y hortalizas tecnificadas representan un
consumo sustancialmente menor por ciclo, lo que los convierte en los candidatos
ideales para la reconversión hídrica.

== Balance de Déficit Hídrico Climatológico por Municipio

El déficit hídrico climatológico ($E T_o - P_("ef")$) representa la brecha física
que la precipitación efectiva es incapaz de cubrir para satisfacer la demanda
de evapotranspiración de referencia en el suelo.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/deficit_hidrico_municipios.png",
      width: 80%,
    ),
    caption: [Municipios con Mayor Déficit Hídrico Climatológico Anual (mm)],
  )
]

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/mapa_deficit_hidrico.png",
      width: 75%,
    ),
    caption: [Mapa de Distribución del Déficit Hídrico Climatológico],
  )
]

Los resultados cuantitativos demuestran que el municipio de Naco registra el mayor
déficit con 1,240.24 mm anuales, seguido de cerca por Arizpe y Bacoachi. Este
déficit tan pronunciado significa que para sostener cualquier cultivo en estas
zonas, el agricultor debe extraer y bombear volúmenes enormes de agua de riego
suplementario. Esto eleva los costos operativos y acelera el abatimiento local
de los acuíferos. En municipios con déficits superiores a 1,000 mm, la reconversión
hacia cultivos de bajo consumo es una necesidad ambiental imperiosa.

== Dependencia de Riego vs. Lluvia (Fracción Azul vs. Verde)

Este análisis calcula la proporción de la evapotranspiración de los cultivos que
se cubre con agua extraída de presas o acuíferos (fracción azul) en contraste con
la fracción de agua de lluvia efectiva retenida en el suelo (fracción verde).

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/fraccion_azul_verde_municipios.png",
      width: 80%,
    ),
    caption: [Dependencia de Riego (Fracción Azul) vs. Lluvia (Fracción Verde)],
  )
]

La fracción azul supera el 90% en la gran mayoría de los municipios de la planicie
costera e hiperáridos de Sonora, lo cual ratifica que la agricultura estatal tiene
una dependencia casi absoluta de las fuentes de extracción física y de la
infraestructura hidráulica. Esto confirma que la sustentabilidad de la agricultura
está ligada a reducir la huella hídrica azul mediante la reconversión productiva hacia
cultivos de menores láminas, disminuyendo la presión sobre presas y acuíferos.

== Presión Hídrica por Concesiones de Extracción (REPNA)

El análisis de los títulos de concesión del REPNA otorgados por la CONAGUA revela
la severa presión de extracción que ejerce la agricultura comercial sobre las cuencas
e infraestructura hidráulica del estado. El caso más crítico es el de la región del
*DDR Hermosillo (Costa de Hermosillo DR-051)*, cuyos títulos agrícolas autorizan una
extracción superior a los *320 millones de metros cúbicos anuales*. Este volumen es
extraído en su totalidad de fuentes subterráneas, lo que ha provocado un grave
fenómeno de intrusión salina del Golfo de California en el acuífero de la Costa de
Hermosillo. Cruzar este volumen concesionado con una recurrencia de sequía de 16.8%
en el mismo distrito justifica la urgencia legal y física de aplicar reconversión
hacia cultivos eficientes que consuman solo una fracción de su título original.

== Evolución del Volumen Bruto por Distrito de Riego (1998-2024)

Para complementar la presión legal (concesiones), se analizó la serie histórica
de volúmenes brutos de agua superficial y subterránea efectivamente desviados para
riego agrícola en los cinco Distritos de Riego (DR) de Sonora.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/evolucion_volumen_dr.png",
      width: 90%,
    ),
    caption: [Evolución del Volumen Bruto de Riego por DR en Sonora (1998-2024)],
  )
]

El gráfico temporal muestra que el *DR-041 Río Yaqui* domina el consumo estatal,
registrando consumos brutos de agua de hasta 2,400 Mm³ en años favorables. Sin
embargo, muestra una alta vulnerabilidad ante sequías severas; por ejemplo, en 2004,
el volumen disponible colapsó a solo 454 Mm³, obligando a reducir drásticamente el
área sembrada de trigo y maíz y provocando una crisis económica regional. Por su
parte, el *DR-051 Costa de Hermosillo* extrae de manera constante entre 350 y 500
Mm³/año de pozos profundos, sin variabilidad interanual, lo que confirma una presión
constante e independiente del clima que acelera la sobreexplotación del acuífero.

== Volumen Total Acumulado por Distrito de Riego

Este gráfico apilado acumula los volúmenes anuales desviados por los cinco distritos,
dimensionando la demanda hídrica conjunta de la agricultura comercial en el estado.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/volumen_total_apilado_dr.png",
      width: 90%,
    ),
    caption: [Volumen Total de Agua Agrícola Acumulado por DR en Sonora],
  )
]

La demanda total acumulada de la agricultura en distritos de riego oscila entre
los 2,000 y 4,500 Mm³ de agua bruta anuales. Frente a esta escala de consumo, una
reducción de apenas el 10% en el consumo hídrico mediante la reconversión y
tecnificación agrícola liberaría entre 200 y 450 millones de metros cúbicos anuales.
Este volumen recuperado equivale al consumo total de agua potable de todas las áreas
urbanas del estado de Sonora durante un año, demostrando el impacto social y ecológico
que tiene la reconversión productiva.

= Índice Compuesto de Vulnerabilidad Hídrica Municipal (IVH)

Con el fin de consolidar los 13 indicadores previos en una herramienta única y
operativa de planeación y priorización de políticas públicas, se desarrolló el
*Índice de Vulnerabilidad Hídrica (IVH)*. Este indicador pondera y normaliza
los factores climáticos, geográficos y agrícolas del estado:

#align(center)[
  #table(
    columns: (1fr, auto, auto),
    align: (left, center, center),
    [*Componente*], [*Peso*], [*Fuente*],
    [Déficit Hídrico Climatológico ($E T_o - P_("ef")$)], [0.35], [NASA POWER],
    [Vulnerabilidad ISAG (sequía acumulada)], [0.20], [MSM / SMN],
    [Dependencia de Riego (fracción azul)], [0.35], [Modelo HH],
    [Estrés Térmico (calor + helada)], [0.10], [NASA POWER],
  )
]

El IVH clasifica a los municipios en cuatro categorías:
- *Crítica* (IVH $>= 0.70$): Prioridad de reconversión inmediata y total.
- *Alta* ($0.50 <=$ IVH $< 0.70$): Intervención prioritaria y tecnificación.
- *Moderada* ($0.30 <=$ IVH $< 0.50$): Manejable con rotación de cultivos.
- *Baja* (IVH $< 0.30$): Zonas hídricamente estables.

== Mapa de Vulnerabilidad Hídrica Integral

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/mapa_vulnerabilidad_compuesta.png",
      width: 80%,
    ),
    caption: [Índice Compuesto de Vulnerabilidad Hídrica Municipal (IVH)],
  )
]

El mapa muestra un claro gradiente de vulnerabilidad que se intensifica del
este al oeste. Los municipios de la sierra (como Yécora, Quiriego, Álamos)
mostraban niveles bajos o moderados debido a las mayores precipitaciones. En
contraste, la planicie costera (Hermosillo, Guaymas, Cajeme) y el desierto de
Caborca y San Luis Río Colorado presentan vulnerabilidades críticas y altas
debido a la escasez pluvial y la alta dependencia de agua subterránea o
superficial para riego.

== Ranking de Municipios por Vulnerabilidad Hídrica

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/vulnerabilidad_ranking_municipios.png",
      width: 80%,
    ),
    caption: [Top 15 Municipios con Mayor Vulnerabilidad Hídrica (IVH)],
  )
]

El ranking individualiza los 15 municipios con mayores valores de IVH en el estado,
encabezados por San Luis Río Colorado, Puerto Peñasco, Plutarco Elías Calles,
Hermosillo y Caborca. Estos municipios superan el umbral crítico de 0.70 o se sitúan
en la zona de alta vulnerabilidad. Esto indica que cualquier política de
reconversión productiva o restricción agrícola debe iniciarse de manera focalizada
en estas demarcaciones para maximizar el impacto de ahorro de agua.

== Desglose por Componente del Índice

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/vulnerabilidad_desglose_top5.png",
      width: 85%,
    ),
    caption: [Desglose de Vulnerabilidad por Componente — Top 5 Municipios],
  )
]

El desglose por componente revela la causa raíz de la vulnerabilidad, permitiendo
diseñar estrategias personalizadas ("trajes a la medida"):
- En *San Luis Río Colorado*, la vulnerabilidad proviene casi por completo del
  déficit hídrico extremo de su clima desértico.
- En *Hermosillo*, la vulnerabilidad es impulsada principalmente por la altísima
  dependencia de riego (agua azul) sobre un acuífero ya sobreexplotado, combinada
  con el impacto acumulado del ISAG.
Esto justifica que en San Luis Río Colorado la solución sea buscar especies rústicas
que no requieran agua, mientras que en Hermosillo se debe tecnificar drásticamente
el riego (goteo, mallas) o cambiar alfalfa/nogal por cultivos hortícolas rápidos.
