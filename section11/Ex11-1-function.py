'''
파일명: Ex11-1-function.py

함수 (Function)
    특정 작업을 수행하기 위해 독립적으로 설계된 코드 블록입니다.
    입력값을 받아서 처리한 후, 결과를 반환하거나 단순히 작업을 수행할 수 있습니다.

함수 정의 형식:
def 함수이름(매개변수):
    코드 실행문
    return 반환값

매개변수 (Parameter) - 함수가 입력받는 값 (필요한 경우에 사용)
'''

# welcome() 함수 정의 (실행하지 않음)
def welcome():  # 매개변수 없음, 리턴값 없음 -> 실행 후 끝나는 함수
    print('Hello, Python')
    print('Nice to meet you')

# 함수 호출 (실행)
welcome()   
