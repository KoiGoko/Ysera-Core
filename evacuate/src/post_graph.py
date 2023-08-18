import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import subprocess
import xml.etree.ElementTree as ET
import os
import msgpack
from lxml import etree

__author__ = 'Nan Jia'
__email__ = 'KoiGoko@outlook.com'

from evacuate.src.utils import input_args

# 结果分析模块

result_path = r'/evacuate/xiapu/xiapu'


def input_pandas():
    _data = pd.read_csv(os.path.join(result_path, 'stop.csv'), sep=';')
    return _data


# 处理stop画图
def graph_stop(_pd):
    # 设置随机种子，确保x轴和y轴的抽样一致
    random_seed = 42
    # 对x轴和y轴同时进行抽样，抽取一部分数据点
    _pd = _pd.sample(n=200, random_state=random_seed)
    _pd = _pd.sort_values(by='stopinfo_started')
    start = 0
    number = []
    vehicle_cap = {'taxi': 4, 'private': 4, 'motorcycle': 2, 'tricycle': 3}
    types = _pd['stopinfo_type']
    for i in types:
        value = vehicle_cap.get(i)
        start += value
        number.append(start)

    arrival_time = _pd['stopinfo_started']

    sns.lineplot(x=arrival_time, y=number, hue=types, alpha=0.8, palette='bright')
    plt.xlabel('time')
    plt.ylabel('number')

    plt.show()
    print('done')


def graph_fcd(xml_path):
    xml_file = os.path.join(xml_path, 'fcd.xml')
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # 要保留的特定 lane
    target_lane = "588559167#3_0"

    # 找到所有名为 "timestep" 的节点
    timesteps = root.findall(".//timestep")

    remove_timestep = []
    # 遍历timestep节点
    for timestep in timesteps:
        # 找到当前timestep节点下所有名为 "vehicle" 的节点
        vehicles = timestep.findall(".//vehicle")
        # 遍历vehicle节点并移除不满足目标lane值的节点
        flag = False
        for vehicle in vehicles:
            if vehicle.get("lane") == target_lane:
                flag = True
                continue
            if vehicle.get("lane") != target_lane:
                # 如果lane值不是目标值，则从父节点中移除当前vehicle节点
                timestep.remove(vehicle)
        if not flag:
            root.remove(timestep)
        # 如果当前timestep节点下没有vehicle节点，则将当前timestep节点添加到待移除列表中
    tree.write('modified_xml_file.xml')

    tree1 = ET.parse('modified_xml_file.xml')
    root1 = tree1.getroot()

    # 找到所有名为 "timestep" 的节点
    timesteps1 = root1.findall(".//timestep")

    vehicle_count = {}
    for timestep1 in timesteps1:
        vehicles = timestep1.findall(".//vehicle")
        vehicle_count[timestep1.get("time")] = len(vehicles)
    print(vehicle_count)
    # 保存修改后的XML文件
    timestep_list = list(vehicle_count.keys())
    vehicle_number = list(vehicle_count.values())
    # 画图
    sns.lineplot(x=timestep_list, y=vehicle_number, alpha=0.9)
    plt.xlabel('timestep')
    plt.ylabel('vehicle_number')

    plt.show()

    print('done')


def read_output_xml():
    xml_file_path = r'/evacuate/xiapu/xiapu/stop1.xml'
    tree = etree.parse(xml_file_path, parser=etree.XMLParser(encoding='utf-8'))
    root = tree.getroot()

    evacuate = input_args(r'D:\Ysera\Ysera-Core\evacuate\cfg', 'evacuate')

    settlements = evacuate['settlements']
    default_population = evacuate['default_population']

    settles = [x + '_0' for x in settlements.values()]

    print(settles)

    data = []
    for settle in settles:
        elements = []
        elements.extend(root.xpath(f'//stopinfo[@lane="{settle}"]'))
        print(elements)
        if len(elements) > 0:
            for stopinfo in elements:
                id = stopinfo.get('id')
                type = stopinfo.get('type')
                lane = stopinfo.get('lane')
                pos = stopinfo.get('pos')
                parking = stopinfo.get('parking')

                print(id, type, lane, pos, parking)

                data.append([id, type, lane, pos, parking])

    pd_data = pd.DataFrame(data, columns=['id', 'type', 'lane', 'pos', 'parking'])
    print(pd_data)

    # root = tree.getroot()
    # xml_data = r'D:\Ysera\Ysera-Core\evacuate\xiapu\xiapu\fcd.xml'
    # binary_data = msgpack.packb(xml_data)
    #
    # decoded_data = msgpack.unpackb(binary_data)
    #
    # df = pd.DataFrame([decoded_data])
    # print(df)
    # print(binary_data)


if __name__ == '__main__':
    read_output_xml()
    # graph_fcd(result_path)
    # # pd = input_pandas()
    # # graph_stop(pd)
    # print('结果后处理模块')
