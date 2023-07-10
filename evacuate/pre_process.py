''''''"""
@author: Nan Jia
@time: 2023/6/7 10:46
@desc:
''''''"""

# 模拟环境预处理
import yaml
import os
import numpy as np
import random

with open('evacuate.yaml', encoding='utf-8') as f:
    evacuate = yaml.load(f, Loader=yaml.FullLoader)

with open('capacity.yaml', encoding='utf-8') as f:
    capacity = yaml.load(f, Loader=yaml.FullLoader)

with open('environment.yaml', encoding='utf-8') as f:
    environment = yaml.load(f, Loader=yaml.FullLoader)

towns = list(evacuate['population'].keys())
populations = np.array(list(evacuate['population'].values()))

# 人口分布
pop_distribute = populations / np.sum(populations)

# 根据人口分布计算车辆分布
allocate_cars = capacity['per_vehicle'] / 100 * np.sum(populations) * pop_distribute

# 车辆分布
vehicle_capacity = np.array(list(capacity['vehicle_capacity'].values()))
veh_distribute = 1 - vehicle_capacity / np.sum(vehicle_capacity)
veh_distribute = veh_distribute / np.sum(veh_distribute)

allocate = {}

for i, allocate_car in enumerate(allocate_cars):
    allocate[towns[i]] = np.ceil(allocate_car * veh_distribute)

# 分配车辆完成

# 生成路线
routes = []
for town, lane in evacuate['evacuates'].items():
    settle, settle_lane = random.choice(list(evacuate['settlements'].items()))
    route = [town, settle, lane, settle_lane]
    routes.append(route)

# 生成路线完成

# 计算回程次数




print('hello')
