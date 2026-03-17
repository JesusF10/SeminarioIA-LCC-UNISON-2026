#set page(
  paper: "a4",
  margin: 2cm,
)
#set text(
  font: "Nimbus Sans",
  size: 10pt,
)

#align(center)[
  #text(size: 16pt, weight: "bold")[Glosario Técnico y Diccionario de Datos] \
  #text(size: 11pt, fill: gray)[Seminario IA 2026 - Reconversión de Cultivos]
]

#v(0.5cm)

=== 1. Instituciones y Siglas
/ *SIAP*: Servicio de Información Agroalimentaria y Pesquera. Proporciona las 
estadísticas oficiales de producción.
/ *INIFAP*: Instituto Nacional de Investigaciones Forestales, Agrícolas y 
Pecuarias. Desarrolla las guías técnicas de siembra.
/ *CONAGUA*: Comisión Nacional del Agua. Administra el recurso hídrico y la 
infraestructura de los Distritos de Riego (DR).
/ *REPNA / REPDA*: Registro Público de Derechos de Agua.
/ *FIRA*: Fideicomisos Instituidos en Relación con la Agricultura.

=== 2. División Territorial y Niveles de Análisis
/ *DR (Distrito de Riego)*: Delimitación geográfica de **CONAGUA** basada en 
infraestructura hidráulica (presas y canales). No coincide necesariamente con 
límites municipales.
/ *DDR (Distrito de Desarrollo Rural)*: División administrativa de la **SADER** 
para planeación y estadística. Sonora cuenta con 13 DDRs que agrupan municipios.
/ *Municipio*: Unidad político-administrativa base. Es la **llave maestra** 
(`CVE_MUN`) que conecta los datos de producción, sequía y concesiones.
/ *Cader*: Centro de Apoyo al Desarrollo Rural. Oficina operativa local dentro 
de un DDR.

=== 3. Unidades y Estándares
/ *hm3*: Hectómetro cúbico ($10^6$ "m"^3).
/ *mm*: Milímetros de lámina de riego ($1 "mm" = 10 "m"^3/"Ha"$).
/ *Ha*: Hectárea ($10,000$ "m"^2).
/ *Ton*: Tonelada métrica ($1,000$ kg).
/ *PMR*: Precio Medio Rural (\$ / Ton).

=== 4. Atributos Técnicos (Columnas de Datos)
/ *CVE_MUN / CVEGEO*: Código INEGI/SIAP del municipio (Crucial para integración).
/ *Idddr / Nomddr*: Identificador y nombre del Distrito de Desarrollo Rural.
/ *ISAG*: Índice de Severidad de Sequía Agrícola.
/ *cap_namo*: Capacidad de Almacenamiento Máximo Operativo de presas.
/ *Sembrada / Siniestrada*: Hectáreas establecidas vs. hectáreas perdidas.

#v(0.5cm)
#line(length: 100%, stroke: 0.5pt + gray)
#text(size: 8pt, style: "italic")[Documento consolidado tras aclaración de 
jerarquía territorial - Marzo 2026]
