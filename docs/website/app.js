/**
 * app.js - Lógica e interactividad de la SPA de documentación.
 * Controla la carga de datos, el enrutado, los temas, la calculadora FAO-56,
 * y los gráficos interactivos de eficiencia hídrica.
 */

// Estado global de la aplicación
const AppState = {
    data: null,
    dashboardData: null,
    theme: "dark",
    activeSection: "inicio",
    charts: {},
    db: {
        level: "estatal",
        region: "Estatal",
        crop: "",
        analysis: "balance_produccion",
        yearStart: 2010,
        yearEnd: 2024
    },
    tableSort: {
        column: "volumen_produccion",
        direction: "desc"
    }
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

    // Cargar y renderizar según la pestaña activa
    if (hash === "estadisticas") {
        renderCharts();
    } else if (hash === "dashboard") {
        loadDashboard();
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

// --- Lógica de Control e Interactividad del Dashboard ---
function loadDashboard() {
    if (AppState.dashboardData) {
        updateDashboard();
        return;
    }

    const kpiElements = ["kpi-hh-total", "kpi-rendimiento", "kpi-sequia", "kpi-superficie"];
    kpiElements.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.textContent = "Cargando...";
    });

    fetch("dashboard_data.json")
        .then((res) => res.json())
        .then((data) => {
            AppState.dashboardData = data;
            initDashboard();
            updateDashboard();
        })
        .catch((err) => {
            console.error("Error cargando base de datos del dashboard:", err);
            kpiElements.forEach(id => {
                const el = document.getElementById(id);
                if (el) el.textContent = "Error";
            });
        });
}

// Funciones auxiliares para calcular promedios dinámicos en un rango de años
function calculateRangeAverages(hist, yearStart, yearEnd) {
    if (!hist) return null;
    const years = Object.keys(hist).map(Number).filter(y => y >= yearStart && y <= yearEnd);
    if (years.length === 0) return null;

    let sup_cos = 0;
    let vol_prod = 0;
    let vol_agua_total = 0;
    let vol_agua_verde = 0;
    let vol_agua_azul = 0;
    let sum_rend = 0;
    let sum_sequia = 0;
    let sum_ptot = 0;
    let sum_pef = 0;
    let sum_pmr = 0;
    let count = 0;

    years.forEach(yr => {
        const yData = hist[String(yr)];
        if (yData) {
            sup_cos += yData.superficie_cosechada || 0;
            vol_prod += yData.volumen_produccion || 0;
            vol_agua_total += yData.consumo_agua_total || 0;
            
            const hhTotal = yData.hh_total || 0;
            if (hhTotal > 0 && yData.consumo_agua_total) {
                vol_agua_verde += (yData.hh_verde / hhTotal) * yData.consumo_agua_total;
                vol_agua_azul += (yData.hh_azul / hhTotal) * yData.consumo_agua_total;
            }
            
            sum_rend += yData.rendimiento || 0;
            sum_sequia += yData.sequia_isag || 0;
            sum_ptot += yData.ptot_total_mm || 0;
            sum_pef += yData.pef_total_mm || 0;
            sum_pmr += yData.pmr || 0;
            count++;
        }
    });

    if (count === 0) return null;

    const rend = sup_cos > 0 ? vol_prod / sup_cos : sum_rend / count;
    const hh_verde = vol_prod > 0 ? vol_agua_verde / vol_prod : 0;
    const hh_azul = vol_prod > 0 ? vol_agua_azul / vol_prod : 0;
    const hh_total = hh_verde + hh_azul;
    const eficiencia_fisica = hh_total > 0 ? 1.0 / hh_total : 0;
    const pmr = sum_pmr / count;
    const productividad_economica = hh_total > 0 ? pmr / hh_total : 0;
    const uac_total = sup_cos > 0 ? vol_agua_total / sup_cos : 0;

    return {
        rendimiento: rend,
        hh_total: hh_total,
        hh_azul: hh_azul,
        hh_verde: hh_verde,
        uac_total: uac_total,
        eficiencia_fisica: eficiencia_fisica,
        pmr: pmr,
        productividad_economica: productividad_economica,
        consumo_agua_total: vol_agua_total,
        ptot_total_mm: sum_ptot / count,
        pef_total_mm: sum_pef / count,
        sequia_isag: sum_sequia / count,
        superficie_cosechada: sup_cos,
        volumen_produccion: vol_prod
    };
}

function calculateCropsAveragesForRange(data, level, region, yearStart, yearEnd) {
    const regionHist = data.historico_anual[level][region];
    if (!regionHist) return {};

    const averages = {};
    Object.keys(regionHist).forEach(cropName => {
        const cropHist = regionHist[cropName];
        const avg = calculateRangeAverages(cropHist, yearStart, yearEnd);
        if (avg) {
            averages[cropName] = avg;
        }
    });
    return averages;
}

function initDashboard() {
    const data = AppState.dashboardData;
    if (!data) return;

    // 1. Poblar selector de cultivos
    const cropSelect = document.getElementById("db-crop-select");
    if (cropSelect) {
        cropSelect.innerHTML = "";
        data.catalogos.cultivos.forEach((crop) => {
            const option = document.createElement("option");
            option.value = crop;
            option.textContent = crop;
            cropSelect.appendChild(option);
        });

        // Seleccionar trigo por defecto o el primero
        const defaultCrop = data.catalogos.cultivos.includes("Trigo (grano)") ? "Trigo (grano)" : data.catalogos.cultivos[0];
        AppState.db.crop = defaultCrop;
        cropSelect.value = defaultCrop;
    }

    // 2. Event Listeners para Nivel Territorial (Tabs)
    const tabs = document.querySelectorAll("#db-level-tabs .segment-btn");
    tabs.forEach((btn) => {
        btn.addEventListener("click", (e) => {
            tabs.forEach((t) => t.classList.remove("active"));
            e.target.classList.add("active");

            const level = e.target.dataset.level;
            AppState.db.level = level;

            const regionGroup = document.getElementById("db-region-group");
            const regionSelect = document.getElementById("db-region-select");

            if (level === "estatal") {
                if (regionGroup) regionGroup.style.display = "none";
                AppState.db.region = "Estatal";
            } else {
                if (regionGroup) regionGroup.style.display = "flex";

                // Poblar regiones
                if (regionSelect) {
                    regionSelect.innerHTML = "";
                    const list = level === "ddr" ? data.catalogos.ddrs : data.catalogos.municipios;
                    list.forEach((reg) => {
                        const option = document.createElement("option");
                        option.value = reg;
                        option.textContent = reg;
                        regionSelect.appendChild(option);
                    });

                    AppState.db.region = list[0];
                    regionSelect.value = list[0];
                }
            }
            updateDashboard();
        });
    });

    // 3. Listener para select de región
    const regionSelect = document.getElementById("db-region-select");
    if (regionSelect) {
        regionSelect.addEventListener("change", (e) => {
            AppState.db.region = e.target.value;
            updateDashboard();
        });
    }

    // 4. Listener para select de cultivo
    const cropSelectDb = document.getElementById("db-crop-select");
    if (cropSelectDb) {
        cropSelectDb.addEventListener("change", (e) => {
            AppState.db.crop = e.target.value;
            updateDashboard();
        });
    }

    // 5. Listener para select de análisis (Nuevo)
    const analysisSelect = document.getElementById("db-analysis-select");
    if (analysisSelect) {
        analysisSelect.addEventListener("change", (e) => {
            AppState.db.analysis = e.target.value;
            updateDashboard();
        });
    }

    // 6. Poblar selectores de años (Nuevo)
    const yearStartSelect = document.getElementById("db-year-start");
    const yearEndSelect = document.getElementById("db-year-end");
    if (yearStartSelect && yearEndSelect) {
        yearStartSelect.innerHTML = "";
        yearEndSelect.innerHTML = "";
        
        // Años de 2010 a 2024
        for (let y = 2010; y <= 2024; y++) {
            const optStart = document.createElement("option");
            optStart.value = y;
            optStart.textContent = y;
            yearStartSelect.appendChild(optStart);

            const optEnd = document.createElement("option");
            optEnd.value = y;
            optEnd.textContent = y;
            yearEndSelect.appendChild(optEnd);
        }

        AppState.db.yearStart = 2010;
        AppState.db.yearEnd = 2024;
        yearStartSelect.value = 2010;
        yearEndSelect.value = 2024;

        yearStartSelect.addEventListener("change", (e) => {
            const val = parseInt(e.target.value);
            AppState.db.yearStart = val;
            if (AppState.db.yearEnd < val) {
                AppState.db.yearEnd = val;
                yearEndSelect.value = val;
            }
            updateDashboard();
        });

        yearEndSelect.addEventListener("change", (e) => {
            const val = parseInt(e.target.value);
            AppState.db.yearEnd = val;
            if (AppState.db.yearStart > val) {
                AppState.db.yearStart = val;
                yearStartSelect.value = val;
            }
            updateDashboard();
        });
    }
}

function updateDashboard() {
    const data = AppState.dashboardData;
    if (!data) return;

    const level = AppState.db.level;
    const region = AppState.db.region;
    const analysis = AppState.db.analysis || "balance_produccion";
    const yearStart = AppState.db.yearStart || 2010;
    const yearEnd = AppState.db.yearEnd || 2024;

    // --- FILTRAR DINÁMICAMENTE EL SELECTOR DE CULTIVOS CON VALORES VÁLIDOS ---
    const cropSelect = document.getElementById("db-crop-select");
    if (cropSelect) {
        // Encontrar qué cultivos tienen información (consumo o producción > 0) para este nivel, región y rango de años
        const validCrops = ["Todos los cultivos"];
        data.catalogos.cultivos.forEach(c => {
            if (c !== "Todos los cultivos") {
                if (data.historico_anual[level] && data.historico_anual[level][region] && data.historico_anual[level][region][c]) {
                    const cHist = data.historico_anual[level][region][c];
                    const avg = calculateRangeAverages(cHist, yearStart, yearEnd);
                    if (avg && (avg.consumo_agua_total > 0 || avg.volumen_produccion > 0)) {
                        validCrops.push(c);
                    }
                }
            }
        });

        // Regenerar opciones del selector
        const currentSelected = AppState.db.crop;
        cropSelect.innerHTML = "";
        validCrops.forEach(c => {
            const option = document.createElement("option");
            option.value = c;
            option.textContent = c;
            cropSelect.appendChild(option);
        });

        // Mantener la selección si sigue siendo válida; de lo contrario, reajustar a "Todos los cultivos" o al primer elemento válido
        if (validCrops.includes(currentSelected)) {
            cropSelect.value = currentSelected;
            AppState.db.crop = currentSelected;
        } else {
            const fallback = validCrops.includes("Todos los cultivos") ? "Todos los cultivos" : validCrops[0];
            cropSelect.value = fallback;
            AppState.db.crop = fallback;
        }
    }

    const crop = AppState.db.crop;

    // 1. Obtener datos históricos de la combinación activa
    let hist = null;
    if (data.historico_anual[level] && data.historico_anual[level][region]) {
        hist = data.historico_anual[level][region][crop];
    }

    // 2. Calcular promedios del rango de forma dinámica
    let prom = calculateRangeAverages(hist, yearStart, yearEnd);

    // Obtener concesión REPNA para la región
    let repnaConcession = 0.0;
    if (data.concesiones_repna && data.concesiones_repna[level]) {
        repnaConcession = data.concesiones_repna[level][region] || 0.0;
    }

    // Elementos de UI de KPIs
    const k1Title = document.getElementById("kpi-1-title");
    const k1Val = document.getElementById("kpi-hh-total");
    const k1Sub = document.getElementById("kpi-hh-desglose");

    const k2Title = document.getElementById("kpi-2-title");
    const k2Val = document.getElementById("kpi-rendimiento");
    const k2Sub = document.getElementById("kpi-produccion-total");

    const k3Title = document.getElementById("kpi-3-title");
    const k3Val = document.getElementById("kpi-sequia");
    const k3Sub = document.getElementById("kpi-sequia-desc");

    const k4Title = document.getElementById("kpi-4-title");
    const k4Val = document.getElementById("kpi-superficie");
    const k4Sub = document.getElementById("kpi-4-sub");

    const isAllCrops = crop === "Todos los cultivos";

    if (prom) {
        // --- ACTUALIZAR KPIS DINÁMICAMENTE SEGÚN EL ANÁLISIS ---
        if (analysis === "balance_produccion") {
            k1Title.textContent = "Huella Hídrica Total";
            k1Val.textContent = `${Math.round(prom.hh_total).toLocaleString()} m³/Ton`;
            const pctVerde = prom.hh_total > 0 ? Math.round((prom.hh_verde / prom.hh_total) * 100) : 0;
            const pctAzul = prom.hh_total > 0 ? Math.round((prom.hh_azul / prom.hh_total) * 100) : 0;
            k1Sub.textContent = `Verde: ${pctVerde}% | Azul: ${pctAzul}%`;

            k2Title.textContent = "Rendimiento Promedio";
            k2Val.textContent = isAllCrops ? "Multi-cultivo" : `${prom.rendimiento.toFixed(2)} Ton/Ha`;
            k2Sub.textContent = `Producción: ${Math.round(prom.volumen_produccion).toLocaleString()} Ton`;

            k3Title.textContent = "Estrés por Sequía (ISAG)";
            k3Val.textContent = prom.sequia_isag.toFixed(2);
            let seqDescText = "Sin Estrés / Leve";
            if (prom.sequia_isag > 3.0) seqDescText = "Severa a Extrema";
            else if (prom.sequia_isag > 1.8) seqDescText = "Moderada";
            k3Sub.textContent = seqDescText;

            k4Title.textContent = "Superficie Cosechada";
            k4Val.textContent = `${Math.round(prom.superficie_cosechada).toLocaleString()} Ha`;
            k4Sub.textContent = "Total acumulado en el ciclo";

        } else if (analysis === "agua_concesiones") {
            k1Title.textContent = "Consumo Hídrico Total";
            k1Val.textContent = `${(prom.consumo_agua_total / 1e6).toFixed(2)} Mm³`;
            k1Sub.textContent = "Demanda agrícola estimada";

            k2Title.textContent = "Concesión Hídrica (REPNA)";
            k2Val.textContent = repnaConcession > 0 ? `${(repnaConcession / 1e6).toFixed(2)} Mm³` : "Sin Límite Legal";
            k2Sub.textContent = "Derechos de extracción Conagua";

            k3Title.textContent = "Precipitación Promedio";
            k3Val.textContent = `${Math.round(prom.ptot_total_mm)} mm`;
            k3Sub.textContent = `Lluvia Efectiva: ${Math.round(prom.pef_total_mm)} mm`;

            k4Title.textContent = "Presión de Extracción";
            if (repnaConcession > 0) {
                // BUG FIX: Dividir el consumo total acumulado entre el número de años para obtener el promedio anual vs la concesión anual.
                const numYears = Math.max(1, yearEnd - yearStart + 1);
                const avgConsumoAnual = prom.consumo_agua_total / numYears;
                const pctPresion = (avgConsumoAnual / repnaConcession) * 100;
                k4Val.textContent = `${pctPresion.toFixed(1)}%`;
                k4Sub.textContent = "Consumo Anual vs Concesión";
            } else {
                k4Val.textContent = "0.0%";
                k4Sub.textContent = "Sin concesiones registradas";
            }

        } else if (analysis === "eficiencia_fisica_economica") {
            k1Title.textContent = "Eficiencia Física";
            k1Val.textContent = `${prom.eficiencia_fisica.toFixed(5)} Ton/m³`;
            k1Sub.textContent = "Masa producida por m³";

            k2Title.textContent = "Productividad Económica";
            k2Val.textContent = `$${prom.productividad_economica.toFixed(2)} MXN/m³`;
            k2Sub.textContent = "Retorno bruto del recurso";

            k3Title.textContent = "Precio Medio Rural (PMR)";
            k3Val.textContent = `$${Math.round(prom.pmr).toLocaleString()} MXN`;
            k3Sub.textContent = "Precio de mercado por Ton";

            k4Title.textContent = "Consumo Hídrico Acumulado";
            k4Val.textContent = `${(prom.consumo_agua_total / 1e6).toFixed(2)} Mm³`;
            k4Sub.textContent = "Agua transpirada/evaporada";
        }
    } else {
        k1Val.textContent = "--";
        k2Val.textContent = "--";
        k3Val.textContent = "--";
        k4Val.textContent = "--";
    }

    // --- RENDERIZAR GRÁFICOS Y TABLA ---
    renderChartsByAnalysis(data, level, region, crop, hist, prom, repnaConcession, analysis, isAllCrops, yearStart, yearEnd);

    // Tabla dinámica detallada (solo para "Todos los cultivos")
    if (isAllCrops) {
        renderDataTable(data, level, region, analysis, yearStart, yearEnd);
    } else {
        const tableContainer = document.getElementById("db-table-container");
        if (tableContainer) tableContainer.style.display = "none";
    }
}

function renderChartsByAnalysis(data, level, region, crop, hist, prom, repnaConcession, analysis, isAllCrops, yearStart, yearEnd) {
    const canvasA = document.getElementById("chart-db-history");
    const canvasA2 = document.getElementById("chart-db-history-secondary");
    const canvasB = document.getElementById("chart-db-compare");
    const canvasB2 = document.getElementById("chart-db-compare-secondary");
    const titleA = document.getElementById("chart-a-title");
    const titleA2 = document.getElementById("chart-a2-title");
    const titleB = document.getElementById("chart-b-title");
    const titleB2 = document.getElementById("chart-b2-title");
    const containerA2 = document.getElementById("db-chart-a2-container");
    const containerB2 = document.getElementById("db-chart-b2-container");

    if (!canvasA || !canvasB || !canvasB2) return;

    // Resetear altura del parent de canvasB y canvasB2 por defecto
    canvasB.parentElement.style.height = "350px";
    canvasB2.parentElement.style.height = "350px";

    if (AppState.charts.history) AppState.charts.history.destroy();
    if (AppState.charts.historySecondary) AppState.charts.historySecondary.destroy();
    if (AppState.charts.compare) AppState.charts.compare.destroy();
    if (AppState.charts.compareSecondary) AppState.charts.compareSecondary.destroy();

    // Ocultar por defecto los contenedores de las segundas gráficas
    if (containerA2) containerA2.style.display = "none";
    if (containerB2) containerB2.style.display = "none";

    const isDark = document.documentElement.getAttribute("data-theme") !== "light";
    const textColor = isDark ? "#9ca3af" : "#4b5563";
    const gridColor = isDark ? "rgba(156, 163, 175, 0.1)" : "rgba(75, 85, 99, 0.1)";

    // 1. Extraer años comunes en el rango seleccionado
    const years = [];
    if (hist) {
        Object.keys(hist).sort((a, b) => parseInt(a) - parseInt(b)).forEach(yr => {
            const yNum = parseInt(yr);
            if (yNum >= yearStart && yNum <= yearEnd) {
                years.push(yr);
            }
        });
    }

    if (years.length === 0) {
        // Gráficos vacíos si no hay historial para el rango
        const emptyConfig = { type: 'bar', data: { labels: ["Sin Datos en el Rango"] }, options: { plugins: { legend: { display: false } } } };
        AppState.charts.history = new Chart(canvasA.getContext("2d"), emptyConfig);
        AppState.charts.compare = new Chart(canvasB.getContext("2d"), emptyConfig);
        return;
    }

    // Calcular promedios del rango para todos los cultivos (utilizado para el gráfico comparativo B)
    const regionCropsAverages = calculateCropsAveragesForRange(data, level, region, yearStart, yearEnd);

    // --- OPCIÓN 1: BALANCE E HISTÓRICO DE PRODUCCIÓN ---
    if (analysis === "balance_produccion") {
        if (containerA2) containerA2.style.display = "block";

        titleA.textContent = isAllCrops
            ? `Histórico de Consumo de Agua en ${region} (${yearStart}-${yearEnd})`
            : `Evolución de la Huella Hídrica de ${crop} en ${region} (${yearStart}-${yearEnd})`;

        titleA2.textContent = isAllCrops
            ? `Histórico de Producción en ${region} (${yearStart}-${yearEnd})`
            : `Evolución del Rendimiento de ${crop} en ${region} (${yearStart}-${yearEnd})`;

        titleB.textContent = `Eficiencia Hídrica por Cultivo en ${region} (Promedio ${yearStart}-${yearEnd})`;

        const hhVerde = [];
        const hhAzul = [];
        const rend = [];

        years.forEach(yr => {
            if (isAllCrops) {
                hhVerde.push(hist[yr].hh_verde * hist[yr].volumen_produccion);
                hhAzul.push(hist[yr].hh_azul * hist[yr].volumen_produccion);
                rend.push(hist[yr].volumen_produccion);
            } else {
                hhVerde.push(hist[yr].hh_verde);
                hhAzul.push(hist[yr].hh_azul);
                rend.push(hist[yr].rendimiento);
            }
        });

        // Gráfico A (Consumo de Agua / Huella Hídrica)
        AppState.charts.history = new Chart(canvasA.getContext("2d"), {
            type: "bar",
            data: {
                labels: years,
                datasets: [
                    {
                        label: isAllCrops ? "Consumo Verde (Lluvia m³)" : "HH Verde (Lluvia)",
                        data: hhVerde,
                        backgroundColor: "rgba(163, 230, 53, 0.65)",
                        borderColor: "#a3e635",
                        borderWidth: 1.5,
                        stack: "agua"
                    },
                    {
                        label: isAllCrops ? "Consumo Azul (Riego m³)" : "HH Azul (Riego)",
                        data: hhAzul,
                        backgroundColor: "rgba(56, 189, 248, 0.65)",
                        borderColor: "#38bdf8",
                        borderWidth: 1.5,
                        stack: "agua"
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { grid: { display: false }, ticks: { color: textColor } },
                    y: {
                        stacked: true,
                        title: { display: true, text: isAllCrops ? "Consumo de Agua (m³)" : "Huella Hídrica (m³/Ton)", color: textColor },
                        grid: { color: gridColor }, ticks: { color: textColor }
                    }
                },
                plugins: { legend: { labels: { color: textColor } } }
            }
        });

        // Gráfico A2 (Producción / Rendimiento)
        AppState.charts.historySecondary = new Chart(canvasA2.getContext("2d"), {
            type: "line",
            data: {
                labels: years,
                datasets: [
                    {
                        label: isAllCrops ? "Producción Total (Ton)" : "Rendimiento (Ton/Ha)",
                        data: rend,
                        borderColor: "#fb923c",
                        backgroundColor: "rgba(251, 146, 60, 0.15)",
                        borderWidth: 3,
                        tension: 0.35,
                        fill: true
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { grid: { display: false }, ticks: { color: textColor } },
                    y: {
                        title: { display: true, text: isAllCrops ? "Producción (Ton)" : "Rendimiento (Ton/Ha)", color: textColor },
                        grid: { color: gridColor }, ticks: { color: textColor }
                    }
                },
                plugins: { legend: { labels: { color: textColor } } }
            }
        });

        // Gráfico B (Comparación)
        const cropsList = [];
        Object.keys(regionCropsAverages).forEach(c => {
            if (c !== "Todos los cultivos") {
                const hhT = regionCropsAverages[c].hh_total || 0;
                if (hhT > 0) {
                    cropsList.push({ 
                        name: c, 
                        hh_verde: regionCropsAverages[c].hh_verde, 
                        hh_azul: regionCropsAverages[c].hh_azul, 
                        hh_total: hhT 
                    });
                }
            }
        });
        cropsList.sort((a, b) => a.hh_total - b.hh_total);

        const names = cropsList.map(c => c.name);
        const verde = cropsList.map(c => c.hh_verde);
        const azul = cropsList.map(c => c.hh_azul);

        const bgVerde = names.map(n => n === crop ? "rgba(163, 230, 53, 0.95)" : "rgba(163, 230, 53, 0.5)");
        const bgAzul = names.map(n => n === crop ? "rgba(56, 189, 248, 0.95)" : "rgba(56, 189, 248, 0.5)");

        // Ajustar altura dinámica del contenedor basado en la cantidad de cultivos
        const numCrops = names.length;
        const dynamicHeight = Math.max(350, numCrops * 35 + 50);
        canvasB.parentElement.style.height = `${dynamicHeight}px`;

        AppState.charts.compare = new Chart(canvasB.getContext("2d"), {
            type: "bar",
            data: {
                labels: names,
                datasets: [
                    { label: "HH Verde (Lluvia)", data: verde, backgroundColor: bgVerde, borderColor: "#a3e635", borderWidth: 1 },
                    { label: "HH Azul (Riego)", data: azul, backgroundColor: bgAzul, borderColor: "#38bdf8", borderWidth: 1 }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: "y",
                scales: {
                    x: { stacked: true, grid: { color: gridColor }, ticks: { color: textColor }, title: { display: true, text: "Huella Hídrica Total (m³/Ton)", color: textColor } },
                    y: { stacked: true, grid: { display: false }, ticks: { color: textColor } }
                },
                plugins: { legend: { labels: { color: textColor } } }
            }
        });

    // --- OPCIÓN 2: DISPONIBILIDAD DE AGUA Y CONCESIONES (REPNA) ---
    } else if (analysis === "agua_concesiones") {
        titleA.textContent = `Consumo de Agua vs. Oferta en ${region} (${yearStart}-${yearEnd})`;
        titleB.textContent = `Desglose de Consumo Hídrico en ${region} (Promedio ${yearStart}-${yearEnd})`;

        const consumoAgua = [];
        const precipRegion = [];
        const concesionRepnaLine = [];

        years.forEach(yr => {
            const cAgua = hist[yr].consumo_agua_total;
            consumoAgua.push(cAgua);

            // Precipitación regional estimada en m3: lluvia (mm) * superficie cosechada (ha) * 10 (conversión a m3)
            const pMm = hist[yr].ptot_total_mm;
            const supHa = hist[yr].superficie_cosechada;
            precipRegion.push(pMm * supHa * 10.0);
            
            concesionRepnaLine.push(repnaConcession);
        });

        // Gráfico A (Consumo vs Oferta y Concesiones)
        AppState.charts.history = new Chart(canvasA.getContext("2d"), {
            type: "bar",
            data: {
                labels: years,
                datasets: [
                    {
                        label: "Consumo Hídrico de Cultivos (m³)",
                        data: consumoAgua,
                        backgroundColor: "rgba(56, 189, 248, 0.75)",
                        borderColor: "#38bdf8",
                        borderWidth: 1.5,
                        yAxisID: "y"
                    },
                    {
                        label: "Precipitación Equivalente Recibida (m³)",
                        data: precipRegion,
                        type: "line",
                        borderColor: "rgba(34, 197, 94, 0.8)",
                        backgroundColor: "transparent",
                        borderWidth: 2,
                        yAxisID: "y",
                        fill: false
                    },
                    {
                        label: "Límite de Concesión Conagua (REPNA m³)",
                        data: concesionRepnaLine,
                        type: "line",
                        borderColor: "rgba(239, 68, 68, 0.95)",
                        backgroundColor: "transparent",
                        borderWidth: 2.5,
                        borderDash: [6, 4],
                        pointStyle: 'none',
                        pointRadius: 0,
                        yAxisID: "y",
                        fill: false
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { grid: { display: false }, ticks: { color: textColor } },
                    y: {
                        type: "linear",
                        title: { display: true, text: "Volumen de Agua (m³)", color: textColor },
                        grid: { color: gridColor }, ticks: { color: textColor }
                    }
                },
                plugins: { legend: { labels: { color: textColor } } }
            }
        });

        // Gráfico B (Consumo por tipo en promedio de cultivos)
        const cropsList = [];
        Object.keys(regionCropsAverages).forEach(c => {
            if (c !== "Todos los cultivos") {
                const cons = regionCropsAverages[c].consumo_agua_total || 0;
                if (cons > 0) {
                    cropsList.push({
                        name: c,
                        consumo: cons
                    });
                }
            }
        });
        cropsList.sort((a, b) => b.consumo - a.consumo);

        const names = cropsList.map(c => c.name);
        const consumos = cropsList.map(c => c.consumo / 1e6); // En Mm3

        // Ajustar altura dinámica del contenedor basado en la cantidad de cultivos
        const numCrops = names.length;
        const dynamicHeight = Math.max(350, numCrops * 35 + 50);
        canvasB.parentElement.style.height = `${dynamicHeight}px`;

        AppState.charts.compare = new Chart(canvasB.getContext("2d"), {
            type: "bar",
            data: {
                labels: names,
                datasets: [
                    {
                        label: "Consumo Hídrico Estimado (Mm³)",
                        data: consumos,
                        backgroundColor: names.map(n => n === crop ? "rgba(251, 146, 60, 0.95)" : "rgba(107, 114, 128, 0.6)"),
                        borderColor: names.map(n => n === crop ? "#fb923c" : "#6b7280"),
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: "y",
                scales: {
                    x: { grid: { color: gridColor }, ticks: { color: textColor }, title: { display: true, text: "Volumen de Agua Acumulado (Mm³)", color: textColor } },
                    y: { grid: { display: false }, ticks: { color: textColor } }
                },
                plugins: { legend: { display: false } }
            }
        });

    // --- OPCIÓN 3: EFICIENCIA FÍSICA Y PRODUCTIVIDAD ---
    } else if (analysis === "eficiencia_fisica_economica") {
        titleA.textContent = `Evolución de la Eficiencia Física de ${isAllCrops ? "Cultivos" : crop} en ${region} (${yearStart}-${yearEnd})`;
        titleB.textContent = `Eficiencia Física vs. Productividad del Agua (Promedio ${yearStart}-${yearEnd})`;

        const efFisica = [];
        const prodEcon = [];

        years.forEach(yr => {
            efFisica.push(hist[yr].eficiencia_fisica);
            prodEcon.push(hist[yr].productividad_economica);
        });

        // Gráfico A (Evolución de Eficiencia Física)
        AppState.charts.history = new Chart(canvasA.getContext("2d"), {
            type: "line",
            data: {
                labels: years,
                datasets: [
                    {
                        label: "Eficiencia Física (Ton/m³)",
                        data: efFisica,
                        borderColor: "#3b82f6",
                        backgroundColor: "rgba(59, 130, 246, 0.1)",
                        borderWidth: 3,
                        yAxisID: "y"
                    },
                    {
                        label: "Productividad Económica (MXN/m³)",
                        data: prodEcon,
                        borderColor: "#10b981",
                        backgroundColor: "rgba(16, 185, 129, 0.1)",
                        borderWidth: 3,
                        yAxisID: "y2"
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { grid: { display: false }, ticks: { color: textColor } },
                    y: {
                        position: "left",
                        title: { display: true, text: "Eficiencia Física (Ton/m³)", color: textColor },
                        grid: { color: gridColor }, ticks: { color: textColor }
                    },
                    y2: {
                        position: "right",
                        title: { display: true, text: "Productividad Económica (MXN/m³)", color: textColor },
                        grid: { drawOnChartArea: false }, ticks: { color: textColor }
                    }
                },
                plugins: { legend: { labels: { color: textColor } } }
            }
        });

        // Gráfico B (Líderes y Menos Eficientes en barras horizontales)
        const cropsList = [];
        Object.keys(regionCropsAverages).forEach(c => {
            if (c !== "Todos los cultivos") {
                const efF = regionCropsAverages[c].eficiencia_fisica || 0;
                if (efF > 0) {
                    cropsList.push({
                        name: c,
                        ef_fisica: efF
                    });
                }
            }
        });
        cropsList.sort((a, b) => b.ef_fisica - a.ef_fisica);

        const names = cropsList.map(c => c.name);
        const efs = cropsList.map(c => c.ef_fisica);

        // Mapear colores: top 3 en verde fuerte, peores 3 en rojo/naranja, intermedios en azul/gris
        const count = names.length;
        const colors = names.map((n, idx) => {
            if (n === crop) return "rgba(59, 130, 246, 0.95)"; // Selección activa en azul brillante
            if (idx < 3) return "rgba(34, 197, 94, 0.75)"; // Líderes en verde
            if (idx >= count - 3 && count > 3) return "rgba(239, 68, 68, 0.75)"; // Menos eficientes en rojo
            return isDark ? "rgba(75, 85, 99, 0.5)" : "rgba(209, 213, 219, 0.7)"; // Intermedios
        });

        // Ajustar altura dinámica del contenedor basado en la cantidad de cultivos
        const numCrops = names.length;
        const dynamicHeight = Math.max(350, numCrops * 35 + 50);
        canvasB.parentElement.style.height = `${dynamicHeight}px`;

        AppState.charts.compare = new Chart(canvasB.getContext("2d"), {
            type: "bar",
            data: {
                labels: names,
                datasets: [
                    {
                        label: "Eficiencia Física (Ton/m³)",
                        data: efs,
                        backgroundColor: colors,
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: "y",
                scales: {
                    x: { grid: { color: gridColor }, ticks: { color: textColor }, title: { display: true, text: "Eficiencia Física (Ton/m³)", color: textColor } },
                    y: { grid: { display: false }, ticks: { color: textColor } }
                },
                plugins: {
                    legend: { display: false }
                }
            }
        });

        // Segundo gráfico de comparación: Productividad Económica ($/m3)
        if (containerB2) containerB2.style.display = "block";
        titleB2.textContent = `Productividad Económica por Cultivo en ${region} (Promedio ${yearStart}-${yearEnd})`;

        const cropsListEcon = [];
        Object.keys(regionCropsAverages).forEach(c => {
            if (c !== "Todos los cultivos") {
                const prodEc = regionCropsAverages[c].productividad_economica || 0;
                if (prodEc > 0) {
                    cropsListEcon.push({
                        name: c,
                        prod_econ: prodEc
                    });
                }
            }
        });
        cropsListEcon.sort((a, b) => b.prod_econ - a.prod_econ);

        const namesEcon = cropsListEcon.map(c => c.name);
        const ecs = cropsListEcon.map(c => c.prod_econ);

        const countEcon = namesEcon.length;
        const colorsEcon = namesEcon.map((n, idx) => {
            if (n === crop) return "rgba(59, 130, 246, 0.95)";
            if (idx < 3) return "rgba(34, 197, 94, 0.75)";
            if (idx >= countEcon - 3 && countEcon > 3) return "rgba(239, 68, 68, 0.75)";
            return isDark ? "rgba(75, 85, 99, 0.5)" : "rgba(209, 213, 219, 0.7)";
        });

        // Ajustar altura dinámica
        const numCropsEcon = namesEcon.length;
        const dynamicHeightEcon = Math.max(350, numCropsEcon * 35 + 50);
        canvasB2.parentElement.style.height = `${dynamicHeightEcon}px`;

        AppState.charts.compareSecondary = new Chart(canvasB2.getContext("2d"), {
            type: "bar",
            data: {
                labels: namesEcon,
                datasets: [
                    {
                        label: "Productividad Económica (MXN/m³)",
                        data: ecs,
                        backgroundColor: colorsEcon,
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: "y",
                scales: {
                    x: { grid: { color: gridColor }, ticks: { color: textColor }, title: { display: true, text: "Productividad Económica (MXN/m³)", color: textColor } },
                    y: { grid: { display: false }, ticks: { color: textColor } }
                },
                plugins: {
                    legend: { display: false }
                }
            }
        });

        // --- AGREGAR GRÁFICA HISTÓRICA SECUNDARIA EN EFICIENCIA HÍDRICA (PMR VS EFICIENCIA) ---
        if (containerA2) containerA2.style.display = "block";
        titleA2.textContent = `Rentabilidad (PMR) vs. Eficiencia Física Histórica de ${isAllCrops ? "Cultivos" : crop} en ${region}`;

        const pmrSeries = [];
        const efFisicaHist = [];
        years.forEach(yr => {
            pmrSeries.push(hist[yr].pmr || 0);
            efFisicaHist.push(hist[yr].eficiencia_fisica || 0);
        });

        AppState.charts.historySecondary = new Chart(canvasA2.getContext("2d"), {
            type: "line",
            data: {
                labels: years,
                datasets: [
                    {
                        label: "Precio Medio Rural (MXN/Ton)",
                        data: pmrSeries,
                        borderColor: "#fb923c",
                        backgroundColor: "rgba(251, 146, 60, 0.1)",
                        borderWidth: 3,
                        yAxisID: "y",
                        tension: 0.3
                    },
                    {
                        label: "Eficiencia Física (Ton/m³)",
                        data: efFisicaHist,
                        borderColor: "#3b82f6",
                        backgroundColor: "rgba(59, 130, 246, 0.1)",
                        borderWidth: 3,
                        yAxisID: "y2",
                        tension: 0.3
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { grid: { display: false }, ticks: { color: textColor } },
                    y: {
                        position: "left",
                        title: { display: true, text: "Precio Medio Rural ($/Ton)", color: textColor },
                        grid: { color: gridColor }, ticks: { color: textColor }
                    },
                    y2: {
                        position: "right",
                        title: { display: true, text: "Eficiencia Física (Ton/m³)", color: textColor },
                        grid: { drawOnChartArea: false }, ticks: { color: textColor }
                    }
                },
                plugins: { legend: { labels: { color: textColor } } }
            }
        });
    }
}

function renderDataTable(data, level, region, analysis, yearStart, yearEnd) {
    const tableContainer = document.getElementById("db-table-container");
    const tableHeader = document.getElementById("db-table-header");
    const tableBody = document.getElementById("db-table-body");
    const tableTitle = document.getElementById("db-table-title");

    if (!tableContainer || !tableHeader || !tableBody || !tableTitle) return;

    // Calcular promedios del rango de forma dinámica para todos los cultivos en la región activa
    const regionData = calculateCropsAveragesForRange(data, level, region, yearStart, yearEnd);
    if (!regionData || Object.keys(regionData).length === 0) {
        tableContainer.style.display = "none";
        return;
    }

    tableContainer.style.display = "block";
    tableTitle.textContent = `Resultados Detallados de Cultivos en ${region} (Promedio ${yearStart}-${yearEnd})`;

    // Adjuntar event listener de ordenación una sola vez usando delegación de eventos
    if (!tableHeader.dataset.sortEventAttached) {
        tableHeader.addEventListener("click", (e) => {
            const th = e.target.closest("th.sortable");
            if (!th) return;
            const col = th.dataset.col;
            if (AppState.tableSort.column === col) {
                AppState.tableSort.direction = AppState.tableSort.direction === 'asc' ? 'desc' : 'asc';
            } else {
                AppState.tableSort.column = col;
                AppState.tableSort.direction = 'desc';
            }
            updateDashboard();
        });
        tableHeader.dataset.sortEventAttached = "true";
    }

    // Helper para retornar la flechita de ordenación activa
    function getSortIcon(col) {
        if (AppState.tableSort.column === col) {
            return AppState.tableSort.direction === 'asc' ? ' ▲' : ' ▼';
        }
        return ' ↕';
    }

    // Generar cabeceras con cursor e identificador de ordenación
    tableHeader.innerHTML = `
        <tr>
            <th class="sortable" data-col="name" style="cursor: pointer; user-select: none;">Cultivo${getSortIcon('name')}</th>
            <th class="sortable text-right" data-col="superficie_cosechada" style="cursor: pointer; user-select: none; text-align: right;">Superficie Cosechada (Ha)${getSortIcon('superficie_cosechada')}</th>
            <th class="sortable text-right" data-col="volumen_produccion" style="cursor: pointer; user-select: none; text-align: right;">Producción (Ton)${getSortIcon('volumen_produccion')}</th>
            <th class="sortable text-right" data-col="rendimiento" style="cursor: pointer; user-select: none; text-align: right;">Rendimiento (Ton/Ha)${getSortIcon('rendimiento')}</th>
            <th class="sortable text-right" data-col="hh_total" style="cursor: pointer; user-select: none; text-align: right;">Huella Hídrica (m³/Ton)${getSortIcon('hh_total')}</th>
            <th class="sortable text-right" data-col="uac_total" style="cursor: pointer; user-select: none; text-align: right;">Uso de Agua (m³/Ha)${getSortIcon('uac_total')}</th>
            <th class="sortable text-right" data-col="eficiencia_fisica" style="cursor: pointer; user-select: none; text-align: right;">Eficiencia Física (Ton/m³)${getSortIcon('eficiencia_fisica')}</th>
            <th class="sortable text-right" data-col="productividad_economica" style="cursor: pointer; user-select: none; text-align: right;">Productividad Económica (MXN/m³)${getSortIcon('productividad_economica')}</th>
            <th class="sortable text-right" data-col="pmr" style="cursor: pointer; user-select: none; text-align: right;">PMR (MXN/Ton)${getSortIcon('pmr')}</th>
            <th class="sortable text-right" data-col="consumo_agua_total" style="cursor: pointer; user-select: none; text-align: right;">Consumo Hídrico (Mm³)${getSortIcon('consumo_agua_total')}</th>
        </tr>
    `;

    // Obtener y ordenar los cultivos (excluyendo "Todos los cultivos")
    const cropsList = Object.keys(regionData)
        .filter(c => c !== "Todos los cultivos")
        .map(c => ({ name: c, ...regionData[c] }));

    const sortCol = AppState.tableSort.column;
    const sortDir = AppState.tableSort.direction;

    cropsList.sort((a, b) => {
        let valA = a[sortCol];
        let valB = b[sortCol];

        if (sortCol === 'name') {
            return sortDir === 'asc'
                ? String(valA).localeCompare(String(valB))
                : String(valB).localeCompare(String(valA));
        }

        if (valA === undefined || valA === null) valA = 0;
        if (valB === undefined || valB === null) valB = 0;
        return sortDir === 'asc' ? valA - valB : valB - valA;
    });

    tableBody.innerHTML = "";
    cropsList.forEach(crop => {
        const row = document.createElement("tr");
        const consumoMm3 = crop.consumo_agua_total / 1e6;

        row.innerHTML = `
            <td><strong>${crop.name}</strong></td>
            <td style="text-align: right;">${Math.round(crop.superficie_cosechada).toLocaleString()}</td>
            <td style="text-align: right;">${Math.round(crop.volumen_produccion).toLocaleString()}</td>
            <td style="text-align: right;">${crop.rendimiento.toFixed(2)}</td>
            <td style="text-align: right;">${Math.round(crop.hh_total).toLocaleString()}</td>
            <td style="text-align: right;">${Math.round(crop.uac_total).toLocaleString()}</td>
            <td style="text-align: right; font-weight: 600; color: var(--accent-blue);">${crop.eficiencia_fisica.toFixed(5)}</td>
            <td style="text-align: right; font-weight: 600; color: var(--accent-green);">$${crop.productividad_economica.toFixed(2)}</td>
            <td style="text-align: right;">$${Math.round(crop.pmr).toLocaleString()}</td>
            <td style="text-align: right;">${consumoMm3.toFixed(2)}</td>
        `;
        tableBody.appendChild(row);
    });

    // Configurar el botón de descarga de CSV
    const downloadBtn = document.getElementById("db-download-csv");
    if (downloadBtn) {
        // Remover listener anterior clonando el botón para evitar duplicados
        const newBtn = downloadBtn.cloneNode(true);
        downloadBtn.parentNode.replaceChild(newBtn, downloadBtn);
        newBtn.addEventListener("click", () => {
            let csvContent = "Cultivo,Superficie Cosechada (Ha),Produccion (Ton),Rendimiento (Ton/Ha),Huella Hidrica (m3/Ton),Uso de Agua (m3/Ha),Eficiencia Fisica (Ton/m3),Productividad Economica (MXN/m3),PMR (MXN/Ton),Consumo Hidrico (Mm3)\n";
            cropsList.forEach(crop => {
                const consumoMm3 = crop.consumo_agua_total / 1e6;
                const row = [
                    `"${crop.name}"`,
                    Math.round(crop.superficie_cosechada),
                    Math.round(crop.volumen_produccion),
                    crop.rendimiento.toFixed(2),
                    Math.round(crop.hh_total),
                    Math.round(crop.uac_total),
                    crop.eficiencia_fisica.toFixed(5),
                    crop.productividad_economica.toFixed(2),
                    Math.round(crop.pmr),
                    consumoMm3.toFixed(2)
                ].join(",");
                csvContent += row + "\n";
            });

            const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.setAttribute("href", url);
            link.setAttribute("download", `detalles_cultivos_${region.toLowerCase().replace(/\s+/g, "_")}_${yearStart}_${yearEnd}.csv`);
            link.style.visibility = "hidden";
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    }
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

    // Actualizar gráficos dinámicos del dashboard o estáticos según corresponda
    if (AppState.activeSection === "dashboard" && AppState.dashboardData) {
        updateDashboard();
    } else if (AppState.activeSection === "estadisticas") {
        renderCharts();
    }
}

// --- Renderizado de Gráficos Estáticos (Estadísticas Originales) ---
function renderCharts() {
    if (AppState.charts.efficiency) AppState.charts.efficiency.destroy();
    if (AppState.charts.economic) AppState.charts.economic.destroy();

    const ctxEff = document.getElementById("chart-efficiency");
    if (ctxEff) {
        const isDark = document.documentElement.getAttribute("data-theme") !== "light";
        const textColor = isDark ? "#9ca3af" : "#4b5563";
        const gridColor = isDark ? "rgba(156, 163, 175, 0.1)" : "rgba(75, 85, 99, 0.1)";

        AppState.charts.efficiency = new Chart(ctxEff.getContext("2d"), {
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
                        grid: { color: gridColor },
                        ticks: { color: textColor },
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: textColor },
                    },
                },
                plugins: {
                    legend: { display: false },
                },
            },
        });
    }

    const ctxEco = document.getElementById("chart-ddr-economic");
    if (ctxEco) {
        const isDark = document.documentElement.getAttribute("data-theme") !== "light";
        const textColor = isDark ? "#9ca3af" : "#4b5563";
        const gridColor = isDark ? "rgba(156, 163, 175, 0.1)" : "rgba(75, 85, 99, 0.1)";

        AppState.charts.economic = new Chart(ctxEco.getContext("2d"), {
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
                        grid: { color: gridColor },
                        ticks: { color: textColor },
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: textColor },
                    },
                },
                plugins: {
                    legend: { display: false },
                },
            },
        });
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
