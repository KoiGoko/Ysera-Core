''''''"""
@author: Nan Jia
@time: 2023/6/7 10:25
@desc:
''''''"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import xml.etree.ElementTree as ET

trip_info = ET.parse(r'D:\sumo\xiapu\xiapu\tripinfo.xml')
trip_info_root = trip_info.getroot()
trip_infos = trip_info_root.findall('tripinfo')
data = []
for trip_info in trip_infos:
    row = {'id': trip_info.get('id'),
           'depart': float(trip_info.get('depart')),
           'departLane': trip_info.get('departLane'),
           'departPos': float(trip_info.get('departPos')),
           'departSpeed': float(trip_info.get('departSpeed')),
           'departDelay': float(trip_info.get('departDelay')),
           'arrival': float(trip_info.get('arrival')),
           'arrivalLane': trip_info.get('arrivalLane'),
           'arrivalPos': float(trip_info.get('arrivalPos')),
           'arrivalSpeed': float(trip_info.get('arrivalSpeed')),
           'duration': float(trip_info.get('duration')),
           'routeLength': float(trip_info.get('routeLength')),
           'waitingTime': float(trip_info.get('waitingTime')),
           'waitingCount': float(trip_info.get('waitingCount')),
           'stopTime': float(trip_info.get('stopTime')),
           'timeLoss': float(trip_info.get('timeLoss')),
           'rerouteNo': float(trip_info.get('rerouteNo')),
           'devices': trip_info.get('devices'),
           'vType': trip_info.get('vType'),
           'speedFactor': float(trip_info.get('speedFactor')),
           'vaporized': trip_info.get('vaporized'),
           }
    data.append(row)

df = pd.DataFrame(data).sort_values('id')
# df.to_csv('tripinfo.csv', index=False)

grouped_df = df.groupby('vType')['duration'].mean().reset_index()

plt.Figure(figsize=(10, 5))
sns.barplot(x='vType', y='duration', data=grouped_df)
plt.xlabel('Vehicle Type')
plt.ylabel('Average Duration')
plt.title('Average Duration by Vehicle Type')
plt.show()

print('hello')
