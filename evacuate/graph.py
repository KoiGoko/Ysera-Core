''''''"""
@author: Nan Jia
@time: 2023/6/7 10:25
@desc:
''''''"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

stop_data = pd.read_csv(r'D:\Ysera\Ysera-Core\evacuate\xiapu\xiapu\stop.csv', sep=';')

grouped = stop_data.groupby('stopinfo_id')['stopinfo_ended'].apply(list)

grouped = grouped.reset_index()
sum1 = 1200
capacity = 40
x = grouped['stopinfo_ended'][5]
y = [1200, 800, 300]
sns.set_style('darkgrid')
sns.lineplot(x=x, y=y)
plt.xticks(x)
plt.yticks(y)
plt.legend()
plt.xlabel('time')
plt.ylabel('population')
plt.title('population change')
plt.show()
print(grouped)
print('hello')
