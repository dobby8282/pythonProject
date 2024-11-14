'''
파일명: Ex02-4-String.py
내용: 문자열의 기본 사용법 학습

문자열이란?
   - 하나 이상의 문자를 나열한 것
   - 작은따옴표(') 또는 큰따옴표(")로 감싸서 표현
'''

# 1. 문자열 만들기
str1 = 'Hello'
str2 = "Hello"
print('두 문자열이 같나요?', str1 == str2)  # True

# 2. 여러 줄 문자열
pokemon = """피카츄
라이츄
파이리"""
print('여러 줄 문자열:')
print(pokemon)

# 3. 문자열 인덱싱
'''
예시: 'hello' 문자열
순서번호:   0   1   2   3   4
문자:      h   e   l   l   o
역순번호:  -5  -4  -3  -2  -1
'''
str = 'hello'
print('2번 문자:', str[2])        # l
print('뒤에서 2번 문자:', str[-2])  # l

# 4. 문자열 자르기(슬라이싱)
str = "Hello, World"
print('2~4번 문자:', str[2:5])     # llo
print('처음~4번 문자:', str[:5])    # Hello
print('2번부터 끝까지:', str[2:])    # llo, World

# 5. 문자열 다루기
str = "Hello, World"
print('대문자로:', str.upper())    # HELLO, WORLD
print('소문자로:', str.lower())    # hello, world
print('문자 바꾸기:', str.replace("H", "J"))  # Jello, World