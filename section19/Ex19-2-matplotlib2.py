'''
파일명: Ex19-2-matplotlib2.py
'''
import matplotlib.pyplot as plt  # Matplotlib 라이브러리 임포트

# Figure와 Axes 객체를 동시에 생성
# fig: 전체 그래프를 담는 컨테이너
# ax: 실제 그래프가 그려지는 영역
fig, ax = plt.subplots()

# 그래프에 사용될 데이터 설정
fruits = ['apple', 'blueberry', 'cherry', 'orange']  # x축에 표시될 과일 이름
counts = [40, 100, 30, 55]  # 각 과일의 수량 데이터
bar_labels = ['red', 'blue', '_red', 'orange']  # 각 막대의 레이블 (_red는 범례에서 제외됨)
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']  # 각 막대의 색상

# 막대 그래프 생성
# fruits: x축 위치
# counts: 각 막대의 높이
# label: 범례에 표시될 레이블
# color: 막대의 색상
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

# y축 레이블 설정
ax.set_ylabel('fruit supply')

# 그래프 제목 설정
ax.set_title('Fruit supply by kind and color')

# 범례 표시 및 범례 제목 설정
ax.legend(title='Fruit color')

# 그래프 화면에 표시
plt.show()