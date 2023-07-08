'''
파일명: Ex20-0-recursive.py

재귀함수(Recursive function)
    함수 내부에서 자기자신 호출하는 것을 말한다.

'''

def count_number(n):
    while n > 0:
        print(n)
        n -= 1

def recursive_count_number(n):
    if(n <= 0):
        return
    print(n)
    recursive_count_number(n - 1)

# 실행 코드
# count_number(5)
recursive_count_number(5)

