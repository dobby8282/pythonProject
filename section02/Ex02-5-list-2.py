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


# 1. 리스트 조작 기본 메서드
starter_pokemon = ['피카츄', '파이리', '꼬부기']
starter_pokemon.append('이상해씨')    # 끝에 추가
starter_pokemon.insert(1, '잠만보')   # 중간 삽입
print('새로운 스타터:', starter_pokemon)

# 2. 리스트 제거 메서드
legendary_pokemon = ['그란돈', '가이오가', '레쿠쟈', '히드런']
print('전설의 포켓몬:', legendary_pokemon)

legendary_pokemon.remove('히드런')  # 값으로 제거
print('방출 후:', legendary_pokemon)

released = legendary_pokemon.pop(1)  # 인덱스로 제거
print(f'방출된 포켓몬: {released}')
print('현재 남은 포켓몬:', legendary_pokemon)

# 2. 리스트 확장과 초기화
hoenn_team = ['나무지기', '가디안']
sinnoh_team = ['불꽃숭이', '팽도리']
hoenn_team.extend(sinnoh_team)    # 리스트 합치기
print('연합팀:', hoenn_team)

hoenn_team.clear()    # 리스트 비우기
print('리셋된 팀:', hoenn_team)

# del hoenn_team      # 리스트 객체 삭제