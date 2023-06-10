'''
파일명: Ex11-2-function2.py
'''

# 매개변수 o, 리턴 x
def introduce(name, age): # name = 홍길동 , age = 25
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))

introduce('홍길동', 25)

# 가변 매개변수 함수
def show(*args):
    print(type(args))
    for item in args:
        print(item)

show('Python')
show('Python', 'Java', 'C++')




