'''
파일명: Ex02-1-circle.py
내용: 원의 넓이 계산 프로그램
'''

# 1. math 모듈 포함
import math

# 2. 원의 넓이를 계산하는 함수 만들기
def get_area(radius):
    """원의 넓이를 계산하는 함수
    입력값: radius(반지름)
    반환값: 원의 넓이
    """
    area = math.pi * math.pow(radius, 2)
    return area

# 3. 함수 사용해보기
radius = 1.5  # 반지름 값 저장
print('반지름:', radius)

# 4. 원의 넓이 계산하고 출력하기
area = get_area(radius)
print('원의 넓이:', area)

# 5. 함수 설명(docstring) 확인하기
print('함수 설명서:', get_area.__doc__)

'''
실행 결과:
반지름: 1.5
원의 넓이: 7.0685834705770345
함수 설명서: 원의 넓이를 계산하는 함수
    입력값: radius(반지름)
    반환값: 원의 넓이
'''