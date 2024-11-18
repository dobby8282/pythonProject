'''
파일명: Ex03-4-input.py
input() 함수:
   - 사용자 입력을 받는 함수
   - 모든 입력은 문자열(str)로 저장
   - 숫자 활용 시 int(), float() 등으로 형변환 필요
'''

# 1. 기본 입력
trainer_name = input('트레이너 이름: ')
trainer_age = int(input('나이: '))
print(f'이름: {trainer_name}, 나이: {trainer_age}세')

# 2. 포켓몬 능력치 입력
pokemon = input('포켓몬 이름: ')
level = int(input('레벨: '))
hp = float(input('체력: '))
print(f'{pokemon} (Lv.{level}) HP: {hp:.1f}')

# 3. 데미지 계산기
attack = int(input('공격력: '))
defense = int(input('방어력: '))
damage = attack - defense

print('\n===== 전투 결과 =====')
print(f'공격력: {attack}')
print(f'방어력: {defense}')
print(f'데미지: {damage}')

'''
실행 예시:
트레이너 이름: 지우
나이: 10
이름: 지우, 나이: 10세

포켓몬 이름: 피카츄
레벨: 25
체력: 35.5
피카츄 (Lv.25) HP: 35.5

공격력: 55
방어력: 30

===== 전투 결과 =====
공격력: 55
방어력: 30
데미지: 25
'''

# 주의사항
# 1. 숫자 입력 시 반드시 형변환
# 2. 잘못된 입력 → ValueError
# 3. 0으로 나누기 → ZeroDivisionError