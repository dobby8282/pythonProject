'''
파일명: Ex11-4-variable-local-global.py

지역변수(local)
    함수 내부에 선언
    함수 내부에서만 사용이 가능하다.
    함수 종료시 같이 소멸된다.

전역변수(global)
    함수 외부선언
    함수 내부 외부 모두 사용 가능하다.
'''

gVar = '전역'
def globalAndLocal():
    lVar = '지역'
    print(gVar, '변수 입니다.') # 전역변수 참조만 한다.
    print(lVar, '변수 입니다.')

def globalAndLocal2():
    lVar = '지역2'
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globalAndLocal()
globalAndLocal2()

gVar = '전역'
def globalAndLocal3():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역' # 이름이 같은 지역변수
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globalAndLocal3()
print(gVar)

# 전역변수 선언
total = 0
def gift(dic, who, money):
    global total # 전역변수  total를 사용하겠다.
    total += money
    dic[who] = money

wedding = {}
name = '영희'
gift(wedding, name, 5) # wedding: {'영희':5 }, total: 5
gift(wedding, '철수', 6) # wedding: {'영희':5, '철수':6 }, total: 11
gift(wedding, '이모', 10) # wedding: {'영희':5, '철수':6, '이모':10 }, total: 21
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))














