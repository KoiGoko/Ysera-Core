''''''"""
@author: Nan Jia
@time: 2023/6/21 13:48
@desc:
''''''"""

import os
import osmnx as ox
import requests

# 指定霞浦县的地理范围
place_name = "霞浦县, 中国"
tags = {"place": "village"}

# 使用osmnx获取村庄数据
gdf = ox.geometries_from_place(place_name, tags)

# 输出村庄信息
print(gdf)
print('hello world')

# 设置下载链接
download_url = 'https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/0_Mosaicked/ppp_2020_1km_Aggregated.tif'  # 替换为实际的下载链接

# 设置保存文件路径
save_path = 'path/to/save/file.tif'  # 替换为实际的保存路径和文件名

# 发送HTTP请求并下载文件
response = requests.get(download_url)

# 检查请求是否成功
if response.status_code == 200:
    # 保存文件
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print('下载完成')
else:
    print('下载失败:', response.status_code)

if os.path.exists(save_path):
    os.remove(save_path)
