'''
파일명: Ex11-3-function3.py
'''

# 반환(return) 값이 있는 함수
def address(): # 매개변수 x, 리턴 o
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()
print(result)

# 매개변수 o, 리턴 o
def plus(num1, num2):   # num1 = 5, num2 = 7
    return num1 + num2

result = plus(5, 7)
print(result)
print(plus(2, 3))





