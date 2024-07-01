import rasterio
import pandas as pd
import geopandas as gpd
import glob
import os
from osgeo import gdal
# import gdal_version



# 读取nvdi影像
def read_ndvi(file_path):
    with rasterio.open(file_path) as src:
        ndvi = src.read(0)
        transform = src.transform
    return ndvi, transform

#获取像元值
def get_pixel_value(ndvi, transform, lon, lat):
    row, col = ~transform * (lon, lat)
    row, col = int(row), int(col)
    return ndvi[row, col]

#从shp读取点
def read_points_from_shapefile(shapefile_path):
    gdf = gpd.read_file(shapefile_path)
    points = [(row['uid'], row.geometry.x, row.geometry.y) for idx, row in gdf.iterrows()]
    return points

#主函数以提取时间序列数据
def extract_ndvi_timeseries(file_paths, points):
    data = []
    for uid, lon, lat in points:
        time_series = {'uid': uid, 'lon': lon, 'lat': lat}
        for file_path in file_paths:
            date = file_path.split('_')[-1].split('.')[0]  # 假设文件名包含日期
            ndvi, transform = read_ndvi(file_path)
            ndvi_value = get_pixel_value(ndvi, transform, lon, lat)
            time_series[date] = ndvi_value
        data.append(time_series)
    return pd.DataFrame(data)

file_paths = 'E:/for timeseries/ndvi'
points = 'D:\\Desktop\\data\\basic\\10kcd.shp'

ndvi_df = extract_ndvi_timeseries(file_paths, points)
print(ndvi_df)