#!/usr/bin/env python3
"""
build_docs.py - Compilador de reportes Typst a formato JSON/HTML.
Este script lee los archivos Typst en la carpeta docs/ y los convierte
en contenido estructurado para el sitio web en docs/website/.
"""

import json
import re
from pathlib import Path

# Configuración de rutas
BASE_DIR = Path(__file__).parent.parent.resolve()
DOCS_DIR = BASE_DIR / "docs"
WEBSITE_DIR = DOCS_DIR / "website"

# Asegurar que el directorio de salida existe
WEBSITE_DIR.mkdir(parents=True, exist_ok=True)


def clean_typst_math_to_latex(math_expr: str) -> str:
    """
    Convierte expresiones matemáticas de Typst a formato LaTeX estándar.
    """
    expr = math_expr.strip()

    # Reemplazos con expresiones regulares usando funciones lambda para evitar
    # problemas de escape de backslashes en re.sub
    expr = re.sub(r"frac\((.*?),\s*(.*?)\)", lambda m: f"\\frac{{{m.group(1)}}}{{{m.group(2)}}}", expr)
    expr = re.sub(r"exp\((.*?)\)", lambda m: f"\\exp\\left({m.group(1)}\\right)", expr)
    expr = re.sub(r"sin\((.*?)\)", lambda m: f"\\sin\\left({m.group(1)}\\right)", expr)
    expr = re.sub(r"cos\((.*?)\)", lambda m: f"\\cos\\left({m.group(1)}\\right)", expr)
    expr = re.sub(r"tan\((.*?)\)", lambda m: f"\\tan\\left({m.group(1)}\\right)", expr)
    expr = re.sub(r"arccos\((.*?)\)", lambda m: f"\\arccos\\left({m.group(1)}\\right)", expr)
    expr = re.sub(r"sqrt\((.*?)\)", lambda m: f"\\sqrt{{{m.group(1)}}}", expr)
    expr = re.sub(r"min\((.*?),\s*(.*?)\)", lambda m: f"\\min\\left({m.group(1)}, {m.group(2)}\\right)", expr)
    expr = re.sub(r"max\((.*?),\s*(.*?)\)", lambda m: f"\\max\\left({m.group(1)}, {m.group(2)}\\right)", expr)
    expr = re.sub(r"sum_\"(.*?)\"", lambda m: f"\\sum_{{\\text{{{m.group(1)}}}}}", expr)
    expr = re.sub(r"\"(.*?)\"", lambda m: f"\\text{{{m.group(1)}}}", expr)

    # Reemplazos literales simples (no regex)
    literal_replacements = [
        ("approx", r"\approx"),
        ("dot", r"\cdot"),
        ("times", r"\times"),
        ("sum", r"\sum"),
        ("T_\"max\"", r"T_{\text{max}}"),
        ("T_\"min\"", r"T_{\text{min}}"),
        ("T_(max, K)", r"T_{\text{max}, K}"),
        ("T_(min, K)", r"T_{\text{min}, K}"),
        ("E T_o", r"ET_o"),
        ("E T_c", r"ET_c"),
        ("E T_\"verde\"", r"ET_{\text{verde}}"),
        ("E T_\"azul\"", r"ET_{\text{azul}}"),
        ("P_\"ef\"", r"P_{\text{ef}}"),
        ("P_\"total\"", r"P_{\text{total}}"),
        ("P_\"ciclo\"", r"P_{\text{ciclo}}"),
        ("R_\"ns\"", r"R_{\text{ns}}"),
        ("R_\"nl\"", r"R_{\text{nl}}"),
        ("R_\"so\"", r"R_{\text{so}}"),
        ("G_\"sc\"", r"G_{\text{sc}}"),
    ]

    for old, new in literal_replacements:
        expr = expr.replace(old, new)

    # Variables griegas usando regex de frontera de palabra
    greek_vars = [
        ("phi", r"\phi"),
        ("Delta", r"\Delta"),
        ("gamma", r"\gamma"),
        ("sigma", r"\sigma"),
        ("epsilon", r"\epsilon"),
        ("lambda", r"\lambda"),
        ("pi", r"\pi"),
        ("omega_s", r"\omega_s"),
        ("delta", r"\delta"),
        ("alpha", r"\alpha"),
    ]

    for word, replacement in greek_vars:
        expr = re.sub(r"\b" + word + r"\b", lambda m, r=replacement: r, expr)

    return expr


def parse_typst_tables(content: str) -> str:
    """
    Detecta bloques de #table(...) en Typst y los convierte a tablas HTML limpias.
    """

    def table_replacer(match):
        table_body = match.group(1)
        # Extraer elementos de la tabla entre corchetes [...]
        items = re.findall(r"\[(.*?)\]", table_body, re.DOTALL)
        if not items:
            return ""

        # Determinar columnas (por defecto asumimos el número de encabezados en negrita)
        headers = [item for item in items if item.startswith("*") and item.endswith("*")]
        num_cols = len(headers) if headers else 3

        html = '<div class="table-responsive"><table class="table-premium"><thead><tr>'

        # Renderizar headers
        for i in range(num_cols):
            if i < len(items):
                item = items[i].strip("*")
                html += f"<th>{item}</th>"
        html += "</tr></thead><tbody>"

        # Renderizar filas
        row_items = items[num_cols:]
        for idx, item in enumerate(row_items):
            if idx % num_cols == 0:
                html += "<tr>"
            # Formatear negritas dentro de celdas
            item_clean = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", item)
            html += f"<td>{item_clean}</td>"
            if (idx + 1) % num_cols == 0 or (idx + 1) == len(row_items):
                html += "</tr>"

        html += "</tbody></table></div>"
        return html

    # Regex para capturar bloques de #table(...)
    # Soporta paréntesis anidados simples
    table_pattern = r"#table\((.*?)\n\)"
    return re.sub(table_pattern, table_replacer, content, flags=re.DOTALL)


def parse_typst_file(filepath: Path) -> list[dict]:
    """
    Parsea un archivo Typst y lo divide en secciones estructuradas por headings.
    """
    if not filepath.exists():
        print(f"Advertencia: El archivo {filepath} no existe.")
        return []

    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # Pre-procesar tablas de Typst a HTML
    content = parse_typst_tables(content)

    sections = []
    current_section = {"title": "General", "level": 1, "blocks": []}

    lines = content.split("\n")
    
    started = False  # Para ignorar cabeceras y setups de Typst hasta el primer heading
    in_code_block = False
    in_figure = False
    parenthesis_count = 0
    
    code_lang = "python"
    code_lines = []

    for line in lines:
        stripped = line.strip()

        # 1. Ignorar cabeceras, imports y configuraciones hasta el primer encabezado
        if not started:
            if stripped.startswith("="):
                started = True
            else:
                continue

        # 2. Manejo de bloques de código
        if stripped.startswith("```"):
            if in_code_block:
                in_code_block = False
                current_section["blocks"].append(
                    {
                        "type": "code",
                        "lang": code_lang,
                        "content": "\n".join(code_lines),
                    }
                )
                code_lines = []
            else:
                in_code_block = True
                code_lang = stripped[3:] if len(stripped) > 3 else "python"
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        # 3. Detectar e ignorar bloques #figure(...) completos
        if stripped.startswith("#figure("):
            in_figure = True
            parenthesis_count = stripped.count("(") - stripped.count(")")
            continue

        if in_figure:
            parenthesis_count += stripped.count("(") - stripped.count(")")
            if parenthesis_count <= 0:
                in_figure = False
            continue

        # 4. Ignorar directivas de configuración o imports de Typst
        if (stripped.startswith("#import") or 
            stripped.startswith("#set") or 
            stripped.startswith("#show") or
            stripped.startswith("#v(") or
            stripped.startswith("#pagebreak")):
            continue

        # Evitar diagramas Fletcher y paréntesis de cierre sueltos
        if "diagram(" in line or "fletcher" in line or stripped == ")":
            continue

        # Capturar tablas pre-renderizadas en HTML para que no se envuelvan en <p>
        if stripped.startswith('<div class="table-responsive">'):
            current_section["blocks"].append({"type": "html", "content": line})
            continue

        if not stripped:
            continue

        # 5. Manejo de encabezados (e.g. "= Introducción" o "== NASA POWER")
        heading_match = re.match(r"^(=+)\s+(.*)$", stripped)
        if heading_match:
            if current_section["blocks"]:
                sections.append(current_section)

            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            current_section = {"title": title, "level": level, "blocks": []}
            continue

        # 6. Ecuaciones de bloque completo
        if stripped.startswith("$") and stripped.endswith("$") and len(stripped) > 2:
            math_content = stripped[1:-1].strip()
            latex_math = clean_typst_math_to_latex(math_content)
            current_section["blocks"].append({"type": "math-block", "content": latex_math})
            continue

        # 7. Párrafos y ecuaciones inline
        def inline_math_replacer(match):
            math_expr = match.group(1)
            latex = clean_typst_math_to_latex(math_expr)
            return f"\\({latex}\\)"

        paragraph = re.sub(r"\$([^\$]+)\$", inline_math_replacer, line)
        paragraph = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", paragraph)

        if paragraph.startswith("- "):
            current_section["blocks"].append({"type": "list-item", "content": paragraph[2:]})
        else:
            current_section["blocks"].append({"type": "paragraph", "content": paragraph})

    if current_section["blocks"]:
        sections.append(current_section)

    return sections


def main():
    print("Compilando reportes técnicos a formato web JSON...")

    # Compilar reporte hídrico
    reporte_hh_path = DOCS_DIR / "reporte-calculo-hh.typst"
    sections_hh = parse_typst_file(reporte_hh_path)

    # Compilar reporte estadísticas
    reporte_est_path = DOCS_DIR / "fase3/reporte-estadisticas.typ"
    sections_est = parse_typst_file(reporte_est_path)

    # Cargar catálogo de cultivos para indexar en la documentación
    cultivos_path = BASE_DIR / "data/config/cultivos.json"
    cultivos_data = {}
    if cultivos_path.exists():
        with open(cultivos_path, encoding="utf-8") as f:
            cultivos_data = json.load(f)

    # Cargar codificaciones
    codificaciones_path = BASE_DIR / "data/config/codificacion.json"
    codificaciones_data = {}
    if codificaciones_path.exists():
        with open(codificaciones_path, encoding="utf-8") as f:
            codificaciones_data = json.load(f)

    # Consolidar toda la base de datos de contenido
    compiled_data = {
        "reporte_hh": sections_hh,
        "reporte_est": sections_est,
        "cultivos": cultivos_data,
        "codificaciones": codificaciones_data,
        "meta": {
            "title": "Seminario IA - Reconversión Productiva Sonora 2026",
            "version": "1.0.0",
            "author": "Equipo LCC UNISON 2026",
        },
    }

    # Guardar en archivo JSON para la aplicación web
    output_path = WEBSITE_DIR / "data_content.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(compiled_data, f, ensure_ascii=False, indent=2)

    # Copiar imágenes al sitio web de documentación
    images_src = BASE_DIR / "images"
    images_dest = WEBSITE_DIR / "images"
    if images_src.exists():
        import shutil
        if images_dest.exists():
            shutil.rmtree(images_dest)
        shutil.copytree(images_src, images_dest)

    print(f"Compilación terminada con éxito. Archivo escrito en: {output_path}")


if __name__ == "__main__":
    main()
