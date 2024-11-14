'''
파일명: Ex03-3-format.py
내용: 문자열 포매팅(String Formatting)

포매팅이란?
    - 문자열 중간에 특정 값을 삽입하여 조합하는 방법
    - {} placeholder를 활용하여 다양한 값을 깔끔하게 표현
    - 데이터의 종류에 상관없이 print문으로 표현이 가능
'''

# 1. 기본 포매팅
print('===== 기본 포매팅 =====')
print('올해는 {}년 입니다.'.format(2023))
print('나는 {}을 공부합니다.'.format('Python'))

# 2. 여러 값 포매팅
print('\n===== 여러 값 포매팅 =====')
print('올해는 {}년, 내년은 {}년 입니다.'.format(2023, 2024))
print('나는 {}과 {}를 탑니다.'.format('지하철', '버스'))

# 3. f-string (Python 3.6+)
print('\n===== f-string 포매팅 =====')
name = '홍길동'
age = '20'
print(f'제 이름은 {name} 입니다.')
print(f'나이는 {age}살 입니다.')

# 4. format() vs f-string 비교
print('\n===== format()과 f-string 비교 =====')
# format() 사용
print('제 이름은 {} 입니다.\n나이는 {}살 입니다.'.format(name, age))
# f-string 사용
print(f'제 이름은 {name} 입니다.\n나이는 {age}살 입니다.')

# 5. 변수명으로 포매팅
print('\n===== 변수명으로 포매팅 =====')
address = '''서울특별시 강남구
테헤란로 123'''
print('주소: {addr}'.format(addr=address))

# 6. 포매팅 응용
print('\n===== 포매팅 응용 =====')
# 정수 표현
print('10진수: {0}, 2진수: {0:b}, 8진수: {0:o}, 16진수: {0:x}'.format(42))
# 소수점 표현
print('원주율: {:.2f}'.format(3.141592))
# 정렬
print('왼쪽 정렬: {:<10}'.format('Python'))
print('오른쪽 정렬: {:>10}'.format('Python'))
print('가운데 정렬: {:^10}'.format('Python'))
'''
출력결과:
왼쪽 정렬: Python    
오른쪽 정렬:     Python
가운데 정렬:   Python  
'''