import os
import rasterio
import geopandas as gpd
import pandas as pd

# 定义输入和输出路径
input_dir = "E:/for timeseries/dnb"  # 替换为你的图像文件目录
shapefile_path = "D:/Desktop/data/basic/10kcd.shp"  # 替换为你的点位shapefile路径
output_dir = "D:/Desktop/data/csv"  # 输出CSV文件的目录

# 读取 shapefile 文件
points = gpd.read_file(shapefile_path)

# 确保点文件的坐标系与 TIFF 文件的坐标系匹配
# 假设 TIFF 文件使用的是 WGS84 坐标系 (EPSG:4326)
if points.crs != "EPSG:4326":
    points = points.to_crs("EPSG:4326")

# 创建输出目录（如果不存在）
# os.makedirs(output_dir, exist_ok=True)

# 遍历目录中的所有 .tif 文件
for filename in os.listdir(input_dir):
    if filename.endswith(".tif"):
        filepath = os.path.join(input_dir, filename)

        # 读取 .tif 图像文件
        with rasterio.open(filepath) as src:
            # 创建一个 DataFrame 来存储结果
            df = pd.DataFrame(columns=["longitude", "latitude", "dnb_value"])

            # 提取每个点的 DNB 值
            for point in points.itertuples():
                # 获取点的坐标
                lon, lat = point.geometry.x, point.geometry.y

                # 将坐标转换为栅格索引
                row, col = src.index(lon, lat)

                # 提取栅格值
                try:
                    dnb_value = src.read(1)[row, col]
                except IndexError:
                    dnb_value = None  # 如果点不在栅格范围内，则设置为 None

                # 将结果添加到 DataFrame 中
                df = df.append({"longitude": lon, "latitude": lat, "dnb_value": dnb_value}, ignore_index=True)

        # 将 DataFrame 保存为 CSV 文件
        output_csv = os.path.join(output_dir, f"{filename}.csv")
        df.to_csv(output_csv, index=False)
        print(f"CSV 文件已保存到 {output_csv}")