# %% Cell 1
import pandas as pd
import requests

# %% Cell 2

columns = ["RH2M", "T2M_MAX", "PRECTOTCORR"]
# Define API settings
base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
params = {
    "parameters": ",".join(columns),  # Relative Humidity at 2 Meters
    "community": "AG",  # Agricultural community
    "longitude": -0.12,  # Longitude for London
    "latitude": 51.50,  # Latitude for London
    "start": "20230101",  # Start date (YYYYMMDD)
    "end": "20230110",  # End date (YYYYMMDD)
    "format": "JSON",
}

# 1. Execute the GET request
response = requests.get(base_url, params=params)

# 2. Check for success and extract data
if response.status_code == 200:
    data = response.json()
    # 3. Extract the actual humidity values
    # Structure: data -> properties -> parameter -> RH2M
    all_params = data["properties"]["parameter"]

    # Convert the dictionary to a DataFrame
    # Each parameter key (RH2M, T2M, etc.) becomes a column
    df = pd.DataFrame(all_params).reset_index()
    df.columns = ["DATE"] + columns
    # 4. Create a clean DataFrame
    # df = pd.DataFrame.from_dict(rh_values, orient="index", columns=["RH2M"])
    # df.index.name = "Date"
    print(df)
else:
    print(f"Error: {response.status_code}")
