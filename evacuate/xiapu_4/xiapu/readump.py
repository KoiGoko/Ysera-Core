''''''"""
@author: Nan Jia
@time: 2023/6/25 10:21
@desc:
''''''"""
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import seaborn as sns

# xml = ET.parse('dump1.xml')
#
# root = xml.getroot()
#
# data = []
#
# settlements = ['977360507#0', '-51691749#4', '715792677', '1172895350#7', '543863877#1', '-777284203', '-778378294',
#                '1172895341#1', '544267905#1']
#
# land = ['717098972#1', '588559167#3', '717098972#2', '588559167#1']
#
# # 遍历每个timestep标签
# for timestep in root.iter('timestep'):
#
#     time = timestep.attrib['time']  # 获取时间步的值
#     print(f"Time: {time}")
#
#     # 遍历当前timestep下的edge标签
#     for edge in timestep.iter('edge'):
#         edge_id = edge.attrib['id']
#
#         # 遍历当前edge标签下的lane标签
#         for lane in edge.iter('lane'):
#             lane_id = lane.attrib['id']
#
#             # 遍历当前lane标签下的vehicle标签
#             for vehicle in lane.iter('vehicle'):
#                 vehicle_id = vehicle.attrib['id']
#                 pos = vehicle.attrib['pos']
#                 speed = vehicle.attrib['speed']
#
#                 if 'bus' in vehicle_id:
#                     vehicle_type = 'bus'
#                 elif 'private' in vehicle_id:
#                     vehicle_type = 'car'
#                 elif 'taxi' in vehicle_id:
#                     vehicle_type = 'taxi'
#                 elif 'motorcycle' in vehicle_id:
#                     vehicle_type = 'motorcycle'
#                 elif 'tricycle' in vehicle_id:
#                     vehicle_type = 'tricycle'
#                 data.append([time, edge_id, lane_id, vehicle_id, pos, speed, vehicle_type])
#                 # 打印或处理数据
#                 # print(
#                 #     f"Time: {time}, Edge ID: {edge_id}, Lane ID: {lane_id}, Vehicle ID: {vehicle_id}, Position: {pos}, Speed: {speed}")
#
# df = pd.DataFrame(data, columns=['Time', 'Edge ID', 'Lane ID', 'Vehicle ID', 'Position', 'Speed', 'type'])
#
# df = df[df['Edge ID'] == '1068471749#0']
#
# vehicle_capacity = {
#     'bus': 50,
#     'private': 5,
#     'motorcycle': 2,
#     'tricycle': 3,
#     'taxi': 4
# }
#
# # df.to_csv('output2.csv')
# #
# # df = pd.read_csv('output2.csv')
#
# df1 = df.groupby('Time').agg({'type': 'sum'}).reset_index()
# # df1.to_csv('output3.csv')
#
# df = df1
# # 使用apply函数和lambda表达式统计"bus"和"car"的数量，并将结果存储在新列中
# df[['bus_count', 'car_count', 'taxi_count', 'motorcycle_count', 'tricycle_count']] = df['type'].apply(
#     lambda x: pd.Series([x.count('bus'), x.count('car'), x.count('taxi'), x.count('motorcycle'), x.count('tricycle')]))
#
# df = df.drop('type', axis=1)

df = pd.read_csv('output4.csv')

sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))
sns.lineplot(x='Time', y='bus_count', data=df, label='bus')

# 设置图表标题和坐标轴标签
plt.title('Bus Count over Time')
plt.xlabel('Time')

plt.show()

# df = pd.read_csv('output.csv')

#
#
# group_df = df.groupby('Time').agg({'Edge ID': 'first', 'Lane ID': 'first', 'Vehicle ID': 'first', 'Position': 'mean', 'Speed': 'mean'})
#
#
# group_df.to_csv('output1.csv', index=False)
