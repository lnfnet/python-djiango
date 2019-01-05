#\usr\bin\python3
#coding=utf-8

import csv
filename = 'sitka_weather_07-2014.csv'
#打开csv文件读取第一行表头
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	print(header_row)
	#最高气温每天
	highs=[]
	for row in reader:
		high = int(row[1])
		highs.append(row[1])
	print(highs)

#指定头表头进行枚举数据格式化
for index, column_header in enumerate(header_row):
	print(index, column_header)
	
from matplotlib import pyplot as plt
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
# 设置图形的格式
plt.title(" July 2014",fontproperties="SimSun", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
