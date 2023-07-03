''''''"""
@author: Nan Jia
@time: 2023/6/7 16:11
@desc:
''''''"""
# 运行
# python run.py
import sys
import subprocess
if sys.version_info < (3, 7):
    raise RuntimeError("需要 Python 3.7 或更高版本")

# 运行 script1.py 并为其指定 Python 环境
subprocess.run(['python', 'script1.py'], check=True)

# 运行 script2.py 并为其指定 Python 环境
subprocess.run(['python', 'script2.py'], check=True)



