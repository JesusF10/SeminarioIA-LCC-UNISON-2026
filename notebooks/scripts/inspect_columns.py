import os
import polars as pl
import pandas as pd
from pathlib import Path

def inspect_data():
    raw_dir = Path("data/raw")
    results = []
    
    # Extensiones de interés
    extensions = [".csv", ".xlsx", ".xls"]
    
    for root, dirs, files in os.walk(raw_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in extensions:
                try:
                    cols = []
                    if file_path.suffix.lower() == ".csv":
                        # Leer solo el header para rapidez
                        df = pl.read_csv(file_path, n_rows=0, ignore_errors=True)
                        cols = df.columns
                    else:
                        # Para Excel, usar pandas para el header de la primera hoja
                        df = pd.read_excel(file_path, nrows=0)
                        cols = list(df.columns)
                    
                    results.append({
                        "file": file,
                        "path": str(file_path),
                        "columns": ", ".join(cols)
                    })
                except Exception as e:
                    results.append({
                        "file": file,
                        "path": str(file_path),
                        "columns": f"Error reading: {str(e)}"
                    })
    
    # Crear reporte sintético
    report_path = Path("data/processed/inventory_report.csv")
    os.makedirs("data/processed", exist_ok=True)
    pd.DataFrame(results).to_csv(report_path, index=False)
    print(f"Reporte de inventario guardado en: {report_path}")

if __name__ == "__main__":
    inspect_data()
