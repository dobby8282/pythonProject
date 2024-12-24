'''
파일명: Ex19-5-matplotlib5.py
'''

import random  # 난수 생성을 위한 라이브러리
import matplotlib.pyplot as plt

# Figure 객체(전체 그래프를 담는 컨테이너) 생성
figure = plt.figure()

# 1행 2열의 그리드에서 첫 번째 위치에 axes 생성 (121)
axes = figure.add_subplot(121)

# 1행 2열의 그리드에서 두 번째 위치에 axes 생성 (122)
axes2 = figure.add_subplot(122)

# x축 데이터 생성 (0부터 100까지의 수를 리스트로)
# 리스트 컴프리헨션 사용
x = [n for n in range(101)]  # [0, 1, 2, ..., 100]

# y축 데이터를 저장할 빈 리스트 생성
y1 = []  # 첫 번째 그래프용 데이터
y2 = []  # 두 번째 그래프용 데이터

# 0부터 100까지 반복하면서 난수 생성
for i in range(101):
    y1.append(random.randint(0, 100))  # y1에 0~100 사이의 난수 추가
    y2.append(random.randint(0, 100))  # y2에 0~100 사이의 난수 추가

# 첫 번째 서브플롯에 선 그래프 그리기
# color='r': 빨간색 선
# marker='.': 점 형태의 마커
axes.plot(x, y1, color='r', marker='.')

# 두 번째 서브플롯에 막대 그래프 그리기
# color='g': 초록색 막대
axes2.bar(x, y2, color='g')

# 그래프 화면에 표시
plt.show()