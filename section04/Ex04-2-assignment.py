'''
파일명: Ex04-2-assignment.py
대입연산자:
   
   - 단순 대입
   변수에 값을 할당
   (=)
   - 복합 대입
   연산과 할당을 동시에 수행하는 복합 대입연산
   (+=, -=, *=, /=, %=)
'''

# 1. 기본 대입
pokemon_name = "피카츄"
level = 25
print(f'포켓몬: {pokemon_name}, 레벨: {level}')

# 2. 다중 대입과 값 교환
hp, mp = 100, 50
print(f'체력: {hp}, 마나: {mp}')

hp, mp = mp, hp  # 값 교환
print(f'교환 후 - 체력: {hp}, 마나: {mp}')

# 3. 복합 대입
exp = 0
print(f'현재 경험치: {exp}')

exp += 50        # 경험치 획득
print(f'경험치 획득: {exp}')

exp *= 2         # 경험치 2배 이벤트
print(f'경험치 2배: {exp}')

# 4. 포켓몬 스탯 변화
attack = 55
defense = 40

print(f'\n=== 스탯 변화 ===')
print('초기 - 공격력: %d, 방어력: %d' % (attack, defense))

attack += 10     # 공격력 강화
defense *= 1.5   # 방어력 1.5배 증가
print('강화 - 공격력: %d, 방어력: %.1f' % (attack, defense))

'''
주의사항:
1. 복합 대입 연산 시 타입 변환 주의
2. /= 연산자는 항상 실수 결과 반환
3. %= 연산자는 나머지 계산에 활용
'''
