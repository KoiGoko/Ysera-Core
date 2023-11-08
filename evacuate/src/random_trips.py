import os.path
import random
import xml.etree.ElementTree as ET

from evacuate.src.pre_vehicle import init_vehicle_cfg
from evacuate.src.utils import get_all_lanes
from evacuate.src.utils import input_args

net_xml_path = 'osm.net.xml'
random_trips_lanes_number = 200
random_vehicle_number = 100
random_departs_start = 1
random_departs_end = 1
random_stop_max = 100
random_loop_max = 5
evacuate = {}
vehicle = {}
cfg_path = ''


# 配置初始化
def init_random_cfg(_cfg_path):
    _evacuate = input_args(_cfg_path, 'evacuate')
    _vehicle = input_args(_cfg_path, 'vehicle')
    global cfg_path
    cfg_path = _cfg_path
    evacuate.update(_evacuate)
    vehicle.update(_vehicle)


def init_random_lanes():
    all_lanes = get_all_lanes(net_xml_path)
    lane_number = len(all_lanes) + 1
    random_trips_lanes_index = random.sample(range(1, lane_number), random_trips_lanes_number)
    random_trips_lanes = []
    for i in random_trips_lanes_index:
        random_trips_lanes.append(all_lanes[i - 1])

    return random_trips_lanes


def init_random_vehicle():
    vehicle_type = vehicle['vehicle_type'].values()
    vehicle_number = len(vehicle_type)
    pre_random_vehicle = random.sample(range(1, random_vehicle_number), vehicle_number)
    random_vehicle_infos = {}
    for i in range(len(pre_random_vehicle)):
        random_vehicle_infos[vehicle_type[i]] = pre_random_vehicle[i]
    return random_vehicle_infos


def init_random_departs(random_vehicle_infos):
    random_vehicle_total = sum(random_vehicle_infos.values())
    random_departs = random.sample(range(random_departs_start, random_departs_end), random_vehicle_total)
    random_departs = sorted(random_departs)
    return random_departs


def init_random_from_to(random_trips_lanes):
    from_s = []
    to_s = []
    for lane in range(1, random_trips_lanes_number // 2):
        from_s.append(lane['id'])
    for lane in range(100, random_trips_lanes_number):
        to_s.append(lane['id'])

    from_s = random.shuffle(from_s)
    to_s = random.shuffle(to_s)

    return [from_s, to_s]


def init_random_vehicles_loops():
    return list(range(1, random_loop_max))


def init_random_stop():
    return list(range(1, random_stop_max))


def init_random_vehicles_trips(random_departs,
                               random_trips_lanes,
                               random_vehicle_infos,
                               random_file_dir,
                               random_stop,
                               random_loops,
                               ):
    root = ET.Element('routes')
    init_tree = ET.ElementTree(root)
    random_file_path = os.path.join(random_file_dir, 'random_trips.xml')
    if os.path.exists(random_file_path):
        os.remove(random_file_path)
    init_tree.write(random_file_path)
    random_route_tree = ET.parse(random_file_path)
    root = random_route_tree.getroot()
    vehicle_types = random_vehicle_infos.keys()
    for vehicle_type in vehicle_types:
        v_type = ET.SubElement(root, 'vType')
        v_type.set("id", vehicle_type)
        v_type.set("vClass", vehicle_type)
    from_s = random_trips_lanes[0]
    to_s = random_trips_lanes[1]
    for vehicle_type, vehicle_number in random_vehicle_infos.items():
        for i in range(vehicle_number):
            trip = ET.SubElement(root, 'trip')
            trip.set("id", f"random_{vehicle_type}_{i}")
            trip.set("depart", str(random_departs[i]))
            from_lane = str(random.choice(from_s))
            to_lane = str(random.choice(to_s))
            trip.set("from", from_lane)
            trip.set("to", to_lane)
            random_loop = random.choice(random_loops)
            for loop in range(random_loop):
                stop_times = str(random.choice(random_stop))
                ET.SubElement(trip, "stop", attrib={"edge": random_trips_lanes[i]['to'],
                                                    "parking": f"{stop_times}",
                                                    "duration": "0"})
    random_route_tree.write(random_file_path)


def random_trips():
    init_vehicle_cfg()


if __name__ == '__main__':
    init_random_lanes()
