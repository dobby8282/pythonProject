'''
파일명: Ex04-5-bitwise.py
내용: 비트 연산자(Bitwise Operators)

비트 연산자란?
   - 값을 2진수(비트)로 변환한 후 비트 단위로 연산을 수행
   - 하드웨어 제어, 암호화, 최적화 등에 활용

비트 연산자 종류
   & (AND)  : 두 비트 모두 1일 때만 1
   | (OR)   : 두 비트 중 하나라도 1이면 1
   ^ (XOR)  : 두 비트가 서로 다르면 1
   ~ (NOT)  : 비트 반전 (1→0, 0→1)
   << (Left Shift)  : 비트를 왼쪽으로 N칸 이동
   >> (Right Shift) : 비트를 오른쪽으로 N칸 이동
'''

# 1. 기본 비트 연산
print('===== 기본 비트 연산 =====')
a = 6  # 0110
b = 5  # 0101

print('a = {} (이진수: {:04b})'.format(a, a))
print('b = {} (이진수: {:04b})'.format(b, b))
print('a & b = {} (이진수: {:04b})'.format(a & b, a & b))   # AND
print('a | b = {} (이진수: {:04b})'.format(a | b, a | b))   # OR
print('a ^ b = {} (이진수: {:04b})'.format(a ^ b, a ^ b))   # XOR
print('~a = {} (이진수: {:b})'.format(~a, ~a & 0xF))        # NOT
print('a << 1 = {} (이진수: {:04b})'.format(a << 1, a << 1))  # Left Shift
print('a >> 1 = {} (이진수: {:04b})'.format(a >> 1, a >> 1))  # Right Shift

# 2. 비트 연산 진리표
print('\n===== 비트 연산 진리표 =====')
print('  A  B  AND OR  XOR')
print('  0  0   0   0   0')
print('  0  1   0   1   1')
print('  1  0   0   1   1')
print('  1  1   1   1   0')

# 3. 실용적인 비트 연산 예제
print('\n===== 비트 연산 활용 =====')
# 2의 거듭제곱 계산
num = 1
print('1 << 0 = {} (2^0)'.format(num << 0))  # 1
print('1 << 1 = {} (2^1)'.format(num << 1))  # 2
print('1 << 2 = {} (2^2)'.format(num << 2))  # 4
print('1 << 3 = {} (2^3)'.format(num << 3))  # 8

# 비트 마스킹
ADMIN = 8     # 1000
WRITE = 4     # 0100
READ = 2      # 0010
EXEC = 1      # 0001

permission = READ | WRITE  # 읽기와 쓰기 권한 부여
print('\n권한 확인:')
print('읽기 권한: {}'.format(bool(permission & READ)))    # True
print('쓰기 권한: {}'.format(bool(permission & WRITE)))   # True
print('실행 권한: {}'.format(bool(permission & EXEC)))    # False
print('관리 권한: {}'.format(bool(permission & ADMIN)))   # False

'''
실행 결과:
===== 기본 비트 연산 =====
a = 6 (이진수: 0110)
b = 5 (이진수: 0101)
a & b = 4 (이진수: 0100)
a | b = 7 (이진수: 0111)
a ^ b = 3 (이진수: 0011)
~a = -7 (이진수: 1001)
a << 1 = 12 (이진수: 1100)
a >> 1 = 3 (이진수: 0011)

===== 비트 연산 진리표 =====
 A  B  AND OR  XOR
 0  0   0   0   0
 0  1   0   1   1
 1  0   0   1   1
 1  1   1   1   0

===== 비트 연산 활용 =====
1 << 0 = 1 (2^0)
1 << 1 = 2 (2^1)
1 << 2 = 4 (2^2)
1 << 3 = 8 (2^3)

권한 확인:
읽기 권한: True
쓰기 권한: True
실행 권한: False
관리 권한: False
'''