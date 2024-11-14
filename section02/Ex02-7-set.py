'''
파일명: Ex02-7-set.py
내용: 세트(Set) 자료형 학습

세트란?
   - 순서가 없는 자료형
   - 중복된 값을 가질 수 없음
   - 중괄호 {} 로 감싸서 표현
'''

# 1. 세트 만들기
pokemons = {"피카츄", "라이츄", "파이리"}
print('포켓몬 세트:', pokemons)   # 실행할 때마다 순서가 변경될 수 있음

# 2. 세트 반복하기
print('## 세트 항목 반복 ##')
for pokemon in pokemons:
   print(pokemon)

# 3. 값 존재 여부 확인하기
pokemons = {"피카츄", "잠만보", "야도란"}
print('피카츄가 있나요?', "피카츄" in pokemons)  # True
print('꼬부기가 있나요?', "꼬부기" in pokemons)  # False

# 4. 세트 수정하기
## 4-1. 항목 추가
pokemons = {"피카츄", "라이츄", "파이리"}
print('추가 전:', pokemons)
pokemons.add("꼬부기")
print('추가 후:', pokemons)

## 4-2. 다른 세트 추가
set1 = {"피카츄", "라이츄"}
set2 = {"파이리", "꼬부기"}
set1.update(set2)
print('세트 합치기 결과:', set1)

# 5. 세트 항목 제거하기
pokemons = {"피카츄", "라이츄", "파이리"}
print('제거 전:', pokemons)

## 5-1. remove() - 없는 항목 제거시 에러 발생
pokemons.remove("피카츄")
print('remove() 후:', pokemons)
# pokemons.remove("피카츄")  # 에러 발생!

## 5-2. discard() - 없는 항목 제거시 에러 발생 안 함
pokemons.discard("라이츄")
print('discard() 후:', pokemons)
pokemons.discard("없는포켓몬")  # 에러 발생 안 함

## 5-3. 임의의 항목 제거
pokemons.pop()
print('pop() 후:', pokemons)

## 5-4. 모든 항목 제거
pokemons.clear()
print('clear() 후:', pokemons)