'''
파일명: Ex03-2-print.py
내용: print() 함수의 다양한 사용법

print() 함수의 주요 매개변수
    - sep: 출력할 값들 사이에 들어갈 구분자 (기본값: 공백)
    - end: 출력 후 맨 끝에 출력할 문자 (기본값: 줄바꿈 문자 \n)
    - file: 출력 방향 지정 (기본값: 표준출력 sys.stdout)
'''

# 1. 기본 출력
print('===== 기본 출력 =====')
print('재미있는', '파이썬')    # 값들 사이에 자동으로 공백 추가

# 2. sep 매개변수 활용
print('\n===== sep 매개변수 =====')
print('Python', 'Java', 'C', sep=',')    # 쉼표로 구분
print('010', '1234', '5678', sep='-')    # 하이픈으로 구분

# 3. end 매개변수 활용
print('\n===== end 매개변수 =====')
print('Welcome', end='')    # 줄바꿈 없이 출력
print('to Python')          # 바로 이어서 출력
'''
출력결과: Welcome to Python
'''

# 4. file 매개변수 활용
print('\n===== file 매개변수 =====')
# 파일로 출력 보내기
fos = open('sample.py', mode='wt')
print('print("Hello World")', file=fos)
fos.close()