'''
파일명: Ex04-6-conditions.py
내용: 게임 시스템에서의 조건 연산자 활용

조건 연산자:
   result = value1 if condition else value2
'''

# 1. 플레이어 상태 체크
hp = 80
max_hp = 100
mp = 50
max_mp = 100

# HP/MP 상태 표시
hp_status = "양호" if hp >= max_hp * 0.5 else "위험"
mp_status = "충분" if mp >= max_mp * 0.3 else "부족"

print(f'체력 상태: {hp_status} ({hp}/{max_hp})')
print(f'마나 상태: {mp_status} ({mp}/{max_mp})')

# 2. 아이템 강화 시스템
item_level = 7
success_rate = 95 if item_level < 5 else (80 if item_level < 8 else 60)
print(f'\n강화 성공 확률: {success_rate}%')

# 3. 플레이어 레벨별 던전 추천
player_level = 25
recommended_dungeon = (
   "고급 던전" if player_level >= 30 else
   "중급 던전" if player_level >= 20 else
   "초급 던전"
)
print(f'추천 던전: {recommended_dungeon}')

# 4. PVP 매칭 시스템
rating = 1850
tier = (
   "다이아몬드" if rating >= 2000 else
   "플래티넘" if rating >= 1800 else
   "골드" if rating >= 1500 else
   "실버"
)
print(f'\n현재 티어: {tier} ({rating}점)')

# 5. 퀘스트 보상 계산
quest_difficulty = "하드"
quest_reward = 1000 if quest_difficulty == "노말" else 2000
bonus = quest_reward * (0.5 if player_level > 20 else 0.2)
print(f'퀘스트 보상: {quest_reward + bonus}골드')
