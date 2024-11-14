'''
파일명: Ex04-4-logical.py
내용: 논리 연산자(Logical Operators)

논리 연산자란?
   - 관계 연산자와 함께 사용되는 연산자
   - 2개 이상의 조건을 논리적으로 연결할 때 사용
   - 결과값으로 True 또는 False를 반환

논리 연산자 종류
   and : 두 조건 모두 True일 때만 True
   or  : 두 조건 중 하나라도 True이면 True
   not : 논리값을 반전 (True → False, False → True)

진리표 (Truth Table)
   and 연산자             or 연산자
   A   B   결과         A   B   결과
   F   F   F           F   F   F
   F   T   F           F   T   T
   T   F   F           T   F   T
   T   T   T           T   T   T
'''

# 1. 기본 논리 연산자
print('===== 기본 논리 연산자 =====')
a = 10
b = 0

# and 연산자
print('{} > 0 and {} > 0 : {}'.format(a, b, a > 0 and b > 0))   # False
print('{} > 0 and {} >= 0 : {}'.format(a, b, a > 0 and b >= 0)) # True

# or 연산자
print('{} > 0 or {} > 0 : {}'.format(a, b, a > 0 or b > 0))     # True
print('{} < 0 or {} < 0 : {}'.format(a, b, a < 0 or b < 0))     # False

# not 연산자
print('not {} : {}'.format(a, not a))    # False (0이 아닌 숫자는 True로 인식)
print('not {} : {}'.format(b, not b))    # True (0은 False로 인식)

# 2. 논리 연산자 활용
print('\n===== 논리 연산자 활용 =====')
age = 25
height = 175

# 군 입대 조건 (20세 이상, 키 170cm 이상)
is_eligible = age >= 20 and height >= 170
print('나이: {}, 키: {}'.format(age, height))
print('군 입대 가능 여부: {}'.format(is_eligible))

# 3. 진리값 판정
print('\n===== 진리값 판정 =====')
# False로 판정되는 값들
print('False로 판정되는 값들:')
print('0: {}'.format(bool(0)))           # False
print('빈 문자열: {}'.format(bool('')))   # False
print('None: {}'.format(bool(None)))     # False
print('빈 리스트: {}'.format(bool([])))   # False

# True로 판정되는 값들
print('\nTrue로 판정되는 값들:')
print('숫자 1: {}'.format(bool(1)))              # True
print('문자열 "False": {}'.format(bool("False"))) # True
print('리스트 [0]: {}'.format(bool([0])))        # True

# 4. 복합 논리 연산
print('\n===== 복합 논리 연산 =====')
x = 10
y = 20
z = 30

# 여러 조건 조합
result = x < y and y < z
print('{} < {} and {} < {} : {}'.format(x, y, y, z, result))  # True

result = x < y and y > z
print('{} < {} and {} > {} : {}'.format(x, y, y, z, result))  # False

result = not (x < y and y > z)
print('not ({} < {} and {} > {}) : {}'.format(x, y, y, z, result))  # True

'''
실행 결과:
===== 기본 논리 연산자 =====
10 > 0 and 0 > 0 : False
10 > 0 and 0 >= 0 : True
10 > 0 or 0 > 0 : True
10 < 0 or 0 < 0 : False
not 10 : False
not 0 : True

===== 논리 연산자 활용 =====
나이: 25, 키: 175
군 입대 가능 여부: True

===== 진리값 판정 =====
False로 판정되는 값들:
0: False
빈 문자열: False
None: False
빈 리스트: False

True로 판정되는 값들:
숫자 1: True
문자열 "False": True
리스트 [0]: True

===== 복합 논리 연산 =====
10 < 20 and 20 < 30 : True
10 < 20 and 20 > 30 : False
not (10 < 20 and 20 > 30) : True
'''