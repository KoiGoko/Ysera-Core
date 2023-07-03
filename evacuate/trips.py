''''''"""
@author: Nan Jia
@time: 2023/6/7 10:15
@desc:
''''''"""
import custom_input as input
import xml.etree.ElementTree as ET
import os
import glob
import random
import copy

# 撤离村镇
countrys = input.countrys

# 撤离村镇信息
country_infos = {}

for country in countrys:
    country_info = getattr(input, country)
    country_infos[country] = country_info

# 撤离路线
routes = []

# 安置点
settlement_points = input.settlement_points

# 人口点
pop_points = input.pop_points

for name, points_id in pop_points.items():
    settle_name, settle_id = random.choice(list(settlement_points.items()))
    route = [name, settle_name, points_id, settle_id]
    routes.append(route)

vehicle_capacity = input.vehicle_capacity

# 回程次数
route_numbers = {}

vehicle_en = input.vehicle_en

for country, info in country_infos.items():
    sum = 0
    for vehicle_name, vehicle_type in vehicle_en.items():
        sum = sum + info[vehicle_name] * vehicle_capacity[vehicle_type]
    numbers = info['总人口'] // sum + 1
    route_numbers[country] = numbers

# sumo trips文件
trips_name = {}
trips_dir = input.trips_dir
vehicles = input.vehicles

for vehicle in vehicles:
    vehicle_path = glob.glob(os.path.join(trips_dir, 'osm.' + str(vehicle) + '.trips.xml'))
    trips_name[vehicle] = vehicle_path

for route in routes:
    if route[0] in route_numbers.keys():
        route_number = route_numbers[route[0]]
    else:
        route_number = 1
    route.append(route_number)

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


for route in routes:
    for country, info in country_infos.items():
        if route[0] == country:
            generate_xml(route, info, trips_name)

