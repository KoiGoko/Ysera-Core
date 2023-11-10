# 添加自定义交通灯
import xml.etree.ElementTree as ET

from evacuate.src.utils import input_args

public_transport_cfg = {}
cfg_path = ''


def init_public_transport_cfg(_cfg_path):
    _public_transport_cfg = input_args(_cfg_path, 'public_transport')
    global cfg_path
    cfg_path = _cfg_path
    public_transport_cfg.update(_public_transport_cfg)


def init_custom_traffic_light(net_path):
    custom_light_info = public_transport_cfg['traffic_light']
    traffic_names = custom_light_info.keys()
    light_connect_lanes = custom_light_info.values()
    net_tree = ET.parse(net_path)
    net_root = net_tree.getroot()
    net_root.find('connections')
    for net_root in net_tree.iter('connection'):
        if net_root.get('from') in light_connect_lanes:
            net_root.set('tl', 'custom_light')


def generate_custom_traffic_light_xml(xml_path):
    return 'hello world'


def init_traffic_light():
    init_public_transport_cfg(cfg_path)


if __name__ == '__main__':
    print(init_traffic_light())
