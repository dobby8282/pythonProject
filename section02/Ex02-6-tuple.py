'''
파일명: Ex02-6-tuple.py
내용: 튜플의 기본 사용법 학습

튜플(Tuple)이란?
   - 리스트와 비슷하지만 값을 변경할 수 없음
   - 소괄호 () 로 감싸서 표현
   - 순서가 있는 자료형
'''

# 1. 튜플 만들기
pokemons = ('피카츄', '라이츄', '파이리')
print('포켓몬 튜플:', pokemons)
print('튜플 길이:', len(pokemons))

# 2. 튜플 데이터 접근하기
print('두번째 포켓몬:', pokemons[1])      # 인덱스로 접근
print('마지막 포켓몬:', pokemons[-1])     # 뒤에서부터 접근
print('일부 추출:', pokemons[1:3])       # 슬라이싱

# 3. 튜플의 값 변경하기 (튜플→리스트→튜플)
pokemons = ('피카츄', '라이츄', '파이리')
print('변경 전:', pokemons)

# 리스트로 변환하여 값 변경
pokemon_list = list(pokemons)    # 튜플→리스트
pokemon_list[1] = '잠만보'       # 값 변경
pokemons = tuple(pokemon_list)   # 리스트→튜플

print('변경 후:', pokemons)

# 4. 튜플 압축풀기(각 변수에 값 넣기)
pokemons = ('피카츄', '라이츄', '파이리', '꼬부기')
(p1, p2, p3, p4) = pokemons     # 각 변수에 튜플 값 저장

print('## 압축풀기 결과 ##')
print('첫번째 포켓몬:', p1)
print('두번째 포켓몬:', p2)
print('세번째 포켓몬:', p3)
print('네번째 포켓몬:', p4)

# 5. 튜플 합치기
tuple1 = ('피카츄', '라이츄')
tuple2 = ('파이리', '꼬부기')
new_tuple = tuple1 + tuple2
print('합쳐진 튜플:', new_tuple)