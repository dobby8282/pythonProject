'''
파일명: Ex04-3-comparison.py
관계 연산자:
   - 두 값을 비교하여 bool 값 반환
   - >, >=, <, <=, ==, !=
'''

# 1. 포켓몬 레벨 비교
pikachu_level = 25
charmander_level = 20

print(f'피카츄 레벨 > 파이리 레벨: {pikachu_level > charmander_level}')
print(f'피카츄 레벨 == 파이리 레벨: {pikachu_level == charmander_level}')

# 2. 체력 상태 확인
max_hp = 100
current_hp = 45

print('\n=== HP 상태 체크 ===')
print(f'체력 50% 이상: {current_hp >= max_hp/2}')
print(f'체력 30% 이하: {current_hp <= max_hp*0.3}')

# 3. 진화 가능 여부
level = 16
evolve_level = 16
has_stone = False

can_evolve = level >= evolve_level
print(f'\n진화 가능?: {can_evolve}')

# 4. 타입 비교
type1 = "불꽃"
type2 = "물"
print(f'같은 타입?: {type1 == type2}')

# 5. None 비교 (능력치 미설정)
speed = None
print(f'스피드 설정됨?: {speed is not None}')

# 6. 객체 비교
team1 = ['피카츄', '파이리']
team2 = ['피카츄', '파이리']
print('\n=== 객체 비교 ===')
print(f'같은 멤버?: {team1 == team2}')      # True (값 비교)
print(f'같은 팀?: {team1 is team2}')        # False (객체 비교)

'''
주의사항:
1. 실수 비교시 근사값 주의
2. is는 객체 비교, == 는 값 비교
3. None 비교는 is 사용 권장
'''