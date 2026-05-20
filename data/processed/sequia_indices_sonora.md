# Diccionario de datos — `sequia_indices_sonora.csv`

Archivo de referencia con índices de vulnerabilidad a la sequía agrícola para los 72 municipios de Sonora.
Valores **atemporales** (estructurales, no varían por año).

Fuente: shapefile `data/raw/datos-sequia/impacto_sequia.shp` (CONAGUA / INIFAP).

---

## Identificación

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `CVE_MUN` | int | Clave del municipio (≡ `IdMunicipio` en SIAP) |
| `Municipio` | str | Nombre del municipio |

---

## Componentes — Primavera-Verano (PV)

Factores que componen la vulnerabilidad para el ciclo agrícola primavera-verano.

| Variable | Rango | Descripción |
|----------|-------|-------------|
| `REC_PV` | 16–41 | **Recarga** de acuífero (mm/año estimado). Mayor valor = mayor disponibilidad de agua subterránea. |
| `CON_PV` | 5–35 | **Condición** del suelo y vegetación. Índice compuesto; mayor = mejor condición agronómica. |
| `SP_PV` | 4–6 | **Susceptibilidad potencial** a sequía. Categoría (4=menor, 6=mayor riesgo inherente). |
| `EXP_PV` | 2–3 | **Exposición** del cultivo. Grado en que el cultivo está expuesto a déficit hídrico (2=menor, 3=mayor). |

---

## Componentes — Otoño-Invierno (OI)

Factores para el ciclo otoño-invierno.

| Variable | Rango | Descripción |
|----------|-------|-------------|
| `REC_OI` | 8–29 | **Recarga** de acuífero (mm/año) para OI. |
| `CON_OI` | 0–30 | **Condición** del suelo y vegetación para OI. |
| `SP_OI` | 3–6 | **Susceptibilidad potencial** para OI. |
| `EXP_OI` | 2–3 | **Exposición** para OI. |

---

## Componentes — Generales (aplican a ambos ciclos)

| Variable | Rango | Descripción |
|----------|-------|-------------|
| `PER_CA` | 20–100 | **Pérdida de capa arable** (% de degradación). 100 = pérdida total de suelo fértil. |
| `TEMP_CA` | 0–100 | **Temperatura de capa arable**. Índice de estrés térmico del suelo (mayor = más estrés). |
| `EROS` | 0–100 | **Riesgo de erosión**. Índice (mayor = mayor riesgo de pérdida de suelo por erosión). |

---

## Scores compuestos

Resultado de la ponderación de los componentes anteriores.

| Variable | Rango | Descripción |
|----------|-------|-------------|
| `SPT_PV` | 6–12 | **Susceptibilidad Ponderada Total** para PV. Score compuesto de REC + CON + SP + EXP + PER_CA + TEMP_CA + EROS. Mayor = mayor vulnerabilidad. |
| `SPT_OI` | 6–12 | **Susceptibilidad Ponderada Total** para OI. Misma composición para ciclo OI. |

---

## Índice de Sequía Agrícola (ISAG)

Categorización del SPT en 3 niveles.

| Variable | Valores | Descripción |
|----------|---------|-------------|
| `ISAG_PV` | 1, 2, 3 | **Índice de Sequía Agrícola** para PV. |
| `ISAG_OI` | 1, 2, 3 | **Índice de Sequía Agrícola** para OI. |
| `ISAG_PV_label` | Alta, Media, Baja | Etiqueta descriptiva para ISAG_PV. |
| `ISAG_OI_label` | Alta, Media, Baja | Etiqueta descriptiva para ISAG_OI. |

### Correspondencia SPT → ISAG

| SPT | ISAG | Etiqueta |
|-----|------|----------|
| 6–8 | 1 | **Alta** vulnerabilidad |
| 9 | 2 | **Media** vulnerabilidad |
| 10–12 | 3 | **Baja** vulnerabilidad |

---

## Unión con el CSV maestro

```python
sequia = pd.read_csv("data/processed/sequia_indices_sonora.csv")
master = pd.read_csv("data/processed/analisis_municipal_sonora_2010_2024.csv")

# Unir por clave de municipio
merged = master.merge(sequia, left_on="IdMunicipio", right_on="CVE_MUN")
```
