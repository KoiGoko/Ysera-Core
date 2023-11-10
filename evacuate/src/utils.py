import logging
import os
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET

import yaml

_author_ = 'Nan Jia'
_email_ = 'KoiGoko@outlook.com'

# 配置日志记录器
logging.basicConfig(filename='../sumo.log', level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')


# 读取参数
def input_args(_cfg_path, select):
    # 参数文件
    _cfg_yaml = ['evacuate.yaml', 'vehicle.yaml', 'environment.yaml', 'result.yaml', 'person.yaml',
                 'dose.yaml', 'emergency.yaml', 'public_transport.yaml', 'ship.yaml', 'tram.yaml', ]
    with open(os.path.join(_cfg_path, _cfg_yaml[0]), encoding='utf-8') as f:
        _evacuate = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'evacuate':
            return _evacuate

    with open(os.path.join(_cfg_path, _cfg_yaml[1]), encoding='utf-8') as f:
        _vehicle = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'vehicle':
            return _vehicle

    with open(os.path.join(_cfg_path, _cfg_yaml[2]), encoding='utf-8') as f:
        _environment = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'environment':
            return _environment

    with open(os.path.join(_cfg_path, _cfg_yaml[3]), encoding='utf-8') as f:
        _result = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'result':
            return _result

    with open(os.path.join(_cfg_path, _cfg_yaml[4]), encoding='utf-8') as f:
        _person = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'person':
            return _person

    with open(os.path.join(_cfg_path, _cfg_yaml[5]), encoding='utf-8') as f:
        _dose = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'dose':
            return _dose

    with open(os.path.join(_cfg_path, _cfg_yaml[6]), encoding='utf-8') as f:
        _emergency = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'emergency':
            return _emergency

    with open(os.path.join(_cfg_path, _cfg_yaml[7]), encoding='utf-8') as f:
        _public_transport = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'public_transport':
            return _public_transport

    with open(os.path.join(_cfg_path, _cfg_yaml[8]), encoding='utf-8') as f:
        _ship = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'ship':
            return _ship

    with open(os.path.join(_cfg_path, _cfg_yaml[9]), encoding='utf-8') as f:
        _tram = yaml.load(f, Loader=yaml.FullLoader)
        if select == 'tram':
            return _tram

    if select == 'all':
        return _evacuate, _vehicle, _environment, _result, _person, _dose, _emergency, _public_transport, _ship, _tram
    else:
        raise ValueError('select must be in evacuate, capacity, environment, result ro all')


# 字符串标准化
def standardization_xml(root):
    # 创建字符串
    xml_str = ET.tostring(root, encoding="utf-8")
    # 创建minidom解析器
    dom = minidom.parseString(xml_str)
    # 格式化XML
    pretty_xml_str = dom.toprettyxml(indent="  ")
    return pretty_xml_str


def get_similar_type_count(xml_path, type_name):
    evacuate = input_args(xml_path, 'evacuate')
    vehicle_data = evacuate['vehicle_number']

    vehicle_counts = {}

    for region in vehicle_data:
        for vehicle_type, count in vehicle_data[region].items():
            if vehicle_type in vehicle_counts:
                vehicle_counts[vehicle_type] += count
            else:
                vehicle_counts[vehicle_type] = count

    return vehicle_counts[type_name]


def get_distribute(count, distribute_type):
    pass


def get_all_lanes(net_xml_path):
    tree = ET.parse(net_xml_path)
    root = tree.getroot()
    lanes = root.findall('edge/lane')
    return lanes


def trips_template(pattern):
    trip_template = {}
    # 根据边生成路线
    if pattern == 'lane':
        trip_template = {
            "id": "",
            "type": "",
            "depart": "",
            "departLane": "best",
            "from": "",
            "to": "",
        }
    return trip_template


if __name__ == '__main__':
    get_all_lanes('osm.net.xml')
    # input_args(r'D:\Ysera\Ysera-Core\evacuate\cfg', 'all')
    # # get_similar_type_count(r'E:\Ysera-Core\evacuate\cfg', 'bus')
    # print('工具函数模块')
