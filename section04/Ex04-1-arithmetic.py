'''
파일명: Ex04-1-arithmetic.py
내용: 산술연산자(Arithmetic Operators)

연산자(Operators)란?
   - 특정한 작업을 수행하기 위해서 사용하는 기호
   - 수학적 계산이나 프로그램 로직을 구현할 때 사용

산술연산자 종류
   + : 덧셈
   - : 뺄셈
   * : 곱셈
   ** : 거듭제곱
   / : 나누기 (실수형 반환)
   // : 몫 (정수형 반환)
   % : 나머지
'''

# 1. 기본 산술연산
print('===== 기본 산술연산 =====')
a = 7
b = 2

print('{} + {} = {}'.format(a, b, a + b))    # 덧셈
print('{} - {} = {}'.format(a, b, a - b))    # 뺄셈
print('{} * {} = {}'.format(a, b, a * b))    # 곱셈
print('{} ** {} = {}'.format(a, b, a ** b))  # 거듭제곱
print('{} / {} = {}'.format(a, b, a / b))    # 나누기
print('{} // {} = {}'.format(a, b, a // b))  # 몫
print('{} % {} = {}'.format(a, b, a % b))    # 나머지

# 2. 산술연산 활용 예제
print('\n===== 산술연산 활용 =====')
# 원의 넓이 구하기 (π * r²)
radius = 5
pi = 3.14159
area = pi * (radius ** 2)
print('반지름이 {}인 원의 넓이: {:.2f}'.format(radius, area))

# 시간 계산
total_minutes = 125
hours = total_minutes // 60    # 시간 (몫)
minutes = total_minutes % 60   # 분 (나머지)
print('{}분은 {}시간 {}분입니다.'.format(total_minutes, hours, minutes))

# 3. 주의사항
print('\n===== 주의사항 =====')
# 1) 나누기 연산자(/)는 항상 실수 반환
print('5 / 2 = {}'.format(5 / 2))      # 2.5
print('4 / 2 = {}'.format(4 / 2))      # 2.0

# 2) 몫 연산자(//)는 정수 반환
print('5 // 2 = {}'.format(5 // 2))    # 2
print('4 // 2 = {}'.format(4 // 2))    # 2

# 3) 나머지 연산자(%)의 결과는 항상 0 이상, 나누는 수 미만
print('5 % 2 = {}'.format(5 % 2))      # 1
print('4 % 2 = {}'.format(4 % 2))      # 0

'''
실행 결과:
===== 기본 산술연산 =====
7 + 2 = 9
7 - 2 = 5
7 * 2 = 14
7 ** 2 = 49
7 / 2 = 3.5
7 // 2 = 3
7 % 2 = 1

===== 산술연산 활용 =====
반지름이 5인 원의 넓이: 78.54
125분은 2시간 5분입니다.

===== 주의사항 =====
5 / 2 = 2.5
4 / 2 = 2.0
5 // 2 = 2
4 // 2 = 2
5 % 2 = 1
4 % 2 = 0
'''