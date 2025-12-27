import geopandas as gpd

shp_path = r"data\mrshape\mrt_admbnda_adm2_ansade_20240327.shp"
gdf = gpd.read_file(shp_path)

print("COLUMNS:", list(gdf.columns))
print(gdf.head(2))
