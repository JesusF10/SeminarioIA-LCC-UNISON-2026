#import "@preview/tablex:0.0.8": tablex, cellx

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
    caption: [Top 15 Cultivos más Eficientes en Sonora (Promedio 2010-2024)],
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
    caption: [Top 15 Cultivos MENOS Eficientes en Sonora],
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
    caption: [Top 15 Cultivos con mayor Valor Económico por m³ de Agua],
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

= Conclusiones y Recomendaciones

1. *Reconversión Selectiva:* Se recomienda priorizar la expansión de cultivos
   de alta eficiencia en zonas con déficit hídrico crítico.
2. *Caso de la Nuez:* Los frutales como la nuez muestran las eficiencias más
   bajas (frecuentemente < 0.0001 Ton/m³), lo que exige una revisión de su
   viabilidad a largo plazo en regiones de alta escasez.
3. *Eficiencia en Forrajes:* Cultivos como la avena y el trigo forrajero
   presentan una eficiencia media-alta (0.006 - 0.007 Ton/m³), siendo opciones
   viables para la seguridad alimentaria ganadera con menor impacto hídrico que
   la alfalfa.
