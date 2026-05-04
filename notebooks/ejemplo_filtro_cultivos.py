"""
Ejemplo de uso del filtro de cultivos en get_prod_data.

Este script demuestra las diferentes formas de filtrar datos de producción
agrícola por cultivo específico, y cómo combinar este filtro con otros
parámetros para análisis detallados.

Autor: Jesús Flores Lacarra
Fecha: 2024
Proyecto: Reconversión de cultivos en Sonora
"""

from seminario_ia.datasets import get_crop_data, get_mun_coordinates, get_prod_data
from seminario_ia.models import Crop, Region

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

    df = get_prod_data(years=2020, crop_name="Trigo grano")

    print("Datos de producción de Trigo grano en Sonora (2020)\n")
    print(f"Total de registros: {len(df)}")
    print(f"Municipios productores: {df['Nommunicipio'].nunique()}")
    print(f"Producción total: {df['Volumenproduccion'].sum():,.2f} toneladas")
    print(f"Superficie cosechada: {df['Cosechada'].sum():,.2f} hectáreas")
    print(f"Valor de producción: ${df['Valorproduccion'].sum():,.2f} miles\n")

    top_5 = (
        df.groupby("Nommunicipio")["Volumenproduccion"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    print("Top 5 municipios productores de trigo:")
    for i, (municipio, produccion) in enumerate(top_5.items(), 1):
        print(f"  {i}. {municipio:20s} {produccion:>12,.2f} ton")


def ejemplo_2_filtro_con_modelo_crop():
    """Ejemplo 2: Filtrado usando objeto Crop."""
    separador("EJEMPLO 2: Filtrado con Objeto Crop")

    trigo = get_crop_data("Trigo grano")

    df = get_prod_data(years=2020, crop_name=trigo)

    print(f"Usando objeto Crop: {trigo.name}\n")
    print(f"Registros encontrados: {len(df)}")
    print(f"Cultivo: {df['Nomcultivo'].iloc[0] if len(df) > 0 else 'N/A'}")
    print(
        f"Período del cultivo: {trigo.start_month:02d}/{trigo.start_day:02d} - {trigo.end_month:02d}/{trigo.end_day:02d}"
    )


def ejemplo_3_combinacion_filtros():
    """Ejemplo 3: Combinar filtros de cultivo y municipio."""
    separador("EJEMPLO 3: Filtro de Cultivo + Municipio")

    df = get_prod_data(
        years=(2018, 2023),
        loc_name="Hermosillo",
        crop_name="Trigo grano",
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

    cultivos = ["Trigo grano", "Maíz grano", "Espárrago"]

    print("Comparación de cultivos en Sonora (2020-2023)\n")
    print(f"{'Cultivo':<20} {'Producción (ton)':>20} {'Valor (millones $)':>20}")
    print("-" * 62)

    for nombre in cultivos:
        df = get_prod_data(years=(2020, 2023), crop_name=nombre)

        if len(df) > 0:
            produccion = df["Volumenproduccion"].sum()
            valor = df["Valorproduccion"].sum() / 1000
            print(f"{nombre:<20} {produccion:>20,.2f} {valor:>20,.2f}")
        else:
            print(f"{nombre:<20} {'Sin datos':>20} {'Sin datos':>20}")


def ejemplo_5_analisis_temporal():
    """Ejemplo 5: Análisis temporal de un cultivo."""
    separador("EJEMPLO 5: Análisis Temporal de Cultivo")

    df = get_prod_data(years=(2018, 2023), crop_name="Uva")

    print("Evolución de la producción de Uva en Sonora (2018-2023)\n")

    if len(df) > 0:
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

        prod_inicial = anual["Prod. (ton)"].iloc[0]
        prod_final = anual["Prod. (ton)"].iloc[-1]
        cambio = ((prod_final - prod_inicial) / prod_inicial) * 100

        print(f"\nCambio en producción 2018-2023: {cambio:+.2f}%")

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
        df = get_prod_data(years=(2020, 2022), loc_name=municipio, crop_name=cultivo)

        if len(df) > 0:
            produccion = df["Volumenproduccion"].sum()
            valor = df["Valorproduccion"].sum()
            resultados.append((cultivo, produccion, valor))
            print(f"{cultivo:<20} {produccion:>20,.2f} {valor:>20,.2f}")

    if resultados:
        resultados.sort(key=lambda x: x[2], reverse=True)
        mejor_cultivo = resultados[0]
        print(f"\nCultivo más valioso: {mejor_cultivo[0]}")
        print(f"Valor total: ${mejor_cultivo[2]:,.2f} miles de pesos")


def ejemplo_7_region_objeto():
    """Ejemplo 7: Usar objeto Region para filtrar por municipio."""
    separador("EJEMPLO 7: Filtrado con Objeto Region")

    coords = get_mun_coordinates("Hermosillo")

    if coords.empty:
        print("No se encontraron coordenadas para Hermosillo")
        return

    row = coords.iloc[0]
    region = Region(
        name="Hermosillo",
        latitude=row["lat"],
        longitude=row["lon"],
        altitude=row["z_m"],
    )

    df = get_prod_data(
        years=(2018, 2023),
        loc_name=region,
        crop_name="Trigo grano",
    )

    print(f"Usando objeto Region: {region.name}")
    print(
        f"Coordenadas: lat={region.latitude}, lon={region.longitude}, alt={region.altitude}m\n"
    )

    if len(df) > 0:
        evolucion = df.groupby("Anio")["Volumenproduccion"].sum()
        print(f"Producción de trigo en {region.name}:\n")
        print(evolucion)
        print(f"\nTotal: {evolucion.sum():,.2f} toneladas")
    else:
        print("No hay datos disponibles para esta combinación")


def ejemplo_8_reconversion_productiva():
    """Ejemplo 8: Caso de uso - Análisis de reconversión productiva."""
    separador("EJEMPLO 8: Caso de Uso - Reconversión Productiva")

    municipio = "Hermosillo"
    cultivo_actual = "Alfalfa achicalada"
    cultivos_alternativos = ["Trigo grano", "Maíz grano", "Papa"]

    print(f"Análisis de reconversión productiva en {municipio} (2020-2023)\n")
    print(f"Cultivo actual: {cultivo_actual}\n")

    df_actual = get_prod_data(
        years=(2020, 2023),
        loc_name=municipio,
        crop_name=cultivo_actual,
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
    print("=" * 80)

    ejemplos = [
        ejemplo_1_filtro_basico,
        ejemplo_2_filtro_con_modelo_crop,
        ejemplo_3_combinacion_filtros,
        ejemplo_4_comparacion_cultivos,
        ejemplo_5_analisis_temporal,
        ejemplo_6_multiples_cultivos,
        ejemplo_7_region_objeto,
        ejemplo_8_reconversion_productiva,
    ]

    for ejemplo in ejemplos:
        ejemplo()
        input("\nPresiona Enter para continuar...\n")

    separador("EJEMPLOS COMPLETADOS")
    print("Todos los ejemplos se ejecutaron exitosamente.\n")


if __name__ == "__main__":
    main()
