''''''"""
@author: Nan Jia
@time: 2023/6/7 10:46
@desc:
''''''"""
# 自定义输入
trips_dir = r'D:\sumo\xiapu\xiapu'

# 安置点
settlement_points = {
    '霞浦第十八中学': '977360507#0',
    '霞浦县第六小学': '-51691749#4',
    '霞浦县第四小学': '715792677',
    '霞浦县第一中学': '1172895350#7',
    '福宁中学': '543863877#1',
    '霞浦县实验幼儿园': '-777284203',
    '福建宏翔高级中学': '-778378294',
    '福建霞浦第六中学': '1172895341#1',
    '霞浦县人民政府': '544267905#1'
}
# 撤离点
pop_points = {
    'dongchong': '1163782197#2',
    'beibi': '296185646#0',
    'beigang': '1068471749#0',
    'houshan': '1068471755#2',
    'panqian': '1068471755#2',
    'xiahu': '229540619#2',
    'jinxie': '1164353535',
    'liujin': '-474258045',
    'changchun': '978380505#6',
    'xiaxi': '-1163559853#0',
    'wuqu': '778098717#0',
    'changmen': '-1164370191',
    'xiapunuclear': '978658158#0',
    'tingxiaxi': '-1163559854#0',
    'waihaihu': '778098710#1',
    'qiuzhugang': '588559167#3',
    'yuyang': '978380509#0',
    'shangqi': '-1163801077'
}

# 撤离人口
population = {
    '东冲村南一口': 80000,
    '东冲村南二口': 80000,
    '东冲村出口': 80000,
    '北壁乡北口': 80000,
    '北壁乡南口': 80000,
    '北港村': 80000,
    '后山刘前村': 80000,
    '牛角湾蜂坑村': 80000,
    '盘前村': 80000,
    '下浒镇一口': 80000,
    '下浒镇二口': 80000,
    '下浒镇三口': 80000,
    '金蟹村一口': 80000,
    '金蟹村二口': 80000,
    '留金村': 80000,
    '吕侠村一口': 80000,
    '吕侠村二口': 80000,
    '长春镇': 80000,
    '下溪村': 80000,
    '武曲村': 80000,
    '长门村': 80000,
    '霞浦核电': 80000,
    '亭下溪村': 80000,
    '外海湖村': 80000,
    '秋竹岗村': 80000,
    '渔洋村': 80000,
    '上崎村': 80000
}

dongchong = {
    '总人口': 21672,
    '私家车': 632,
    '三轮车': 503,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

beibi = {
    '总人口': 13386,
    '私家车': 632,
    '三轮车': 925,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

beigang = {
    '总人口': 28844,
    '私家车': 780,
    '三轮车': 344,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

houshan = {
    '总人口': 23820,
    '私家车': 438,
    '三轮车': 785,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}
293
niujiaowan = {
    '总人口': 45781,
    '私家车': 1139,
    '三轮车': 403,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

panqian = {
    '总人口': 21678,
    '私家车': 1237,
    '三轮车': 293,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

xiahu = {
    '总人口': 9912,
    '私家车': 853,
    '三轮车': 228,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

jinjie = {
    '总人口': 44627,
    '私家车': 1179,
    '三轮车': 570,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

liujin = {
    '总人口': 1017,
    '私家车': 1912,
    '三轮车': 381,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

lvxia = {
    '总人口': 7889,
    '私家车': 1200,
    '三轮车': 223,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

changchun = {
    '总人口': 40564,
    '私家车': 512,
    '三轮车': 272,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

xiaxi = {
    '总人口': 2213,
    '私家车': 1167,
    '三轮车': 366,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

wuqu = {
    '总人口': 44141,
    '私家车': 774,
    '三轮车': 781,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

changmen = {
    '总人口': 28105,
    '私家车': 1760,
    '三轮车': 926,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

tinxiaxi = {
    '总人口': 23460,
    '私家车': 1581,
    '三轮车': 744,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

waihaihu = {
    '总人口': 20403,
    '私家车': 539,
    '三轮车': 514,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15985
}

qiuzhugang = {
    '总人口': 43404,
    '私家车': 672,
    '三轮车': 985,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

yuyang = {
    '总人口': 28103,
    '私家车': 1216,
    '三轮车': 720,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

xiapu_nuclear = {
    '总人口': 5000,
    '私家车': 432,
    '三轮车': 50,
    '公交车': 10,
    '摩托车': 420,
    '出租车': 15
}

vehicle_capacity = {
    'bus': 50,
    'private': 5,
    'motorcycle': 2,
    'tricycle': 3,
    'taxi': 4
}

countrys = [
    'dongchong', 'beibi', 'beigang', 'houshan', 'panqian', 'xiahu', 'jinjie', 'liujin',
    'lvxia', 'changchun', 'xiaxi', 'wuqu', 'changmen', 'tinxiaxi', 'waihaihu', 'qiuzhugang', 'yuyang', 'xiapu_nuclear'
]

vehicle_en = {
    '私家车': 'private',
    '三轮车': 'tricycle',
    '公交车': 'bus',
    '摩托车': 'motorcycle',
    '出租车': 'taxi'
}

vehicles = ['bus', 'private', 'motorcycle', 'taxi', 'tricycle']



