"""
Módulo de utilidades para manejo de fechas.
"""

from datetime import datetime, timedelta


def date_from_year_doy(year: int, doy: int) -> datetime:
    """
    Regresa un objeto datetime correspondiente a la fecha calendario dada por
    un año (YEAR) y un día juliano (DOY).

    Parámetros:
        - year: Año calendario (ej. 2010).
        - doy: Día del año (1-365/366).

    Regresa:
        - datetime correspondiente a la fecha dada por year y doy.
    """
    return datetime(year, 1, 1) + timedelta(days=int(doy) - 1)


def year_doy_from_date(date: datetime | str) -> tuple[int, int]:
    """
    Regresa el año (YEAR) y día juliano (DOY) correspondientes a un objeto datetime.

    Parámetros:
        - date: Objeto datetime del cual extraer el año y día juliano.

    Regresa:
        - Tuple con el año (int) y día juliano (int) correspondientes a la fecha dada.
    """
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    year = date.year
    doy = date.timetuple().tm_yday
    return year, doy
