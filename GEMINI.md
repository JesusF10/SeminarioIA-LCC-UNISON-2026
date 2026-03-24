# Contexto del Proyecto: Seminario IA - Reconversión Productiva (LCC UNISON 2026)

Este proyecto es un esfuerzo de equipo de Ciencias de la Computación enfocado en 
el aprendizaje del dominio agrícola, la recopilación de datos y el análisis 
sistémico de los recursos hídricos en Sonora para proponer la reconversión de 
**múltiples cultivos**.

## Objetivos Generales
1.  **Exploración y Diagnóstico (Fase 1):** Inmersión en el contexto agrícola, 
    aprendizaje técnico y recopilación masiva de datos oficiales.
2.  **Análisis de Mercado y Rentabilidad (Fase 2):** Evaluación económica.
3.  **Análisis Técnico y Viabilidad (Fase 3):** Correlación hídrica y climática.
4.  **Recomendación (Fase 4):** Propuesta sistémica de alternativas.

## Estándares del Proyecto
- **Entorno:** Se utiliza `uv` para gestión de dependencias.
- **Formato de Escritura:** Máximo de **80 caracteres** por línea en Markdown y 
  Typst para facilitar la legibilidad.
- **Jerarquía Territorial:** El análisis se fundamenta en tres niveles:
    1. **Municipio:** Unidad base de integración de datos (`CVE_MUN`).
    2. **DDR (Distrito de Desarrollo Rural):** Nivel de agregación administrativa 
       y estadística (SADER).
    3. **DR (Distrito de Riego):** Delimitación por infraestructura hidráulica 
       (CONAGUA).
- **Estrategia de Análisis:** La prioridad técnica es el **Municipio**, usando 
  el **DDR** como eje de agrupación administrativa.

## Inventario de Datos (Contexto Operativo)
- **SIAP:** Series municipales (2003-2024) y nacionales (1980-2002).
- **Hídricos:** Almacenamiento de presas y títulos de concesión (REPNA).
- **Cultivos Actuales:** Datos sobre variedades, tecnología y ciclos.
- **Sequía:** Capas geospaciales de impacto por municipio.

## Reglas para Gemini CLI
1.  **Distinción DDR vs DR:** No confundir Distritos de Desarrollo Rural 
    (administrativos) con Distritos de Riego (hidráulicos).
2.  **Unidad Maestra:** Priorizar el cruce de datos mediante la clave municipal.
3.  **Estado de Fase 1:** Enfoque en recopilación e inventario, sin filtros aún.
4.  **Enfoque Sistémico:** Análisis multicultivo para Sonora.
5.  **Seguridad:** No cargar archivos >100MB sin filtrar.
