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
/ *SIAP*: Servicio de Información Agroalimentaria y Pesquera. Fuente oficial
de estadísticas de producción en México.
/ *INIFAP*: Instituto Nacional de Investigaciones Forestales, Agrícolas y
Pecuarias. Genera los "Paquetes Tecnológicos" (guías de siembra).
/ *CONAGUA*: Comisión Nacional del Agua. Administra el recurso hídrico y la
infraestructura de presas.
/ *REPNA / REPDA*: Registro Público de Derechos de Agua. Base de datos de
concesiones legales para extracción de agua.
/ *FIRA*: Fideicomisos Instituidos en Relación con la Agricultura. Fuente de
referencia para costos de producción (*Agrocostos*).
/ *DDR*: Distrito de Desarrollo Rural. Sonora cuenta con 13 DDRs (unidades de
gestión administrativa).
/ *Cader*: Centro de Apoyo al Desarrollo Rural. Unidad operativa local dentro
de un DDR.

=== 2. Unidades y Estándares
/ *hm3*: Hectómetro cúbico ($10^6$ "m"^3). Unidad estándar para volumen de presas.
/ *mm*: Milímetros de lámina de riego. Representa la altura de agua aplicada
sobre una superficie ($1 "mm" = 10 "m"^3/"Ha"$).
/ *Ha*: Hectárea ($10,000$ "m"^2). Unidad de medida de superficie agrícola.
/ *Ton / Ton/Ha*: Tonelada métrica y Rendimiento (eficiencia por hectárea).
/ *PMR*: Precio Medio Rural (\$ / Ton). Pago bruto recibido por el productor.
/ *EPSG:4326*: Sistema de coordenadas geográficas WGS84 (usado en shapefiles).

=== 3. Conceptos Agronómicos de Sonora
/ *Agua Rodada*: Riego por gravedad proveniente de presas o canales.
/ *Bombeo*: Extracción de agua de acuíferos mediante pozos profundos.
/ *Reconversión Productiva*: Sustitución de un cultivo por otro con menor
demanda hídrica o mayor rentabilidad.
/ *Etapa Fenológica*: Fases del desarrollo del cultivo (germinación,
floración, llenado de grano, madurez).
/ *Lámina Bruta vs Neta*: La lámina bruta incluye las pérdidas por conducción;
la neta es lo que consume realmente la planta.
/ *OI / PV*: Ciclos productivos Otoño-Invierno (ej. Trigo) y
Primavera-Verano (ej. Sorgo).
/ *Modalidad de Riego*: Clasificación del cultivo en Riego (con suministro
controlado) o Temporal (dependiente de lluvia).

=== 4. Atributos Técnicos (Columnas de Datos)
/ *CVE_MUN / CVEGEO*: Clave INEGI del municipio (ID único para cruces).
/ *Nomcultivo*: Nombre del cultivo (ej. Trigo Grano, Alfalfa).
/ *Sembrada / Cosechada*: Superficie establecida vs superficie recolectada.
/ *Siniestrada*: Superficie perdida por desastres climáticos o falta de agua.
/ *ISAG*: Índice de Severidad de Sequía Agrícola (calculado en shapefiles).
/ *cap_namo*: Capacidad de Almacenamiento Máximo Operativo de una presa.
/ *vol_muerto*: Agua inalcanzable por debajo de las tomas de la presa.
/ *Uso (REPNA)*: Destino del agua concesionada (debe ser "Agrícola").
/ *Fuente_Riego*: Clasificación en Superficial (Presa) o Subterráneo (Pozo).

#v(0.5cm)
#line(length: 100%, stroke: 0.5pt + gray)
#text(size: 8pt, style: "italic")[Documento generado en la Fase 1 - Marzo 2026]
