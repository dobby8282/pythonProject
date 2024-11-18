'''
파일명: Ex03-2-print.py
print() 함수:
   - sep: 값 사이 구분자 (기본: 공백)
   - end: 출력 끝 문자 (기본: \n)
   - file: 출력 대상 (기본: sys.stdout)
'''

# 1. 기본 출력
pokemon = '피카츄'
level = 25
print('포켓몬:', pokemon, '레벨:', level)  # 자동 공백 추가

# 2. sep 매개변수
stats = ['피카츄', '전기', '35', '55']
print(*stats, sep=',')  # 쉼표로 구분
print('010', '1234', '5678', sep='-')  # 전화번호 형식

# 3. end 매개변수
print('피카츄', end='>')
print('라이츄', end='>')
print('파이리')
# 출력: 피카츄>라이츄>파이리

# 4. 파일 출력
with open('pokemon.txt', 'w') as file:
   print('name: 피카츄', file=file)
   print('type: 전기', file=file)