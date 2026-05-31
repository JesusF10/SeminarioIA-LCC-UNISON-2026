
#set page(paper: "us-letter", margin: 2.5cm)
#set text(font: "Libertinus Serif", size: 11pt, lang: "es")
#set par(leading: 0.75em, justify: true)

#align(center)[
  #text(size: 18pt, weight: "bold")[Reporte: Reconversión de Cultivos en Sonora]
  #v(1em)
  #text(size: 12pt)[Seminario de Inteligencia Artificial 2026 \
  Licenciatura en Ciencias de la Computación, Universidad de Sonora (UNISON)]
  #v(2em)
]

= Integrantes
- Jesús Flores Lacarra
- Michell Berenice Altamirano Ocejo
- Orlando López Roque
- Sebastián Rodríguez Serrano

= Colaboración Técnica
Lic. Manuel Alberto Valenzuela Arce (Equipo de Ciencia de Datos, UNISON)

= Introducción
Este documento detalla la metodología computacional desarrollada para el análisis de la reconversión productiva en el estado de Sonora. El proyecto busca optimizar el uso del agua y mejorar la rentabilidad agrícola mediante un análisis técnico de la huella hídrica.

= Metodología
El sistema implementa los siguientes estándares y fuentes de datos para el periodo 2003–2024:

- *Huella Hídrica:* Cálculo de componentes verde y azul conforme a estándares internacionales.
- *Evapotranspiración:* Aplicación de la metodología FAO-56 Penman-Monteith.
- *Datos Climáticos:* Integración con la API de NASA POWER.
- *Estadísticas de Producción:* Datos obtenidos del SIAP (Servicio de Información Agroalimentaria y Pesquera).

= Objetivo
Evaluar 128 cultivos distintos a lo largo de los 72 municipios de Sonora para proporcionar herramientas técnicas que soporten la toma de decisiones estratégicas en la reconversión de cultivos, priorizando la sostenibilidad hídrica y la eficiencia económica regional.
