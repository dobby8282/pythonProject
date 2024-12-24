'''
파일명: Ex19-1-matplotlib.py

데이터 시각화(data visualization)
    데이터를 분석한 결과를 사용자가 쉽게 이해할 수 있도록
    표현하여 전달한것을 의미한다.

'''

import matplotlib.pyplot as plt  # Matplotlib 라이브러리에서 pyplot 모듈을 plt로 임포트

# Figure(도화지) 객체 생성 - 그래프를 그릴 전체 캔버스를 생성
figure = plt.figure()

# subplot 생성 (2행 2열의 그리드에서 3번째 위치에 axes 생성)
# add_subplot(223)에서 첫 번째 2는 행, 두 번째 2는 열, 세 번째 3은 위치를 의미
axes = figure.add_subplot(223)

# x축 데이터 - 월별 레이블
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# y축 데이터 - 월별 값
y = [1200, 800, 500, 400, 700, 800]

# 그래프 그리기
# linestyle='--': 점선 스타일
# marker='^': 삼각형 모양의 데이터 포인트 마커
# color='red': 빨간색 선 색상
axes.plot(x, y, linestyle='--', marker='^', color='red')

# 그래프 화면에 표시
plt.show()





