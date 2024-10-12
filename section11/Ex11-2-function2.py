'''
파일명: Ex11-2-function2.py

함수는 다양한 입력값(매개변수)을 받을 수 있으며, 입력값을 바탕으로 작업을 수행합니다.
매개변수(Parameter)와 인자(Argument)의 차이:
    - 매개변수(Parameter): 함수 정의 시 함수가 입력받는 변수.
    - 인자(Argument): 함수 호출 시 실제로 함수에 전달되는 값.
'''

# 매개변수 있음, 리턴 값 없음
def introduce(name, age):  # name과 age는 함수 정의 시의 매개변수
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))

# 함수 호출 시 '홍길동'과 25는 함수에 전달되는 인자(Argument)
introduce('홍길동', 25)

# 가변 매개변수 함수
# 여러 개의 인자를 받을 수 있는 함수
def show(*args):  # args는 가변 매개변수로, 함수가 받을 인자의 개수가 정해지지 않음
    print(type(args))  # args는 튜플로 전달됨
    for item in args:  # 전달받은 각 인자를 순차적으로 출력
        print(item)

# show 함수 호출 (가변 인자를 사용하여 여러 값을 전달)
# 'Python'은 하나의 인자(Argument)
show('Python')  
# 'Python', 'Java', 'C++'은 여러 개의 인자(Argument)
show('Python', 'Java', 'C++')  
