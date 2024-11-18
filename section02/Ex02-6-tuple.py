'''
파일명: Ex02-6-tuple.py
튜플(Tuple):
   - 수정 불가능한 순서가 있는 자료구조
   - 소괄호 () 사용
   - 읽기 전용 리스트와 유사
'''

# 1. 튜플 생성과 기본 조작
game_starters = ('파이리', '이상해씨', '꼬부기')
print('스타터 포켓몬:', game_starters)
print('첫 번째 스타터:', game_starters[0])
print('마지막 스타터:', game_starters[-1])
print('전체 스타터 수:', len(game_starters))

# 2. 튜플 슬라이싱
legendary_birds = ('프리져', '썬더', '파이어', '루기아')
print('전설의 새:', legendary_birds[1:3])    # 썬더, 파이어

# 3. 튜플 수정 (변환 활용)
evolve_chain = ('치코리타', '베이리프', '메가니움')
print('진화 전:', evolve_chain)

# 임시로 리스트 변환하여 수정
temp_list = list(evolve_chain)
temp_list[1] = '메가베이리프'
evolve_chain = tuple(temp_list)
print('진화 후:', evolve_chain)

# 4. 튜플 언패킹
gym_leaders = ('웅', '아야', '하야토', '마니')
(leader1, leader2, leader3, leader4) = gym_leaders
print('체육관 관장:')
print(f'1번 관장: {leader1}')
print(f'2번 관장: {leader2}')

# 5. 튜플 결합
kanto = ('이상해씨', '파이리')
johto = ('치코리타', '브케인')
starters = kanto + johto
print('전체 스타터:', starters)