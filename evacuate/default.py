''''''"""
@author: Nan Jia
@time: 2023/6/21 13:51
@desc:
''''''"""
import os
path = 'cache'
if os.path.exists(path) and os.path.isdir(path):
    os.remove('path/to/file')
