''''''"""
@author: Nan Jia
@time: 2023/6/7 10:24
@desc:
''''''"""
import traci
import os

cpu_counts = os.cpu_count()
cfg_dir = r'D:\sumo\xiapu\xiapu\osm.sumocfg'
# 启动 SUMO 模拟
traci.start(["sumo", "-c", cfg_dir])

# 主循环，模拟时间步长为 1 秒
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

# 加载路网和模型文件
traci.load(["-c", "path/to/sumo_config.sumocfg"])
traci.close()
