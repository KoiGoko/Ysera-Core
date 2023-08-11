import evacuate.src.pre_private as private
import evacuate.src.pre_public as public
from evacuate.src.global_init import global_init
import glob
import os
import xml.etree.ElementTree as ET

__author__ = 'Nan Jia'
__email__ = 'KoiGoko@outlook.com'

if __name__ == '__main__':
    # 配置参数路径
    cfg_path = r'E:\Ysera-Core\evacuate\cfg'
    # 模拟文件路径
    xml_path = r'E:\Ysera-Core\evacuate\xiapu\xiapu'

    #
    global_init(cfg_path)
    ########################################################################################################################
    # 私家车配置初始化
    private.init_private_cfg(cfg_path)

    # 获取私家车车辆类型
    private_types = private.cal_private_trips_type()

    # 初始化私家车行程文件
    private.init_trips(xml_path, private_types)

    # 生成私家车行程文件
    private.generate_trips(xml_path)

    ########################################################################################################################

    # 初始化公共车辆调度

    # 配置初始化
    public.init_public_cfg(cfg_path)

    # 初始化公共车辆调度
    public.init_public_routes('custom')

    # 计算公共车辆类型
    public_types = public.cal_public_type('custom')

    # 初始化公共车辆行程文件
    public.init_public_xml(xml_path, public_types)

    # 生成公共车辆行程文件
    public.generate_public_trips(xml_path)

    ########################################################################################################################
    trips = glob.glob(os.path.join(xml_path, 'osm.*.trips.xml'))

    trip_name = [path.split('\\')[-1] for path in trips]

    trip_name = ', '.join(trip_name)

    sumo_cfg = r'E:\Ysera-Core\evacuate\xiapu\xiapu'

    sumo_cfg = os.path.join(sumo_cfg, 'osm.sumocfg')

    tree = ET.parse(sumo_cfg)

    root = tree.getroot()

    route_files_element = root.find('./input/route-files')

    route_files_element.attrib.pop('value')

    # Set the new value
    route_files_element.set('value', trip_name)

    # Save the changes to the XML file
    tree.write(sumo_cfg)
