'''
파일명: Ex11-4-variable-local-global.py

지역변수 (Local Variable)
    - 함수 내부에서 선언된 변수로, 해당 함수 안에서만 사용 가능합니다.
    - 함수가 종료되면 해당 변수는 소멸됩니다.

전역변수 (Global Variable)
    - 함수 외부에서 선언된 변수로, 프로그램 전체에서 사용 가능합니다.
    - 함수 내부에서도 사용할 수 있지만, 함수 내부에서 전역변수를 변경하려면 'global' 키워드를 사용해야 합니다.
'''

# 전역변수 선언
gVar = '전역'

def globalAndLocal():
    # 지역변수 선언
    lVar = '지역'
    # 전역변수 참조 (읽기만 가능)
    print(gVar, '변수 입니다.')
    # 지역변수 참조
    print(lVar, '변수 입니다.')

def globalAndLocal2():
    # 다른 함수의 지역변수는 공유되지 않음
    lVar = '지역2'
    # 전역변수 참조
    print(gVar, '변수 입니다.')
    # 해당 함수의 지역변수 참조
    print(lVar, '변수 입니다.')

# 함수 호출
globalAndLocal()
globalAndLocal2()

# 전역변수와 같은 이름의 지역변수 사용 예시
def globalAndLocal3():
    lVar = '지역'
    # 같은 이름을 가진 새로운 지역변수 선언 (전역변수가 아닌 지역변수로 처리됨)
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(gVar, '변수 입니다.')  # 지역변수 gVar 출력
    print(lVar, '변수 입니다.')  # 지역변수 lVar 출력

# 함수 호출
globalAndLocal3()
# 전역변수 gVar 출력 (함수 내에서 변경된 gVar는 지역변수일 뿐 전역변수는 영향을 받지 않음)
print(gVar)  # '전역'이 출력됨

# 전역변수를 함수에서 사용하는 예시
total = 0  # 전역변수 선언
def gift(dic, who, money):
    global total  # 함수 내부에서 전역변수 total을 사용하겠다는 선언
    total += money  # 전역변수 total에 money 값을 더함
    dic[who] = money  # 딕셔너리 dic에 누구(who)가 얼마(money)를 낸 기록을 저장

# 축의금 기록을 저장할 딕셔너리
wedding = {}
name = '영희'
# 함수 호출하여 축의금 기록
gift(wedding, name, 5)  # wedding: {'영희': 5}, total: 5
gift(wedding, '철수', 6)  # wedding: {'영희': 5, '철수': 6}, total: 11
gift(wedding, '이모', 10)  # wedding: {'영희': 5, '철수': 6, '이모': 10}, total: 21

# 축의금 명단과 전체 금액 출력
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))
