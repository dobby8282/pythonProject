'''
파일명: Ex19-2-matplotlib2.py
'''
import matplotlib.pyplot as plt


# Figure와 Axes 객체 생성
fig, ax = plt.subplots()

# 데이터설정
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

# 막대 그래프
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')

#범례 제목설정
ax.legend(title='Fruit color')

plt.show()
