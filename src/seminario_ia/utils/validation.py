"""
Utilidades para validación de datos usando Pydantic.
"""

from seminario_ia.models.data_models import WeatherAdapter

import pandas as pd


def validate_weather_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Valida un DataFrame de clima usando WeatherRecord.
    Regresa el DataFrame validado (con alias convertidos a nombres de campo).
    """
    records = df.to_dict("records")
    validated_records = WeatherAdapter.validate_python(records)

    # Convertir de vuelta a DF con nombres de campos PEP8
    # Usamos model_dump() para obtener diccionarios con nombres de campos (no alias)
    clean_data = [r.model_dump(by_alias=True) for r in validated_records]
    return pd.DataFrame(clean_data)
