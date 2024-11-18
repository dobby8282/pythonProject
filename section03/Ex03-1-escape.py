'''
파일명: Ex03-1-escape.py
이스케이프 문자(Escape Character):
   - 특수 기능을 가진 제어 문자
   - 백슬래시(\)로 시작
'''

# 1. 이스케이프 문자 활용
pokemon_info = 'ID: \'피카츄\'\n타입: \'전기\'\tLevel: 25'
print(pokemon_info)
"""출력결과:
ID: '피카츄'
타입: '전기'    Level: 25
"""

# 2. 포켓몬 능력치 표시
stats = '이름\t체력\t공격\n피카츄\t35\t55\n라이츄\t60\t90'
print(stats)
"""출력결과:
이름    체력    공격
피카츄  35      55
라이츄  60      90
"""

# 3. 경로 표시
file_path = 'C:\\Pokemon\\Data\\stats.txt'
print('파일 경로:', file_path)

# 4. 자주 쓰는 이스케이프 문자
print('큰따옴표: \"')   # 큰따옴표
print('작은따옴표: \'')  # 작은따옴표
print('백슬래시: \\')   # 백슬래시
print('줄바꿈\n들여쓰기\t효과')