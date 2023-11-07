import os
import xml.etree.ElementTree as ET
import glob
import logging
import itertools
from evacuate.src.utils import input_args
from evacuate.src.utils import standardization_xml
from evacuate.src.pre_vehicle import get_vehicle_speed
from evacuate.src.pre_vehicle import init_vehicle_cfg
from evacuate.src.utils import get_similar_type_count
import evacuate.src.evacuate_distribution as evacuate_distribution

evacuate = {}
pb_info = {}
cfg_path = ''


# 配置初始化
def init_public_cfg(_cfg_path):
    _evacuate = input_args(_cfg_path, 'evacuate')
    global cfg_path
    cfg_path = _cfg_path
    evacuate.update(_evacuate)
