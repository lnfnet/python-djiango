# coding=UTF-8
import matplotlib.pyplot as plt
from random import randint
import pygal

"""squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)
#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

plt.scatter(2, 4)
plt.show() """


class Die():
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides
    def roll(self):
        """"返回一个位于1和骰子面数之间的随机值"""
        return randint(1,self.num_sides)
die=Die()
results=[]
for roll_num in range(100):
    result=die.roll()
    results.append(result)

# print(results)



# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
print(frequencies)
hist.render_to_file('die_visual.svg')
