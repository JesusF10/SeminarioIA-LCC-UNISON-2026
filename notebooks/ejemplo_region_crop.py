"""
Ejemplo completo: Usando las clases Region y Crop con indentación correcta.

Este script demuestra:
1. Creación de cultivos
2. Creación de regiones
3. Visualización con indentación en cascada
4. Comparación de __str__() vs __repr__()

Autor: Jesus Flores Lacarra
"""

from seminario_ia.models import Crop, Region


def separador(titulo: str = "", ancho: int = 80):
    """Imprime un separador visual con título opcional."""
    if titulo:
        print("\n" + "=" * ancho)
        print(titulo.center(ancho))
        print("=" * ancho + "\n")
    else:
        print("\n" + "-" * ancho + "\n")


def crear_cultivos_sonora():
    """Crea cultivos representativos de Sonora."""
    cultivos = {
        "Trigo": Crop(
            name="Trigo grano",
            start_month=10,
            start_day=30,
            end_month=4,
            end_day=19,
            kc_ini=0.3,
            kc_mid=1.15,
            kc_end=0.25,
            durations=(31, 47, 63, 31),
        ),
        "Maíz": Crop(
            name="Maíz grano",
            start_month=5,
            start_day=1,
            end_month=10,
            end_day=15,
            kc_ini=0.5,
            kc_mid=1.2,
            kc_end=0.4,
            durations=(25, 40, 50, 35),
        ),
        "Papa": Crop(
            name="Papa",
            start_month=2,
            start_day=15,
            end_month=6,
            end_day=30,
            kc_ini=0.5,
            kc_mid=1.15,
            kc_end=0.75,
            durations=(25, 35, 50, 30),
        ),
        "Alfalfa": Crop(
            name="Alfalfa",
            start_month=1,
            start_day=1,
            end_month=12,
            end_day=31,
            kc_ini=0.4,
            kc_mid=1.0,
            kc_end=0.5,
            durations=(30, 60, 120, 30),
        ),
    }
    return cultivos


def ejemplo_1_region_simple():
    """Ejemplo 1: Región con un cultivo."""
    separador("EJEMPLO 1: Región con Un Cultivo")

    # Crear región
    region = Region(
        name="San Ignacio Río Muerto",
        latitude=27.32498,
        longitude=-110.39104,
        altitude=7.0,
    )

    # Crear y agregar cultivo
    trigo = Crop(
        name="Trigo grano",
        start_month=10,
        start_day=30,
        end_month=4,
        end_day=19,
        kc_ini=0.3,
        kc_mid=1.15,
        kc_end=0.25,
        durations=(31, 47, 63, 31),
    )
    region.add_crop(trigo)

    print("Visualización con __str__():")
    print(region)


def ejemplo_2_region_multiples_cultivos():
    """Ejemplo 2: Región con múltiples cultivos."""
    separador("EJEMPLO 2: Región con Múltiples Cultivos")

    cultivos = crear_cultivos_sonora()

    region = Region(
        name="Hermosillo",
        latitude=29.0961,
        longitude=-110.9570,
        altitude=200.0,
    )

    # Agregar varios cultivos
    for cultivo in cultivos.values():
        region.add_crop(cultivo)

    print(f"Región '{region.name}' con {len(region.crops)} cultivos:")
    separador()
    print(region)


def ejemplo_3_comparacion_str_repr():
    """Ejemplo 3: Comparación de __str__() vs __repr__()."""
    separador("EJEMPLO 3: __str__() vs __repr__()")

    region = Region(
        name="Caborca",
        latitude=31.1470,
        longitude=-112.1553,
        altitude=200.0,
    )

    papa = Crop(
        name="Papa",
        start_month=2,
        start_day=15,
        end_month=6,
        end_day=30,
        kc_ini=0.5,
        kc_mid=1.15,
        kc_end=0.75,
        durations=(25, 35, 50, 30),
    )
    region.add_crop(papa)

    print("1. __str__() - Legible para humanos:")
    print("-" * 80)
    print(region)

    print("\n2. __repr__() - Compacto para debugging:")
    print("-" * 80)
    print(repr(region))

    print("\nDiferencias:")
    msg1 = "  __str__()  → Múltiples líneas, estructura clara,"
    msg2 = " bonito"
    print(msg1 + msg2)
    msg3 = "  __repr__() → Una línea, compacto, útil para"
    msg4 = " debugging"
    print(msg3 + msg4)


def ejemplo_4_region_vacia():
    """Ejemplo 4: Región sin cultivos."""
    separador("EJEMPLO 4: Región Sin Cultivos")

    region = Region(
        name="DDR Vacío",
        latitude=28.0,
        longitude=-111.0,
        altitude=300.0,
    )

    print("Región sin cultivos agregados:")
    print(region)


def ejemplo_5_analisis_cultivo_individual():
    """Ejemplo 5: Análisis de un cultivo individual."""
    separador("EJEMPLO 5: Análisis Individual de Cultivo")

    trigo = Crop(
        name="Trigo grano",
        start_month=10,
        start_day=30,
        end_month=4,
        end_day=19,
        kc_ini=0.3,
        kc_mid=1.15,
        kc_end=0.25,
        durations=(31, 47, 63, 31),
    )

    print("Información del cultivo Trigo:")
    print(trigo)

    print("\n\nAcceso a propiedades:")
    print(f"  Fecha de inicio: {trigo.start_date}")
    print(f"  Fecha de fin: {trigo.end_date}")
    print(f"  Coeficientes Kc: {trigo.kc}")
    print(f"  Total de días: {sum(trigo.durations)}")


def ejemplo_6_verificacion_indentacion():
    """Ejemplo 6: Verificación detallada de indentación."""
    separador("EJEMPLO 6: Verificación de Indentación en Cascada")

    region = Region(
        name="Test Region",
        latitude=28.0,
        longitude=-111.0,
        altitude=100.0,
    )

    cultivo = Crop(
        name="Test Crop",
        start_month=1,
        start_day=1,
        end_month=12,
        end_day=31,
        kc_ini=0.4,
        kc_mid=1.0,
        kc_end=0.5,
        durations=(30, 60, 120, 30),
    )
    region.add_crop(cultivo)

    salida = str(region)
    lineas = salida.split("\n")

    print("Análisis de indentación línea por línea:")
    print("-" * 80)
    print(f"{'Línea':<6} {'Espacios':<10} {'Contenido':<60}")
    print("-" * 80)

    for i, linea in enumerate(lineas, 1):
        espacios = len(linea) - len(linea.lstrip())
        contenido = linea.lstrip()[:55]
        print(f"{i:<6} {espacios:<10} {contenido:<60}")

    print("\nJerarquía de indentación:")
    print("  0 espacios  → Región (nivel raíz)")
    indent_msg1 = "  2 espacios  → Propiedades de región"
    indent_msg2 = " (latitud, longitud, etc.)"
    print(indent_msg1 + indent_msg2)
    print("  4 espacios  → Cada cultivo en la lista")
    indent_msg3 = "  10 espacios → Propiedades del cultivo"
    print(indent_msg3)
    indent_msg4 = "  12 espacios → Valores detallados"
    indent_msg5 = " (duraciones, coeficientes)"
    print(indent_msg4 + indent_msg5)


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("\n" + "=" * 80)
    titulo = "EJEMPLOS: REGIÓN Y CULTIVO CON INDENTACIÓN"
    print(titulo.center(80))
    print("Seminario de IA - Reconversión de Cultivos en Sonora 2026".center(80))
    print("=" * 80)

    ejemplos = [
        ejemplo_1_region_simple,
        ejemplo_2_region_multiples_cultivos,
        ejemplo_3_comparacion_str_repr,
        ejemplo_4_region_vacia,
        ejemplo_5_analisis_cultivo_individual,
        ejemplo_6_verificacion_indentacion,
    ]

    for ejemplo in ejemplos:
        ejemplo()

    separador("EJEMPLOS COMPLETADOS")
    print("Todos los ejemplos se ejecutaron correctamente.")
    print("La indentación en cascada funciona perfectamente.\n")


if __name__ == "__main__":
    main()
