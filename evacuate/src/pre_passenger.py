import xml.etree.ElementTree as ET

from evacuate.src.utils import input_args

person = {}
cfg_path = ''


# 配置初始化
def init_passenger_cfg(_cfg_path):
    _person = input_args(_cfg_path, 'person')
    global cfg_path
    cfg_path = _cfg_path
    person.update(_person)


def init_passenger_trips(passenger_xml_path):
    passenger_root = ET.parse(passenger_xml_path)
    passenger_root = passenger_root.getroot()
    return 'hello world'


def pre_passenger(passenger_xml_path):
    passenger_root = ET.parse(passenger_xml_path)
    passenger_root = passenger_root.getroot()
    return 'hello world'


if __name__ == '__main__':
    pre_passenger()
    print('初始化乘客信息')
