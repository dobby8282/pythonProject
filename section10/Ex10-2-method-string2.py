'''
파일명: Ex10-2-method-string2.py
'''

# join() 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)

# split() 메소드
s = 'Life is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)
print(result[2])

data = '홍길동|25|프로그래머'
result = data.split('|')
print(result)
print('이름: {}'.format(result[0]))
print('나이: {}'.format(result[1]))
print('직업: {}'.format(result[2]))

# replace() 메소드 - 문자열 치환
s = 'Life is to short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백제거 메소드
s = '       apple'
result = s.lstrip() # 왼쪽 공백제거
print(result)

s = 'apple       '
result = s.rstrip() # 오른쪽 공백제거
print(result)

s = '       apple       '
result = s.strip() # 양쪽 공백 제거
print(result)

s = ' a p p l e '
result = s.strip()
print(result)

s = ' a p p l e '
result = s.replace(' ', '')
print(result)



















