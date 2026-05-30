

**UNIVERSIDAD DE SONORA**

División de Ingeniería  |  Licenciatura en Ciencias de la Computación

Seminario de Inteligencia Artificial  —  2026

**RECONVERSIÓN DE CULTIVOS EN EL ESTADO DE SONORA**

*Análisis de Huella Hídrica y Viabilidad Productiva para la Optimización*

*del Uso del Agua en la Agricultura Sonorense*

Equipo de investigación:

Jesús Flores Lacarra

Michell Berenice Altamirano Ocejo

Orlando López Roque

Sebastián Rodríguez Serrano

Colaboración técnica:

Lic. Manuel Alberto Valenzuela Arce — Equipo de Ciencia de Datos, UNISON

Proyecto en colaboración con la Secretaría de Agricultura y Desarrollo Rural (SAGARPA / SADER)

Hermosillo, Sonora, México — 2026

# **RESUMEN**

El estado de Sonora enfrenta una creciente presión sobre sus recursos hídricos derivada de condiciones climáticas desérticas, sequías históricas recurrentes y una agricultura que depende en gran medida del riego artificial. Con el objetivo de identificar alternativas productivas más sostenibles, el presente proyecto desarrolló una metodología computacional para calcular la huella hídrica de los cultivos registrados en el estado durante el periodo 2003–2024, a nivel municipal, utilizando el estándar internacional FAO-56 Penman-Monteith.

Los datos climáticos diarios fueron obtenidos a través de la API de NASA POWER para los 72 municipios de Sonora, y las estadísticas de producción agrícola provienen del SIAP. Se implementó en Python un sistema modular que calcula la evapotranspiración de referencia (ETo), la evapotranspiración del cultivo (ETc) mediante coeficientes de cultivo (Kc) derivados del FAO-56, la precipitación efectiva, y la huella hídrica en sus componentes verde (agua de lluvia) y azul (agua de riego). El sistema fue validado con el cultivo de trigo grano como caso piloto, revelando que en municipios como Cajeme la huella hídrica azul representa aproximadamente el 93% de la demanda total, con un valor de 1,646 m³ por tonelada producida.

Los resultados generados constituyen la base técnica para comparar el desempeño hídrico de 128 cultivos registrados, con miras a formular recomendaciones de reconversión productiva que optimicen el uso del agua y mejoren la rentabilidad para los agricultores sonorenses.

**Palabras clave:** *huella hídrica, reconversión de cultivos, Penman-Monteith, FAO-56, evapotranspiración, NASA POWER, SIAP, Sonora, agricultura sostenible.*

# **1\. INTRODUCCIÓN**

## **1.1 Contexto y Problemática**

El estado de Sonora ocupa una posición estratégica en la agricultura nacional. Sus actividades primarias —agricultura, ganadería, pesca y minería— constituyen el eje de su economía regional. La agricultura sonorense se ha consolidado históricamente en torno a cultivos de alta demanda hídrica como el trigo grano, el algodón y distintas hortalizas, sustentados por una extensa infraestructura de distritos de riego que abarca las principales llanuras aluviales del estado.

Sin embargo, el patrón climático predominantemente árido y semiárido de Sonora, sumado a un historial documentado de sequías severas —agravadas por la variabilidad climática creciente— pone en riesgo la continuidad de estos sistemas productivos. La disponibilidad de agua para uso agrícola se ve comprometida por la sobreexplotación de acuíferos, la reducción de almacenamiento en presas y las restricciones crecientes sobre las concesiones registradas en el REPDA (Registro Público de Derechos de Agua). En este contexto, mantener los patrones de cultivo actuales sin un análisis riguroso de su eficiencia hídrica representa un riesgo ambiental, económico y social de magnitud creciente.

El análisis del ciclo 2019–2024 en el municipio de Cajeme —uno de los principales productores de trigo del estado— ilustra con claridad la gravedad de la situación: la huella hídrica azul del trigo grano, es decir, el agua de riego consumida, representa aproximadamente el 93% de su huella total, con un valor cercano a 1,646 m³ por tonelada producida. Esta cifra refleja la alta dependencia del riego artificial y la vulnerabilidad del sistema ante cualquier reducción en la disponibilidad hídrica.

## **1.2 Objetivo General**

*Proponer alternativas de reconversión de cultivos en el estado de Sonora que optimicen el uso del recurso hídrico y mejoren la rentabilidad de los productores agrícolas, a través del cálculo sistemático de la huella hídrica y el análisis del contexto económico de los principales cultivos del estado.*

## **1.3 Objetivos Específicos**

* Calcular la huella hídrica verde y azul de los cultivos registrados en el SIAP para los 72 municipios de Sonora, para el periodo 2003–2024, utilizando la metodología FAO-56 Penman-Monteith.

* Identificar los cultivos con mayor y menor consumo hídrico por tonelada producida, tanto a nivel estatal como por Distrito de Desarrollo Rural (DDR).

* Analizar la rentabilidad de los cultivos candidatos mediante precios medios rurales, costos de producción estimados y demanda de mercado.

* Desarrollar un dashboard interactivo que permita visualizar y comparar la huella hídrica y rentabilidad de los cultivos a nivel municipal.

* Generar recomendaciones de reconversión productiva fundamentadas en criterios de eficiencia hídrica y viabilidad económica, orientadas a la toma de decisiones de SAGARPA/SADER.

## **1.4 Justificación**

La justificación de este proyecto se articula en tres dimensiones complementarias. En primer lugar, la dimensión ambiental: Sonora es una entidad con un índice de estrés hídrico elevado; identificar cultivos que reduzcan la demanda de agua de riego contribuye directamente a la preservación de acuíferos sobreexplotados y a la prolongación de la vida útil de las presas. En segundo lugar, la dimensión económica: los productores agrícolas enfrentan costos crecientes por concepto de bombeo, electricidad y acceso al agua, por lo que una reconversión hacia cultivos con menor demanda hídrica implica también una reducción de costos operativos y un aumento del margen de rentabilidad. En tercer lugar, la dimensión social: apoyar a los agricultores con información técnica objetiva para la toma de decisiones sobre qué sembrar es una forma concreta de contribuir a la seguridad alimentaria y a la estabilidad del sector rural sonorense.

El proyecto se enmarca en la colaboración entre la Universidad de Sonora y la Secretaría de Agricultura y Desarrollo Rural (SAGARPA/SADER), con el propósito de ofrecer una herramienta de análisis replicable, de base científica y actualizable con datos abiertos, que sirva de soporte técnico para futuras políticas de reconversión productiva en la región.

## **1.5 Alcance y Limitaciones**

El análisis abarca los 72 municipios de Sonora con presencia en los registros del SIAP, para el periodo 2003–2024. Se trabaja con 128 cultivos configurados con parámetros técnicos derivados del FAO-56. Las principales limitaciones identificadas en el desarrollo del proyecto son:

* Heterogeneidad en las unidades de medición de producción agrícola entre distintas fuentes y periodos, lo que requirió una estandarización cuidadosa de la nomenclatura municipal para garantizar la comparabilidad.

* Ausencia de parámetros técnicos específicos en el FAO-56 para cultivos regionales no convencionales (como Agave, Jojoba, Pitahaya y Stevia), para los cuales se utilizaron valores de cultivos agronómicamente similares, lo que introduce un grado de incertidumbre en los resultados de dichas especies.

* El análisis de rentabilidad comparativa entre cultivos —que integra costos de producción, precio de mercado y análisis de demanda— se encuentra en fase de integración y no forma parte de los resultados finales de este reporte.

* Los modelos de balance hídrico no incorporan aún las restricciones legales de extracción derivadas del REPDA/REPNA, ni la variabilidad proyectada bajo escenarios de cambio climático.

# **2\. MARCO TEÓRICO**

## **2.1 Reconversión de Cultivos**

La reconversión de cultivos es un proceso planificado mediante el cual se sustituyen parcial o totalmente las especies vegetales cultivadas en una región por otras que ofrecen ventajas comparativas en términos de sostenibilidad ambiental, viabilidad económica o adaptabilidad climática. No se trata de un proceso espontáneo ni arbitrario: requiere un diagnóstico técnico riguroso que evalúe las condiciones edafoclimáticas de la zona, la disponibilidad de agua, los costos de producción, la demanda de mercado y los marcos normativos vigentes.

En el contexto de regiones con estrés hídrico severo, como las llanuras áridas y semiáridas del noroeste de México, la reconversión adquiere un carácter estratégico. La Secretaría de Agricultura y Desarrollo Rural (SADER) ha impulsado programas de reconversión orientados a sustituir cultivos de alto consumo de agua por especies con mayor eficiencia hídrica o de mayor valor económico por unidad de agua consumida. Entre los criterios considerados destacan la lámina de riego requerida por ciclo, el rendimiento por hectárea, el precio medio rural y la compatibilidad con los sistemas de riego existentes.

La presente investigación adopta un enfoque cuantitativo para la reconversión, basado en el cálculo sistemático de la huella hídrica como indicador central de eficiencia hídrica, complementado por indicadores económicos de rentabilidad. Este enfoque permite ordenar y clasificar los cultivos de acuerdo con su desempeño en ambas dimensiones, proporcionando una base objetiva para las recomendaciones de política agrícola.

## **2.2 Huella Hídrica**

El concepto de huella hídrica fue introducido por Hoekstra y Hung (2002) como un indicador del volumen total de agua dulce utilizado para producir un bien o servicio a lo largo de toda su cadena de producción. En el ámbito agrícola, la huella hídrica se descompone en tres componentes según el origen del agua consumida:

* Huella Hídrica Verde: Volumen de agua de lluvia almacenada en el suelo que es consumida por el cultivo a través de la evapotranspiración. Representa el aprovechamiento del agua meteorológica y no implica extracción de fuentes superficiales o subterráneas.

* Huella Hídrica Azul: Volumen de agua proveniente de fuentes de riego —ríos, acuíferos, canales— consumido por el cultivo. Es el componente de mayor relevancia en regiones áridas como Sonora, donde la lluvia es insuficiente para cubrir los requerimientos del cultivo y el riego es indispensable.

* Huella Hídrica Gris: Volumen de agua necesario para diluir los contaminantes generados por la actividad agrícola (fertilizantes, pesticidas) hasta niveles de calidad aceptables. Este componente no es calculado en el presente proyecto.

La huella hídrica total de un cultivo (HH) se expresa en metros cúbicos por tonelada producida (m³/ton), lo que permite comparar la eficiencia hídrica entre cultivos con independencia de su escala de producción. Esta métrica es especialmente útil para identificar qué cultivos generan mayor valor de producción por unidad de agua consumida, criterio central para las decisiones de reconversión en entornos con agua escasa.

## **2.3 Evapotranspiración y Estándar FAO-56**

El cálculo de la huella hídrica agrícola requiere estimar con precisión cuánta agua consume el cultivo a lo largo de su ciclo de desarrollo. Esta estimación se realiza a través del concepto de evapotranspiración, que integra dos procesos físicos simultáneos: la evaporación del agua desde la superficie del suelo y la transpiración de las plantas.

### **2.3.1 Evapotranspiración de Referencia (ETo)**

La evapotranspiración de referencia (ETo) cuantifica la demanda atmosférica de agua sobre una superficie hipotética de referencia: pasto con una altura uniforme de 0.12 m, bien irrigado, con resistencia de superficie de 70 s/m y albedo de 0.23. Este concepto permite separar el efecto del clima del efecto del cultivo sobre la demanda de agua.

El estándar internacional para el cálculo de ETo es la ecuación de Penman-Monteith, establecida en el manual FAO-56 (Allen et al., 1998). Esta ecuación integra el balance de energía y la transferencia de masa de vapor de agua, utilizando variables climáticas medibles:

**ETo \= \[0.408·Δ·(Rn \- G) \+ γ·(900/(T+273))·u₂·(eₛ \- eₐ)\] / \[Δ \+ γ·(1 \+ 0.34·u₂)\]**

Donde ETo es la evapotranspiración de referencia en mm/día; Rn es la radiación neta en la superficie del cultivo en MJ/m²/día; G es el flujo de calor del suelo en MJ/m²/día (asumido como cero para cálculos diarios); T es la temperatura media del aire a 2 m de altura en °C; u₂ es la velocidad del viento a 2 m en m/s; eₛ es la presión de vapor de saturación en kPa; eₐ es la presión real de vapor en kPa; Δ es la pendiente de la curva de presión de vapor en kPa/°C; y γ es la constante psicrométrica en kPa/°C.

### **2.3.2 Coeficiente de Cultivo (Kc) y Curva Fenológica**

La evapotranspiración de referencia corresponde a una superficie estándar de pasto. Para estimar la demanda hídrica real de un cultivo específico, se introduce el coeficiente de cultivo (Kc), que relaciona la demanda del cultivo con la demanda de referencia:

**ETc \= Kc · ETo**

El valor de Kc no es constante a lo largo del ciclo de desarrollo del cultivo. Varía en función de la etapa fenológica, siguiendo una curva de cuatro fases: etapa inicial (germinación y establecimiento), etapa de desarrollo (crecimiento vegetativo), etapa de mediados (máxima cobertura foliar y floración) y etapa final (maduración y senescencia). El FAO-56 proporciona valores tabulados de Kc para cada etapa y para las condiciones climáticas áridas y semiáridas prevalecientes en Sonora.

Como ejemplo ilustrativo, para el cultivo de trigo grano bajo condiciones de Sonora, los coeficientes de cultivo utilizados son: Kc inicial \= 0.30 (fase de emergencia, 31 días), Kc mediados \= 1.15 (fase de llenado de grano, 63 días) y Kc final \= 0.25 (maduración y cosecha, 31 días). El ciclo comprende del 30 de octubre al 19 de abril, correspondiente al ciclo Otoño-Invierno característico de la región.

## **2.4 Precipitación Efectiva**

No toda la precipitación que cae sobre el campo agrícola es aprovechada por el cultivo. Una fracción se pierde por escurrimiento superficial, percolación profunda o evaporación directa del suelo. La precipitación efectiva (Pef) representa únicamente la fracción que queda disponible en la zona radical del suelo y puede ser utilizada por las plantas.

El método simplificado de la FAO para estimar la precipitación efectiva, aplicado en este proyecto, establece un factor de aprovechamiento dependiente del volumen total de lluvia recibida durante el ciclo:

Si precipitación total del ciclo \< 250 mm  →  Pef \= 0.80 × Ptotal

Si precipitación total del ciclo ≥ 250 mm  →  Pef \= 0.60 × Ptotal

Este método es apropiado para condiciones de suelos de textura media y sistemas de riego por gravedad o aspersión, dominantes en los Distritos de Riego de Sonora. En el contexto semiárido del estado, la precipitación efectiva resulta generalmente inferior a los requerimientos del cultivo, lo que se traduce en una huella hídrica azul dominante.

## **2.5 Situación Agrícola e Hídrica de Sonora**

Sonora es la segunda entidad federativa de México en extensión territorial, con una superficie de 179,503 km². Su actividad agrícola se concentra en los grandes valles aluviales del sur y noroeste del estado, irrigados por los ríos Yaqui, Mayo, Fuerte, Sonora, Magdalena y Altar. Los principales Distritos de Riego (DR) operados por la CONAGUA —entre ellos el DR 041 Río Yaqui y el DR 038 Río Mayo— soportan una producción agrícola de escala nacional e internacional.

Los cultivos de mayor relevancia histórica en el estado incluyen el trigo grano, el maíz, el garbanzo, el cártamo, el sorgo y diversas hortalizas como el tomate, el pepino y el chile. Esta diversidad coexiste con una problemática hídrica estructural: la sobreexplotación de acuíferos, la reducción del almacenamiento en presas —documentada por CONAGUA a partir de 1941— y la competencia creciente entre usos agrícolas, urbanos e industriales del agua.

Los registros del Monitor de Sequía de México y el Índice de Severidad de Sequía Agrícola (ISAG) disponibles para el estado revelan que Sonora ha atravesado periodos de sequía severa y excepcional de forma recurrente, con impactos significativos sobre la superficie siniestrada de cultivos y los volúmenes de producción. Este contexto hace de la eficiencia hídrica un criterio no negociable en cualquier propuesta de planificación agrícola regional.

## **2.6 Fuentes de Datos e Instituciones**

El proyecto integra datos de múltiples fuentes oficiales e institucionales, que se describen a continuación:

| Fuente | Datos | Uso en el proyecto |
| :---- | :---- | :---- |
| NASA POWER API | Variables climáticas diarias (Rs, Tmax, Tmin, RH, u2, P) | Cálculo de ETo y precipitación efectiva |
| SIAP — SADER | Producción agrícola municipal 2003–2024 (superficie, rendimiento, PMR) | ETc, HH y análisis de rentabilidad |
| CONAGUA | Volúmenes en distritos de riego, almacenamiento de presas | Contexto hídrico regional |
| REPDA / REPNA | Concesiones de extracción superficial y de pozos | Viabilidad hídrica legal |
| SADER — Precios de Garantía | Precios subsidiados para granos básicos | Análisis de rentabilidad |
| FAO-56 | Coeficientes Kc y duraciones fenológicas para 128 cultivos | Cálculo de ETc por cultivo |
| SonoraLatLongAlt.csv | Coordenadas y altitud de los 72 municipios de Sonora | Georreferenciación de cálculos |

# **3\. METODOLOGÍA**

La metodología del proyecto se estructura en cuatro etapas secuenciales: adquisición y preparación de datos, cálculo de la evapotranspiración de referencia y del cultivo, determinación de la huella hídrica y construcción del sistema de visualización. Cada etapa fue implementada computacionalmente en Python, con módulos reutilizables y documentados que permiten la replicación del análisis para cualquier cultivo con ficha técnica disponible en el FAO-56.

## **3.1 Arquitectura del Sistema**

El sistema de análisis sigue una arquitectura de procesamiento de tres capas:

| Capa | Componentes | Salidas |
| :---- | :---- | :---- |
| Entrada | NASA POWER API, SIAP, FAO-56, SonoraLatLongAlt.csv, CONAGUA, REPDA | Datos climáticos diarios por municipio, parámetros técnicos de cultivos, estadísticas de producción |
| Procesamiento | Scripts Python: ETo (Penman-Monteith), curva Kc, Pef, ET verde/azul, UAC, HH | Huella hídrica verde y azul por municipio, ciclo y cultivo (m³/ton) |
| Salida | Dashboard interactivo, exportación tabular | Visualizaciones comparativas, tablas para toma de decisiones |

## **3.2 Adquisición y Preparación de Datos**

### **3.2.1 Datos Climáticos — NASA POWER API**

Los datos meteorológicos diarios fueron obtenidos mediante la API pública de NASA POWER (Prediction of Worldwide Energy Resources, comunidad AG, frecuencia diaria). Se desarrollaron scripts de automatización en Python para la descarga masiva de datos para los 72 municipios de Sonora, cubriendo el periodo del 1 de enero de 2003 al 31 de diciembre de 2024 (7,670 días por municipio). Las variables extraídas y sus identificadores en la API fueron:

| Variable API | Símbolo | Descripción | Unidades |
| :---- | :---- | :---- | :---- |
| ALLSKY\_SFC\_SW\_DWN | Rs | Radiación solar de onda corta incidente en superficie | MJ/m²/día |
| WS2M | u₂ | Velocidad del viento a 2 metros de altura | m/s |
| T2M\_MAX | Tmax | Temperatura máxima del aire a 2 metros | °C |
| T2M\_MIN | Tmin | Temperatura mínima del aire a 2 metros | °C |
| RH2M | HR | Humedad relativa media a 2 metros | % |
| PRECTOTCORR | P | Precipitación corregida acumulada diaria | mm/día |

### **3.2.2 Datos de Producción Agrícola — SIAP**

Las estadísticas de producción agrícola municipal fueron obtenidas del SIAP (Servicio de Información Agroalimentaria y Pesquera), correspondientes a los cierres agrícolas del estado de Sonora para el periodo 2003–2024. Las variables utilizadas en el análisis son:

* Superficie sembrada (ha): Total de hectáreas destinadas al cultivo por ciclo agrícola y municipio.

* Superficie cosechada (ha): Superficie efectivamente cosechada, equivalente a la sembrada menos la siniestrada.

* Producción total (ton): Volumen de producto cosechado en el ciclo.

* Rendimiento (ton/ha): Cociente entre producción y superficie cosechada, utilizado como denominador en el cálculo de la huella hídrica.

* Precio Medio Rural — PMR ($/ton): Precio promedio pagado al productor en campo, sin considerar costos de empaque o comercialización.

Las series temporales del SIAP presentaron inconsistencias en la nomenclatura municipal en distintos periodos, resueltas mediante rutinas de limpieza y estandarización que aseguran la trazabilidad de cada registro hacia la clave única municipal (CVE\_MUN) para su cruce con las capas de datos climáticos e hídricos.

### **3.2.3 Parámetros Técnicos de Cultivos**

Para cada uno de los 128 cultivos registrados en el SIAP con presencia histórica en Sonora se definió un archivo de configuración técnica que contiene:

* Coeficientes de cultivo (Kc): Valores para etapa inicial (Kc\_ini), etapa de mediados (Kc\_mid) y etapa final (Kc\_end), derivados de los Cuadros 11 y 12 del FAO-56, ajustados a condiciones de clima árido y semiárido.

* Duración por fase fenológica: Número de días para las etapas inicial, de desarrollo, de mediados y final, con base en bibliografía agrícola regional.

* Calendario agrícola: Fecha representativa de siembra y fecha estimada de cosecha para Sonora (ciclos Otoño-Invierno y Primavera-Verano).

* Georreferenciación: Coordenadas (latitud, longitud) y altitud de cada municipio, almacenadas en el archivo SonoraLatLongAlt.csv.

Para cultivos no contemplados explícitamente en el FAO-56 —como Agave, Jojoba, Pitahaya y Stevia— se asignaron parámetros de cultivos agronómicamente similares (suculentas, arbustos desérticos, hortalizas de hoja pequeña), indicando en los metadatos el grado de aproximación utilizado.

## **3.3 Cálculo de la Evapotranspiración de Referencia (ETo)**

La evapotranspiración de referencia fue calculada de forma diaria para cada municipio y para cada día del periodo 2003–2024 mediante la implementación Python de la ecuación FAO-56 Penman-Monteith, desarrollada por el Lic. Manuel Alberto Valenzuela Arce y adaptada por el equipo del proyecto. La función principal es eto\_fao56\_mm(), que recibe las variables climáticas diarias, la latitud, la longitud y la altitud del municipio, y devuelve un diccionario con todos los componentes intermedios del cálculo.

Las variables intermedias calculadas en cada paso diario son:

| Variable | Símbolo | Ecuación / Fuente | Unidades |
| :---- | :---- | :---- | :---- |
| Temperatura media | Tmean | (Tmax \+ Tmin) / 2 | °C |
| Presión atmosférica | P | 101.3·((293 \- 0.0065·z) / 293)^5.26 | kPa |
| Constante psicrométrica | γ | (cp·P) / (ε·λ) ≈ 0.000665·P | kPa/°C |
| Presión de vapor de saturación | eₛ | 0.6108·exp(17.27·T / (T+237.3)) | kPa |
| Presión real de vapor | eₐ | eₛ · (HR/100) | kPa |
| Pendiente curva vapor | Δ | 4098·eₛ / (T+237.3)² | kPa/°C |
| Radiación extraterrestre | Ra | FAO-56 Ecs. 21–25 (función de latitud y día juliano) | MJ/m²/día |
| Radiación onda corta neta | Rns | (1 \- 0.23)·Rs | MJ/m²/día |
| Radiación onda larga neta | Rnl | σ·T⁴·(0.34 \- 0.14·√eₐ)·(1.35·Rs/Rso \- 0.35) | MJ/m²/día |
| Radiación neta total | Rn | Rns \- Rnl | MJ/m²/día |

## **3.4 Cálculo de la Evapotranspiración del Cultivo (ETc)**

La evapotranspiración real del cultivo se obtiene al multiplicar la ETo diaria por el coeficiente de cultivo correspondiente a la etapa fenológica de ese día:

**ETc \[mm/día\] \= Kc(día) · ETo \[mm/día\]**

La curva de Kc diaria se construye mediante la función daily\_kc\_curve(), que asigna el valor de Kc constante para cada fase del ciclo (inicial, desarrollo, mediados y final) según las duraciones configuradas para cada cultivo. En la implementación actual, la transición entre fases se realiza mediante saltos directos, sin interpolación lineal entre etapas. Esta aproximación es consistente con la versión simplificada del FAO-56 para condiciones de datos limitados.

## **3.5 Cálculo de la Precipitación Efectiva (Pef)**

La precipitación efectiva diaria se estima mediante la función pef\_simple\_fao\_per\_day(), que aplica el método simplificado de la FAO descrito en la sección 2.4. El factor de aprovechamiento (f \= 0.80 o f \= 0.60) se determina con base en la precipitación total acumulada durante el ciclo completo del cultivo y se aplica de forma homogénea a cada día del ciclo:

**Pef \[mm/día\] \= f · P \[mm/día\]   donde   f \= 0.80 si Pciclo \< 250 mm, f \= 0.60 si Pciclo ≥ 250 mm**

## **3.6 Cálculo de la Huella Hídrica**

### **3.6.1 Componentes Verde y Azul**

Para cada día del ciclo agrícola se calculan los componentes diarios de la huella hídrica a partir de la ETc y la precipitación efectiva del día:

**ET\_verde \[mm/día\] \= min(ETc, Pef)**

**ET\_azul \[mm/día\] \= max(ETc \- Pef, 0\)**

El componente verde representa el agua de lluvia efectivamente consumida por el cultivo; el componente azul representa el déficit hídrico que debe cubrirse con riego. En condiciones áridas y semiáridas como las de Sonora, donde la precipitación durante los ciclos Otoño-Invierno es escasa, la ET azul domina en la gran mayoría de los municipios y cultivos analizados.

### **3.6.2 Consumo Unitario de Agua (UAC)**

El consumo unitario de agua representa el volumen total de agua consumida por hectárea durante el ciclo agrícola completo. Se obtiene sumando los valores diarios de ET y aplicando el factor de conversión de milímetros de lámina a metros cúbicos por hectárea (1 mm de lámina sobre 1 ha equivale a 10 m³):

**UAC \[m³/ha\] \= Σ(ciclo) ET \[mm/día\] × 10**

### **3.6.3 Huella Hídrica por Tonelada (HH)**

La huella hídrica se expresa en términos de volumen de agua consumido por unidad de masa producida, lo que permite comparar cultivos con independencia de su escala:

**HH \[m³/ton\] \= UAC \[m³/ha\] / Rendimiento \[ton/ha\]**

El rendimiento utilizado corresponde al reportado por el SIAP para cada municipio, cultivo y ciclo agrícola. La función calculate\_wf\_uac() centraliza este cálculo, devolviendo los valores de HH verde y azul por separado, así como los UAC correspondientes. Cuando el rendimiento reportado es cero o no disponible, el valor de HH se asigna como no definido (NaN) para evitar divisiones inválidas.

## **3.7 Dashboard de Visualización**

El entregable computacional del proyecto es un dashboard interactivo diseñado para la visualización comparativa de los resultados. El dashboard permite:

* Seleccionar un municipio o Distrito de Desarrollo Rural (DDR) y visualizar la huella hídrica de todos los cultivos registrados para esa zona.

* Comparar la HH verde y azul entre cultivos mediante gráficas de barras ordenadas por consumo hídrico.

* Filtrar por ciclo agrícola (Otoño-Invierno / Primavera-Verano) y por periodo temporal.

* Exportar la tabulación completa de resultados por municipio en formato CSV para uso externo.

El código fuente completo del sistema —incluyendo los módulos de descarga de NASA POWER, la implementación de Penman-Monteith, el cálculo de huella hídrica y el dashboard— está disponible en el repositorio público del proyecto:

*Repositorio GitHub: https://github.com/JesusF10/SeminarioIA-LCC-UNISON-2026*

# **4\. RESULTADOS**

**Sección pendiente de resultados finales**

## **4.1 Huella Hídrica del Trigo Grano (Caso Piloto)**

## **4.2 Comparativa de Huella Hídrica entre Cultivos**

## **4.3 Cultivos con Mayor Eficiencia Hídrica**

## **4.4 Análisis de Rentabilidad por Cultivo**

## **4.5 Cultivos Candidatos para Reconversión**

# **5\. DISCUSIÓN**

  **Sección a completar una vez obtenidos los resultados comparativos**

## **5.1 Interpretación de la Huella Hídrica en el Contexto de Sonora**

El dominio de la huella hídrica azul en los cultivos de Sonora refleja una realidad estructural de la agricultura en regiones áridas: la demanda hídrica de los cultivos supera con amplitud la oferta de agua meteorológica, por lo que el riego artificial no es una práctica complementaria sino la columna vertebral del sistema productivo. Este patrón, documentado de forma cuantitativa para el trigo grano, se anticipa igualmente para la mayoría de los cultivos anuales bajo ciclo Otoño-Invierno en los Distritos de Riego del sur del estado.

La comparación de la HH azul entre municipios permite identificar gradientes de eficiencia hídrica que no son evidentes a partir de los datos brutos de producción. Municipios con mayor rendimiento por hectárea presentan una huella hídrica por tonelada más baja, aun cuando su consumo absoluto de agua sea similar o mayor. Esta relación entre productividad y eficiencia hídrica es un hallazgo relevante para la formulación de incentivos orientados a la tecnificación del riego.

## **5.2 Criterios para la Reconversión**

La viabilidad de una propuesta de reconversión productiva no puede sustentarse exclusivamente en el criterio de menor consumo hídrico. Un cultivo alternativo debe satisfacer simultáneamente condiciones mínimas en al menos cuatro dimensiones: eficiencia hídrica (HH azul reducida), rentabilidad económica (margen positivo a precios de mercado), viabilidad técnica (compatibilidad con el suelo, el clima y la infraestructura de riego existente) y viabilidad comercial (existencia de compradores y mercados accesibles para el productor). La integración de estas dimensiones en un índice compuesto de reconversión es el objetivo de la Fase 4 del proyecto.

## **5.3 Limitaciones Metodológicas**

Las principales limitaciones identificadas en la metodología aplicada y sus implicaciones sobre la interpretación de resultados son:

* La asignación de parámetros Kc aproximados para cultivos no listados en el FAO-56 introduce incertidumbre en los valores de HH para especies como Agave, Jojoba y Pitahaya. Los resultados para estos cultivos deben interpretarse con cautela y validarse con mediciones experimentales de campo cuando estén disponibles.

* El método simplificado de precipitación efectiva de la FAO supone suelos de textura media y no distingue entre tipos de riego. En zonas con riego tecnificado por goteo o microaspersión, la eficiencia de aplicación es mayor y la HH azul real puede ser inferior a la estimada por el modelo.

* El rendimiento utilizado en el cálculo corresponde al promedio histórico reportado por el SIAP, que puede incluir años con superficie siniestrada o condiciones climatológicas atípicas. Los valores de HH calculados reflejan el desempeño promedio histórico, no necesariamente el potencial productivo del cultivo bajo condiciones óptimas de manejo.

# **6\. CONCLUSIONES Y RECOMENDACIONES**

  **Las conclusiones específicas y recomendaciones finales se elaborarán una vez que los resultados comparativos de todos los cultivos estén disponiblesPENDIENTE**

## **6.1 Conclusiones**

La metodología computacional desarrollada en este proyecto constituye una contribución técnica concreta al problema de la gestión hídrica agrícola en Sonora. La implementación modular de la ecuación Penman-Monteith FAO-56 en Python, integrada con datos satelitales de NASA POWER y estadísticas de producción del SIAP, permite cuantificar de forma sistemática y reproducible la huella hídrica de 128 cultivos en los 72 municipios del estado para un periodo de dos décadas.

El análisis piloto del trigo grano confirma la hipótesis de trabajo: en las condiciones áridas de Sonora, la huella hídrica azul —agua de riego— domina la demanda hídrica de los cultivos de ciclo Otoño-Invierno, representando más del 90% de la huella total en los principales municipios productores. Este resultado establece una línea base cuantitativa contra la cual comparar cultivos alternativos en términos de eficiencia en el uso del agua.

\[Completar con las conclusiones derivadas de los resultados comparativos entre cultivos y el análisis de rentabilidad.\]

## **6.2 Recomendaciones para SAGARPA / SADER**

Con base en el marco metodológico establecido y los resultados preliminares, se plantean las siguientes líneas de recomendación para los tomadores de decisiones de política agrícola:

* Adoptar la huella hídrica por tonelada (HH azul) como indicador complementario oficial en los instrumentos de planeación de los Distritos de Riego de Sonora, junto con los indicadores tradicionales de rendimiento y precio.

* Priorizar incentivos de tecnificación del riego y cambio de cultivo en los municipios donde la HH azul supere el umbral estatal promedio, especialmente en zonas con acuíferos en condición de sobreexplotación según el REPDA.

* Diseñar programas piloto de reconversión productiva en uno o dos Distritos de Desarrollo Rural, orientados a los cultivos identificados con mayor eficiencia hídrica y rentabilidad comparable al trigo, con el apoyo de los Precios de Garantía como mecanismo de estabilización de ingresos durante la transición.

* Establecer un mecanismo de actualización anual de la base de datos de huella hídrica, integrando automáticamente los datos del SIAP y de NASA POWER conforme estén disponibles, con el repositorio GitHub del proyecto como plataforma de mantenimiento.

## **6.3 Trabajo Futuro**

* Incorporar el componente gris de la huella hídrica (contaminación por agroquímicos) para ampliar el análisis de impacto ambiental.

* Integrar las restricciones legales de extracción derivadas del REPDA/REPNA como capa adicional en el modelo de viabilidad hídrica por municipio.

* Desarrollar escenarios proyectados de huella hídrica bajo distintos modelos de cambio climático para el horizonte 2030–2050.

* Validar los resultados del modelo con datos experimentales de campo y estudios agronómicos publicados para las condiciones específicas de Sonora.

* Extender el análisis de rentabilidad para incorporar la dinámica de mercado (sustitución de importaciones, demanda de centrales de abasto, cultivos forrajeros) documentada en la Fase 2 del proyecto.

# **REFERENCIAS**

Allen, R. G., Pereira, L. S., Raes, D., y Smith, M. (1998). Crop evapotranspiration — Guidelines for computing crop water requirements. FAO Irrigation and Drainage Paper No. 56\. Food and Agriculture Organization of the United Nations, Rome. ISBN 92-5-304219-2.

Allen, R. G., Pereira, L. S., Raes, D., y Smith, M. (2006). Evapotranspiración del cultivo: Guía para la determinación de los requerimientos de agua de los cultivos. Estudio FAO Riego y Drenaje No. 56\. FAO, Roma.

Hoekstra, A. Y., y Hung, P. Q. (2002). Virtual water trade: A quantification of virtual water flows between nations in relation to international crop trade. Value of Water Research Report Series No. 11\. IHE Delft, Netherlands.

Hoekstra, A. Y., Chapagain, A. K., Aldaya, M. M., y Mekonnen, M. M. (2011). The Water Footprint Assessment Manual: Setting the Global Standard. Earthscan, London and Washington, DC.

NASA POWER Project. (2024). Prediction of Worldwide Energy Resources (POWER) — Agroclimatology Community Data Access API. National Aeronautics and Space Administration. Recuperado de https://power.larc.nasa.gov

SIAP — Servicio de Información Agroalimentaria y Pesquera. (2024). Cierre de la Producción Agrícola: Base de datos municipal 2003–2024. Secretaría de Agricultura y Desarrollo Rural (SADER). Recuperado de https://www.gob.mx/siap

CONAGUA — Comisión Nacional del Agua. (2024). Estadística agrícola de los Distritos de Riego. Subdirección General de Infraestructura Hidroagrícola. Gobierno de México.

SADER — Secretaría de Agricultura y Desarrollo Rural. (2024). Precios de Garantía a productos alimentarios básicos. Gobierno de México. Recuperado de https://www.gob.mx/sader

CONAGUA — Comisión Nacional del Agua. (2024). Registro Público de Derechos de Agua (REPDA) / Registro Público de Derechos Nacionales del Agua (REPNA). Gobierno de México.

# **ANEXOS**

## **Anexo A — Derivaciones Matemáticas Detalladas (FAO-56)**

El presente anexo documenta las ecuaciones auxiliares que sustentan el cálculo de la evapotranspiración de referencia. Todas las funciones fueron implementadas en Python y validadas contra los ejemplos numéricos del manual FAO-56.

### **A.1 Constantes Físicas y Atmosféricas**

**Presión Atmosférica (P):**

**P \[kPa\] \= 101.3 · ((293 \- 0.0065·z) / 293)^5.26**

def atm\_pressure\_kpa(z\_m: float) \-\> float:

    return 101.3 \* ((293.0 \- 0.0065 \* z\_m) / 293.0) \*\* 5.26

**Constante Psicrométrica (γ):**

**γ \[kPa/°C\] \= (cp · P) / (ε · λ) ≈ 0.000665 · P     \[cp=1.013×10⁻³ MJ/kg/°C, ε=0.622, λ=2.45 MJ/kg\]**

def psychrometric\_constant\_kpa\_per\_c(p\_kpa: float) \-\> float:

    return (1.013e-3 \* p\_kpa) / (0.622 \* 2.45)

**Presión de Vapor de Saturación (eₛ) y Real (eₐ):**

**eₛ \[kPa\] \= \[e°(Tmax) \+ e°(Tmin)\] / 2    donde   e°(T) \= 0.6108 · exp(17.27·T / (T+237.3))**

**eₐ \[kPa\] \= eₛ · (HR / 100\)**

def es\_kpa(t\_c: float) \-\> float:

    return 0.6108 \* math.exp((17.27 \* t\_c) / (t\_c \+ 237.3))

**Pendiente de la Curva de Presión de Vapor (Δ):**

**Δ \[kPa/°C\] \= 4098 · eₛ(Tmean) / (Tmean \+ 237.3)²**

def delta\_kpa\_per\_c(t\_c: float) \-\> float:

    return 4098.0 \* es\_kpa(t\_c) / ((t\_c \+ 237.3) \*\* 2\)

### **A.2 Balance de Radiación (Rn)**

**Radiación Extraterrestre (Ra):**

**Ra \= (24·60/π) · Gsc · dr · \[ωs·sin(φ)·sin(δ) \+ cos(φ)·cos(δ)·sin(ωs)\]**

**Donde:** Gsc \= 0.0820 MJ/m²/min (constante solar);  dr \= 1 \+ 0.033·cos(2π·J/365) (distancia relativa inversa);  δ \= 0.409·sin(2π·J/365 \- 1.39) (declinación solar);  ωs \= arccos(-tan(φ)·tan(δ)) (ángulo de puesta de sol);  J \= día juliano.

def extraterrestrial\_radiation\_mj\_m2d(lat\_deg, doy):

    phi \= math.radians(lat\_deg)

    dr \= 1.0 \+ 0.033 \* math.cos(2.0 \* math.pi / 365.0 \* doy)

    delta \= 0.409 \* math.sin(2.0 \* math.pi / 365.0 \* doy \- 1.39)

    ws \= math.acos(-math.tan(phi) \* math.tan(delta))

    return (24.0\*60.0/math.pi) \* GSC \* dr \* (

        ws\*math.sin(phi)\*math.sin(delta) \+ math.cos(phi)\*math.cos(delta)\*math.sin(ws))

**Radiación Neta de Onda Corta (Rns):**

**Rns \[MJ/m²/día\] \= (1 \- α) · Rs     con α \= 0.23 (albedo cultivo de referencia)**

**Radiación Neta de Onda Larga (Rnl):**

**Rnl \= σ · \[(Tmax,K⁴ \+ Tmin,K⁴)/2\] · (0.34 \- 0.14·√eₐ) · (1.35·Rs/Rso \- 0.35)**

**Donde:** σ \= 4.903×10⁻⁹ MJ/K⁴/m²/día (constante de Stefan-Boltzmann);  T,K \= temperatura en Kelvin;  Rso \= (0.75 \+ 2×10⁻⁵·z)·Ra (radiación en cielo despejado).

def net\_longwave\_rnl\_fao56(tmax\_c, tmin\_c, ea\_kpa, rs\_mjm2d, rso\_mjm2d):

    tmaxk, tmink \= tmax\_c \+ 273.16, tmin\_c \+ 273.16

    t4 \= (tmaxk\*\*4 \+ tmink\*\*4) / 2.0

    rsrso \= max(0.0, min(rs\_mjm2d / rso\_mjm2d, 1.0)) if rso\_mjm2d \> 0 else 0.0

    fcloud \= 1.35 \* rsrso \- 0.35

    return SIGMA \* t4 \* (0.34 \- 0.14 \* math.sqrt(max(ea\_kpa, 0.0))) \* fcloud

**Radiación Neta Total (Rn):**

**Rn \[MJ/m²/día\] \= Rns \- Rnl**

### **A.3 Función Principal ETo**

def eto\_fao56\_mm(tmax, tmin, rh\_pct, u2\_ms, rs\_mjm2d, lat\_deg, z\_m, doy, g\_mjm2d=0.0):

    tmean \= (tmax \+ tmin) / 2.0

    es \= (es\_kpa(tmax) \+ es\_kpa(tmin)) / 2.0

    ea \= es \* (rh\_pct / 100.0)

    delta \= delta\_kpa\_per\_c(tmean)

    p \= atm\_pressure\_kpa(z\_m)

    gamma \= psychrometric\_constant\_kpa\_per\_c(p)

    rso \= extraterrestrial\_radiation\_mj\_m2d(lat\_deg, doy)  \# Ra (versión equipo)

    rns \= net\_shortwave\_rns(rs\_mjm2d=rs\_mjm2d, albedo=ALBEDO)

    rnl \= net\_longwave\_rnl\_fao56(tmax, tmin, ea, rs\_mjm2d, rso)

    rn  \= rns \- rnl

    num \= 0.408\*delta\*(rn \- g\_mjm2d) \+ gamma\*(900.0/(tmean+273.0))\*u2\_ms\*(es \- ea)

    den \= delta \+ gamma\*(1.0 \+ 0.34\*u2\_ms)

    return max(0.0, num / den)  \# ETo \[mm/día\]

### **A.4 Función Principal de Huella Hídrica**

def calculate\_wf\_uac(green\_et\_mm, blue\_et\_mm, performance\_ton\_ha):

    et\_verde \= float(pd.Series(green\_et\_mm).fillna(0).sum())

    et\_azul  \= float(pd.Series(blue\_et\_mm).fillna(0).sum())

    uac\_verde \= et\_verde \* 10.0  \# mm → m³/ha

    uac\_azul  \= et\_azul  \* 10.0

    if performance\_ton\_ha and performance\_ton\_ha \> 0:

        hh\_verde \= uac\_verde / performance\_ton\_ha  \# m³/ton

        hh\_azul  \= uac\_azul  / performance\_ton\_ha

    else:

        hh\_verde \= hh\_azul \= float('nan')

    return {'UACverde\_m3\_ha': uac\_verde, 'UACazul\_m3\_ha': uac\_azul,

            'HHverde\_m3\_ton': hh\_verde,  'HHazul\_m3\_ton': hh\_azul}

## **Anexo B — Inventario de Fuentes de Datos**

El siguiente inventario resume las fuentes de datos integradas en el proyecto, organizadas por dimensión de análisis conforme al modelo de tres capas descrito en la metodología.

| Dimensión | Fuente | Archivo / Sistema | Variables clave |
| :---- | :---- | :---- | :---- |
| Territorial | UNISON | SonoraLatLongAlt.csv | Latitud, longitud, altitud por municipio |
| Productiva | SIAP | Cierres agrícolas municipales 2003–2024 | Sembrada, cosechada, producción, rendimiento, PMR |
| Hídrica (clima) | NASA POWER | API AG diaria, 2003–2024 | Rs, Tmax, Tmin, RH, u2, P por municipio |
| Hídrica (concesiones) | CONAGUA / REPDA | reporte-repna-1.csv, reporte-repna-2.csv | Volúmenes concesionados de extracción |
| Infraestructura | SAGARPA | tecnificacion-riego-DDR\_2021.xlsx | Grado de tecnificación por DDR |
| Económica | SIAP / SADER | PMR histórico, Precios de Garantía | Precio por tonelada, subsidios por cultivo |
| Técnica cultivos | FAO-56 / INIFAP | manual-tecnico-cultivos-sonora-2024.csv | Kc, láminas, costos, rendimientos por cultivo |
| Riesgo climático | SMN / CONAGUA | Shapefiles ISAG por municipio | Índice de Severidad de Sequía Agrícola |

## **Anexo C — Glosario de Términos**

Se incluye a continuación un glosario de los términos técnicos utilizados en el reporte:

| Término | Definición |
| :---- | :---- |
| ETo — Evapotranspiración de Referencia | Tasa de evapotranspiración estimada para una superficie hipotética de pasto bien irrigado. Expresa la demanda atmosférica de agua \[mm/día\]. |
| ETc — Evapotranspiración del Cultivo | Evapotranspiración real del cultivo, obtenida como ETc \= Kc × ETo. Representa el consumo hídrico diario del cultivo específico \[mm/día\]. |
| Kc — Coeficiente de Cultivo | Factor adimensional que relaciona la demanda hídrica de un cultivo con la demanda de referencia (ETo). Varía según la etapa fenológica. |
| Pef — Precipitación Efectiva | Fracción de la precipitación total que queda disponible en la zona radical del suelo para el cultivo, descontando escurrimiento y percolación. |
| HH Verde | Componente de la huella hídrica correspondiente al agua de lluvia consumida por evapotranspiración \[m³/ton\]. |
| HH Azul | Componente de la huella hídrica correspondiente al agua de riego consumida por evapotranspiración \[m³/ton\]. |
| UAC — Consumo Unitario de Agua | Volumen total de agua consumida por hectárea durante el ciclo agrícola completo \[m³/ha\]. |
| PMR — Precio Medio Rural | Precio promedio pagado al productor en campo, sin considerar costos de empaque o transporte \[$/ton\]. Fuente: SIAP. |
| DDR — Distrito de Desarrollo Rural | Unidad de organización territorial de la SADER para la prestación de servicios de fomento agropecuario en México. |
| SIAP | Servicio de Información Agroalimentaria y Pesquera de la SADER. Principal fuente de estadísticas de producción agrícola en México. |
| REPDA / REPNA | Registro Público de Derechos de Agua / Registro Público de Derechos Nacionales del Agua. Administrado por CONAGUA. Contiene las concesiones vigentes de extracción de agua. |
| ISAG | Índice de Severidad de Sequía Agrícola. Indicador que cuantifica el grado de afectación por sequía en la producción agrícola municipal. |
| FAO-56 | Manual de la FAO: 'Crop evapotranspiration — Guidelines for computing crop water requirements', publicación de referencia mundial para el cálculo de demanda hídrica agrícola. |
| NASA POWER | Plataforma de datos climáticos satelitales de la NASA que proporciona variables meteorológicas diarias para cualquier punto geográfico del planeta. |

## **Anexo D — Repositorio del Proyecto**

El código fuente completo del proyecto, incluyendo los módulos de descarga de datos climáticos, la implementación de la ecuación Penman-Monteith FAO-56, el sistema de cálculo de huella hídrica y el dashboard de visualización, está disponible en el repositorio público de GitHub:

*https://github.com/JesusF10/SeminarioIA-LCC-UNISON-2026*

El repositorio incluye documentación técnica, archivos de configuración por municipio y cultivo, y las instrucciones de instalación y ejecución del sistema.