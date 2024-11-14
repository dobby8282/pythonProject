'''
파일명: Ex03-5-casting.py
내용: 형변환(Type Casting)

형변환(casting)이란?
   - 변수나 값의 자료형을 다른 자료형으로 변환하는 것
   - 파이썬의 주요 형변환 함수: int(), float(), str()
   - 데이터 처리나 연산 시 자료형을 일치시키기 위해 사용
'''

# 1. 정수형 변환 - int()
print('===== 정수형 변환 =====')
print(int(1))          # 정수 1
print(int(2.8))        # 실수 -> 정수 (소수점 버림)
print(int('3'))        # 문자열 -> 정수
print(int('10', 2))    # 2진수 문자열 -> 정수
print(int('A', 16))    # 16진수 문자열 -> 정수

# 2. 실수형 변환 - float()
print('\n===== 실수형 변환 =====')
print(float(1))        # 정수 -> 실수
print(float('3'))      # 문자열 -> 실수
print(float('3.14'))   # 문자열 -> 실수

# 3. 문자열 변환 - str()
print('\n===== 문자열 변환 =====')
x = str(1)    # 정수 -> 문자열
y = str(2)    # 정수 -> 문자열
print('문자열 연결: ' + x + y)    # 문자열 + 문자열 = 문자연결
print('곱셈: ' + str(int(x) * int(y)))    # 문자열로 변환된 계산 결과

# 4. 문자와 아스키코드 변환
print('\n===== 아스키코드 변환 =====')
# 문자 -> 아스키코드
print('A의 아스키코드: {}'.format(ord('A')))
print('a의 아스키코드: {}'.format(ord('a')))
print('0의 아스키코드: {}'.format(ord('0')))

# 아스키코드 -> 문자
print('아스키코드 65: {}'.format(chr(65)))    # A
print('아스키코드 97: {}'.format(chr(97)))    # a
print('아스키코드 48: {}'.format(chr(48)))    # 0

# 5. 형변환 주의사항
print('\n===== 형변환 주의사항 =====')
# 1) 문자열 정수 vs 정수
str_num = "123"
num = 123
print('타입 비교: str_num={}, num={}'.format(type(str_num), type(num)))
print('값 비교: str_num={}, num={}'.format(str_num, num))

# 2) 계산 시 형변환 영향
print('문자열 연결: ' + str_num + str_num)    # 123123
print('숫자 계산: ' + str(num + num))         # 246

'''
형변환 불가능한 경우 - 에러 발생
x = int('Hello')    # ValueError
y = float('3.14.15')# ValueError
z = int('3.14')     # ValueError
'''