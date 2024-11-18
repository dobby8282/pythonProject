'''
파일명: Ex02-4-String.py 정리본
문자열(String):
   - 문자들의 순서가 있는 나열
   - 작은따옴표(') 또는 큰따옴표(")로 표현
   - 문자열은 변경불가능(immutable)
'''

# 1. 문자열 생성 방법
str1 = 'Hello Python'    # 작은따옴표
str2 = "Hello Python"    # 큰따옴표
str3 = '''Hello         # 여러줄 문자열(작은따옴표)
Python'''
str4 = """Hello         # 여러줄 문자열(큰따옴표) 
Python"""

print('str1:', str1)
print('str2:', str2)
print('str3:')
print(str3)
print('str4:')
print(str4)

# 2. 문자열 인덱싱
'''
      |  h  |  e  |  l  |  l  |  o  |
index     0     1     2     3     4
역순번호   -5    -4    -3    -2    -1
'''
str = 'hello'
print('1번째 문자:', str[0])       # h
print('마지막 문자:', str[-1])      # o
print('마지막 문자:', str[4])       # o

# 3. 문자열 슬라이싱
str = "Python Programming"
print('처음부터 4글자:', str[0:4])    # Pyth
print('처음부터 4글자:', str[:4])      # Pyth
print('7번째 문자부터:', str[7:])      # Programming
print('마지막 5글자:', str[-5:])       # ming

# 4. 주요 문자열 메소드
str = "  Python  "
print('공백제거:', str.strip())         # 'Python'
print('모두 대문자:', str.upper())      # '  PYTHON  '
print('모두 소문자:', str.lower())      # '  python  '
print('문자 교체:', str.replace('P','J')) # '  Jython  '