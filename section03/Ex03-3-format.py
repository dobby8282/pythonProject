'''
파일명: Ex03-3-format.py
문자열 포매팅:
   - % 포매팅: 파이썬 초기부터 있던 방식
   - format(): 파이썬 2.6부터 도입
   - f-string: 파이썬 3.6부터 도입 (현재 권장)
'''

# 1. % 포매팅 (레거시)
pokemon = '피카츄'
level = 25
hp = 35.5

print('포켓몬: %s' % pokemon)              # %s: 문자열
print('레벨: %d' % level)                  # %d: 정수
print('체력: %.1f' % hp)                   # %f: 실수
print('%s의 레벨은 %d입니다.' % (pokemon, level))  # 여러 값 동시 사용

# 2. format() 메서드
print('포켓몬: {}'.format(pokemon))
print('포켓몬: {}, 레벨: {}'.format(pokemon, level))
print('체력: {:.1f}'.format(hp))

# 3. f-string (현재 권장)
trainer = '지우'
badges = 8
print(f'트레이너: {trainer}')
print(f'획득한 배지: {badges}개')

# 4. 포매팅 옵션
stats = {
   'attack': 55,
   'defense': 40,
   'speed': 90
}

# 정렬
print(f'공격력: {stats["attack"]:>5}')     # 오른쪽 정렬
print(f'방어력: {stats["defense"]:<5}')     # 왼쪽 정렬
print(f'스피드: {stats["speed"]:^5}')       # 가운데 정렬

# 진법 변환
level = 16
print(f'레벨(2진수): {level:b}')
print(f'레벨(16진수): {level:x}')

# 소수점
accuracy = 98.7654
print(f'명중률: {accuracy:.2f}%')