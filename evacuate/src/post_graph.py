import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import xml.etree.ElementTree as ET
import os

__author__ = 'Nan Jia'
__email__ = 'KoiGoko@outlook.com'

from evacuate.src.utils import input_args

# 结果分析模块

result_path = r'/evacuate/xiapu/xiapu'


# 处理stop画图


def read_stop_xml(xml_path):
    context = ET.iterparse(xml_path)
    datas = {}
    i = 0
    for event, elem in context:
        if elem.tag == 'stopinfo' and event == 'end':
            stop = {'id': elem.get('id'),
                    'type': elem.get('type'),
                    'started': elem.get('started'),
                    'stop_lane': elem.get('lane'),
                    'ended': elem.get('ended')}

            i += 1
            datas[i] = stop
            elem.clear()
    datas = pd.DataFrame.from_dict(datas, orient='index')
    datas['started'] = datas['started'].astype(float)
    datas['ended'] = datas['ended'].astype(float)
    datas['stop_lane'] = datas['stop_lane'].str[:-2]
    datas = datas.sort_values(by=['started'])

    datas = datas.groupby('stop_lane').agg({'id': list, 'type': list, 'started': list, 'ended': list})
    return datas


if __name__ == '__main__':
    result_path = r'D:\Ysera\Ysera-Core\evacuate\xiapu\xiapu'
    stops = read_stop_xml(os.path.join(result_path, 'stop.xml'))

    vehicle = input_args(r'D:\Ysera\Ysera-Core\evacuate\cfg', 'vehicle')
    evacuate = input_args(r'D:\Ysera\Ysera-Core\evacuate\cfg', 'evacuate')
    population = evacuate['default_population']
    settlements = evacuate['settlements']
    reverse_settlements = {value: key for key, value in settlements.items()}
    vehicle_capacity = vehicle['vehicle_capacity']

    stop_infos = {}
    for pd_ele in stops.iterrows():

        lane = pd_ele[0]
        settle_name = reverse_settlements[lane]
        vehicles = []
        for i in pd_ele[1]['id']:
            if len(i.split('_')) == 4:
                vehicles.append(i.split('_')[0] + '_' + i.split('_')[3])
                continue
            vehicles.append(i.split('_')[0])

        types = pd_ele[1]['type']
        starts = []
        s = 0
        for i in types:
            value = vehicle_capacity.get(i)
            if 'public' in i:
                t = i.split('_')[1]
                value = population.get(t)
                continue
            s += value
            starts.append(s)

        start_times = pd_ele[1]['started']
        end_times = pd_ele[1]['ended']

        stop_infos[settle_name] = {'vehicles': vehicles,
                                   'types': types,
                                   'starts': starts,
                                   'start_times': start_times,
                                   'end_times': end_times}

    pd.DataFrame.from_dict(stop_infos, orient='index').to_csv(os.path.join(result_path, 'stop.csv'), sep=';')
    if os.path.exists('stop.xlsx'):
        os.remove('stop.xlsx')
    with pd.ExcelWriter('stop.xlsx') as writer:
        for i in stop_infos:
            print(i)
            pd_ele = pd.DataFrame.from_dict(stop_infos[i], orient='index')
            pd_ele.to_excel(writer, sheet_name=i)
    print('done')
