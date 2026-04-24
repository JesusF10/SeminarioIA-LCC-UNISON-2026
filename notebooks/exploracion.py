from seminario_ia.datasets import get_mun_coordinates, get_prod_data
from seminario_ia.models import Crop, Region

coords = get_mun_coordinates()


prod_df = get_prod_data((2010, 2024), muni=True, crop_name="Trigo grano")

trigo = Crop(
    name="Trigo",
    start_month=10,
    start_day=30,
    end_month=4,
    end_day=19,
    kc_ini=0.3,
    kc_mid=1.15,
    kc_end=0.25,
    durations=(31, 47, 63, 31),
)

# Crear diccionario de regiones
regions = {}
for row in coords.itertuples():
    _, municipio, latitud, longitud, z_m = row

    region = Region(
        name=municipio,
        crops=trigo,
        latitude=latitud,
        longitude=longitud,
        altitude=z_m,
    )
    regions[municipio] = region
    print(region)

print(prod_df.head())
