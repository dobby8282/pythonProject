'''
파일명: Ex02-3-type-2.py
내용: 파이썬 컬렉션 타입과 형변환 학습

컬렉션 타입:
    - 리스트(list): 여러 값을 순서대로 저장
    - 튜플(tuple): 리스트와 비슷하지만 수정 불가능
    - 딕셔너리(dict): 키와 값의 쌍으로 저장
    - 세트(set): 중복없이 저장
'''

# 1. 컬렉션 타입 예제
pokemons_list = ['피카츄', '라이츄', '파이리']
pokemons_tuple = ('피카츄', '라이츄', '파이리')
pokemon_dict = {"name": "피카츄", "기술": "백만볼트!"}
pokemons_set = {"피카츄", "라이츄", "파이리"}

print('리스트:', pokemons_list)
print('튜플:', pokemons_tuple)
print('딕셔너리:', pokemon_dict)
print('세트:', pokemons_set)

# 2. 형변환 예제
name = '피카츄'
age = 27
# 문자 + 숫자 (형변환 필요)
result = name + str(age)
print('형변환 결과:', result)

# 3. 문자열 연결하기
text1 = 'Hello'
text2 = 'Python'
print('문자열 연결:', text1 + ' ' + text2)