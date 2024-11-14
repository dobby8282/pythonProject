'''
파일명: Ex02-5-list-2.py
내용: 리스트 조작하기

주요 메소드:
    - append(): 끝에 항목 추가
    - insert(): 지정 위치에 항목 추가
    - remove(): 항목 제거
    - pop(): 지정 위치 항목 제거
    - clear(): 리스트 비우기
'''

# 1. 리스트에 항목 추가하기
pokemons = ['피카츄', '라이츄', '파이리']
print('원본:', pokemons)

pokemons.append('꼬부기')      # 끝에 추가
print('append 후:', pokemons)

pokemons.insert(1, '잠만보')   # 중간에 추가
print('insert 후:', pokemons)

# 2. 리스트 항목 제거하기
pokemons = ['피카츄', '라이츄', '파이리', '꼬부기']
print('원본:', pokemons)

pokemons.remove('라이츄')      # 값으로 제거
print('remove 후:', pokemons)

pokemons.pop(1)               # 인덱스로 제거
print('pop 후:', pokemons)

# 3. 리스트 확장하기
pokemons = ['피카츄', '라이츄']
new_pokemons = ['버터플', '잠만보']
pokemons.extend(new_pokemons)
print('확장된 리스트:', pokemons)

# 4. 리스트 비우기
pokemons.clear()
print('빈 리스트:', pokemons)