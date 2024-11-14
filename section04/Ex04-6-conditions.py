'''
파일명: Ex04-6-conditions.py
내용: 조건 연산자(Conditional Operator) 또는 삼항 연산자(Ternary Operator)

조건 연산자란?
   - 조건식의 결과에 따라 참 또는 거짓의 결과를 반환하는 연산자
   - if-else문을 한 줄로 작성할 수 있어 코드를 간결하게 만들 수 있음

문법:
   결과값 = 참값 if 조건식 else 거짓값
'''

# 1. 기본 조건 연산자
print('===== 기본 조건 연산자 =====')
a = 20
b = 100

# 일반적인 if-else문
if a >= b:
   result = a - b
else:
   result = b - a

# 조건 연산자 사용
result = (a - b) if (a >= b) else (b - a)
print('{}과 {}의 차이는 {}입니다.'.format(a, b, result))

# 2. 조건 연산자 활용 예제
print('\n===== 조건 연산자 활용 =====')
# 점수에 따른 합격/불합격
score = 75
result = "합격" if score >= 70 else "불합격"
print('점수 {}: {}'.format(score, result))

# 홀수/짝수 판별
num = 11
result = "짝수" if num % 2 == 0 else "홀수"
print('{}: {}'.format(num, result))

# 절댓값 계산
x = -99
abs_x = x if x >= 0 else -x
print('{}의 절댓값: {}'.format(x, abs_x))

# 3. 중첩 조건 연산자
print('\n===== 중첩 조건 연산자 =====')
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print('점수 {}: 등급 {}'.format(score, grade))

# 4. 조건 연산자와 문자열 포매팅
print('\n===== 조건 연산자와 문자열 포매팅 =====')
age = 20
status = "성인" if age >= 20 else "미성년자"
print('나이 {}세: {}'.format(age, status))

temperature = 38.5
condition = "정상" if temperature <= 37.5 else "발열"
print('체온 {:.1f}도: {}'.format(temperature, condition))

'''
실행 결과:
===== 기본 조건 연산자 =====
20과 100의 차이는 80입니다.

===== 조건 연산자 활용 =====
점수 75: 합격
11: 홀수
-99의 절댓값: 99

===== 중첩 조건 연산자 =====
점수 85: 등급 B

===== 조건 연산자와 문자열 포매팅 =====
나이 20세: 성인
체온 38.5도: 발열
'''