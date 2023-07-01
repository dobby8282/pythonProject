'''
파일명: Ex19-1-matplotlib.py

데이터 시각화(data visualization)
    데이터를 분석한 결과를 사용자가 쉽게 이해할 수 있도록
    표현하여 전달한것을 의미한다.

'''

import matplotlib.pyplot as plt

# Figure 객체 생성
fiqure = plt.figure()

axes = fiqure.add_subplot(223) # 행, 열, 번호
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
y = [1200, 800, 500, 400, 700, 800]
axes.plot(x, y, linestyle='--', marker='^', color='red')
plt.show()






