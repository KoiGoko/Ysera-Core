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
import xml.etree.ElementTree as ET
import glob
import copy

cfg_file = 'evacuate.yaml'


def input_args(cfg_path):
    with open('evacuate.yaml', encoding='utf-8') as f:
        evacuate = yaml.load(f, Loader=yaml.FullLoader)

    with open('vehicle.yaml', encoding='utf-8') as f:
        capacity = yaml.load(f, Loader=yaml.FullLoader)

    with open('environment.yaml', encoding='utf-8') as f:
        environment = yaml.load(f, Loader=yaml.FullLoader)
    return evacuate, capacity, environment


def distribute_cars():
    return 'distribute cars'
    pass


def generate_routes():
    return 'generate routes'
    pass


def generate_trips():
    return 'generate xml'
    pass


evacuate, capacity, environment = input_args(cfg_file)

# with open('evacuate.yaml', encoding='utf-8') as f:
#     evacuate = yaml.load(f, Loader=yaml.FullLoader)
#
# with open('vehicle.yaml', encoding='utf-8') as f:
#     capacity = yaml.load(f, Loader=yaml.FullLoader)
#
# with open('environment.yaml', encoding='utf-8') as f:
#     environment = yaml.load(f, Loader=yaml.FullLoader)

towns = list(evacuate['population'].keys())
populations = np.array(list(evacuate['population'].values()))

# 人口分布
pop_distribute = populations / np.sum(populations)

# 根据人口分布计算车辆分布
allocate_cars = capacity['per_vehicle'] / 100 * np.sum(populations) * pop_distribute

# 车辆分布
vehicle_names = list(capacity['vehicle_capacity'].keys())
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
    # 随机指定安置点
    settle, settle_lane = random.choice(list(evacuate['settlements'].items()))
    route = [town, settle, lane, settle_lane]
    routes.append(route)

# 生成路线完成

# 计算回程次数

# 一次的撤离数量
temp = np.array(list(allocate.values())) * vehicle_capacity
temp = np.sum(temp, axis=1)
# 撤离次数
per_capacity = np.ceil(populations / temp)

# 计算回程次数完成

# 生成trips文件

trips_path1 = ''

# 创建根元素 routes
root = ET.Element("routes")
root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
root.set("xsi:noNamespaceSchemaLocation", "http://sumo.dlr.de/xsd/routes_file.xsd")

for vehicle_name in vehicle_names:
    tree = ET.ElementTree(root)
    # 创建 vType 元素
    vtype = ET.SubElement(root, "vType")
    vtype.set("id", vehicle_name)
    vtype.set("vClass", vehicle_name)
    filename = f"osm.{vehicle_name}.trips.xml"
    tree.write(filename, encoding="utf-8", xml_declaration=True)

trip_template = {
    "id": "",
    "type": "",
    "depart": "0.00",
    "departLane": "best",
    "from": "",
    "to": "",
    "stop": [
        {"edge": "", "parking": "true", "duration": ""},
    ]
}

# trips_paths = glob.glob(os.path.join(trips_path1, 'osm.*.trips.xml'))

trips_paths = list(map(lambda item: glob.glob(
    os.path.join(trips_path1, f"osm.{item}.trips.xml")), vehicle_names))
trips_paths = [path for sublist in trips_paths for path in sublist]

vehicle_names1 = vehicle_names

for trips_path in trips_paths:
    tree = ET.parse(trips_path)
    root = tree.getroot()
    trip = copy.deepcopy(trip_template)
    for j, route in enumerate(routes):
        trip["id"] = f"{route[0]}_{vehicle_names[i]}0"


    def generate_xml(_route, _info, _trips_name):
        number = 0
        for xml_name, path in _trips_name.items():
            trips = []
            if xml_name == 'bus':
                number = _info['公交车']
            elif xml_name == 'private':
                number = _info['私家车']
            elif xml_name == 'motorcycle':
                number = _info['摩托车']
            elif xml_name == 'tricycle':
                number = _info['三轮车']
            elif xml_name == 'taxi':
                number = _info['出租车']

            trip = copy.deepcopy(trip_template)
            trip["id"] = f"{_route[0]}_{xml_name}0"
            trip['depart'] = '0.00'
            trip['type'] = f'{xml_name}'
            trip["from"] = _route[2]
            trip["to"] = _route[3]
            stop_index = 3
            trip_template['stop'] = []
            stops = []
            for j in range(_route[4] * 2 - 1):
                stop = {
                    "edge": f"{_route[stop_index]}",
                    "parking": "true",
                    "duration": "10.00"
                }
                stops.append(stop)
                if stop_index == 3:
                    stop_index = 2
                    continue
                if stop_index == 2:
                    stop_index = 3
                    continue
            trip['stop'] = stops
            trips.append(trip)
            for j in range(1, number):
                new_trip = trip.copy()
                new_trip['id'] = f"{_route[0]}_{xml_name}{j}"
                trips.append(new_trip)
            xml_tree = ET.parse(path[0])
            root = xml_tree.getroot()
            for trips_data in trips:
                trip_element = ET.SubElement(root, "trip")
                for key, value in trips_data.items():
                    if key == "stop":
                        for stop in value:
                            stop_element = ET.SubElement(trip_element, "stop")
                            for stop_key, stop_value in stop.items():
                                stop_element.set(stop_key, stop_value)
                    else:
                        trip_element.set(key, value)
            xml_tree.write(path[0], encoding="utf-8", xml_declaration=True)

print('hello')
