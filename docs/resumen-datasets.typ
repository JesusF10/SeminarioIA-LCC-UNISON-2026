= Resumen Exhaustivo de Conjuntos de Datos (Fase 1)

Este documento detalla los conjuntos de datos recopilados para el proyecto de
reconversión productiva en Sonora, incluyendo su origen, estructura y variables
clave.

== 1. SIAP (Servicio de Información Agroalimentaria y Pesquera)

El SIAP es la fuente oficial de estadísticas institucionales de la Secretaría
de Agricultura y Desarrollo Rural (SADER).

=== 1.1 Cierre Agrícola Municipal Sonora (2003-2024)
- *Fuente:* Datos Abiertos SIAP.
- *Frecuencia:* Anual.
- *Variables Clave:*
  - `Anio`: Año del ciclo agrícola.
  - `Nommunicipio`: Nombre del municipio (Clave SIAP/INEGI).
  - `Nomcultivo`: Nombre del cultivo (especie).
  - `Nomcicloproductivo`: Ciclo (OI: Otoño-Invierno, PV: Primavera-Verano, PE:
    Perennes).
  - `Nommodalidad`: Riego o Temporal.
  - `Sembrada`, `Cosechada`, `Siniestrada`: Superficies en hectáreas (ha).
  - `Volumenproduccion`: Producción en toneladas (t).
  - `Rendimiento`: Eficiencia (t/ha).
  - `Preciomediorural`: Precio pagado al productor (MXN/t).
  - `Valorproduccion`: Valor total (MXN).

=== 1.2 Cierre Agrícola Nacional (1980-2002)
- *Fuente:* Histórico SIAP.
- *Nota:* Proporciona la serie histórica de largo plazo para análisis de
  tendencias climáticas y cambios en patrones de cultivo.
- *Variables:* Similares a la serie municipal, pero con menor detalle geográfico
  (estatal) en los años más antiguos.

== 2. SIACON (Sistema de Información Agroalimentaria de Consulta)

- *Fuente:* Software SIACON-NG (SADER).
- *Formato:* Archivos de texto estructurados como reportes.
- *Contenido:* Datos históricos de producción agrícola a escala municipal para
  Sonora.
- *Variables:* Año, Cultivo, Ciclo, Modalidad, Superficies, Producción,
  Rendimiento y Precios. Requiere limpieza de datos debido a su formato de
  salida de reporte.

== 3. Datos Abiertos del Gobierno de Sonora

=== 3.1 Agricultura Sonora (1999-2023)
- *Fuente:* Portal de Datos Abiertos del Estado de Sonora.
- *Variables:* Incluye desgloses por Distrito de Desarrollo Rural (DDR) y
  variedades específicas de cultivos (ej. Trigo Cristalino vs. Panificable).

=== 3.2 Recursos Hídricos (Presas)
- *Fuente:* CONAGUA / Gobierno de Sonora.
- *Variables:*
  - `Clave`: Identificador de la presa.
  - `Fecha`: Registro diario/mensual.
  - `Almacenamiento (hm³)`: Volumen de agua almacenado en hectómetros cúbicos.
  - `Capacidad NAMO/NAME`: Niveles de operación.

== 4. Datos de Sequía (Georeferenciados)

- *Fuente:* Mapa de Impacto de la Sequía (Gobierno de México).
- *Formato:* Shapefile (Vectorial).
- *Variables Clave:*
  - `ISAG_P-V`, `ISAG_O-I`: Índice de Impacto de la Sequía en la Agricultura.
  - `PER_CA`: Porcentaje de pérdida de capacidad.
  - `geometry`: Delimitación geográfica municipal para mapas de calor.

== 5. Datos Proporcionados e Internos

=== 5.1 REPNA (Registro Público de Derechos de Agua)
- *Fuente:* CONAGUA.
- *Variables:* Titular del derecho, volumen de extracción concesionado (m³/año),
  uso (Agrícola), y desglose entre aguas superficiales y subterráneas.

=== 5.2 Manual Técnico de Cultivos Sonora (2024)
- *Fuente:* INIFAP / FIRA.
- *Propósito:* Proporcionar parámetros técnicos para la reconversión.
- *Variables:*
  - `lamina_riego_mm`: Necesidad hídrica del cultivo.
  - `costo_prod_mxn_ha`: Costos directos de producción.
  - `ciclo_dias`: Duración del cultivo.
  - `etapa_critica`: Periodo donde la falta de agua es fatal.

=== 5.3 Tecnificación de Riego (2021)
- *Fuente:* SADER (Distritos de Desarrollo Rural).
- *Contenido:* Inventario de hectáreas con riego por goteo, aspersión o gravedad
  desglosado por DDR en Sonora.
