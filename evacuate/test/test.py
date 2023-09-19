import seaborn as sns
import matplotlib.pyplot as plt

# 假设你有一些数据
times = [1, 2, 3, 4, 5]
pops = [10, 12, 15, 18, 20]
name = "Data"
zh_name = {"Data": "data111"}

# 设置图形大小
plt.figure(figsize=(14, 6))

# 创建Seaborn的lineplot
sns.lineplot(x=times, y=pops, label=zh_name[name])

# 获取当前的图形对象
ax = plt.gca()

# 将标签放在图的右下方
ax.legend(loc='upper left')

# 显示图形
plt.show()