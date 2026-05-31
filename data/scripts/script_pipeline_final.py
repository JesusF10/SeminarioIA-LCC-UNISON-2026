"""
Script final para ejecución del pipeline en municipios seleccionados y verificación de variabilidad anual.
"""

from pathlib import Path

from seminario_ia.analysis.pipeline import (
    consolidate_results,
    run_municipality_pipeline,
)
from seminario_ia.datasets import get_crop_data, get_mun_coordinates, get_prod_data
from seminario_ia.models import Region

import pandas as pd


def verify_yearly_variability(mun_name):
    """Verifica que la Huella Hídrica varíe por año para un municipio dado."""
    safe_name = mun_name.replace(" ", "_")
    file_path = Path(f"data/processed/analisis_municipal/{safe_name}_2010_2024.csv")

    if not file_path.exists():
        print(f"\n[ERROR] No se encontró archivo para {mun_name}")
        return

    df = pd.read_csv(file_path)

    # Contar valores únicos de HHtotal por cultivo
    # Si es > 1, significa que varió entre años (lo cual es correcto si el rendimiento varió)
    variability = df.groupby("Cultivo")["HHtotal_m3_ton"].nunique()

    print(f"\n>>> Verificación de variabilidad en {mun_name}:")
    print(f"Cultivos procesados: {len(variability)}")

    v_count = (variability > 1).sum()
    print(f"Cultivos con HH variable por año: {v_count}")

    if v_count > 0:
        example_crop = variability[variability > 1].index[0]
        print(f"Ejemplo: {example_crop}")
        print(
            df[df["Cultivo"] == example_crop][
                ["Anio", "Rend_t_ha", "HHtotal_m3_ton"]
            ].head()
        )
    else:
        print(
            "Aviso: No se detectó variabilidad (puede ser por falta de datos en varios años)."
        )


def main(consolidate: bool = False):
    # 1. Configuración de municipios de prueba
    years_range = "2010-2024"

    # 2. Carga de datos globales
    coords_df = get_mun_coordinates()
    crops = get_crop_data()
    all_prod_data = get_prod_data(years_range)

    # Remover cultivos con unidades distintas a la tonelada:
    all_prod_data = all_prod_data[all_prod_data["Nomunidad"] == "Tonelada"]

    if not isinstance(crops, dict):
        crops = {crops.name: crops}

    # 3. Ejecución por municipio
    for mun in coords_df.itertuples():
        _, mun_name, lat, lon, alt = mun
        region = Region(name=mun_name, latitude=lat, longitude=lon, altitude=alt)
        print(f"Procesando {mun}...")
        run_municipality_pipeline(region, crops, all_prod_data, years_range)

    # 4. Verificación de resultados
    for mun in coords_df.itertuples():
        _, mun_name, _, _, _ = mun
        verify_yearly_variability(mun_name)

    # 5. Consolidación final (opcional, consolidará todo lo que haya en la carpeta)
    if consolidate:
        print("\nConsolidando resultados maestros...")
        consolidate_results()


if __name__ == "__main__":
    main(consolidate=True)
    print("Pipeline finalizado.")
