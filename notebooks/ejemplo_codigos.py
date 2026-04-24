"""
Ejemplo de uso de los getters de códigos del módulo datasets.

Este script demuestra las tres formas de usar las funciones get_*_code:
1. Sin argumentos: Obtener el diccionario completo de códigos
2. Con código (int): Obtener el nombre correspondiente al código
3. Con nombre (str): Obtener el código correspondiente al nombre

Autor: Jesus Flores Lacarra
Fecha: Abril 2026
"""

from seminario_ia.datasets import (
    get_cycle_code,
    get_ddr_code,
    get_mod_code,
    get_mun_code,
    get_unit_code,
)


def ejemplo_diccionarios_completos():
    """Ejemplo 1: Obtener diccionarios completos sin argumentos."""
    print("=" * 80)
    print("EJEMPLO 1: Obtener diccionarios completos")
    print("=" * 80)
    print()

    # Obtener todos los ciclos
    ciclos = get_cycle_code()
    print(f" + Ciclos agrícolas ({len(ciclos)} registros):")
    for codigo, nombre in ciclos.items():
        print(f"  {codigo}: {nombre}")
    print()

    # Obtener todos los municipios
    municipios = get_mun_code()
    print(f" +  Municipios de Sonora ({len(municipios)} registros):")
    print("  Primeros 5:")
    for codigo, nombre in list(municipios.items())[:5]:
        print(f"  {codigo}: {nombre}")
    print("  ...")
    print()

    # Obtener todos los DDRs
    ddrs = get_ddr_code()
    print(f" + Distritos de Desarrollo Rural ({len(ddrs)} registros):")
    for codigo, nombre in ddrs.items():
        print(f"  {codigo}: {nombre}")
    print()

    # Obtener todas las modalidades
    modalidades = get_mod_code()
    print(f" + Modalidades de producción ({len(modalidades)} registros):")
    for codigo, nombre in modalidades.items():
        print(f"  {codigo}: {nombre}")
    print()

    # Obtener todas las unidades
    unidades = get_unit_code()
    print(f" + Unidades de medida ({len(unidades)} registros):")
    for codigo, nombre in unidades.items():
        print(f"  {codigo}: {nombre}")
    print()


def ejemplo_busqueda_por_codigo():
    """Ejemplo 2: Buscar nombres usando códigos (int)."""
    print("=" * 80)
    print("EJEMPLO 2: Buscar nombres por código (argumento int)")
    print("=" * 80)
    print()

    # Buscar municipios por código
    print(" +  Municipios:")
    print(f"  Código 30 → {get_mun_code(30)}")
    print(f"  Código 1  → {get_mun_code(1)}")
    print(f"  Código 72 → {get_mun_code(72)}")
    print()

    # Buscar ciclos por código
    print(" + Ciclos:")
    print(f"  Código 1 → {get_cycle_code(1)}")
    print(f"  Código 2 → {get_cycle_code(2)}")
    print()

    # Buscar DDRs por código
    print(" + DDRs:")
    print(f"  Código 1  → {get_ddr_code(1)}")
    print(f"  Código 10 → {get_ddr_code(10)}")
    print()

    # Buscar modalidades por código
    print(" + Modalidades:")
    print(f"  Código 1 → {get_mod_code(1)}")
    print(f"  Código 2 → {get_mod_code(2)}")
    print()


def ejemplo_busqueda_por_nombre():
    """Ejemplo 3: Buscar códigos usando nombres (str)."""
    print("=" * 80)
    print("EJEMPLO 3: Buscar códigos por nombre (argumento str)")
    print("=" * 80)
    print()

    # Buscar códigos de municipios
    print(" +  Municipios:")
    print(f"  'Hermosillo'      → {get_mun_code('Hermosillo')}")
    print(f"  'Caborca'         → {get_mun_code('Caborca')}")
    print(f"  'Agua Prieta'     → {get_mun_code('Agua Prieta')}")
    print()

    # Buscar códigos de ciclos
    print(" + Ciclos:")
    nombre_ciclo = "Ciclo Primavera-Verano"
    print(f"  '{nombre_ciclo}' → {get_cycle_code(nombre_ciclo)}")
    nombre_ciclo = "Ciclo Perennes"
    print(f"  '{nombre_ciclo}' → {get_cycle_code(nombre_ciclo)}")
    print()

    # Buscar códigos de DDRs
    print(" + DDRs:")
    print(f"  'Hermosillo'      → {get_ddr_code('Hermosillo')}")
    print(f"  'Guaymas'         → {get_ddr_code('Guaymas')}")
    print()

    # Buscar códigos de modalidades
    print(" + Modalidades:")
    print(f"  'Riego'           → {get_mod_code('Riego')}")
    print(f"  'Temporal'        → {get_mod_code('Temporal')}")
    print()


def ejemplo_manejo_errores():
    """Ejemplo 4: Manejo de valores no encontrados."""
    print("=" * 80)
    print("EJEMPLO 4: Manejo de valores no encontrados")
    print("=" * 80)
    print()

    # Códigos que no existen
    print("X Búsquedas que retornan None:")
    print(f"  get_mun_code(999)            → {get_mun_code(999)}")
    print(f"  get_mun_code('NoExiste')     → {get_mun_code('NoExiste')}")
    print(f"  get_cycle_code(99)           → {get_cycle_code(99)}")
    print(f"  get_ddr_code('Inexistente')  → {get_ddr_code('Inexistente')}")
    print()

    # Uso recomendado con validación
    print("++ Uso recomendado con validación:")
    municipio = "Hermosillo"
    codigo = get_mun_code(municipio)
    if codigo is not None:
        print(f"  El municipio '{municipio}' tiene código: {codigo}")
    else:
        print(f"  !!!  El municipio '{municipio}' no fue encontrado")
    print()


def ejemplo_caso_uso_real():
    """Ejemplo 5: Caso de uso real - Iterar sobre municipios."""
    print("=" * 80)
    print("EJEMPLO 5: Caso de uso real - Análisis por municipio")
    print("=" * 80)
    print()

    # Obtener todos los municipios
    municipios = get_mun_code()

    print("Procesando análisis para todos los municipios de Sonora...")
    print()

    # Simular procesamiento de algunos municipios
    municipios_ejemplo = ["01", "30", "13", "72"]

    for codigo in municipios_ejemplo:
        nombre = get_mun_code(int(codigo))
        if nombre:
            # Aquí iría la lógica de análisis real
            print(f"  ✓ Procesando {codigo:>2} - {nombre:<30} [OK]")

    print()
    print(f"Total de municipios en Sonora: {len(municipios)}")
    print()


if __name__ == "__main__":
    print()
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "EJEMPLOS DE USO DE CÓDIGOS" + " " * 32 + "║")
    print("║" + " " * 15 + "Seminario IA - LCC UNISON 2026" + " " * 33 + "║")
    print("╚" + "═" * 78 + "╝")
    print()

    # Ejecutar todos los ejemplos
    ejemplo_diccionarios_completos()
    input("Presiona Enter para continuar...\n")

    ejemplo_busqueda_por_codigo()
    input("Presiona Enter para continuar...\n")

    ejemplo_busqueda_por_nombre()
    input("Presiona Enter para continuar...\n")

    ejemplo_manejo_errores()
    input("Presiona Enter para continuar...\n")

    ejemplo_caso_uso_real()

    print("=" * 80)
    print("✅ Ejemplos completados exitosamente")
    print("=" * 80)
    print()
