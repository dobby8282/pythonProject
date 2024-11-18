'''
파일명: Ex02-7-set.py
세트(Set):
   - 중복을 허용하지 않는 자료구조
   - 순서가 없음 (인덱싱 불가)
   - 집합 연산 가능
'''

# 1. 세트 생성과 기본 기능
pokemon_types = {'불꽃', '물', '풀', '전기'}
print('포켓몬 속성:', pokemon_types)

# 포함 여부 확인
print('불꽃 타입 있나요?:', '불꽃' in pokemon_types)
print('얼음 타입 있나요?:', '얼음' in pokemon_types)

# 2. 세트 수정
fire_types = {'파이리', '마그마', '브케인'}
print('초기 불꽃타입:', fire_types)

# 단일 추가
fire_types.add('리자몽')
print('메가진화 추가:', fire_types)

# 여러 항목 추가
new_fire = {'마그케인', '볼케니온'}
fire_types.update(new_fire)
print('새 포켓몬 추가:', fire_types)

# 3. 세트 제거 메서드 비교
water_types = {'꼬부기', '잉어킹', '라프라스'}
print('물타입들:', water_types)

water_types.remove('잉어킹')      # 없으면 에러
print('remove 후:', water_types)

water_types.discard('없는포켓몬')  # 에러 없음
print('discard 후:', water_types)

removed = water_types.pop()      # 임의 제거
print(f'방출된 포켓몬: {removed}')

water_types.clear()              # 전체 제거
print('리셋 후:', water_types)