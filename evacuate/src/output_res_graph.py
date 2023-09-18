import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so
import os
import glob


def process_evacuate_graph(path, graph_title):
    evacuate_path = os.path.join(path, 'evacuate.xlsx')
    evacuate_datas = pd.read_excel(evacuate_path, sheet_name=None, index_col=0)
    evacuate_names = list(evacuate_datas.keys())

    sns.set()

    zh_name = {
        'dianchang_huaneng': '电厂-华能',
        'dianchang_zhonghe': '电厂-中核',
        'changmen': '长门村',
        'tiantang': '天堂村',
        'yujiadi': '渔家地村',
        'wuqu': '武曲村',
        'doumi': '斗米村',
        'jishi': '积石村',
        'yuyangli': '渔洋里村',
        'yuyanghan': '渔洋垾村',
        'qiuzhugang': '秋竹岗村',
        'zhizhuwang': '蜘蛛网村',
        'tingxiaxi': '亭下溪村',
        'xiayangcheng': '下洋城村',
        'gaoluo': '高罗海滩旅游景点',
        'dajing': '大京村',
        'zucuo': '祖厝村',
        'chuanlu': '传胪村',
        'changchun': '长春镇'
    }

    plt.figure(figsize=(10, 6))
    for name in evacuate_names:
        sums = evacuate_datas[name].loc['sum'].values
        pops = evacuate_datas[name].loc['start_times'].values / 3600
        sns.lineplot(x=pops, y=sums, label=zh_name[name])

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.title(graph_title)
    plt.xlabel('时间（小时）')
    plt.ylabel('撤离人数')
    plt.legend(title='待撤离点')

    plt.savefig(os.path.join(path, 'evacuate_' + graph_title + '.png'))


def process_settlement_graph(path, graph_title):
    settlement_path = os.path.join(path, 'settlement.xlsx')
    evacuate_path = os.path.join(path, 'evacuate.xlsx')
    evacuate_names = list(pd.read_excel(evacuate_path, sheet_name=None, index_col=0).keys())

    settlement_datas = pd.read_excel(
        settlement_path,
        sheet_name=[sheet for sheet in pd.ExcelFile(settlement_path).sheet_names
                    if sheet not in evacuate_names], index_col=0)

    settlement_names = list(settlement_datas.keys())

    sns.set()

    plt.figure(figsize=(10, 6))
    for name in settlement_names:
        sums = settlement_datas[name].loc['starts'].values
        pops = settlement_datas[name].loc['start_times'].values / 3600
        sns.lineplot(x=pops, y=sums, label=name)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.title(graph_title)
    plt.xlabel('时间（小时）')
    plt.ylabel('到达安置点人数')
    plt.legend(title='安置点')

    plt.savefig(os.path.join(path, 'settlement_' + graph_title + '.png'))


def process_road_graph(road_id):
    pass


if __name__ == '__main__':
    paths = glob.glob(r'F:\厂址应急道路专题数据\*')

    for path in paths:
        graph_title = os.path.basename(path)

        process_evacuate_graph(path, graph_title)
        process_settlement_graph(path, graph_title)
