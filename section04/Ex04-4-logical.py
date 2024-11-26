'''
파일명: Ex04-4-logical.py
내용: 논리 연산자와 활용

논리 연산자
   참/거짓을 판단하는 연산자
   and : 둘 다 True일 때만 True
   or  : 하나라도 True이면 True
   not : True ⟷ False 반전
'''

# 1. 게임 캐릭터 상태 체크
level = 30
hp = 100
mp = 80

# 풀피, 풀엠일 때 버프 발동
is_full_state = hp == 100 and mp == 100
print(f'캐릭터 버프 발동: {is_full_state}')  # False

# 레벨업 또는 퀘스트 완료시 보상
quest_complete = True
gets_reward = level >= 30 or quest_complete
print(f'보상 획득: {gets_reward}')  # True

# 2. 던전 입장 조건 체크
dungeon_level = 25
required_items = ['드래곤의 검', '마법 방패']
player_items = ['드래곤의 검', '마법 방패', '체력 포션']

can_enter = (level >= dungeon_level and
           all(item in player_items for item in required_items))
print(f'\n던전 입장 가능?: {can_enter}')

# 3. 게임 시스템 상태
server_status = True
maintenance = False
emergency = False

# 게임 플레이 가능 여부
can_play = server_status and not (maintenance or emergency)
print(f'게임 플레이 가능?: {can_play}')  # True

# 4. 플레이어 상태 이상
poisoned = True
cursed = False
stunned = True

# 상태이상 해제 아이템 사용 조건
needs_healing = poisoned or cursed or stunned
needs_immediate = poisoned and stunned

print(f'\n===== 플레이어 상태 =====')
print(f'상태이상 해제 필요: {needs_healing}')
print(f'긴급 치료 필요: {needs_immediate}')
