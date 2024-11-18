'''
파일명: Ex03-5-casting.py
형변환(Type Casting):
   - 데이터 타입을 다른 타입으로 변환
   - 주요 함수: int(), float(), str()
'''

# 1. 숫자형 변환
level_str = "25"
hp_str = "35.5"

level = int(level_str)          # 문자열 -> 정수
hp = float(hp_str)             # 문자열 -> 실수
print(f'레벨: {level}, 체력: {hp}')

# 2. 진법 변환
binary = "1010"  # 2진수
hex_num = "A5"   # 16진수

dec1 = int(binary, 2)          # 2진수 -> 10진수
dec2 = int(hex_num, 16)        # 16진수 -> 10진수
print(f'2진수 변환: {dec1}')
print(f'16진수 변환: {dec2}')

# 3. 문자열 변환과 연산
attack = 55
defense = 40

stat_str = str(attack) + "/" + str(defense)  # 숫자 -> 문자열
print(f'스탯: {stat_str}')
print(f'데미지: {str(attack - defense)}')    # 계산 후 문자열

# 4. 문자와 아스키코드
print(f'P의 아스키코드: {ord("P")}')        # 문자 -> 아스키코드
print(f'아스키코드 80의 문자: {chr(80)}')    # 아스키코드 -> 문자

'''
주의사항:
1. 부적절한 형변환 시도 시 ValueError 발생
  - int('3.14')  # 실수 문자열을 정수로 변환 불가
  - int('ABC')   # 숫자가 아닌 문자열을 정수로 변환 불가
2. 형변환 전 데이터 유효성 검사 필요
'''