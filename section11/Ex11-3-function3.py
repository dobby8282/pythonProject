'''
파일명: Ex11-3-function3.py

함수는 작업을 수행한 결과를 반환(return)할 수 있습니다. 
반환된 값은 함수 호출한 위치에서 사용할 수 있습니다.
'''

# 반환 값이 있는 함수 (매개변수 x, 리턴 값 o)
def address():  # 매개변수 없음, 리턴 값 있음
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'  # 주소 문자열을 생성
    return str  # 생성된 문자열을 반환

# 함수 호출 후 반환된 값을 result 변수에 저장
result = address()
print(result)  # 반환된 주소 출력

# 매개변수 o, 리턴 값 o
def plus(num1, num2):  # num1과 num2는 함수가 입력받는 매개변수
    return num1 + num2  # 두 매개변수의 합을 반환

# 함수 호출 시 5와 7은 인자로 전달되어 더한 결과를 반환
result = plus(5, 7)
print(result)  # 5 + 7의 결과인 12 출력

# 함수 호출 시 2와 3이 인자로 전달되어 더한 결과를 직접 출력
print(plus(2, 3))  # 2 + 3의 결과인 5 출력
