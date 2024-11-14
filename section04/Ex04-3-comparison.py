'''
파일명: Ex04-3-comparison.py
내용: 관계 연산자(Comparison Operators)

관계 연산자란?
   - 두 개의 항을 비교하여 그 결과를 논리(bool) 자료형으로 반환
   - 비교 연산자(Comparison) 또는 비교 연산자(Relational)라고도 함

관계 연산자 종류
   > : 크다
   >= : 크거나 같다
   < : 작다
   <= : 작거나 같다
   == : 같다
   != : 같지 않다
'''

# 1. 기본 관계 연산자
print('===== 기본 관계 연산자 =====')
a = 15
print('{} > 10 : {}'.format(a, a > 10))     # True
print('{} < 10 : {}'.format(a, a < 10))     # False
print('{} >= 10 : {}'.format(a, a >= 10))   # True
print('{} <= 10 : {}'.format(a, a <= 10))   # False
print('{} == 10 : {}'.format(a, a == 10))   # False
print('{} != 10 : {}'.format(a, a != 10))   # True

# 2. 실수 비교
print('\n===== 실수 비교 =====')
b = 3.14
print('{} > 3 : {}'.format(b, b > 3))       # True
print('{} >= 3.14 : {}'.format(b, b >= 3.14)) # True
print('{} < 3.2 : {}'.format(b, b < 3.2))   # True

# 3. 문자열 비교
print('\n===== 문자열 비교 =====')
str1 = 'Python'
str2 = 'python'
print('{} == {} : {}'.format(str1, str2, str1 == str2))  # False
print('{} != {} : {}'.format(str1, str2, str1 != str2))  # True
print('{} > {} : {}'.format(str1, str2, str1 > str2))    # False
# 아스키 코드 값 비교: 'P'(80) < 'p'(112)

# 4. 복합 비교
print('\n===== 복합 비교 =====')
age = 25
print('나이: {}'.format(age))
print('20대 여부: {}'.format(20 <= age < 30))    # True
print('학생 (8~19세) 여부: {}'.format(8 <= age <= 19))  # False

# 5. 특수한 비교
print('\n===== 특수한 비교 =====')
# None 비교
x = None
print('x is None : {}'.format(x is None))        # True
print('x == None : {}'.format(x == None))        # True (is 사용 권장)

# 객체 비교
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print('list1 == list2 : {}'.format(list1 == list2))  # True (값 비교)
print('list1 is list2 : {}'.format(list1 is list2))  # False (객체 비교)

'''
실행 결과:
===== 기본 관계 연산자 =====
15 > 10 : True
15 < 10 : False
15 >= 10 : True
15 <= 10 : False
15 == 10 : False
15 != 10 : True

===== 실수 비교 =====
3.14 > 3 : True
3.14 >= 3.14 : True
3.14 < 3.2 : True

===== 문자열 비교 =====
Python == python : False
Python != python : True
Python > python : False

===== 복합 비교 =====
나이: 25
20대 여부: True
학생 (8~19세) 여부: False

===== 특수한 비교 =====
x is None : True
x == None : True
list1 == list2 : True
list1 is list2 : False
'''