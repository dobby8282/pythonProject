'''
파일명: Ex02-4-String.py
문자열(String)
    하나 이상 연속된 문자(character)들의 나열.
    파이썬에서는 문자열 자료형은 큰따옴표(" ") 
    또는 작은 따옴표(' ') 사이에 위치
'''
# 'Hello' 와 "Hello" 동일
print('Hello' == "Hello") # 값이 같으면 True 반환

'''
변수에 문자열 할당
'''
str = "Hello"
print(str)

'''
여러줄 문자열
    세개의 따옴표를 사용하여 변수에 여려줄 문자열 할당
'''
str = """피카츄, 라이튜, 파이리, 꼬부기
버터플, 야도란, 피존투, 또가스
"""
print(str)

'''
문자 배열 => 문자열
    문자열 인덱싱(indexing)
    h   e   l   l   o   <== 문자열
    0   1   2   3   4   <== 인덱스
   -5  -4  -3  -2  -1   <== 마이너스 인덱스
'''
str = 'hello'
print(str[1])
print(str[-4])
print(str[1] == str[-4])

'''
문자열 슬라이싱
    슬라이스 구문을 사용하여 문자를 반환할 수 있다.
    문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 콜론으로 구분
'''
str = "Hello, World"
print(str[2:5])
# 처음부터 인덱스번호 앞까지 슬라이스
print(str[:5]) # str[0:5] 동일
# 인덱스번호부터 끝까지 슬라이스
print(str[2:])

str = "Hello, World"
# 대문자
print(str.upper())
# 소문자
print(str.lower())

# 문자열 바꾸기
str = "Hello, World"
print(str.replace("H", "J"))

