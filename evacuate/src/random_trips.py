import os
import xml.etree.ElementTree as ET
import glob
import logging
import itertools
from evacuate.src.utils import input_args
from evacuate.src.utils import standardization_xml
from evacuate.src.utils import get_all_lanes
from evacuate.src.pre_vehicle import get_vehicle_speed
from evacuate.src.pre_vehicle import init_vehicle_cfg
from evacuate.src.utils import get_similar_type_count
import evacuate.src.evacuate_distribution as evacuate_distribution
import random

net_xml_path = ''
random_trips_lanes_number = 100
random_vehicle_number = 100


def init_random_lanes():
    all_lanes = get_all_lanes(net_xml_path)
    lane_number = len(all_lanes) + 1
    random_trips_lanes_index = random.sample(range(1, lane_number), random_trips_lanes_number)
    random_trips_lanes = []
    for i in random_trips_lanes_index:
        random_trips_lanes.append(all_lanes[i - 1])

    return random_trips_lanes


def init_random_vehicle():
    random_vehicle_index = random.sample(range(1, 100), random_vehicle_number)
    random_vehicle = []
    for i in random_vehicle_index:
        random_vehicle.append(i)

    return random_vehicle


def init_random_departs():
    random_departs = []
    for i in range(1, 100):
        random_departs.append(i)

    return random_departs


def init_random_from_to():
    return random.randint(1, 100), random.randint(1, 100)


def init_random_vehicles_loops():
    return random.randint(1, 100)


def init_random_vehicles_trips():
    return random.randint(1, 100)


def init_random_vehicles_xml():
    return random.randint(1, 100)


def random_trips():
    init_vehicle_cfg()


if __name__ == '__main__':
    random_trips
