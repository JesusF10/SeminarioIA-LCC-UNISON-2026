from playwright.sync_api import sync_playwright


def extraer_siap_intenciones():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://nube.agricultura.gob.mx/agroprograma/")

        # Seleccionar Sonora (Clave 26) en el dropdown de Estado
        # Nota: Los dropdowns 'Chosen' requieren clics específicos
        page.click("#Estado_chosen")
        page.type(".chosen-search input", "Sonora")
        page.keyboard.press("Enter")

        # Repetir para Año, Ciclo, etc.
        page.click("#Consultar")

        # Esperar y descargar el archivo al hacer clic en Exportar
        with page.expect_download() as download_info:
            page.click("#Exportar")
        download = download_info.value
        download.save_as(f"data/raw/siap-produccion-agricola/intenciones_sonora.xlsx")

        browser.close()
