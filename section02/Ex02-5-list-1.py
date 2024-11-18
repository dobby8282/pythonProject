'''
파일명: Ex02-5-list-1.py
리스트(List) 기본:
   - 순서가 있는 데이터 집합
   - 중복 허용, 수정 가능
   - 다양한 자료형 포함 가능
'''

# 1. 리스트 생성과 접근
pokemon_list = ['피카츄', '라이츄', '꼬부기']
print('리스트 전체:', pokemon_list)
print('첫번째 포켓몬:', pokemon_list[0])
print('리스트 길이:', len(pokemon_list))

# 2. 다양한 데이터 타입
string_list = ['사과', '바나나', '딸기']
number_list = [1, 2, 3, 4, 5]
boolean_list = [True, False, True]
mixed_list = ['문자열', 100, True, 3.14]

# 3. 리스트 수정
pokemon_list = ['피카츄', '라이츄', '파이리']
pokemon_list[1] = '잠만보'  # 단일 항목 수정
print('수정된 리스트:', pokemon_list)

# 4. 범위 수정
evolution_list = ['피카츄', '라이츄', '파이리', '리자드', '리자몽']
evolution_list[1:3] = ['라이츄Z', '메가파이리']  # 범위 수정
print('진화 업데이트:', evolution_list)
