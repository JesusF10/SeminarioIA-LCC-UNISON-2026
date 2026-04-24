"""
Script para demostrar la indentación correcta en Region con Crop.

Autor: Equipo Seminario IA
Fecha: 2024
"""

from seminario_ia.models import Crop, Region


def separador(titulo: str):
    """Imprime un separador visual."""
    print("\n" + "=" * 80)
    print(titulo.center(80))
    print("=" * 80 + "\n")


def test_region_with_crops():
    """Prueba una región con múltiples cultivos."""
    separador("PRUEBA: Región con Cultivos - Indentación en Cascada")

    # Crear cultivos
    trigo = Crop(
        name="Trigo",
        start_month=10,
        start_day=30,
        end_month=4,
        end_day=19,
        kc_ini=0.3,
        kc_mid=1.15,
        kc_end=0.25,
        durations=(31, 47, 63, 31),
    )

    maiz = Crop(
        name="Maíz grano",
        start_month=5,
        start_day=1,
        end_month=10,
        end_day=15,
        kc_ini=0.5,
        kc_mid=1.2,
        kc_end=0.4,
        durations=(25, 40, 50, 35),
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

    # Crear región
    san_ignacio = Region(
        name="San Ignacio Río Muerto",
        latitude=27.32498,
        longitude=-110.39104,
        altitude=7.0,
    )

    # Agregar cultivos
    san_ignacio.add_crop(trigo)
    san_ignacio.add_crop(maiz)
    san_ignacio.add_crop(papa)

    print("RESULTADO CON __str__() (formato legible):")
    print("-" * 80)
    print(san_ignacio)

    print("\n\nVERIFICACIÓN DE INDENTACIÓN:")
    print("-" * 80)
    lines = str(san_ignacio).split("\n")
    for i, line in enumerate(lines, 1):
        # Contar espacios al inicio
        spaces = len(line) - len(line.lstrip())
        indicator = "↳ " if spaces > 0 else "↳ "
        print(f"Línea {i:2d} ({spaces:2d} espacios): {indicator}{line}")


def test_empty_region():
    """Prueba una región vacía sin cultivos."""
    separador("PRUEBA: Región Vacía")

    region_vacia = Region(
        name="DDR Sin Cultivos",
        latitude=29.0,
        longitude=-110.0,
        altitude=500.0,
    )

    print("Región sin cultivos:")
    print("-" * 80)
    print(region_vacia)


def test_repr():
    """Prueba la representación __repr__."""
    separador("PRUEBA: __repr__() - Representación Compacta")

    trigo = Crop(
        name="Trigo",
        start_month=10,
        start_day=30,
        end_month=4,
        end_day=19,
        kc_ini=0.3,
        kc_mid=1.15,
        kc_end=0.25,
        durations=(31, 47, 63, 31),
    )

    region = Region(
        name="Test Region",
        latitude=25.0,
        longitude=-110.0,
        altitude=100.0,
    )
    region.add_crop(trigo)

    print("__repr__() para debugging:")
    print("-" * 80)
    print(repr(region))


def main():
    """Función principal."""
    print("\n" + "=" * 80)
    print("PRUEBAS DE INDENTACIÓN EN CASCADA".center(80))
    print("Seminario IA - Reconversión Productiva LCC UNISON 2026".center(80))
    print("=" * 80)

    test_region_with_crops()
    test_empty_region()
    test_repr()

    separador("PRUEBAS COMPLETADAS")
    print("Todas las pruebas de indentación se ejecutaron correctamente.\n")


if __name__ == "__main__":
    main()
