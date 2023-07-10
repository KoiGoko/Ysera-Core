import subprocess
import pandas as pd

# 定义SUMO命令
sumo_cmd = "sumo -c osm.sumocfg"

# 执行SUMO命令并捕获输出
output = subprocess.check_output(sumo_cmd, shell=True)

data = {}
# 将输出解码为字符串并打印
output_str = output.decode('utf-8')
lines = output_str.strip().split('\n')
for line in lines:
    if ':' in line:
        key, value = line.split(':')
        key = key.strip()
        value = value.strip()
        try:
            value = float(value)
        except ValueError:
            pass
        data[key] = value

# 创建DataFrame
df = pd.DataFrame.from_dict(data, orient='index', columns=['Value'])
print(df)
print(output_str)
