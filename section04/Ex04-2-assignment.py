'''
파일명: Ex04-2-assignment.py
내용: 대입 연산자(Assignment Operators)와 print 형식문자

대입 연산자란?
   - 변수에 값을 저장하기 위해 사용하는 연산자
   - 단순 대입 연산자(=)
   - 복합 대입 연산자(+=, -=, *=, /=, %=, **=, //=)

print 형식문자(Format Specifiers)
   %d : 정수(decimal) 데이터
   %f : 실수(float) 데이터
   %o : 8진수(octal) 데이터
   %x : 16진수(hexadecimal) 데이터
   %s : 문자열(string) 데이터
   %c : 문자(character) 하나 데이터
'''

# 1. 기본 대입 연산자
print('===== 기본 대입 연산자 =====')
a = 10          # 단일 변수 대입
b = 20
print('a = %d, b = %d' % (a, b))

# 다중 변수 대입
x, y, z = 1, 2, 3
print('x = %d, y = %d, z = %d' % (x, y, z))

# 2. 값 교환하기(Swapping)
print('\n===== 값 교환하기 =====')
print('교환 전: a = %d, b = %d' % (a, b))

# 방법 1 - 임시 변수 사용
'''
tmp = a
a = b
b = tmp
'''

# 방법 2 - 파이썬 다중 대입 활용
a, b = b, a
print('교환 후: a = %d, b = %d' % (a, b))

# 3. 복합 대입 연산자
print('\n===== 복합 대입 연산자 =====')
piggy_bank = 0
money = 10000

# 입금 예제
piggy_bank += money    # piggy_bank = piggy_bank + money
print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
print('현재 잔액: {}원'.format(piggy_bank))

# 출금 예제
snack = 2000
piggy_bank -= snack    # piggy_bank = piggy_bank - snack
print('저금통에서 스낵 구입비 {}원을 뺐습니다.'.format(snack))
print('현재 잔액: {}원'.format(piggy_bank))

# 4. 다양한 복합 대입 연산자
print('\n===== 다양한 복합 대입 연산자 =====')
number = 10
print('처음 숫자: {}'.format(number))

number += 2    # 더하기
print('+= 2 -> {}'.format(number))

number -= 3    # 빼기
print('-= 3 -> {}'.format(number))

number *= 2    # 곱하기
print('*= 2 -> {}'.format(number))

number /= 2    # 나누기
print('/= 2 -> {}'.format(number))

# 5. print 형식문자 활용
print('\n===== print 형식문자 활용 =====')
name = "Alice"
age = 25
height = 165.5
print('이름: %s' % name)              # 문자열
print('나이: %d세' % age)             # 정수
print('신장: %.1f cm' % height)       # 실수(소수점 1자리)
print('8진수: %o' % age)              # 8진수
print('16진수: %x' % age)             # 16진수
print('%c씨는 %d세입니다.' % (name[0], age))   # 문자와 정수

'''
실행 결과:
===== 기본 대입 연산자 =====
a = 10, b = 20
x = 1, y = 2, z = 3

===== 값 교환하기 =====
교환 전: a = 10, b = 20
교환 후: a = 20, b = 10

===== 복합 대입 연산자 =====
저금통에 용돈 10000원을 넣었습니다.
현재 잔액: 10000원
저금통에서 스낵 구입비 2000원을 뺐습니다.
현재 잔액: 8000원

===== 다양한 복합 대입 연산자 =====
처음 숫자: 10
+= 2 -> 12
-= 3 -> 9
*= 2 -> 18
/= 2 -> 9.0

===== print 형식문자 활용 =====
이름: Alice
나이: 25세
신장: 165.5 cm
8진수: 31
16진수: 19
A씨는 25세입니다.
'''