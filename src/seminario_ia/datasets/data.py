"""
Operaciones de datos para el proyecto.

Este módulo proporciona funciones para acceder a datos procesados,
incluyendo coordenadas de municipios en Sonora.
"""

from .codes import get_mun_code
from .paths import COORDINATES_CSV, PROCESSED_DIR, RAW_DATASETS

import pandas as pd

coordinates = pd.read_csv(COORDINATES_CSV, encoding="utf-8")
coordinates = coordinates.drop(columns=["entidad"])

prod_files = PROCESSED_DIR / "siap_produccion"
prod_muni_files = prod_files / "sonora"
prod_nat_files = prod_files / "nacional"


def get_mun_coordinates(input: str | int = "all") -> pd.DataFrame:
    """
    Regresa las coordenadas del municipio ingresado (clave o nombre),
    y si no se encuentra, devuelve None.

    Si se deja vacío, se regresa un dataframe con las coordenadas de todos los municipios.

    Parámetros:
        - input: str | int - El nombre o código del municipio.

    Regresa:
        - pd.DataFrame | None - La latitud, longitud y altitud del municipio, y en otro caso, None.
    """
    if input == "all":
        return coordinates
    if isinstance(input, int):
        mun = get_mun_code(input)
        if mun is None:
            return pd.DataFrame()
        return coordinates[coordinates["municipio"] == mun]
    if isinstance(input, str):
        if input.isdigit():
            mun = get_mun_code(input)
            if mun is None:
                return pd.DataFrame()
            return coordinates[coordinates["municipio"] == mun]
        return coordinates[coordinates["municipio"] == input]
    return pd.DataFrame()


def load_prod_file(year: int | str, muni: bool = False) -> pd.DataFrame:
    """
    Carga un archivo de producción agrícola de la SIAP en el año especificado.
    Si no existe, devuelve None.

    Parámetros:
        - year: int | str - Año de producción de la SIAP.
        - muni: bool - Si es True, se carga el archivo con datos a nivel municipio. Por defecto es False (datos a nivel nacional).

    Regresa:
        - pd.DataFrame | None - El dataframe con los datos de producción, o None si no se encuentra el archivo.
    """

    path_to_search = prod_muni_files if muni else prod_nat_files

    files = list(path_to_search.glob(f"*{year}.csv"))
    if len(files) == 0:
        return pd.DataFrame()
    return pd.read_csv(files[0], encoding="utf-8")


def get_prod_data(
    years: tuple[int, int] | str | list[int],
    loc_name: str | int = "all",
    crop_name: str | int = "all",
    muni: bool = False,
) -> pd.DataFrame:
    """
    Carga los archivos de producción agrícola de la SIAP para los años especificados.
    Si no se encuentra algún archivo, se omite y se continúa con los demás.

    Parámetros:
        - years: tuple[int, int] | str | list[int] - Años de producción de la SIAP.
            Puede ser un rango (tupla), un año específico (str o int), o una lista de años.
        - loc_name: str | int - El nombre o código del municipio, en el caso de municipal. Si se deja vacío, se
            cargan todos los datos (a nivel municipal).
        - crop_name: str | int - El nombre o código del cultivo. Si se deja vacío ("all"), se
            cargan todos los cultivos.
        - muni: bool - Si es True, se cargan los archivos con datos a nivel municipio.
            Por defecto es False (datos a nivel nacional).
    """
    if isinstance(years, str):
        years = list(map(int, years.split("-")))
        if len(years) == 2:
            years = list(range(years[0], years[1] + 1))
    elif isinstance(years, int):
        years = [years]
    elif isinstance(years, tuple) and len(years) == 2:
        years = list(range(years[0], years[1] + 1))

    dataframes = []
    for year in years:
        df = load_prod_file(year, muni)
        if df is not None:
            dataframes.append(df)

    if len(dataframes) == 0:
        return pd.DataFrame()

    df = pd.concat(dataframes, ignore_index=True)

    # Filter by location (municipal only)
    if muni and loc_name != "all":
        if isinstance(loc_name, int):
            df = df[df["Idmunicipio"] == loc_name]
        elif isinstance(loc_name, str):
            if loc_name.isdigit():
                df = df[df["Idmunicipio"] == int(loc_name)]
            else:
                df = df[df["Nommunicipio"] == loc_name]

    # Filter by crop (both municipal and national)
    if crop_name != "all":
        if isinstance(crop_name, int):
            df = df[df["Idcultivo"] == crop_name]
        elif isinstance(crop_name, str):
            if crop_name.isdigit():
                df = df[df["Idcultivo"] == int(crop_name)]
            else:
                df = df[df["Nomcultivo"] == crop_name]

    return df


if __name__ == "__main__":
    for dataset_name, dataset_path in RAW_DATASETS.items():
        print(f"Cargando dataset: {dataset_name}")
        print(f"Ruta del dataset: {dataset_path}")
