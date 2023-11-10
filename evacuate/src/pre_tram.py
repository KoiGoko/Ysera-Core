import glob
import logging
import os
import xml.etree.ElementTree as ET

from evacuate.src.pre_vehicle import get_vehicle_speed
from evacuate.src.pre_vehicle import init_vehicle_cfg
from evacuate.src.utils import input_args

_author_ = 'Nan Jia'
_email_ = 'KoiGoko@outlook.com'

# 非公共车辆模拟环境预处理模块

# 配置日志记录器
logging.basicConfig(filename='../sumo.log', level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')

tram = {}
cfg_path = ''


# 配置初始化
def init_private_cfg(_cfg_path):
    _tram = input_args(_cfg_path, 'tram')
    global cfg_path
    cfg_path = _cfg_path
    tram.update(_tram)


def init_tram_trips(_xml_path, _vehicle_names):
    # 清除已经存在的trips文件
    files = glob.glob(os.path.join(_xml_path, f'osm.{simulator_name}.*.trips.xml'))
    if not files:
        print('新的非公共车辆行程文件初始化')
    else:
        for file in files:
            if os.path.exists(file):
                os.remove(file)
                print('remove file: {}'.format(file))
    # 创建根元素 routes
    root = ET.Element("routes")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:noNamespaceSchemaLocation", "http://sumo.dlr.de/xsd/routes_file.xsd")

    # 获取自定义的车辆速度

    # 配置初始化
    init_vehicle_cfg(cfg_path)
    speeds = get_vehicle_speed()

    try:
        for vehicle_name in _vehicle_names:
            tree = ET.ElementTree(root)
            # 创建 vType 元素
            vtype = ET.SubElement(root, "vType")
            vtype.set("id", vehicle_name)
            vtype.set("vClass", vehicle_name)
            # 设置车辆速度
            vtype.set('maxSpeed', str(speeds[vehicle_name]))

            filename = f"osm.{simulator_name}.{vehicle_name}.trips.xml"

            tree.write(os.path.join(_xml_path, filename), encoding="utf-8", xml_declaration=True)
            root.remove(vtype)
    except Exception as e:
        logging.error("行程文件生成异常：{}".format(e))


def pre_tram(_cfg_path, _xml_path):
    init_private_cfg(_cfg_path)


if __name__ == '__main__':
    print('轨道交通模拟环境预处理模块')
