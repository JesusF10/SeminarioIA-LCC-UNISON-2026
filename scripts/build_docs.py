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

    # Mapeo estricto para resolver anidamientos complejos de Typst
    strict_mappings = {
        # Ecuaciones de bloque
        'E T_o = frac(0.408 Delta (R_n - G) + gamma frac(900, T + 273) u_2 (e_s - e_a), Delta + gamma (1 + 0.34 u_2))':
            r'ET_o = \frac{0.408 \Delta (R_n - G) + \gamma \frac{900}{T + 273} u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)}',
        'gamma = frac(c_p P, epsilon lambda) approx 0.000665 dot P':
            r'\gamma = \frac{c_p P}{\epsilon \lambda} \approx 0.000665 \cdot P',
        'Delta = frac(4098 [0.6108 exp(frac(17.27 T, T + 237.3))], (T + 237.3)^2)':
            r'\Delta = \frac{4098 \left[0.6108 \exp\left(\frac{17.27 T}{T + 237.3}\right)\right]}{(T + 237.3)^2}',
        'e^o (T) = 0.6108 exp(frac(17.27 T, T + 237.3))':
            r'e^o (T) = 0.6108 \exp\left(\frac{17.27 T}{T + 237.3}\right)',
        'e_s = frac(e^o (T_"max") + e^o (T_"min"), 2)':
            r'e_s = \frac{e^o (T_{\text{max}}) + e^o (T_{\text{min}})}{2}',
        'e_a = e_s dot frac("RH", 100)':
            r'e_a = e_s \cdot \frac{\text{RH}}{100}',
        'R_a = frac(24 dot 60, pi) G_"sc" d_r (omega_s sin(phi) sin(delta) + cos(phi) cos(delta) sin(omega_s))':
            r'R_a = \frac{24 \cdot 60}{\pi} G_{\text{sc}} d_r (\omega_s \sin(\phi) \sin(\delta) + \cos(\phi) \cos(\delta) \sin(\omega_s))',
        'R_"ns" = (1 - alpha) R_s':
            r'R_{\text{ns}} = (1 - \alpha) R_s',
        'R_"nl" = sigma (frac(T_(max, K)^4 + T_(min, K)^4, 2)) (0.34 - 0.14 sqrt(e_a)) (1.35 frac(R_s, R_"so") - 0.35)':
            r'R_{\text{nl}} = \sigma \left(\frac{T_{\text{max}, K}^4 + T_{\text{min}, K}^4}{2}\right) (0.34 - 0.14 \sqrt{e_a}) \left(1.35 \frac{R_s}{R_{\text{so}}} - 0.35\right)',
        'R_n = R_"ns" - R_"nl"':
            r'R_n = R_{\text{ns}} - R_{\text{nl}}',
        'E T_c = K_c dot E T_o':
            r'ET_c = K_c \cdot ET_o',
        'E T_"verde" = min(E T_c, P_"ef")':
            r'ET_{\text{verde}} = \min\left(ET_c, P_{\text{ef}}\right)',
        'E T_"azul" = max(E T_c - P_"ef", 0)':
            r'ET_{\text{azul}} = \max\left(ET_c - P_{\text{ef}}, 0\right)',
        'U A C = sum_"ciclo" E T dot 10':
            r'\text{UAC} = \sum_{\text{ciclo}} ET \cdot 10',
        'H H = frac(U A C, "Rendimiento" (t/h a))':
            r'\text{HH} = \frac{\text{UAC}}{\text{Rendimiento (t/ha)}}',
        'P = 101.3 (frac(293 - 0.0065 z, 293))^(5.26)':
            r'P = 101.3 \left(\frac{293 - 0.0065 z}{293}\right)^{5.26}',
        # Expresiones inline
        'P_"ciclo" < 250': r'P_{\text{ciclo}} < 250',
        'P_"ef" = 0.8 dot P_"total"': r'P_{\text{ef}} = 0.8 \cdot P_{\text{total}}',
        'P_"ciclo" >= 250': r'P_{\text{ciclo}} \ge 250',
        'P_"ef" = 0.6 dot P_"total"': r'P_{\text{ef}} = 0.6 \cdot P_{\text{total}}',
        'c_p': r'c_p',
        '1.013 times 10^(-3)': r'1.013 \times 10^{-3}',
        'epsilon': r'\epsilon',
        'lambda': r'\lambda',
        'omega_s': r'\omega_s',
        'arccos(-tan(phi) tan(delta))': r'\omega_s = \arccos(-\tan(\phi) \tan(\delta))',
        'phi': r'\phi',
        'delta': r'\delta',
        'E T_o': r'ET_o',
        'E T_c': r'ET_c',
        'H H': r'HH',
        'z': r'z',
        'R_s': r'R_s',
        'u_2': r'u_2',
        'T_"max"': r'T_{\text{max}}',
        'T_"min"': r'T_{\text{min}}',
        'R_n': r'R_n',
        'G': r'G',
        'e_s': r'e_s',
        'e_a': r'e_a',
        'e_s - e_a': r'e_s - e_a',
        'Delta': r'\Delta',
        'gamma': r'\gamma',
        'K_c': r'K_c',
        'K_(c, "ini")': r'K_{c, \text{ini}}',
        'K_(c, "mid")': r'K_{c, \text{mid}}',
        'K_(c, "end")': r'K_{c, \text{end}}',
        'E T_"verde"': r'ET_{\text{verde}}',
        'E T_"azul"': r'ET_{\text{azul}}',
        'P': r'P',
        'R_"ns"': r'R_{\text{ns}}',
        'R_"nl"': r'R_{\text{nl}}',
        'R_"so"': r'R_{\text{so}}',
        '1 / "HH"_"total"': r'1/\text{HH}_{\text{total}}',
        '1/"HH"_"total"': r'1/\text{HH}_{\text{total}}',
        '"HH"_"total"': r'\text{HH}_{\text{total}}',
        '"MXN"/m^3': r'\text{MXN}/m^3',
        '"MXN"/m^2': r'\text{MXN}/m^2',
        '"Ton"/"m"^3': r'\text{Ton}/m^3',
        '"Ton"/m^3': r'\text{Ton}/m^3',
        '"PMR"': r'\text{PMR}',
        'P_"ef"': r'P_{\text{ef}}',
        'P_"total"': r'P_{\text{total}}',
        'omega_s sin(phi) sin(delta) + cos(phi) cos(delta) sin(omega_s)': r'\omega_s \sin(\phi) \sin(\delta) + \cos(\phi) \cos(\delta) \sin(\omega_s)'
    }

    if expr in strict_mappings:
        return strict_mappings[expr]

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

    # Limpiar paréntesis en exponentes: ^{(...)} → ^{...}
    expr = re.sub(r"\^\{?\(([^()]*)\)\}?", lambda m: f"^{{{m.group(1)}}}", expr)

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
    # Soporta paréntesis anidados simples e indentación al cierre
    table_pattern = r"#table\((.*?)\n\s*\)"
    return re.sub(table_pattern, table_replacer, content, flags=re.DOTALL)


def parse_typst_figure_to_html(figure_text: str) -> str:
    """
    Parsea un bloque #figure(...) de Typst y lo convierte a un elemento HTML figure
    estetizado si contiene una imagen.
    """
    path_match = re.search(r'image\("([^"]+)"', figure_text)
    if not path_match:
        return ""

    img_path = path_match.group(1)
    img_filename = Path(img_path).name

    # Extraer caption
    caption_match = re.search(r'caption:\s*\[(.*?)\]', figure_text, re.DOTALL)
    caption = caption_match.group(1).strip() if caption_match else ""
    # Traducir negritas de Typst a HTML
    caption = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", caption)

    # Extraer ancho
    width_match = re.search(r'width:\s*([\d%]+)', figure_text)
    width = width_match.group(1) if width_match else "80%"

    html = '<figure class="figure-premium" style="text-align: center; margin: 2rem 0;">'
    html += f'  <img src="images/{img_filename}" style="max-width: {width}; border-radius: var(--border-radius); border: 1px solid var(--card-border); box-shadow: var(--shadow-premium);">'
    if caption:
        html += f'  <figcaption style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.75rem; font-style: italic;">{caption}</figcaption>'
    html += '</figure>'
    return html


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
    pending_paragraph = []

    def flush_paragraph():
        if pending_paragraph:
            full_text = " ".join(pending_paragraph)
            # Traducir ecuaciones inline y formato en párrafos
            def inline_math_replacer(match):
                math_expr = match.group(1)
                latex = clean_typst_math_to_latex(math_expr)
                return f"\\({latex}\\)"

            paragraph = re.sub(r"\$([^\$]+)\$", inline_math_replacer, full_text)
            paragraph = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", paragraph)
            current_section["blocks"].append({"type": "paragraph", "content": paragraph})
            pending_paragraph.clear()

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
            flush_paragraph()
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

        # 3. Detectar, acumular e integrar bloques #figure(...) que contienen imágenes
        if stripped.startswith("#figure("):
            flush_paragraph()
            in_figure = True
            figure_lines = [line]
            parenthesis_count = stripped.count("(") - stripped.count(")")
            continue

        if in_figure:
            figure_lines.append(line)
            parenthesis_count += stripped.count("(") - stripped.count(")")
            if parenthesis_count <= 0:
                in_figure = False
                figure_text = "\n".join(figure_lines)
                html_fig = parse_typst_figure_to_html(figure_text)
                if html_fig:
                    current_section["blocks"].append({"type": "html", "content": html_fig})
            continue

        # 4. Ignorar directivas de configuración o imports de Typst
        if (stripped.startswith("#import") or
            stripped.startswith("#set") or
            stripped.startswith("#show") or
            stripped.startswith("#v(") or
            stripped.startswith("#align") or
            stripped.startswith("#pagebreak")):
            flush_paragraph()
            continue

        # Evitar diagramas Fletcher y paréntesis de cierre sueltos
        if "diagram(" in line or "fletcher" in line:
            flush_paragraph()
            continue

        # Ignorar líneas que solo contienen caracteres de cierre residuales de bloques de diseño (e.g. ']', ')', ',', etc.)
        if re.match(r"^[\s\]\),]+$", stripped):
            flush_paragraph()
            continue

        # Capturar tablas pre-renderizadas en HTML para que no se envuelvan en <p>
        if stripped.startswith('<div class="table-responsive">'):
            flush_paragraph()
            current_section["blocks"].append({"type": "html", "content": line})
            continue

        if not stripped:
            flush_paragraph()
            continue

        # 4b. Continuación de item de lista con sangría
        if (line.startswith(" ") or line.startswith("\t")) and stripped and current_section["blocks"] and current_section["blocks"][-1]["type"] == "list-item" and not pending_paragraph:
            def inline_math_replacer(match):
                math_expr = match.group(1)
                latex = clean_typst_math_to_latex(math_expr)
                return f"\\({latex}\\)"

            clean_text = re.sub(r"\$([^\$]+)\$", inline_math_replacer, stripped)
            clean_text = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", clean_text)
            current_section["blocks"][-1]["content"] += " " + clean_text
            continue

        # 5. Manejo de encabezados (e.g. "= Introducción" o "== NASA POWER")
        heading_match = re.match(r"^(=+)\s+(.*)$", stripped)
        if heading_match:
            flush_paragraph()
            if current_section["blocks"]:
                sections.append(current_section)

            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()

            # Traducir ecuaciones inline y formato en títulos
            def inline_math_replacer(match):
                math_expr = match.group(1)
                latex = clean_typst_math_to_latex(math_expr)
                return f"\\({latex}\\)"

            title = re.sub(r"\$([^\$]+)\$", inline_math_replacer, title)
            title = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", title)

            current_section = {"title": title, "level": level, "blocks": []}
            continue

        # 6. Ecuaciones de bloque completo
        if stripped.startswith("$") and stripped.endswith("$") and len(stripped) > 2:
            flush_paragraph()
            math_content = stripped[1:-1].strip()
            latex_math = clean_typst_math_to_latex(math_content)
            current_section["blocks"].append({"type": "math-block", "content": latex_math})
            continue

        # 7. Listas (viñetas y numeradas)
        list_match = re.match(r"^(?:-\s+|\d+\.\s+)(.*)$", stripped)
        if list_match:
            flush_paragraph()
            item_text = list_match.group(1)
            def inline_math_replacer(match):
                math_expr = match.group(1)
                latex = clean_typst_math_to_latex(math_expr)
                return f"\\({latex}\\)"

            item_text = re.sub(r"\$([^\$]+)\$", inline_math_replacer, item_text)
            item_text = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", item_text)
            
            num_match = re.match(r"^(\d+)\.\s+", stripped)
            prefix = f"{num_match.group(1)}. " if num_match else ""
            
            current_section["blocks"].append({
                "type": "list-item",
                "content": prefix + item_text
            })
            continue

        # 8. Acumular texto para párrafo
        pending_paragraph.append(stripped)

    # Procesar último párrafo pendiente
    flush_paragraph()

    if current_section["blocks"]:
        sections.append(current_section)

    return sections


def generate_dashboard_data(base_dir: Path, website_dir: Path):
    """
    Lee el archivo CSV del pipeline maestro y genera un JSON
    agregado y optimizado para el dashboard interactivo de estadísticas,
    incorporando el mapeo del REPNA, eficiencias físicas y económicas.
    """
    csv_path = base_dir / "data/processed/analisis_municipal_sonora_2010_2024.csv"
    codif_path = base_dir / "data/config/codificacion.json"
    
    if not csv_path.exists():
        print(f"Advertencia: No se encontró el dataset del pipeline en {csv_path}")
        return

    import pandas as pd
    import numpy as np

    # Cargar datos
    df = pd.read_csv(csv_path)

    # Limpiar columnas de texto
    df['Municipio'] = df['Municipio'].str.strip()
    df['DDR'] = df['DDR'].str.strip()
    df['Cultivo'] = df['Cultivo'].str.strip()

    # Catálogos únicos
    municipios = sorted(df['Municipio'].dropna().unique().tolist())
    ddrs = sorted(df['DDR'].dropna().unique().tolist())
    cultivos = sorted(df['Cultivo'].dropna().unique().tolist())

    # Relación DDR -> Municipios
    relacion_ddr_mun = {}
    for ddr in ddrs:
        muns_in_ddr = sorted(df[df['DDR'] == ddr]['Municipio'].dropna().unique().tolist())
        relacion_ddr_mun[ddr] = muns_in_ddr

    # Cargar codificaciones
    codif = {}
    if codif_path.exists():
        with open(codif_path, encoding="utf-8") as f:
            codif = json.load(f)

    # --- PROCESAMIENTO DE CONCESIONES REPNA ---
    concesiones_repna = {
        "estatal": {"Estatal": 0.0},
        "ddr": {},
        "municipio": {}
    }

    # Inicializar con 0
    for mun in municipios:
        concesiones_repna["municipio"][mun] = 0.0
    for ddr in ddrs:
        concesiones_repna["ddr"][ddr] = 0.0

    repna1_path = base_dir / "data/raw/datos_proporcionados/reporte-repna-1.csv"
    repna2_path = base_dir / "data/raw/datos_proporcionados/reporte-repna-2.csv"

    # Mapeo manual de municipios a DDRs
    mun_to_ddr = df.set_index('Municipio')['DDR'].to_dict()

    # Procesar reporte-repna-1 (Distritos de Riego Colectivos)
    if repna1_path.exists():
        try:
            df1 = pd.read_csv(repna1_path)
            vol_col1 = "Volumen de extracción de aguas nacionales" if "Volumen de extracción de aguas nacionales" in df1.columns else df1.columns[5]
            for _, row in df1.iterrows():
                titular = str(row["Titular"]).upper()
                vol = str(row[vol_col1]).replace(" ", "").replace(",", "")
                vol_val = pd.to_numeric(vol, errors="coerce")
                if pd.isna(vol_val): vol_val = 0.0

                # Sumar a total estatal
                concesiones_repna["estatal"]["Estatal"] += vol_val

                # Asignar a municipio núcleo del DR
                assigned_mun = None
                if "COSTA DE HERMOSILLO" in titular or "051" in titular:
                    assigned_mun = "Hermosillo"
                elif "ALTAR-PITIQUITO-CABORCA" in titular or "037" in titular or "CABORCA" in titular:
                    assigned_mun = "Caborca"
                elif "YAQUI" in titular or "041" in titular:
                    assigned_mun = "Cajeme"
                elif "MAYO" in titular or "038" in titular:
                    assigned_mun = "Navojoa"
                elif "COLORADO" in titular or "014" in titular:
                    assigned_mun = "San Luis Río Colorado"

                if assigned_mun and assigned_mun in concesiones_repna["municipio"]:
                    concesiones_repna["municipio"][assigned_mun] += vol_val
                    ddr_assigned = mun_to_ddr.get(assigned_mun)
                    if ddr_assigned and ddr_assigned in concesiones_repna["ddr"]:
                        concesiones_repna["ddr"][ddr_assigned] += vol_val
        except Exception as e:
            print(f"Error procesando reporte-repna-1: {e}")

    # Procesar reporte-repna-2 (Individuales)
    if repna2_path.exists():
        try:
            df2 = pd.read_csv(repna2_path)
            vol_col2 = "Volumen de extracción de aguas nacionales (m3/año)" if "Volumen de extracción de aguas nacionales (m3/año)" in df2.columns else df2.columns[5]
            for _, row in df2.iterrows():
                titulo = str(row["Título"])
                titular = str(row["Titular"]).upper()
                vol = str(row[vol_col2]).replace(" ", "").replace(",", "")
                vol_val = pd.to_numeric(vol, errors="coerce")
                if pd.isna(vol_val): vol_val = 0.0

                # Sumar al estatal
                concesiones_repna["estatal"]["Estatal"] += vol_val

                # Extraer código municipal del título de concesión (ej: .../09AMDA25 -> CveMun 25)
                match = re.search(r'/0\d[A-Z]+(\d{2})$', titulo)
                if match:
                    mun_code = match.group(1)
                    # Traducir código a nombre de municipio
                    if "codigos_municipios" in codif:
                        mun_name = codif["codigos_municipios"].get(mun_code)
                        if mun_name and mun_name in concesiones_repna["municipio"]:
                            concesiones_repna["municipio"][mun_name] += vol_val
                            ddr_assigned = mun_to_ddr.get(mun_name)
                            if ddr_assigned and ddr_assigned in concesiones_repna["ddr"]:
                                concesiones_repna["ddr"][ddr_assigned] += vol_val
                else:
                    # Intento alternativo: buscar el municipio en el nombre del titular
                    for mun in municipios:
                        if mun.upper() in titular:
                            concesiones_repna["municipio"][mun] += vol_val
                            ddr_assigned = mun_to_ddr.get(mun)
                            if ddr_assigned and ddr_assigned in concesiones_repna["ddr"]:
                                concesiones_repna["ddr"][ddr_assigned] += vol_val
                            break
        except Exception as e:
            print(f"Error procesando reporte-repna-2: {e}")

    # Redondear valores del REPNA
    concesiones_repna["estatal"]["Estatal"] = round(concesiones_repna["estatal"]["Estatal"], 1)
    for mun in concesiones_repna["municipio"]:
        concesiones_repna["municipio"][mun] = round(concesiones_repna["municipio"][mun], 1)
    for ddr in concesiones_repna["ddr"]:
        concesiones_repna["ddr"][ddr] = round(concesiones_repna["ddr"][ddr], 1)

    # Inicializar contenedores de resultados
    historico_anual = {
        "estatal": {},
        "ddr": {},
        "municipio": {}
    }
    
    promedios_cultivos = {
        "estatal": {},
        "ddr": {},
        "municipio": {}
    }

    # Definir la función auxiliar de agregación con las nuevas métricas
    def aggregate_group(group):
        sup_cos = group['SupCosechadaTotal_ha'].sum()
        vol_prod = group['VolumenTotal_t'].sum()
        
        # Volumen de agua en m3 (UAC es m3/ha, por tanto UAC * SupCosechada da el total de m3)
        vol_agua_verde = (group['UACverde_m3_ha'] * group['SupCosechadaTotal_ha']).sum()
        vol_agua_azul = (group['UACazul_m3_ha'] * group['SupCosechadaTotal_ha']).sum()
        vol_agua_total = vol_agua_verde + vol_agua_azul
        
        rend = vol_prod / sup_cos if sup_cos > 0 else 0.0
        
        # Huella Hídrica (m3/t)
        hh_verde = vol_agua_verde / vol_prod if vol_prod > 0 else 0.0
        hh_azul = vol_agua_azul / vol_prod if vol_prod > 0 else 0.0
        hh_total = hh_verde + hh_azul
        
        # UAC promedio ponderado (m3/ha)
        uac_total = vol_agua_total / sup_cos if sup_cos > 0 else 0.0
        
        # Eficiencia física (Ton/m3)
        eficiencia_fisica = 1.0 / hh_total if hh_total > 0 else 0.0
        
        # PMR promedio ponderado por producción
        if vol_prod > 0:
            pmr_val = (group['PMR'] * group['VolumenTotal_t']).sum() / vol_prod
        else:
            pmr_val = group['PMR'].mean()
        if pd.isna(pmr_val): pmr_val = 0.0
        
        # Productividad económica (MXN/m3)
        prod_economica = pmr_val / hh_total if hh_total > 0 else 0.0

        # Sequía promedio ponderada por superficie
        if sup_cos > 0:
            sequia_isag = (group['indice_estres_sequia_acumulado'] * group['SupCosechadaTotal_ha']).sum() / sup_cos
            if 'max_intensidad_sequia' in group.columns:
                intensidad_sequia = (group['max_intensidad_sequia'] * group['SupCosechadaTotal_ha']).sum() / sup_cos
            elif 'max_inte_sequia' in group.columns:
                intensidad_sequia = (group['max_inte_sequia'] * group['SupCosechadaTotal_ha']).sum() / sup_cos
            else:
                intensidad_sequia = 0.0
        else:
            sequia_isag = group['indice_estres_sequia_acumulado'].mean()
            if 'max_intensidad_sequia' in group.columns:
                intensidad_sequia = group['max_intensidad_sequia'].mean()
            elif 'max_inte_sequia' in group.columns:
                intensidad_sequia = group['max_inte_sequia'].mean()
            else:
                intensidad_sequia = 0.0

        # Reemplazar NaN o valores no válidos
        if pd.isna(sequia_isag): sequia_isag = 0.0
        if pd.isna(intensidad_sequia): intensidad_sequia = 0.0
        if pd.isna(prod_economica) or np.isinf(prod_economica): prod_economica = 0.0
        if pd.isna(eficiencia_fisica) or np.isinf(eficiencia_fisica): eficiencia_fisica = 0.0
        
        # Precipitación promedio en mm ponderada por superficie
        if sup_cos > 0:
            ptot_mm = (group['Ptot_total_mm'] * group['SupCosechadaTotal_ha']).sum() / sup_cos
            pef_mm = (group['Pef_total_mm'] * group['SupCosechadaTotal_ha']).sum() / sup_cos
        else:
            ptot_mm = group['Ptot_total_mm'].mean()
            pef_mm = group['Pef_total_mm'].mean()
        if pd.isna(ptot_mm): ptot_mm = 0.0
        if pd.isna(pef_mm): pef_mm = 0.0
        
        sup_sem = group['SupSembradaTotal_ha'].sum()
        sup_sin = max(0.0, sup_sem - sup_cos)
        pct_siniestralidad = (sup_sin / sup_sem * 100.0) if sup_sem > 0 else 0.0
        pct_cosechada = (sup_cos / sup_sem * 100.0) if sup_sem > 0 else 0.0

        return {
            "rendimiento": round(float(rend), 3),
            "hh_total": round(float(hh_total), 1),
            "hh_azul": round(float(hh_azul), 1),
            "hh_verde": round(float(hh_verde), 1),
            "uac_total": round(float(uac_total), 1),
            "eficiencia_fisica": round(float(eficiencia_fisica), 5),
            "pmr": round(float(pmr_val), 2),
            "productividad_economica": round(float(prod_economica), 4),
            "consumo_agua_total": round(float(vol_agua_total), 1),
            "ptot_total_mm": round(float(ptot_mm), 1),
            "pef_total_mm": round(float(pef_mm), 1),
            "sequia_isag": round(float(sequia_isag), 3),
            "max_intensidad_sequia": round(float(intensidad_sequia), 2),
            "superficie_cosechada": round(float(sup_cos), 1),
            "superficie_sembrada": round(float(sup_sem), 1),
            "superficie_siniestrada": round(float(sup_sin), 1),
            "pct_siniestralidad": round(float(pct_siniestralidad), 2),
            "pct_cosechada": round(float(pct_cosechada), 2),
            "volumen_produccion": round(float(vol_prod), 1)
        }

    # Agregar "Todos los cultivos" al catálogo
    cultivos = ["Todos los cultivos"] + cultivos

    # --- 1. AGREGACIÓN ESTATAL ---
    # Histórico Anual Estatal por Cultivo
    df_estatal_grouped = df.groupby(['Cultivo', 'Anio'])
    for (cultivo, anio), group in df_estatal_grouped:
        if "Estatal" not in historico_anual["estatal"]:
            historico_anual["estatal"]["Estatal"] = {}
        if cultivo not in historico_anual["estatal"]["Estatal"]:
            historico_anual["estatal"]["Estatal"][cultivo] = {}
        
        historico_anual["estatal"]["Estatal"][cultivo][str(anio)] = aggregate_group(group)

    # Histórico Anual Estatal - Todos los cultivos
    df_estatal_all_grouped = df.groupby(['Anio'])
    for anio, group in df_estatal_all_grouped:
        anio_str = str(anio[0]) if isinstance(anio, tuple) else str(anio)
        if "Estatal" not in historico_anual["estatal"]:
            historico_anual["estatal"]["Estatal"] = {}
        if "Todos los cultivos" not in historico_anual["estatal"]["Estatal"]:
            historico_anual["estatal"]["Estatal"]["Todos los cultivos"] = {}
        
        historico_anual["estatal"]["Estatal"]["Todos los cultivos"][anio_str] = aggregate_group(group)

    # Promedios Históricos Estatales por Cultivo
    df_estatal_crop = df.groupby('Cultivo')
    for cultivo, group in df_estatal_crop:
        cultivo_str = cultivo[0] if isinstance(cultivo, tuple) else cultivo
        if "Estatal" not in promedios_cultivos["estatal"]:
            promedios_cultivos["estatal"]["Estatal"] = {}
        promedios_cultivos["estatal"]["Estatal"][cultivo_str] = aggregate_group(group)

    # Promedios Históricos Estatales - Todos los cultivos
    if "Estatal" not in promedios_cultivos["estatal"]:
        promedios_cultivos["estatal"]["Estatal"] = {}
    promedios_cultivos["estatal"]["Estatal"]["Todos los cultivos"] = aggregate_group(df)

    # --- 2. AGREGACIÓN POR DDR ---
    # Histórico Anual por DDR y Cultivo
    df_ddr_grouped = df.groupby(['DDR', 'Cultivo', 'Anio'])
    for (ddr, cultivo, anio), group in df_ddr_grouped:
        if ddr not in historico_anual["ddr"]:
            historico_anual["ddr"][ddr] = {}
        if cultivo not in historico_anual["ddr"][ddr]:
            historico_anual["ddr"][ddr][cultivo] = {}
        
        historico_anual["ddr"][ddr][cultivo][str(anio)] = aggregate_group(group)

    # Histórico Anual por DDR - Todos los cultivos
    df_ddr_all_grouped = df.groupby(['DDR', 'Anio'])
    for (ddr, anio), group in df_ddr_all_grouped:
        if ddr not in historico_anual["ddr"]:
            historico_anual["ddr"][ddr] = {}
        if "Todos los cultivos" not in historico_anual["ddr"][ddr]:
            historico_anual["ddr"][ddr]["Todos los cultivos"] = {}
        
        historico_anual["ddr"][ddr]["Todos los cultivos"][str(anio)] = aggregate_group(group)

    # Promedios Históricos por DDR y Cultivo
    df_ddr_crop = df.groupby(['DDR', 'Cultivo'])
    for (ddr, cultivo), group in df_ddr_crop:
        if ddr not in promedios_cultivos["ddr"]:
            promedios_cultivos["ddr"][ddr] = {}
        promedios_cultivos["ddr"][ddr][cultivo] = aggregate_group(group)

    # Promedios Históricos por DDR - Todos los cultivos
    df_ddr_all = df.groupby('DDR')
    for ddr, group in df_ddr_all:
        ddr_str = ddr[0] if isinstance(ddr, tuple) else ddr
        if ddr_str not in promedios_cultivos["ddr"]:
            promedios_cultivos["ddr"][ddr_str] = {}
        promedios_cultivos["ddr"][ddr_str]["Todos los cultivos"] = aggregate_group(group)

    # --- 3. AGREGACIÓN POR MUNICIPIO ---
    # Histórico Anual por Municipio y Cultivo
    df_mun_grouped = df.groupby(['Municipio', 'Cultivo', 'Anio'])
    for (mun, cultivo, anio), group in df_mun_grouped:
        if mun not in historico_anual["municipio"]:
            historico_anual["municipio"][mun] = {}
        if cultivo not in historico_anual["municipio"][mun]:
            historico_anual["municipio"][mun][cultivo] = {}
        
        historico_anual["municipio"][mun][cultivo][str(anio)] = aggregate_group(group)

    # Histórico Anual por Municipio - Todos los cultivos
    df_mun_all_grouped = df.groupby(['Municipio', 'Anio'])
    for (mun, anio), group in df_mun_all_grouped:
        if mun not in historico_anual["municipio"]:
            historico_anual["municipio"][mun] = {}
        if "Todos los cultivos" not in historico_anual["municipio"][mun]:
            historico_anual["municipio"][mun]["Todos los cultivos"] = {}
        
        historico_anual["municipio"][mun]["Todos los cultivos"][str(anio)] = aggregate_group(group)

    # Promedios Históricos por Municipio y Cultivo
    df_mun_crop = df.groupby(['Municipio', 'Cultivo'])
    for (mun, cultivo), group in df_mun_crop:
        if mun not in promedios_cultivos["municipio"]:
            promedios_cultivos["municipio"][mun] = {}
        promedios_cultivos["municipio"][mun][cultivo] = aggregate_group(group)

    # Promedios Históricos por Municipio - Todos los cultivos
    df_mun_all = df.groupby('Municipio')
    for mun, group in df_mun_all:
        mun_str = mun[0] if isinstance(mun, tuple) else mun
        if mun_str not in promedios_cultivos["municipio"]:
            promedios_cultivos["municipio"][mun_str] = {}
        promedios_cultivos["municipio"][mun_str]["Todos los cultivos"] = aggregate_group(group)

    # Ensamblar base de datos del dashboard
    dashboard_data = {
        "catalogos": {
            "municipios": municipios,
            "ddrs": ddrs,
            "cultivos": cultivos,
            "relacion_ddr_municipio": relacion_ddr_mun
        },
        "concesiones_repna": concesiones_repna,
        "historico_anual": historico_anual,
        "promedios_cultivos": promedios_cultivos
    }

    # Guardar en archivo JSON
    output_path = website_dir / "dashboard_data.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dashboard_data, f, ensure_ascii=False, indent=2)

    print(f"Archivo de datos del dashboard generado con éxito: {output_path} (Size: {output_path.stat().st_size / 1024:.1f} KB)")


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

    # Cargar resumen de sequía
    resumen_sequia_path = BASE_DIR / "data/processed/resumen_sequia.json"
    resumen_sequia_data = {}
    if resumen_sequia_path.exists():
        with open(resumen_sequia_path, encoding="utf-8") as f:
            resumen_sequia_data = json.load(f)

    # Consolidar toda la base de datos de contenido
    compiled_data = {
        "reporte_hh": sections_hh,
        "reporte_est": sections_est,
        "cultivos": cultivos_data,
        "codificaciones": codificaciones_data,
        "resumen_sequia": resumen_sequia_data,
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
    import shutil
    if images_dest.exists():
        shutil.rmtree(images_dest)
    if images_src.exists():
        shutil.copytree(images_src, images_dest)
    else:
        images_dest.mkdir(parents=True, exist_ok=True)

    # Copiar imágenes del reporte de estadísticas
    report_images_src = BASE_DIR / "reports/fase3/prueba_analisis/images"
    if report_images_src.exists():
        for img_file in report_images_src.glob("*.png"):
            shutil.copy(img_file, images_dest)

    # Generar la base de datos para el dashboard interactivo
    generate_dashboard_data(BASE_DIR, WEBSITE_DIR)

    print(f"Compilación terminada con éxito. Archivo escrito en: {output_path}")


if __name__ == "__main__":
    main()

