"""
Abstracción de acceso a datos. Soporta local y futuro Cloud.
"""

import json
from abc import ABC, abstractmethod

from .paths import (
    CONFIG_DATA_DIR,
    COORDINATES_CSV,
    JSON_CODIFICACION,
    NASA_POWER_DATA,
    PROCESSED_DIR,
)

import pandas as pd


class DataRepository(ABC):
    @abstractmethod
    def load_coordinates(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def load_nasa_power(self, year: str, loc: str = "all") -> pd.DataFrame:
        pass

    @abstractmethod
    def load_config_json(self, name: str) -> dict:
        pass


class LocalRepository(DataRepository):
    def load_coordinates(self) -> pd.DataFrame:
        df = pd.read_csv(COORDINATES_CSV, encoding="utf-8")
        if "entidad" in df.columns:
            df = df.drop(columns=["entidad"])
        return df

    def load_nasa_power(self, year: str, loc: str = "all") -> pd.DataFrame:
        files = NASA_POWER_DATA.glob(f"*{year}.csv")
        dfs = []
        for f in files:
            if loc == "all" or loc in f.stem:
                dfs.append(pd.read_csv(f, encoding="utf-8"))
        if not dfs:
            return pd.DataFrame()
        df = pd.concat(dfs, ignore_index=True)
        df["DATE"] = pd.to_datetime(df["DATE"].astype(str))
        return df

    def load_config_json(self, name: str) -> dict:
        # name: 'cultivos', 'codificacion', etc.
        path = CONFIG_DATA_DIR / f"{name}.json"
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def load_production_file(self, crop_name: str) -> pd.DataFrame:
        # crop_name: 'Trigo grano', 'Maíz grano', etc.
        filename = f"{crop_name.lower().replace(' ', '_')}.csv"
        path = PROCESSED_DIR / filename
        return pd.read_csv(path, encoding="utf-8")


# Repositorio por defecto (Local)
repo = LocalRepository()
