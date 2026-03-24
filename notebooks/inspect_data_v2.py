import pandas as pd

def inspect_xlsx_full(file_path, sheet=0, skip=0):
    print("--- Inspecting XLSX: {} (Sheet: {}, Skip: {}) ---".format(file_path, sheet, skip))
    try:
        df = pd.read_excel(file_path, sheet_name=sheet, skiprows=skip, nrows=10)
        print("Columns: {}".format(df.columns.tolist()))
        print("Sample Data:\n{}".format(df.head(3)))
    except Exception as e:
        print("Error reading {}: {}".format(file_path, e))

# Check the tecnificacion file with skip
inspect_xlsx_full('data/raw/datos_proporcionados/tecnificacion-riego-invernadores_DDR_2021.xlsx', skip=2)

# Get unique DDRs from a known good file
try:
    df_siap = pd.read_csv('data/raw/siap-produccion-agricola/municipal/cierre_agricola_sonora_2023.csv', encoding='latin1')
    ddrs = df_siap['Nomddr'].unique().tolist()
    print("\nDistritos de Desarrollo Rural (DDR) en Sonora (SIAP 2023):")
    print(ddrs)
    
    crops = df_siap['Nomcultivo'].unique().tolist()
    print("\nAlgunos cultivos en Sonora (SIAP 2023):")
    print(crops[:20]) # First 20
except Exception as e:
    print("Error getting unique values: {}".format(e))
