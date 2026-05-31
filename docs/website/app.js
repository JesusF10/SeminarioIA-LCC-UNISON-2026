/**
 * app.js - Lógica e interactividad de la SPA de documentación.
 * Controla la carga de datos, el enrutado, los temas, la calculadora FAO-56,
 * y los gráficos interactivos de eficiencia hídrica.
 */

// Estado global de la aplicación
const AppState = {
    data: null,
    theme: "dark",
    activeSection: "inicio",
    charts: {},
};

// Inventario de Datos Estático (para complementar la UI)
const DATA_INVENTORY = {
    raw: [
        {
            name: "datos-sequia",
            size: "64 MB",
            desc: "Capa vectorial georeferenciada (Shapefile y soporte SIG) que registra el Mapa de Impacto de la sequía sobre la actividad agrícola (ISAG) a nivel municipal en Sonora, provisto por CONAGUA.",
            tag: "raw",
        },
        {
            name: "siap-produccion-agricola",
            size: "14 MB",
            desc: "Registros históricos completos y diccionarios de producción agrícola del SIAP (2003-2024 a escala municipal y 1980-2002 nacional) que contienen variables de superficies sembradas, cosechadas, volumen, precio medio rural y valor financiero.",
            tag: "raw",
        },
    ],
    processed: [
        {
            name: "SonoraLatLongAlt.csv",
            size: "4 KB",
            desc: "Base geográfica municipal de referencia para Sonora que consolida el nombre oficial del municipio junto a sus coordenadas de latitud, longitud y altitud (m.s.n.m.) requeridas en las ecuaciones de radiación FAO-56.",
            tag: "processed",
        },
        {
            name: "monitor_sequia_sonora.csv",
            size: "820 KB",
            desc: "Bitácora histórica transaccional detallada a nivel municipal (quincenal/mensual, 2003-2026) que limpia las categorías cualitativas del Monitor de Sequía de la CONAGUA a valores de intensidad numérica (1-5) para análisis temporal.",
            tag: "processed",
        },
        {
            name: "sequia_indices_sonora.csv",
            size: "12 KB",
            desc: "Matriz estática agregada por municipio que calcula variables atemporales de riesgo (recurrencia, severidad, consecutividad en meses y el Índice ISAG resultante) segmentado para los ciclos Primavera-Verano (PV) y Otoño-Invierno (OI).",
            tag: "processed",
        },
        {
            name: "nasa_power/",
            size: "Variable",
            desc: "Repositorio local de series diarias de tiempo climatológicas (radiación solar de onda corta, humedad relativa, temperatura máxima/mínima, velocidad del viento y lluvias) obtenidas mediante la API de NASA POWER para Sonora.",
            tag: "processed",
        },
        {
            name: "siap_produccion/sonora/",
            size: "2.6 MB",
            desc: "Archivos anuales de producción agrícola de Sonora ya filtrados del catálogo general nacional, depurados en formato estructurado de columnas homologadas y sin datos nulos.",
            tag: "processed",
        },
        {
            name: "analisis_municipal_sonora_2010_2024.csv",
            size: "11 MB",
            desc: "Dataset maestro final que concatena los indicadores productivos de rendimiento del SIAP con las variables climatológicas diarias acumuladas por ciclo (ETo, precipitación efectiva y temperaturas) para modelado predictivo.",
            tag: "processed",
        },
    ],
};

// Estructura de la librería seminario_ia (para el visualizador de arquitectura)
const LIBRARY_STRUCTURE = {
    name: "seminario_ia",
    type: "dir",
    children: [
        {
            name: "models",
            type: "dir",
            children: [
                {
                    name: "data_models.py",
                    type: "file",
                    desc: "Clases base Crop y Region modeladas con Pydantic para tipado estricto.",
                },
            ],
        },
        {
            name: "datasets",
            type: "dir",
            children: [
                {
                    name: "codes.py",
                    type: "file",
                    desc: "Manejo y decodificación de códigos municipales y DDRs.",
                },
                {
                    name: "data.py",
                    type: "file",
                    desc: "API de carga y filtrado de datos climáticos y agrícolas.",
                },
                {
                    name: "paths.py",
                    type: "file",
                    desc: "Constantes y rutas absolutas a archivos crudos y procesados.",
                },
                {
                    name: "repository.py",
                    type: "file",
                    desc: "Módulo I/O para aislamiento físico del almacenamiento de datos.",
                },
            ],
        },
        {
            name: "analysis",
            type: "dir",
            children: [
                {
                    name: "pipeline.py",
                    type: "file",
                    desc: "Flujo de cálculo completo de ETo, huella hídrica y reconversión.",
                },
            ],
        },
        {
            name: "utils",
            type: "dir",
            children: [
                {
                    name: "date.py",
                    type: "file",
                    desc: "Cálculo de días del año y periodos de ciclos agrícolas.",
                },
                {
                    name: "eto.py",
                    type: "file",
                    desc: "Fórmulas matemáticas FAO-56 Penman-Monteith y Hargreaves.",
                },
                {
                    name: "nasa_power.py",
                    type: "file",
                    desc: "Cliente para descargas HTTP automatizadas desde NASA POWER API.",
                },
                {
                    name: "performance.py",
                    type: "file",
                    desc: "Perfilador y decoradores de rendimiento para optimizar cálculo.",
                },
                {
                    name: "validation.py",
                    type: "file",
                    desc: "Funciones de control de esquemas de datos.",
                },
            ],
        },
    ],
};

// --- Gestión de Carga e Inicialización ---
document.addEventListener("DOMContentLoaded", () => {
    // Cargar tema preferido
    const savedTheme = localStorage.getItem("theme") || "dark";
    setTheme(savedTheme);

    // Inicializar enrutamiento
    window.addEventListener("hashchange", handleRouting);

    // Registrar listeners de la calculadora
    setupCalculatorListeners();

    // Cargar datos del compilador
    fetch("data_content.json")
        .then((res) => res.json())
        .then((data) => {
            AppState.data = data;
            renderAllDynamicContent();

            // Ocultar Splash Screen
            const loader = document.getElementById("loader");
            if (loader) {
                loader.style.opacity = "0";
                setTimeout(() => (loader.style.display = "none"), 500);
            }

            // Ejecutar enrutamiento inicial
            handleRouting();
        })
        .catch((err) => {
            console.error("Error cargando base de datos de contenido:", err);
            // Ocultar cargador igualmente pero alertar
            document.getElementById("loader").innerHTML =
                `<div style="text-align:center;color:red;padding:2rem;">
        <h2>Error cargando documentación</h2>
        <p>No se encontró 'data_content.json'. Corre primero 'python3 scripts/build_docs.py'</p>
      </div>`;
        });

    // Tema Toggle Button
    document.getElementById("theme-toggle").addEventListener("click", toggleTheme);
});

// --- Enrutamiento Simple ---
function handleRouting() {
    const hash = window.location.hash.replace("#", "") || "inicio";
    const sections = document.querySelectorAll(".section");
    const navItems = document.querySelectorAll(".nav-item");

    let sectionExists = false;
    sections.forEach((sec) => {
        if (sec.id === hash) {
            sec.classList.add("active");
            sectionExists = true;
        } else {
            sec.classList.remove("active");
        }
    });

    if (!sectionExists) {
        document.getElementById("inicio").classList.add("active");
    }

    navItems.forEach((item) => {
        if (item.dataset.section === hash) {
            item.classList.add("active");
        } else {
            item.classList.remove("active");
        }
    });

    AppState.activeSection = hash;

    // Destruir y recrear gráficos al abrir estadísticas
    if (hash === "estadisticas") {
        renderCharts();
    }
}

// --- Renderizado de Contenidos Dinámicos ---
function renderAllDynamicContent() {
    if (!AppState.data) return;

    // 1. Renderizar Metodología HH (Penman-Monteith)
    const hhContentDiv = document.getElementById("metodologia-content");
    if (hhContentDiv && AppState.data.reporte_hh) {
        hhContentDiv.innerHTML = renderReportSectionsHTML(AppState.data.reporte_hh);
    }

    // 2. Poblar selector de cultivos en calculadora
    const calcCropSelect = document.getElementById("calc-crop");
    if (calcCropSelect && AppState.data.cultivos) {
        calcCropSelect.innerHTML = "";
        Object.keys(AppState.data.cultivos).forEach((cropName) => {
            const option = document.createElement("option");
            option.value = cropName;
            option.textContent = cropName;
            calcCropSelect.appendChild(option);
        });
        // Forzar el cálculo inicial
        calculateFAO56Simulation();
    }

    // 3. Renderizar Inventario de Datos
    renderInventory();

    // 4. Renderizar Árbol de Código interactivo
    const treeContainer = document.getElementById("arch-tree-container");
    if (treeContainer) {
        treeContainer.innerHTML = renderLibraryTree(LIBRARY_STRUCTURE);
    }

    // 5. Renderizar contenido de Estadísticas (Reporte Fase 3)
    const estContentDiv = document.getElementById("estadisticas-content");
    if (estContentDiv && AppState.data.reporte_est) {
        // Encontrar el índice de la sección "= Metodología"
        const methodologyIndex = AppState.data.reporte_est.findIndex(sec => 
            sec.title.toLowerCase().trim() === "metodología"
        );
        
        let filteredSections = [];
        if (methodologyIndex !== -1) {
            // Tomar todas las secciones a partir de Metodología
            filteredSections = AppState.data.reporte_est.slice(methodologyIndex);
        } else {
            // Fallback por si acaso cambia el título
            filteredSections = AppState.data.reporte_est.filter(sec => {
                const title = sec.title.toLowerCase();
                return !title.includes("diagnóstico") &&
                       !title.includes("déficit") &&
                       !title.includes("presión") &&
                       !title.includes("especificaciones") &&
                       !title.includes("tecnificación") &&
                       !title.includes("vulnerabilidad") &&
                       !title.includes("sequía") &&
                       !title.includes("temperatura") &&
                       !title.includes("lluvia") &&
                       !title.includes("clima") &&
                       !title.includes("estrés") &&
                       !title.includes("concesión");
            });
        }
        estContentDiv.innerHTML = renderReportSectionsHTML(filteredSections);
    }

    // 6. Poblar indicadores de sequía en el dashboard de diagnóstico hídrico
    if (AppState.data && AppState.data.resumen_sequia) {
        const rs = AppState.data.resumen_sequia;
        const freqEl = document.getElementById("stat-drought-freq");
        const defEl = document.getElementById("stat-max-deficit");
        const munEl = document.getElementById("stat-max-deficit-mun");
        const fracEl = document.getElementById("stat-frac-azul");

        if (freqEl) freqEl.textContent = `${rs.frecuencia_sequia_estatal_pct.toFixed(2)}%`;
        if (defEl) defEl.textContent = `${rs.max_deficit_mm.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})} mm`;
        if (munEl) munEl.textContent = rs.municipio_mayor_deficit;
        if (fracEl) fracEl.textContent = `${rs.frac_azul_estatal_pct.toFixed(2)}%`;
    }

    // 7. Ejecutar KaTeX sobre todos los contenedores cargados
    renderKaTeXOnPage();

    // 7. Colorear bloques de código con Highlight.js
    if (typeof hljs !== "undefined") {
        document.querySelectorAll("pre code").forEach((el) => {
            hljs.highlightElement(el);
        });
    }
}

// --- Renderizador de Reportes en HTML ---
function renderReportSectionsHTML(sections) {
    let html = "";
    sections.forEach((sec) => {
        const headingTag = `h${sec.level + 1}`; // Nivel 1 = h2, Nivel 2 = h3
        html += `<${headingTag}>${sec.title}</${headingTag}>`;

        let inList = false;
        let isOrdered = false;

        sec.blocks.forEach((block) => {
            if (block.type === "list-item") {
                if (!inList) {
                    const isNum = /^\d+\.\s+/.test(block.content) || /^\d+\.\s*<strong/.test(block.content);
                    isOrdered = isNum;
                    const listClass = isOrdered ? "list-premium ordered" : "list-premium";
                    html += `<ul class="${listClass}">`;
                    inList = true;
                }
                const liStyle = isOrdered ? ' style="padding-left: 0;"' : '';
                html += `<li${liStyle}>${block.content}</li>`;
            } else {
                if (inList) {
                    html += `</ul>`;
                    inList = false;
                }

                if (block.type === "paragraph") {
                    html += `<p>${block.content}</p>`;
                } else if (block.type === "math-block") {
                    html += `<div class="math-block" data-expr="${block.content}"></div>`;
                } else if (block.type === "code") {
                    html += `<pre><code class="language-${block.lang}">${escapeHTML(block.content)}</code></pre>`;
                } else if (block.type === "html" || block.type === "table") {
                    html += block.content;
                }
            }
        });
        if (inList) {
            html += `</ul>`;
        }
    });
    return html;
}

// Renderiza KaTeX de forma dinámica y segura
function renderKaTeXOnPage() {
    if (typeof katex === "undefined") return;

    // Ecuaciones de bloque
    document.querySelectorAll(".math-block").forEach((el) => {
        const expr = el.dataset.expr;
        if (expr) {
            try {
                katex.render(expr, el, { displayMode: true, throwOnError: false });
            } catch (err) {
                el.textContent = expr;
            }
        }
    });

    // Ecuaciones inline
    document.querySelectorAll("p, li, td, h2, h3, h4").forEach((el) => {
        let content = el.innerHTML;
        // Capturar cualquier patrón del tipo \( ... \)
        const inlinePattern = /\\\((.*?)\\\)/g;
        if (inlinePattern.test(content)) {
            content = content.replace(inlinePattern, (match, expr) => {
                try {
                    // Decodificar entidades HTML comunes que rompen el compilador de KaTeX
                    const decodedExpr = expr
                        .replace(/&lt;/g, "<")
                        .replace(/&gt;/g, ">")
                        .replace(/&amp;/g, "&");
                    return katex.renderToString(decodedExpr, {
                        displayMode: false,
                        throwOnError: false,
                    });
                } catch (err) {
                    return expr;
                }
            });
            el.innerHTML = content;
        }
    });
}

// --- Renderizador de Árbol de Código ---
function renderLibraryTree(node) {
    if (node.type === "file") {
        return `<div class="arch-node"><i class="fa-regular fa-file-code" style="color:var(--accent-blue)"></i> <span class="arch-file" title="${node.desc}">${node.name}</span> <span style="font-size:0.8rem;color:var(--text-secondary)">— ${node.desc}</span></div>`;
    }

    let html = `<div class="arch-node">
    <i class="fa-solid fa-folder-open" style="color:var(--accent-green)"></i> <span class="arch-dir">${node.name}/</span>`;

    if (node.children) {
        node.children.forEach((child) => {
            html += renderLibraryTree(child);
        });
    }
    html += `</div>`;
    return html;
}

// --- Renderizador de Inventario ---
function renderInventory() {
    const rawContainer = document.getElementById("raw-inventory-cards");
    const processedContainer = document.getElementById("processed-inventory-cards");

    if (rawContainer) {
        rawContainer.innerHTML = DATA_INVENTORY.raw
            .map(
                (file) => `
      <div class="card">
        <span class="card-tag tag-raw">${file.tag}</span>
        <div class="card-title">${file.name}</div>
        <p style="font-size:0.9rem;margin-bottom:0.5rem;flex-grow:1;">${file.desc}</p>
        <span style="font-size:0.8rem;color:var(--accent-orange)"><i class="fa-solid fa-hard-drive"></i> Peso: ${file.size}</span>
      </div>
    `
            )
            .join("");
    }

    if (processedContainer) {
        processedContainer.innerHTML = DATA_INVENTORY.processed
            .map(
                (file) => `
      <div class="card">
        <span class="card-tag tag-processed">${file.tag}</span>
        <div class="card-title">${file.name}</div>
        <p style="font-size:0.9rem;margin-bottom:0.5rem;flex-grow:1;">${file.desc}</p>
        <span style="font-size:0.8rem;color:var(--accent-blue)"><i class="fa-solid fa-file-csv"></i> Peso: ${file.size}</span>
      </div>
    `
            )
            .join("");
    }
}

// --- Calculadora FAO-56 Penman-Monteith (Simulación) ---
function setupCalculatorListeners() {
    const inputs = [
        "calc-tmax",
        "calc-tmin",
        "calc-rh",
        "calc-u2",
        "calc-rs",
        "calc-precip",
        "calc-rend",
    ];
    inputs.forEach((id) => {
        const el = document.getElementById(id);
        if (el) el.addEventListener("input", calculateFAO56Simulation);
    });

    const select = document.getElementById("calc-crop");
    if (select)
        select.addEventListener("change", (e) => {
            // Al cambiar de cultivo, actualizar rendimientos por defecto del catálogo
            const cropName = e.target.value;
            if (
                AppState.data &&
                AppState.data.cultivos &&
                AppState.data.cultivos[cropName]
            ) {
                // Intentar actualizar rendimiento por defecto o duraciones
                const config = AppState.data.cultivos[cropName];
                console.log(`Cultivo seleccionado: ${cropName}`, config);
            }
            calculateFAO56Simulation();
        });
}

function calculateFAO56Simulation() {
    const tmax = parseFloat(document.getElementById("calc-tmax").value) || 25.0;
    const tmin = parseFloat(document.getElementById("calc-tmin").value) || 12.0;
    const rh = parseFloat(document.getElementById("calc-rh").value) || 50.0;
    const u2 = parseFloat(document.getElementById("calc-u2").value) || 2.0;
    const rs = parseFloat(document.getElementById("calc-rs").value) || 20.0;
    const precip = parseFloat(document.getElementById("calc-precip").value) || 0.0;
    const rend = parseFloat(document.getElementById("calc-rend").value) || 1.0;

    const cropName = document.getElementById("calc-crop").value;
    let kc_ini = 0.3,
        kc_mid = 1.15,
        kc_end = 0.25;
    let dur_total = 180; // duración promedio por defecto

    if (AppState.data && AppState.data.cultivos && AppState.data.cultivos[cropName]) {
        const info = AppState.data.cultivos[cropName];
        kc_ini = parseFloat(info.kc.ini) || kc_ini;
        kc_mid = parseFloat(info.kc.mid) || kc_mid;
        kc_end = parseFloat(info.kc.end) || kc_end;
        if (info.durations) {
            dur_total = info.durations.reduce((a, b) => parseInt(a) + parseInt(b), 0);
        }
    }

    // --- Ecuación de Penman-Monteith (FAO-56 simplificada para promedio diario) ---
    const z = 100; // altitud asumida
    const tmean = (tmax + tmin) / 2;

    // es, ea
    const es_max = 0.6108 * Math.exp((17.27 * tmax) / (tmax + 237.3));
    const es_min = 0.6108 * Math.exp((17.27 * tmin) / (tmin + 237.3));
    const es = (es_max + es_min) / 2;
    const ea = es * (rh / 100);

    // delta
    const delta =
        (4098 * (0.6108 * Math.exp((17.27 * tmean) / (tmean + 237.3)))) /
        Math.pow(tmean + 237.3, 2);

    // P, gamma
    const patm = 101.3 * Math.pow((293 - 0.0065 * z) / 293, 5.26);
    const gamma = 0.000665 * patm;

    // Rns, Rnl, Rn
    const rns = (1 - 0.23) * rs;
    const tmaxk = tmax + 273.16;
    const tmink = tmin + 273.16;
    const t4 = (Math.pow(tmaxk, 4) + Math.pow(tmink, 4)) / 2;
    const rnl = 4.903e-9 * t4 * (0.34 - 0.14 * Math.sqrt(ea)) * 0.7; // fcloud = 0.7 promedio
    const rn = rns - rnl;

    // ETo diario
    const num = 0.408 * delta * rn + gamma * (900 / (tmean + 273)) * u2 * (es - ea);
    const den = delta + gamma * (1 + 0.34 * u2);
    const eto = Math.max(0, num / den);

    // ETc promedio
    const kc_avg = (kc_ini + kc_mid + kc_end) / 3;
    const etc = eto * kc_avg;

    // Consumo acumulado ciclo (en mm)
    const etc_ciclo = etc * dur_total;

    // Precipitación efectiva (método simple FAO)
    const f_pef = precip < 250 ? 0.8 : 0.6;
    const pef = precip * f_pef;

    // Separación verde y azul
    const et_verde = Math.min(etc_ciclo, pef);
    const et_azul = Math.max(0, etc_ciclo - pef);

    // UAC (m3/ha)
    const uac_verde = et_verde * 10;
    const uac_azul = et_azul * 10;

    // Huella Hídrica (m3/ton)
    const hh_verde = uac_verde / rend;
    const hh_azul = uac_azul / rend;
    const hh_total = hh_verde + hh_azul;

    // Actualizar en pantalla
    document.getElementById("res-eto").textContent = `${eto.toFixed(2)} mm/día`;
    document.getElementById("res-etc").textContent =
        `${etc.toFixed(2)} mm/día (Kc avg: ${kc_avg.toFixed(2)})`;
    document.getElementById("res-uac-green").textContent =
        `${Math.round(uac_verde).toLocaleString()} m³/Ha`;
    document.getElementById("res-uac-blue").textContent =
        `${Math.round(uac_azul).toLocaleString()} m³/Ha`;
    document.getElementById("res-hh-green").textContent =
        `${Math.round(hh_verde).toLocaleString()} m³/Ton`;
    document.getElementById("res-hh-blue").textContent =
        `${Math.round(hh_azul).toLocaleString()} m³/Ton`;
    document.getElementById("res-hh-total").textContent =
        `${Math.round(hh_total).toLocaleString()} m³/Ton`;
}

// --- Renderizado de Gráficos (Chart.js) ---
function renderCharts() {
    // Evitar duplicaciones
    if (AppState.charts.efficiency) AppState.charts.efficiency.destroy();
    if (AppState.charts.economic) AppState.charts.economic.destroy();

    // Gráfico 1: Eficiencia Hídrica de Cultivos (Ton / m3)
    const ctxEff = document.getElementById("chart-efficiency").getContext("2d");
    AppState.charts.efficiency = new Chart(ctxEff, {
        type: "bar",
        data: {
            labels: [
                "Col (repollo)",
                "Coliflor",
                "Hortalizas",
                "Caña",
                "Zanahoria",
                "Trigo (grano)",
                "Alfalfa (forrajera)",
                "Frijol",
                "Nuez",
            ],
            datasets: [
                {
                    label: "Eficiencia Hídrica (Ton/m³)",
                    data: [
                        0.0375, 0.0213, 0.0166, 0.0148, 0.0127, 0.0021, 0.0012, 0.00017,
                        0.0001,
                    ],
                    backgroundColor: [
                        "rgba(163, 230, 53, 0.65)",
                        "rgba(163, 230, 53, 0.65)",
                        "rgba(163, 230, 53, 0.65)",
                        "rgba(163, 230, 53, 0.65)",
                        "rgba(163, 230, 53, 0.65)",
                        "rgba(56, 189, 248, 0.65)",
                        "rgba(56, 189, 248, 0.65)",
                        "rgba(251, 146, 60, 0.65)",
                        "rgba(251, 146, 60, 0.65)",
                    ],
                    borderColor: [
                        "#a3e635",
                        "#a3e635",
                        "#a3e635",
                        "#a3e635",
                        "#a3e635",
                        "#38bdf8",
                        "#38bdf8",
                        "#fb923c",
                        "#fb923c",
                    ],
                    borderWidth: 1.5,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: "rgba(156, 163, 175, 0.1)" },
                    ticks: { color: "var(--text-secondary)" },
                },
                x: {
                    grid: { display: false },
                    ticks: { color: "var(--text-secondary)" },
                },
            },
            plugins: {
                legend: { display: false },
            },
        },
    });

    // Gráfico 2: Productividad Económica por DDR
    const ctxEco = document.getElementById("chart-ddr-economic").getContext("2d");
    AppState.charts.economic = new Chart(ctxEco, {
        type: "line",
        data: {
            labels: [
                "Agua Prieta",
                "Caborca",
                "Cajeme",
                "Guaymas",
                "Hermosillo",
                "Magdalena",
                "Navojoa",
            ],
            datasets: [
                {
                    label: "Retorno Hídrico Promedio (MXN/m³)",
                    data: [42.1, 58.5, 74.2, 61.8, 89.4, 95.1, 48.3],
                    backgroundColor: "rgba(56, 189, 248, 0.15)",
                    borderColor: "#38bdf8",
                    borderWidth: 2,
                    tension: 0.35,
                    fill: true,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: "rgba(156, 163, 175, 0.1)" },
                    ticks: { color: "var(--text-secondary)" },
                },
                x: {
                    grid: { display: false },
                    ticks: { color: "var(--text-secondary)" },
                },
            },
            plugins: {
                legend: { display: false },
            },
        },
    });
}

// --- Gestión de Temas Claro/Oscuro ---
function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    AppState.theme = theme;
    localStorage.setItem("theme", theme);

    const icon = document.getElementById("theme-icon");
    const text = document.getElementById("theme-text");

    if (icon && text) {
        if (theme === "light") {
            icon.className = "fa-solid fa-moon";
            text.textContent = "Modo Oscuro";
        } else {
            icon.className = "fa-solid fa-sun";
            text.textContent = "Modo Claro";
        }
    }
}

function toggleTheme() {
    const newTheme = AppState.theme === "dark" ? "light" : "dark";
    setTheme(newTheme);

    // Re-dibujar gráficos si están cargados para actualizar fuentes
    if (AppState.activeSection === "estadisticas") {
        renderCharts();
    }
}

// Auxiliar de escape de HTML
function escapeHTML(str) {
    return str.replace(
        /[&<>'"]/g,
        (tag) =>
            ({
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                "'": "&#39;",
                '"': "&quot;",
            })[tag] || tag
    );
}
