from evacuate.src.utils import input_args
import xml.etree.ElementTree as ET

person = {}
cfg_path = ''


# 配置初始化
def init_pedestrian_cfg(_cfg_path):
    _person = input_args(_cfg_path, 'person')
    global cfg_path
    cfg_path = _cfg_path
    person.update(_person)


def init_pedestrian_walk(pedestrian_xml_path):
    tree = ET.parse(pedestrian_xml_path)
    root = tree.getroot()
    walks = root.find('routes/trip')
    for walk in walks:
        walk.set('depart', '0')
        walk.set('from', '0')
        walk.set('to', '0')
        walk.set('departPos', 'random')
        walk.set('departSpeed', 'random')
        walk.set('departLane', 'random')
        walk.set('arrivalPos', 'random')
        walk.set('arrivalSpeed', 'random')
        walk.set('arrivalLane', 'random')
        walk.set('color', '1,1,0')
        walk.set('type', 'pedestrian')
        walk.set('id', 'pedestrian')
        walk.set('departLane', 'random')
        walk.set('departSpeed', 'random')
        walk.set('departPos', 'random')
        walk.set('arrivalLane', 'random')
        walk.set('arrivalSpeed', 'random')
        walk.set('arrivalPos', 'random')
        walk.set('depart', '0')
        walk.set('from', '0')
        walk.set('to', '0')
        walk.set('color', '1,1,0')
        walk.set('type', 'pedestrian')
        walk.set('id', 'pedestrian')

    return tree


def init_pedestrian_trips(pedestrian_xml_path):
    pedestrian_tree = ET.parse(pedestrian_xml_path)
    pedestrian_root = pedestrian_tree.getroot()
    trip = pedestrian_root.subElement('trips')
    trip.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')

    return pedestrian_tree


def generate_pedestrian_trips(pedestrian_xml_path):
    return 'hello world'


def pre_pedestrian(pedestrian_xml_path):
    init_pedestrian_cfg(cfg_path)
    init_pedestrian_walk(pedestrian_xml_path)
    init_pedestrian_trips(pedestrian_xml_path)
    generate_pedestrian_trips(pedestrian_xml_path)


if __name__ == '__main__':
    print(pre_pedestrian())
