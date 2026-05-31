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
  #text(size: 18pt, weight: "bold")[Análisis Estadístico de Eficiencia Hídrica] \
  #text(size: 14pt)[Fase 3: Reconversión Productiva en Sonora] \
  #text(size: 12pt)[Mayo 2026]
]

#v(1cm)

= Introducción

Este reporte presenta un análisis detallado de la eficiencia hídrica de los
cultivos en Sonora, utilizando datos de la NASA POWER y registros históricos de
producción (2010-2024). El objetivo es identificar los cultivos que maximizan la
producción por unidad de agua consumida (Toneladas por m³), comparando el
rendimiento agrícola con la huella hídrica total (HH total).

= Diagnóstico Hídrico y Riesgo por Sequía

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

= Especificaciones de Cultivos y Condiciones de Contorno

Como paso previo al análisis de eficiencia, se describen las especificaciones
técnicas de los cultivos clave y las condiciones de contorno físicas bajo las
cuales opera el modelo de simulación de reconversión agrícola en Sonora.

== Especificaciones Técnicas de los Cultivos

El modelo de simulación se alimenta de los parámetros fenológicos de la FAO-56
y los requerimientos técnicos oficiales provistos por el INIFAP. Los cultivos
estudiados se clasifican en tres categorías según su ciclo vegetativo:

1. *Cultivos Perennes de Alto Consumo:* Alfalfa, Nuez (Nogal Pecanero) y Dátil.
2. *Cultivos de Ciclo Corto Otoño-Invierno (O-I):* Trigo Grano y Garbanzo Grano.
3. *Cultivos de Ciclo Corto Primavera-Verano (P-V):* Maíz Grano.

=== Parámetros Clave y su Función en el Modelo

Para cada cultivo, se definen los siguientes parámetros de entrada que
condicionan y estructuran los cálculos matemáticos del modelo:

- *Duración del Ciclo Vegetativo (en días):*
  *Definición:* El número de días desde la siembra o brote hasta la cosecha.
  *Función en el cálculo:* Define el rango temporal de integración diaria. La
  evapotranspiración ($"ET"_c$) y la lluvia efectiva ($P_("ef")$) se calculan y
  acumulan día con día a lo largo de este ciclo específico para determinar el
  volumen total de consumo hídrico del cultivo.

- *Coeficiente de Cultivo ($K_c$) por Etapas (Inicial, Media, Final):*
  *Definición:* Factor dimensional que relaciona la demanda evapotranspirativa
  del cultivo con la de un cultivo de referencia (pasto) bajo el mismo clima.
  *Función en el cálculo:* Se multiplica por la evapotranspiración de
  referencia ($"ET"_o$) diaria (Penman-Monteith) para calcular el requerimiento
  fisiológico diario del cultivo ($"ET"_c = K_c dot "ET"_o$).

- *Lámina de Riego Técnica Recomendada (INIFAP, en mm):*
  *Definición:* El volumen total acumulado de riego recomendado para aplicarse
  en parcela bajo prácticas de riego tradicionales de la región.
  *Función en el cálculo:* Sirve como la demanda aplicada de diseño
  ($L_("riego")$). Se contrasta contra la evapotranspiración real del modelo
  para cuantificar la eficiencia de aplicación del riego por gravedad o goteo y
  calcular los ahorros volumétricos potenciales.

- *Rendimiento Físico Esperado (en Ton/Ha):*
  *Definición:* La productividad de cosecha comercial obtenida por unidad de
  superficie sembrada.
  *Función en el cálculo:* Es el denominador en la ecuación de la Huella
  Hídrica ($"HH" = "UAC" / "Rendimiento"$). Permite transformar la variable
  física del agua consumida ($m^3 / "Ha"$) en una métrica de productividad
  física del recurso ($m^3 / "Ton"$).

== Condiciones de Contorno, REPNA y Tecnificación (Bloque 2)

El modelado de reconversión productiva no opera en el vacío, sino que está
acotado por condiciones de contorno físicas, límites legales de concesión y el
nivel de eficiencia de la infraestructura de riego en Sonora.

=== 1. El Cultivo de Referencia de la FAO-56 (Base de $E T_o$)

La evapotranspiración de referencia ($E T_o$) representa el flujo de agua
evaporada por un cultivo teórico de referencia. El estándar internacional
FAO-56 define este cultivo con características biofísicas fijas:
- *Altura uniforme:* $0.12$ metros.
- *Albedo (reflexión de radiación):* $0.23$.
- *Resistencia superficial:* $70$ s/m, que asume un cultivo activo, denso y
  adecuadamente provisto de agua en todo momento.

Este cultivo teórico emula una superficie extensa de pasto verde. Al fijar
estas variables biológicas, la variabilidad de la $E T_o$ depende únicamente del
clima (radiación, temperatura, humedad y viento). Esto justifica
científicamente la introducción de los coeficientes de cultivo ($K_c$), que
funcionan como factores de escala para adaptar esta demanda climática base a la
fenología y morfología real de los cultivos establecidos en Sonora.

=== 2. Condiciones Físicas y Ambientales (NASA POWER)

Las simulaciones de evapotranspiración de referencia ($"ET"_o$) se realizan a
escala diaria para el periodo 2003-2024 utilizando los datos climatológicos de
la NASA POWER a nivel de centroide municipal. Las variables utilizadas son:
- *Radiación Solar Global ($R_s$):* Energía disponible para evaporación.
- *Humedad Relativa ($"RH"$) y Viento ($u_2$):* Poder desecante de la atmósfera.
- *Temperatura Máxima, Mínima y Media:* Regulan el desarrollo fenológico y
  los umbrales de estrés agroclimático por helada ($< 0^o "C"$) o calor extremo
  ($> 40^o "C"$).

=== 3. Derechos de Extracción REPNA como Límite del Modelo

El Registro Público de Derechos de Agua (REPNA) de CONAGUA actúa como una
restricción legal y volumétrica de primer orden:
- *Criterio de Restricción:* Ninguna propuesta de reconversión de cultivos
  puede recomendar una demanda agregada de agua de riego que supere el volumen
  concesionado registrado en el REPNA para el municipio o Distrito de Riego.
- *Rol en los cálculos:* El volumen total de concesión ($V_("concesión")$ en
  $m^3$/año) establece el "techo de demanda hídrica permisible". Si un cultivo
  requiere una lámina que al multiplicarse por la superficie cultivada supera
  este techo, el modelo descarta la viabilidad de la superficie completa o
  fuerza la sustitución inmediata por cultivos de bajo consumo.

=== 4. Niveles de Tecnificación y Eficiencia del Riego

La demanda real de extracción en pozo o presa ($V_("extracción")$) se calcula
dividiendo la demanda fisiológica neta ($"ET"_"azul"$) entre el coeficiente de
eficiencia de aplicación del sistema de riego ($eta$):
$$ V_("extracción") = frac("ET"_"azul", eta) $$

Se modelan tres niveles de tecnificación que condicionan los resultados:
- *Riego por Gravedad (Tradicional):* Riego por surcos o melgas, con una
  eficiencia de aplicación promedio de $eta = 0.60$ a $0.65$. Esto significa que
  entre el 35% y 40% del agua extraída se pierde por infiltración profunda o
  escorrentía, elevando drásticamente el bombeo real.
- *Riego por Aspersión:* Eficiencia intermedia de $eta = 0.75$ a $0.80$, típica
  en cultivos forrajeros tecnificados.
- *Riego Localizado (Goteo):* Eficiencia óptima de $eta = 0.85$ a $0.90$.
  Minimiza las pérdidas por evaporación directa y escorrentía, reduciendo
  la extracción real de agua azul en más de un 30% para cultivos hortícolas
  o perennes reconvertidos.

=== 5. Diagnóstico de la Tecnificación Real en Sonora (SAGARPA/UNISON)

Para calibrar el modelo con la realidad del campo sonorense, se integró el
estudio de actualización de la delegación estatal de SAGARPA y la Universidad de
Sonora. Los datos muestran una baja tecnificación generalizada:

- *Promedio Estatal:* De las 531,701 hectáreas en operación agrícola en el
  estado, solo 106,418 hectáreas están tecnificadas, lo que representa apenas el
  *20.0%* de tecnificación general. El 80.0% restante depende de riego por
  gravedad tradicional con altas tasas de pérdida.
- *Disparidad Regional por DDR:*
  - *DDR Guaymas (78.0%) y DDR Caborca (70.0%):* Presentan los mayores niveles
    de tecnificación debido al predominio de pozos profundos particulares con
    cultivos de alto valor (hortalizas, vid, espárrago).
  - *DDR Hermosillo (47.0%):* Muestra un nivel intermedio, condicionado por
    bombeos subterráneos en la Costa de Hermosillo.
  - *DDR Cajeme (8%) y DDR Navojoa (13%):* Los distritos de mayor superficie
    agrícola del estado (Valles del Yaqui y Mayo) registran niveles críticamente
    bajos. Al depender de agua de canales superficiales de presas, la gran
    mayoría de la superficie de granos (trigo y maíz) opera bajo gravedad.
- *Agricultura Protegida:* Se registran solo 2,872 hectáreas bajo condiciones de
  agricultura protegida (1,370 Ha de invernaderos y 1,501 Ha de malla sombra),
  concentrándose el 65% en los distritos de Cajeme y Hermosillo.

Este diagnóstico demuestra que la reconversión productiva debe ir de la mano con
un programa agresivo de tecnificación en los valles del sur (Yaqui y Mayo), ya
que transicionar a cultivos de bajo consumo sin tecnificar los canales y
parcelas limitaría los ahorros volumétricos de agua azul.

#align(center)[
  #figure(
    image(
      "../../reports/fase3/prueba_analisis/images/tecnificacion_riego_ddr.png",
      width: 85%,
    ),
    caption: [Distribución de la Tecnificación del Riego por DDR en Sonora],
  )
]

= Metodología

La eficiencia se define como la inversa de la Huella Hídrica Total ($1/"HH"_"total"$),
representando la cantidad de producto obtenido por cada metro cúbico de agua
evapotranspirada (verde + azul). Se analizaron 12,747 registros municipales para
extraer tendencias por Distrito de Desarrollo Rural (DDR) y Municipio.

= Resultados Globales

El análisis global revela una disparidad significativa en la eficiencia hídrica
entre diferentes grupos de cultivos. Las hortalizas y flores muestran, en
general, una eficiencia mayor debido a su alto rendimiento en relación con su
consumo hídrico acumulado durante el ciclo.

#align(center)[
  #figure(
    image("../../reports/fase3/prueba_analisis/images/top_eficiencia_global.png", width: 80%),
    caption: [Cultivos más Eficientes en Sonora (Promedio 2010-2024)],
  )
]

== Cultivos Líderes en Eficiencia

A continuación se muestran los cultivos con mayor eficiencia hídrica en el
estado:

#table(
  columns: (auto, 1fr, 1fr, 1fr),
  align: (left, center, center, center),
  [*Cultivo*], [*Eficiencia (Ton/m³)*], [*Rendimiento (Ton/Ha)*], [*Valor (MXN/m³)*],
  [Col (repollo)], [0.0375], [32.20], [156,032],
  [Coliflor], [0.0213], [22.00], [143,770],
  [Hortalizas], [0.0166], [13.75], [72,582],
  [Caña (piloncillo)], [0.0148], [60.00], [33,901],
  [Zanahoria], [0.0127], [28.00], [55,125],
)

= Cultivos con Menor Eficiencia Hídrica

No todos los cultivos presentan un retorno hídrico favorable. Los frutales de
largo ciclo y ciertas leguminosas muestran las eficiencias más bajas del estado,
requiriendo volúmenes masivos de agua por cada tonelada producida.

#align(center)[
  #figure(
    image("../../reports/fase3/prueba_analisis/images/peores_eficiencia_global.png", width: 80%),
    caption: [Cultivos MENOS Eficientes en Sonora],
  )
]

== El Caso Crítico de los Frutales y Granos

Los cultivos enlistados a continuación representan el mayor reto para la
sustentabilidad hídrica en Sonora:

#table(
  columns: (auto, 1fr, 1fr),
  align: (left, center, center),
  [*Cultivo*], [*Eficiencia (Ton/m³)*], [*Consumo (m³/Ton)*],
  [Cereza], [0.000037], [26,850],
  [Nuez], [0.000108], [11,164],
  [Frijol], [0.000175], [6,464],
  [Ajonjolí], [0.000163], [8,883],
  [Cacahuate], [0.000212], [5,615],
)

= Productividad Económica del Agua

La eficiencia no debe medirse solo en masa, sino en valor. La *Productividad
Económica* ($"MXN"/m^3$) se calcula multiplicando el Precio Medio Rural (PMR)
por la eficiencia hídrica ($"Ton"/"m"^3$). Esto permite identificar qué cultivos
generan más riqueza por cada gota de agua invertida.

#align(center)[
  #figure(
    image("../../reports/fase3/prueba_analisis/images/productividad_economica.png", width: 80%),
    caption: [Cultivos con mayor Valor Económico por m³ de Agua],
  )
]

== Análisis de Rentabilidad vs. Eficiencia (Cuadrantes)

Al cruzar la rentabilidad por tonelada (PMR) con la eficiencia hídrica física,
podemos clasificar los cultivos en cuatro categorías. El cuadrante superior
derecho representa los cultivos "ideales": *Alta Rentabilidad y Bajo Consumo*.

#align(center)[
  #figure(
    image("../../reports/fase3/prueba_analisis/images/cuadrante_rentabilidad_eficiencia.png", width: 80%),
    caption: [Análisis de Cuadrantes: Rentabilidad (PMR) vs. Eficiencia Hídrica],
  )
]

Se observa que cultivos como la *Coliflor* y el *Tomate rojo* se posicionan
como líderes absolutos, no solo por producir mucha biomasa por litro, sino por
el alto valor de mercado de dicha biomasa. En contraste, granos como el trigo y
la avena forrajera, aunque eficientes en masa, poseen una productividad
económica significativamente menor debido a sus bajos PMR.

== Relación Valor vs. Consumo (Escala Logarítmica)

Para entender la dispersión total, comparamos el valor ($"PMR"$) contra el
consumo total ($"HH"_"total"$). Esta vista permite identificar cultivos que son
"lujos hídricos" (alto valor pero altísimo consumo) vs. "motores económicos"
(alto valor y bajo consumo).

#align(center)[
  #figure(
    image("../../reports/fase3/prueba_analisis/images/valor_vs_hh_log.png", width: 80%),
    caption: [Relación Valor de Mercado (MXN/Ton) vs. Huella Hídrica (m³/Ton)],
  )
]

= Análisis por Distrito de Desarrollo Rural (DDR)

Cada DDR presenta una especialización distinta y un retorno económico hídrico
diferenciado. La productividad económica media por región revela dónde el agua
se traduce en mayor riqueza local.

#align(center)[
  #figure(
    image("../../reports/fase3/prueba_analisis/images/productividad_economica_ddr.png", width: 80%),
    caption: [Productividad Económica Media por DDR (MXN/m³)],
  )
]

A continuación se detallan los cultivos más eficientes identificados por región
administrativa:

#table(
  columns: (1fr, 1fr, 1fr),
  align: (left, left, center),
  [*DDR*], [*Cultivo más Eficiente*], [*Eficiencia (Ton/m³)*],
  [Agua Prieta], [Hortalizas], [0.0168],
  [Caborca], [Pepino], [0.0147],
  [Cajeme], [Hortalizas], [0.0232],
  [Guaymas], [Pepino], [0.0146],
  [Hermosillo], [Tomate rojo], [0.0117],
  [Magdalena], [Col (repollo)], [0.0375],
  [Navojoa], [Apio], [0.0126],
)

= Correlación Rendimiento vs. Eficiencia

Se observa una correlación positiva general: a mayor rendimiento (Ton/Ha), mayor
eficiencia hídrica relativa. Esto sugiere que las mejoras tecnológicas que
incrementan el rendimiento tienen un impacto directo y proporcional en el
ahorro de agua por unidad producida.

#align(center)[
  #figure(
    image("../../reports/fase3/prueba_analisis/images/rendimiento_vs_eficiencia.png", width: 70%),
    caption: [Correlación entre Rendimiento y Eficiencia Hídrica],
  )
]

= Barreras de Viabilidad y Adopción del Modelo

La viabilidad matemática de la reconversión productiva se enfrenta a limitantes
de carácter socioeconómico, comercial e infraestructural en el campo
sonorense:

1. *Saturación de Mercados y Volatilidad:* Cultivos altamente eficientes como
   las hortalizas (coliflor, pepino) tienen mercados de exportación muy
   volátiles. Reconvertir masivamente superficies de granos a hortalizas
   saturaría la oferta nacional e internacional, desplomando los precios
   rápidamente.
2. *Inversión de Capital en Tecnificación:* La transición eficiente requiere
   sistemas de riego localizado (goteo) que representan una elevada inversión
   de capital por hectárea. La gran mayoría de los productores ejidales carecen
   de acceso a crédito o capital propio para financiar esta infraestructura.
3. *Logística de Cadena de Frío:* Las hortalizas demandan empaques, cuartos
   fríos y transporte refrigerado rápido. Los distritos del sur (Cajeme/Navojoa)
   están diseñados logísticamente para el acopio masivo de granos secos (silos),
   por lo que carecen de infraestructura de frío para hortalizas perecederas.
4. *Inercia Cultural y Técnica:* Los agricultores sonorenses poseen décadas de
   especialización técnica en la producción de trigo. Existe una resistencia
   cultural al cambio que requiere esquemas agresivos de transferencia de
   tecnología y garantías de precios de cobertura por parte del gobierno.
