'''
Ex19-3-matplotlib3.py
'''

from matplotlib import font_manager, rc  # 폰트 관리를 위한 모듈 임포트
import matplotlib.pyplot as plt

# 한글 폰트 경로 설정 (윈도우의 맑은 고딕 폰트 사용)
font_path = 'C:\Windows\Fonts\malgun.ttf'

# 폰트 이름 가져오기 및 설정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)  # matplotlib의 기본 폰트를 한글 폰트로 변경

# Figure 객체 생성
figure = plt.figure()

# 1행 1열의 첫 번째 위치에 axes 생성 (111)
axes = figure.add_subplot(111)

# 파이 차트에 들어갈 데이터 값
data = [0.18, 0.3, 3.33, 3.75, 0.38, 25, 0.25, 2.75, 0.1]

# 각 데이터의 레이블 (한글 사용)
vitamin = ['비타민 A', '비타민 B1', '비타민 B2', '나이아신', '비타민 B6',
           '비타민 C', '비타민 D', '비타민 E', '엽산']

# 파이 차트 생성
# autopct='%0.1f%%': 각 섹션에 백분율을 소수점 첫째자리까지 표시
axes.pie(data, labels=vitamin, autopct='%0.1f%%')

# 파이 차트를 원형으로 표시 (종횡비를 1:1로 설정)
plt.axis('equal')

# 그래프 화면에 표시
plt.show()





