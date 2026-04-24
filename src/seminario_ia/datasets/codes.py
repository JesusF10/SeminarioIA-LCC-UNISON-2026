import json

from seminario_ia.datasets.paths import JSON_CODIFICACION

with open(JSON_CODIFICACION, encoding="utf-8") as f:
    data = json.load(f)
    ciclos = data["codigos_ciclos"]
    municipios = data["codigos_municipios"]
    ddrs = data["codigos_ddrs"]
    modalidades = data["codigos_modalidades"]
    unidades = data["codigos_unidades"]


def get_cycle_code(input: str | int | None = None) -> str | int | dict | None:
    """
    Regresa el nombre del ciclo a partir de su código (valores entre 1 y 4),
    o bien, el código del ciclo si se ingresa el nombre.

    Parámetros:
        - input: str | int | None - El nombre del ciclo, su código, o None para obtener
            el diccionario completo. Por defecto es None.

    Regresa:
        - str | int | dict | None: El código del ciclo si se ingresa el nombre,
            el nombre del ciclo si se ingresa el código, el diccionario completo si
            no se proporciona input, o None si no se encuentra.
    """
    if input is None:
        return ciclos
    if isinstance(input, int):
        return ciclos.get(str(input), None)
    if isinstance(input, str):
        for k, v in ciclos.items():
            if v == input:
                return int(k)

    return None


def get_ddr_code(input: str | int | None = None) -> str | int | dict | None:
    """
    Regresa el nombre del DDR a partir de su código (valores entre 1 y 9),
    o bien, el código del DDR si se ingresa el nombre.

    Parámetros:
        - input: str | int | None - El nombre del DDR, su código, o None para obtener
            el diccionario completo. Por defecto es None.

    Regresa:
        - str | int | dict | None: El código del DDR si se ingresa el nombre,
            el nombre del DDR si se ingresa el código, el diccionario completo si
            no se proporciona input, o None si no se encuentra.
    """
    if input is None:
        return ddrs
    if isinstance(input, int):
        return ddrs.get(str(input), None)
    if isinstance(input, str):
        for k, v in ddrs.items():
            if v == input:
                return int(k)

    return None


def get_mod_code(input: str | int | None = None) -> str | int | dict | None:
    """
    Regresa el nombre de la modalidad a partir de su código (1 o 2),
    o bien, el código de la modalidad si se ingresa el nombre.

    Parámetros:
        - input: str | int | None - El nombre de la modalidad, su código, o None para
            obtener el diccionario completo. Por defecto es None.

    Regresa:
        - str | int | dict | None: El código de la modalidad si se ingresa el nombre,
            el nombre de la modalidad si se ingresa el código, el diccionario completo si
            no se proporciona input, o None si no se encuentra.
    """
    if input is None:
        return modalidades
    if isinstance(input, int):
        return modalidades.get(str(input), None)
    if isinstance(input, str):
        for k, v in modalidades.items():
            if v == input:
                return int(k)

    return None


def get_mun_code(input: str | int | None = None) -> str | int | dict | None:
    """
    Regresa el nombre del municipio a partir de su código (valores entre 1 y 72),
    o bien, el código del municipio si se ingresa el nombre.

    Parámetros:
        - input: str | int | None - El nombre del municipio, su código, o None para
            obtener el diccionario completo. Por defecto es None.

    Regresa:
        - str | int | dict | None: El código del municipio si se ingresa el nombre,
            el nombre del municipio si se ingresa el código, el diccionario completo si
            no se proporciona input, o None si no se encuentra.
    """
    if input is None:
        return municipios
    if isinstance(input, int):
        return municipios.get(str(input), None)
    if isinstance(input, str):
        for k, v in municipios.items():
            if v == input:
                return int(k)

    return None


def get_unit_code(input: str | int | None = None) -> str | int | dict | None:
    """
    Regresa el nombre de la unidad a partir de su código,
    o bien, el código de la unidad si se ingresa el nombre.

    Parámetros:
        - input: str | int | None - El nombre de la unidad, su código, o None para
            obtener el diccionario completo. Por defecto es None.

    Regresa:
        - str | int | dict | None: El código de la unidad si se ingresa el nombre,
            el nombre de la unidad si se ingresa el código, el diccionario completo si
            no se proporciona input, o None si no se encuentra.
    """
    if input is None:
        return unidades
    if isinstance(input, int):
        return unidades.get(str(input), None)
    if isinstance(input, str):
        for k, v in unidades.items():
            if v == input:
                return int(k)

    return None
