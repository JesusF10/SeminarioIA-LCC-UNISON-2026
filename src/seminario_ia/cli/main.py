"""
CLI para Seminario IA.
"""

from seminario_ia import __version__

import click


@click.group()
@click.version_option(version=__version__, prog_name="seminario-ia")
def cli():
    """
    Paquete para seminario de IA.

    Herramienta de línea de comandos.
    """
    print("Hola desde la CLI de Seminario IA!")


def main():
    """Punto de entrada principal."""
    cli()
