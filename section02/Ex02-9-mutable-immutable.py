'''
파일명: Ex02-9-mutable-immutable.py
내용: 변경 가능한 자료형과 변경 불가능한 자료형 학습

1. mutable(변경 가능)
   - list, set, dict
   - 객체의 값이 변경될 때 메모리 주소가 동일

2. immutable(변경 불가능)
   - int, float, str, tuple
   - 객체의 값이 변경될 때 새로운 메모리 주소 할당
'''

# 1. mutable 예제 (리스트)
print('## mutable 예제 ##')
numbers = [1, 2, 3]
print('리스트 초기값:', numbers)
print('메모리 주소:', id(numbers))     # 주소1

numbers.append(4)                      # 값 변경
print('append 후:', numbers)
print('메모리 주소:', id(numbers))     # 주소1 (동일)
print('=> 같은 메모리 주소를 유지합니다.')

# 2. immutable 예제 (정수)
print('\n## immutable 예제 ##')
number = 10
print('숫자 초기값:', number)
print('메모리 주소:', id(number))      # 주소1

number += 1                           # 값 변경
print('증가 후:', number)
print('메모리 주소:', id(number))      # 주소2 (변경)
print('=> 새로운 메모리 주소가 할당됩니다.')