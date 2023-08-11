from evacuate.src.utils import input_args
import os
import ruamel.yaml


def global_init(_cfg_path):
    evacuate = input_args(_cfg_path, 'evacuate')
    vehicle = input_args(_cfg_path, 'vehicle')

    default_population = evacuate['default_population']
    vehicle_number = evacuate['vehicle_number']
    vehicle_capacity = vehicle['vehicle_capacity']
    修正之后的车辆数量 = {}
    new_vehicle_numbers = {}
    需要分配公共车辆的撤离点 = []
    need_distribution = []
    for key, value in default_population.items():
        new_vehicle_number = {}
        flag = True
        for key1, value1 in vehicle_number[key].items():
            for i in range(value1):
                default_population[key] -= vehicle_capacity[key1] * 1
                if default_population[key] <= 0:
                    new_vehicle_number[key1] = i + 1
                    need_distribution.append(key)
                    flag = False
                    break
            if not flag:
                break
            new_vehicle_number[key1] = value1

        new_vehicle_numbers[key] = new_vehicle_number

    with open(os.path.join(_cfg_path, 'evacuate.yaml'), 'r', encoding='utf-8') as file:
        yaml = ruamel.yaml.YAML()
        evacuate_yaml = yaml.load(file)

    # 替换整个 new_vehicle_numbers 部分
    evacuate_yaml['vehicle_number'] = new_vehicle_numbers
    need_distribution = [x for x in default_population.keys() if x not in need_distribution]
    evacuate_yaml['need_distribution'] = need_distribution

    # 将修改后的数据保存回YAML文件
    with open(os.path.join(_cfg_path, 'evacuate.yaml'), 'w', encoding='utf-8') as file:
        yaml.dump(evacuate_yaml, file)

    print(new_vehicle_numbers)
    print(need_distribution)


if __name__ == '__main__':
    global_init('全局初始化')
