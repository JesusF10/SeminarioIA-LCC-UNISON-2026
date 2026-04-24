"""
Ejemplo de uso del filtro de cultivos en get_prod_data.

Este script demuestra las diferentes formas de filtrar datos de producción
agrícola por cultivo específico, y cómo combinar este filtro con otros
parámetros para análisis detallados.

Autor: Equipo Seminario IA
Fecha: 2024
Proyecto: Reconversión Productiva - LCC UNISON 2026
"""

from seminario_ia.datasets import get_prod_data

import pandas as pd

# Configuración de pandas para mejor visualización
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 100)
pd.set_option("display.precision", 2)


def separador(titulo):
    """Imprime un separador visual con título."""
    print("\n" + "=" * 80)
    print(titulo.center(80))
    print("=" * 80 + "\n")


def ejemplo_1_filtro_basico():
    """Ejemplo 1: Filtrado básico por cultivo."""
    separador("EJEMPLO 1: Filtrado Básico por Cultivo")

    # Cargar datos de trigo para 2020
    df = get_prod_data(years=2020, crop_name="Trigo grano", muni=True)

    print("Datos de producción de Trigo grano en Sonora (2020)\n")
    print(f"Total de registros: {len(df)}")
    print(f"Municipios productores: {df['Nommunicipio'].nunique()}")
    print(f"Producción total: {df['Volumenproduccion'].sum():,.2f} toneladas")
    print(f"Superficie cosechada: {df['Cosechada'].sum():,.2f} hectáreas")
    print(f"Valor de producción: ${df['Valorproduccion'].sum():,.2f} miles\n")

    # Mostrar top 5 municipios productores
    top_5 = (
        df.groupby("Nommunicipio")["Volumenproduccion"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    print("Top 5 municipios productores de trigo:")
    for i, (municipio, produccion) in enumerate(top_5.items(), 1):
        print(f"  {i}. {municipio:20s} {produccion:>12,.2f} ton")


def ejemplo_2_filtro_por_codigo():
    """Ejemplo 2: Filtrado usando código de cultivo."""
    separador("EJEMPLO 2: Filtrado por Código de Cultivo")

    # Usar código numérico del cultivo
    df = get_prod_data(years=2020, crop_name=9050000, muni=True)

    print("Usando código de cultivo: 9050000 (Trigo grano)\n")
    print(f"Registros encontrados: {len(df)}")
    print(f"Cultivo: {df['Nomcultivo'].iloc[0] if len(df) > 0 else 'N/A'}")
    print(f"Código verificado: {df['Idcultivo'].iloc[0] if len(df) > 0 else 'N/A'}")


def ejemplo_3_combinacion_filtros():
    """Ejemplo 3: Combinar filtros de cultivo y municipio."""
    separador("EJEMPLO 3: Filtro de Cultivo + Municipio")

    # Analizar trigo en Hermosillo para múltiples años
    df = get_prod_data(
        years=(2018, 2023),
        loc_name="Hermosillo",
        crop_name="Trigo grano",
        muni=True,
    )

    print("Producción de Trigo en Hermosillo (2018-2023)\n")

    if len(df) > 0:
        evolucion = df.groupby("Anio").agg(
            {
                "Volumenproduccion": "sum",
                "Cosechada": "sum",
                "Valorproduccion": "sum",
            }
        )

        evolucion.columns = ["Producción (ton)", "Cosechada (ha)", "Valor (miles)"]
        print(evolucion)
        print(f"\nPromedio anual: {evolucion['Producción (ton)'].mean():,.2f} ton")
    else:
        print("No hay datos disponibles para esta combinación")


def ejemplo_4_comparacion_cultivos():
    """Ejemplo 4: Comparación entre diferentes cultivos."""
    separador("EJEMPLO 4: Comparación entre Cultivos")

    cultivos = {
        "Trigo grano": 9050000,
        "Maíz grano": 7490000,
        "Espárrago": 6650000,
    }

    print("Comparación de cultivos en Sonora (2020-2023)\n")
    print(f"{'Cultivo':<20} {'Producción (ton)':>20} {'Valor (millones $)':>20}")
    print("-" * 62)

    for nombre, codigo in cultivos.items():
        df = get_prod_data(years=(2020, 2023), crop_name=codigo, muni=True)

        if len(df) > 0:
            produccion = df["Volumenproduccion"].sum()
            valor = df["Valorproduccion"].sum() / 1000  # Convertir a millones
            print(f"{nombre:<20} {produccion:>20,.2f} {valor:>20,.2f}")
        else:
            print(f"{nombre:<20} {'Sin datos':>20} {'Sin datos':>20}")


def ejemplo_5_analisis_temporal():
    """Ejemplo 5: Análisis temporal de un cultivo."""
    separador("EJEMPLO 5: Análisis Temporal de Cultivo")

    # Cargar datos de uva para últimos 6 años
    df = get_prod_data(years=(2018, 2023), crop_name="Uva", muni=True)

    print("Evolución de la producción de Uva en Sonora (2018-2023)\n")

    if len(df) > 0:
        # Análisis por año
        anual = df.groupby("Anio").agg(
            {
                "Nommunicipio": "nunique",
                "Volumenproduccion": "sum",
                "Cosechada": "sum",
                "Valorproduccion": "sum",
            }
        )

        anual.columns = ["Municipios", "Prod. (ton)", "Sup. (ha)", "Valor (miles)"]
        print(anual)

        # Calcular tendencia
        prod_inicial = anual["Prod. (ton)"].iloc[0]
        prod_final = anual["Prod. (ton)"].iloc[-1]
        cambio = ((prod_final - prod_inicial) / prod_inicial) * 100

        print(f"\nCambio en producción 2018-2023: {cambio:+.2f}%")

        # Identificar municipios principales
        top_mun = (
            df.groupby("Nommunicipio")["Volumenproduccion"]
            .sum()
            .sort_values(ascending=False)
            .head(3)
        )

        print("\nPrincipales municipios productores:")
        for mun, prod in top_mun.items():
            print(f"  - {mun}: {prod:,.2f} ton")


def ejemplo_6_multiples_cultivos():
    """Ejemplo 6: Análisis de múltiples cultivos en un municipio."""
    separador("EJEMPLO 6: Análisis Multi-Cultivo por Municipio")

    municipio = "Caborca"
    cultivos_analizar = ["Uva", "Espárrago", "Papa", "Melón"]

    print(f"Análisis de cultivos principales en {municipio} (2020-2022)\n")
    print(f"{'Cultivo':<20} {'Producción (ton)':>20} {'Valor (miles $)':>20}")
    print("-" * 62)

    resultados = []

    for cultivo in cultivos_analizar:
        df = get_prod_data(
            years=(2020, 2022), loc_name=municipio, crop_name=cultivo, muni=True
        )

        if len(df) > 0:
            produccion = df["Volumenproduccion"].sum()
            valor = df["Valorproduccion"].sum()
            resultados.append((cultivo, produccion, valor))
            print(f"{cultivo:<20} {produccion:>20,.2f} {valor:>20,.2f}")

    if resultados:
        # Ordenar por valor económico
        resultados.sort(key=lambda x: x[2], reverse=True)
        mejor_cultivo = resultados[0]
        print(f"\nCultivo más valioso: {mejor_cultivo[0]}")
        print(f"Valor total: ${mejor_cultivo[2]:,.2f} miles de pesos")


def ejemplo_7_datos_nacionales():
    """Ejemplo 7: Análisis de cultivo en datos nacionales."""
    separador("EJEMPLO 7: Datos Nacionales por Cultivo")

    # Analizar trigo a nivel nacional (datos históricos)
    df = get_prod_data(years=(1990, 1995), crop_name="Trigo grano", muni=False)

    print("Producción de Trigo en México (1990-1995)\n")

    if len(df) > 0:
        # Top 5 estados productores
        top_estados = (
            df.groupby("Nomestado")["Volumenproduccion"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        print("Top 5 estados productores de trigo (1990-1995):")
        for i, (estado, produccion) in enumerate(top_estados.items(), 1):
            print(f"  {i}. {estado:20s} {produccion:>15,.2f} ton")

        # Participación de Sonora
        sonora = df[df["Nomestado"] == "Sonora"]
        if len(sonora) > 0:
            prod_sonora = sonora["Volumenproduccion"].sum()
            prod_total = df["Volumenproduccion"].sum()
            participacion = (prod_sonora / prod_total) * 100
            print(f"\nParticipación de Sonora: {participacion:.2f}%")


def ejemplo_8_reconversion_productiva():
    """Ejemplo 8: Caso de uso - Análisis de reconversión productiva."""
    separador("EJEMPLO 8: Caso de Uso - Reconversión Productiva")

    municipio = "Hermosillo"
    cultivo_actual = "Alfalfa achicalada"
    cultivos_alternativos = ["Trigo grano", "Maíz grano", "Papa"]

    print(f"Análisis de reconversión productiva en {municipio} (2020-2023)\n")
    print(f"Cultivo actual: {cultivo_actual}\n")

    # Analizar cultivo actual
    df_actual = get_prod_data(
        years=(2020, 2023),
        loc_name=municipio,
        crop_name=cultivo_actual,
        muni=True,
    )

    if len(df_actual) > 0:
        valor_actual = df_actual["Valorproduccion"].mean()
        print(f"Valor promedio anual actual: ${valor_actual:,.2f} miles\n")
    else:
        valor_actual = 0
        print("No hay datos del cultivo actual\n")

    print("Alternativas evaluadas:")
    print(f"{'Cultivo':<20} {'Valor Prom. (miles)':>20} {'vs Actual':>15}")
    print("-" * 57)

    for cultivo_alt in cultivos_alternativos:
        df_alt = get_prod_data(
            years=(2020, 2023),
            loc_name=municipio,
            crop_name=cultivo_alt,
            muni=True,
        )

        if len(df_alt) > 0:
            valor_alt = df_alt["Valorproduccion"].mean()
            diferencia = (
                ((valor_alt - valor_actual) / valor_actual * 100)
                if valor_actual > 0
                else 0
            )
            print(f"{cultivo_alt:<20} ${valor_alt:>19,.2f} {diferencia:>+14.2f}%")
        else:
            print(f"{cultivo_alt:<20} {'Sin datos':>20} {'-':>15}")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("\n" + "=" * 80)
    print("EJEMPLOS DE FILTRADO POR CULTIVO - get_prod_data".center(80))
    print("Seminario IA - Reconversión Productiva LCC UNISON 2026".center(80))
    print("=" * 80)

    ejemplos = [
        ejemplo_1_filtro_basico,
        ejemplo_2_filtro_por_codigo,
        ejemplo_3_combinacion_filtros,
        ejemplo_4_comparacion_cultivos,
        ejemplo_5_analisis_temporal,
        ejemplo_6_multiples_cultivos,
        ejemplo_7_datos_nacionales,
        ejemplo_8_reconversion_productiva,
    ]

    for ejemplo in ejemplos:
        ejemplo()
        input("\nPresiona Enter para continuar...\n")

    separador("EJEMPLOS COMPLETADOS")
    print("Todos los ejemplos se ejecutaron exitosamente.\n")


if __name__ == "__main__":
    main()
