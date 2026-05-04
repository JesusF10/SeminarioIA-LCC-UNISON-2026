"""
Modelos de datos para representar la información de cultivos y regiones.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class Crop(BaseModel):
    """Modelo de cultivo agrícola con características fenológicas."""

    name: str
    start_month: int
    start_day: int
    end_month: int
    end_day: int

    kc_ini: float
    kc_mid: float
    kc_end: float

    durations: tuple[int, int, int, int]

    model_config = ConfigDict(extra="ignore")

    @property
    def start_date(self) -> tuple[int, int]:
        """Retorna tupla (mes, día) de inicio."""
        return self.start_month, self.start_day

    @property
    def end_date(self) -> tuple[int, int]:
        """Retorna tupla (mes, día) de fin."""
        return self.end_month, self.end_day

    @property
    def kc(self) -> dict[str, float]:
        """Retorna diccionario de coeficientes."""
        return {"ini": self.kc_ini, "mid": self.kc_mid, "end": self.kc_end}

    def __str__(self) -> str:
        """Representación amigable para humanos con indentación."""
        start_date = f"{self.start_month:02d}/{self.start_day:02d}"
        end_date = f"{self.end_month:02d}/{self.end_day:02d}"

        duration_names = ["Inicial", "Desarrollo", "Medio", "Maduración"]
        durations_str = "\n        ".join(
            f"{name}: {days} días"
            for name, days in zip(duration_names, self.durations, strict=True)
        )

        return (
            f"Cultivo: {self.name}\n"
            f"      Período: {start_date} - {end_date}\n"
            f"      Coeficientes Kc:\n"
            f"        Inicial: {self.kc_ini}\n"
            f"        Medio: {self.kc_mid}\n"
            f"        Final: {self.kc_end}\n"
            f"      Duraciones por etapa:\n"
            f"        {durations_str}"
        )

    def __repr__(self) -> str:
        """Representación compacta y directa."""
        return (
            f"Crop(name={self.name!r}, "
            f"start_month={self.start_month}, "
            f"start_day={self.start_day}, "
            f"end_month={self.end_month}, "
            f"end_day={self.end_day}, "
            f"kc_ini={self.kc_ini}, "
            f"kc_mid={self.kc_mid}, "
            f"kc_end={self.kc_end}, "
            f"durations={self.durations})"
        )


class Region(BaseModel):
    """Región geográfica con información municipal y cultivos."""

    name: str
    latitude: float
    longitude: float
    altitude: float
    crops: Crop | list[Crop] = []

    model_config = ConfigDict(extra="ignore")

    def add_crop(self, crop: Crop) -> None:
        """Agrega un cultivo a la región."""
        if not self.crops:
            self.crops = [crop]
        elif isinstance(self.crops, Crop):
            self.crops = [self.crops, crop]
        else:
            self.crops.append(crop)

    def get_crops(self) -> list[Crop]:
        """Retorna la lista de cultivos, asegurando que siempre sea una lista."""
        if not self.crops:
            return []
        if isinstance(self.crops, Crop):
            return [self.crops]
        return self.crops

    def get_crop(self, name: str) -> Crop:
        """Obtiene un cultivo por su nombre."""
        crops = self.get_crops()
        for crop in crops:
            if crop.name == name:
                return crop
        raise ValueError(f"Cultivo '{name}' no encontrado en la región '{self.name}'.")

    def __str__(self) -> str:
        """Representación amigable con estructura."""
        crops_str = ""
        if self.crops:
            crops_lines = []
            if isinstance(self.crops, Crop):
                self.crops = [self.crops]
            for crop in self.crops:
                # Indenta el __str__ del cultivo
                crop_str = str(crop)
                indented_crop = "\n".join(
                    "    " + line for line in crop_str.split("\n")
                )
                crops_lines.append(indented_crop)
            crops_str = "\n".join(crops_lines)
        else:
            crops_str = "    (Sin cultivos)"

        return (
            f"Región: {self.name}\n"
            f"  Latitud: {self.latitude}\n"
            f"  Longitud: {self.longitude}\n"
            f"  Altitud (m): {self.altitude}\n"
            f"  Cultivos:\n"
            f"{crops_str}"
        )

    def __repr__(self) -> str:
        """Representación compacta."""
        crops_reprs = ", ".join(repr(c) for c in self.crops)
        return (
            f"Region(name={self.name!r}, "
            f"latitude={self.latitude}, "
            f"longitude={self.longitude}, "
            f"altitude={self.altitude}, "
            f"crops=[{crops_reprs}])"
        )


class WeatherRecord(BaseModel):
    """Registro de datos meteorológicos para una fecha específica."""

    date: datetime = Field(alias="DATE")  # Formato 'YYYY-MM-DD'
    t_max: float = Field(alias="T2M_MAX")  # Temperatura máxima (°C)
    t_min: float = Field(alias="T2M_MIN")  # Temperatura mínima (°C)
    rs: float = Field(alias="ALLSKY_SFC_SW_DWN")  # Radiación solar (MJ/m²/día)
    rl: float = Field(alias="ALLSKY_SFC_LW_DWN")  # Radiación térmica (MJ/m²/día)
    rh: float = Field(alias="RH2M")  # Humedad relativa (%)
    ws: float = Field(alias="WS2M")  # Velocidad del viento (m/s)
    pt: float = Field(alias="PRECTOTCORR")  # Precipitación total corregida (mm/día)

    model_config = ConfigDict(extra="ignore")


WeatherAdapter = TypeAdapter(list[WeatherRecord])


if __name__ == "__main__":
    # Ejemplo de uso
    weather_data = {
        "DATE": "2024-06-01",
        "T2M_MAX": 35.5,
        "T2M_MIN": 20.3,
        "ALLSKY_SFC_SW_DWN": 25.0,
        "ALLSKY_SFC_LW_DWN": 10.0,
        "RH2M": 60.0,
        "WS2M": 5.0,
        "PRECTOTCORR": 0.0,
    }

    t = WeatherRecord.model_validate(weather_data)

    print(t.model_dump(by_alias=True))  # Muestra los datos con alias
