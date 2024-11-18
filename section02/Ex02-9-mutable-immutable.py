'''
파일명: Ex02-9-mutable-immutable.py
데이터 타입의 가변성:
   - mutable: 값 변경 시 메모리 주소 유지 (list, set, dict)
   - immutable: 값 변경 시 새 메모리 주소 할당 (int, str, tuple)
'''

# 1. mutable 예제
pokemon_team = ['피카츄', '파이리']
print('초기 팀:', pokemon_team)
print('메모리 주소:', id(pokemon_team))

pokemon_team.append('꼬부기')
print('팀 추가 후:', pokemon_team)
print('메모리 주소:', id(pokemon_team))  # 동일한 주소 유지
print('=> mutable: 메모리 주소 변경 없음')

# 2. immutable 예제
pokemon_level = 50
print('\n레벨:', pokemon_level)
print('메모리 주소:', id(pokemon_level))

pokemon_level += 1
print('레벨 업:', pokemon_level)
print('메모리 주소:', id(pokemon_level))  # 새로운 주소 할당
print('=> immutable: 새로운 메모리 주소 할당')

# 3. 복합 예제
pokemon_info = ('피카츄', ['전기충격', '아이언테일'])  # tuple(str, list)
print('\n초기 정보:', pokemon_info)
pokemon_info[1].append('10만볼트')  # list는 mutable
print('기술 추가 후:', pokemon_info)
# pokemon_info[0] = '라이츄'  # Error: tuple은 immutable