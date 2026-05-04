"""
Operaciones de datos para el proyecto.

Este módulo proporciona funciones para acceder a datos procesados,
incluyendo coordenadas de municipios en Sonora.
"""

from seminario_ia.models import Crop
from seminario_ia.utils import validate_weather_df

from .codes import get_mun_code
from .paths import PROCESSED_DIR, RAW_DATASETS
from .repository import repo

import pandas as pd

coordinates = repo.load_coordinates()

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

    # Filtrar por municipio (solo municipal)
    if muni and loc_name != "all":
        if isinstance(loc_name, int):
            df = df[df["Idmunicipio"] == loc_name]
        elif isinstance(loc_name, str):
            if loc_name.isdigit():
                df = df[df["Idmunicipio"] == int(loc_name)]
            else:
                df = df[df["Nommunicipio"] == loc_name]

    # Filtrar por cultivo
    if crop_name != "all":
        if isinstance(crop_name, int):
            df = df[df["Idcultivo"] == crop_name]
        elif isinstance(crop_name, str):
            if crop_name.isdigit():
                df = df[df["Idcultivo"] == int(crop_name)]
            else:
                df = df[df["Nomcultivo"] == crop_name]

    return df


def read_nasa_power_file(year: str, loc: str = "all") -> pd.DataFrame:
    """
    Lee un archivo de datos de la API de NASA POWER para el año y ubicación especificados.
    """
    raw_data = repo.load_nasa_power(year, loc)
    if raw_data.empty:
        return pd.DataFrame()
    return validate_weather_df(raw_data)


def get_nasa_power_data(
    loc_name: str | int, year: int | list[int] | str = "all"
) -> pd.DataFrame:
    """
    Carga los datos de la API de NASA POWER para el año y ubicación especificados.
    Si no se encuentra algún dato, se devuelve un dataframe vacío.

    Parámetros:
        - year: int | list[int] | str - Año o años para los cuales se desean los datos de NASA POWER.
            Puede ser un año específico (int), una lista de años (list[int]), o un rango de años en formato "YYYY-YYYY" (str).
        - loc_name: str | int - El nombre o código del municipio.

    Regresa:
        - pd.DataFrame - Un dataframe con los datos de NASA POWER para el año y ubicación especificados, o un
        dataframe vacío si no se encuentra ningún dato.

    """
    # Determinar los años
    years = []
    if year == "all":
        years = list(range(2003, 2025))
    elif isinstance(year, int):
        years = [year]
    elif isinstance(year, str):  # Formato admitido: YYYY-YYYY o YYYY
        year_splitted = year.split("-")
        if len(year_splitted) == 2:
            years = list(range(int(year_splitted[0]), int(year_splitted[1]) + 1))
        else:
            years = [int(year)]
    elif isinstance(year, list):
        years = year

    # Determinar los municipios:
    if isinstance(loc_name, int):
        loc_name_str = get_mun_code(loc_name)
        if loc_name_str is None:
            return pd.DataFrame()
        return pd.concat(
            [read_nasa_power_file(str(year), str(loc_name_str)) for year in years],
            ignore_index=True,
        ).sort_values(by=["DATE"])
    elif isinstance(loc_name, str):
        if loc_name.isdigit():
            loc_name_str = get_mun_code(int(loc_name))
            if loc_name_str is None:
                return pd.DataFrame()
            return pd.concat(
                [read_nasa_power_file(str(year), str(loc_name_str)) for year in years],
                ignore_index=True,
            ).sort_values(by=["DATE"])
        else:
            return pd.concat(
                [read_nasa_power_file(str(year), loc_name) for year in years],
                ignore_index=True,
            ).sort_values(by=["DATE"])

    return pd.DataFrame()


def _build_crop(name: str, crop_info: dict) -> Crop:
    """
    Función auxiliar para construir un objeto Crop a partir de
    información JSON.

    Parámetros:
        - name: str - Nombre del cultivo
        - crop_info: dict - Diccionario con información del cultivo

    Regresa:
        - Crop - Objeto Crop con los parámetros especificados
    """
    if crop_info:
        calendar = crop_info["calendar"]
        kc = crop_info["kc"]
        durations = tuple(map(int, crop_info["durations"]))
        return Crop(
            name=name,
            start_month=int(calendar["start_mmdd"][0]),
            start_day=int(calendar["start_mmdd"][1]),
            end_month=int(calendar["end_mmdd"][0]),
            end_day=int(calendar["end_mmdd"][1]),
            kc_ini=float(kc["ini"]),
            kc_mid=float(kc["mid"]),
            kc_end=float(kc["end"]),
            durations=durations,
        )
    else:
        # Retornar Crop vacío si no existe información
        return Crop(
            name=name,
            start_month=1,
            start_day=1,
            end_month=1,
            end_day=1,
            kc_ini=0.0,
            kc_mid=0.0,
            kc_end=0.0,
            durations=(0, 0, 0, 0),
        )


def get_crop_data(name: str | None = None) -> Crop | dict[str, Crop]:
    """
    Retorna información de cultivos en forma de objeto Crop o
    diccionario.

    Parámetros:
        - name: str | None - Nombre del cultivo específico, o None
          para obtener todos

    Regresa:
        - Crop - Si se especifica un nombre: objeto Crop del cultivo
        - dict[str, Crop] - Si name=None: diccionario
          {nombre_cultivo: Crop}

    Ejemplos:
        # Obtener un cultivo específico
        trigo = get_crop_data("Trigo grano")
        print(trigo.kc_mid)  # 1.15

        # Obtener todos los cultivos
        todos = get_crop_data()
        for nombre, cultivo in todos.items():
            print(f"{nombre}: Kc={cultivo.kc_mid}")

        # Acceder a cultivo específico del diccionario
        papa = get_crop_data()["Papa"]
        print(papa.start_month)  # 2
    """
    crops_dict = repo.load_config_json("cultivos")

    # Si name=None, retornar todos los cultivos como diccionario
    if name is None:
        result = {}
        for crop_name, crop_info in crops_dict.items():
            result[crop_name] = _build_crop(crop_name, crop_info)
        return result

    # Si name especificado, retornar un cultivo individual
    crop_info = crops_dict.get(name, {})
    return _build_crop(name, crop_info)


if __name__ == "__main__":
    for dataset_name, dataset_path in RAW_DATASETS.items():
        print(f"Cargando dataset: {dataset_name}")
        print(f"Ruta del dataset: {dataset_path}")
