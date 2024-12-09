'''
파일명: Ex04-5-bitwise.py
내용: 비트 연산자와 활용

비트 연산자:
    이진수의 비트 단위로 연산
   & (AND)  : 두 비트 모두 1일 때 1
   | (OR)   : 하나라도 1이면 1
   ^ (XOR)  : 두 비트가 다르면 1
   ~ (NOT)  : 비트 반전
   << (Left Shift)  : N칸 왼쪽 이동
   >> (Right Shift) : N칸 오른쪽 이동
'''

# 1. 게임 캐릭터 상태 비트 마스킹
POISONED    = 0b0001  # 1
FROZEN      = 0b0010  # 2
BURNED      = 0b0100  # 4
PARALYZED   = 0b1000  # 8

# 상태이상 부여/해제
status = 0b0000
print(f'초기 상태: {bin(status)}')

# 독과 화상 부여
status = status | POISONED | BURNED
print(f'독+화상 부여: {bin(status)}')

# 해독 처치 (독 해제)
status = status & ~POISONED
print(f'독 해제: {bin(status)}')

# 2. 아이템 조합 시스템
WATER = 0b001   # 1
FIRE  = 0b010   # 2
EARTH = 0b100   # 4

# 아이템 조합 결과
steam = WATER | FIRE         # 물 + 불 = 증기
lava = FIRE | EARTH         # 불 + 땅 = 용암
print(f'\n증기 = {bin(steam)}')
print(f'용암 = {bin(lava)}')

# 3. 플레이어 권한 시스템
READ  = 0b0001    # 읽기
WRITE = 0b0010    # 쓰기
EDIT  = 0b0100    # 수정
ADMIN = 0b1000    # 관리자

# 일반 유저 권한
user_permission = READ | WRITE
print(f'\n일반유저 권한: {bin(user_permission)}')
print(f'읽기 가능?: {bool(user_permission & READ)}')
print(f'관리자 권한?: {bool(user_permission & ADMIN)}')

# 관리자 권한
admin_permission = READ | WRITE | EDIT | ADMIN
print(f'관리자 권한: {bin(admin_permission)}')

# 4. 2의 거듭제곱 계산
power = 1
for i in range(4):
   result = power << i
   print(f'2^{i} = {result} ({bin(result)})')
