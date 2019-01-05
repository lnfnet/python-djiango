#\usr\bin\python3
#coding=utf-8

import csv
filename = 'sitka_weather_07-2014.csv'
#��csv�ļ���ȡ��һ�б�ͷ
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	print(header_row)
	#�������ÿ��
	highs=[]
	for row in reader:
		high = int(row[1])
		highs.append(row[1])
	print(highs)

#ָ��ͷ��ͷ����ö�����ݸ�ʽ��
for index, column_header in enumerate(header_row):
	print(index, column_header)
	
from matplotlib import pyplot as plt
# �������ݻ���ͼ��
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
# ����ͼ�εĸ�ʽ
plt.title(" July 2014",fontproperties="SimSun", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
