'''
파일명: Ex02-8-dict.py
내용: 딕셔너리(Dictionary) 자료형 학습

딕셔너리란?
   - key와 value가 쌍으로 이루어진 자료형
   - 중괄호 {} 안에 key:value 형식으로 작성
   - 순서가 없고 key는 중복 불가능
'''

# 1. 딕셔너리 만들기
shoes = {
   "brand": "나이키",
   "model": "Max90",
   "year": 1990
}
print('신발 정보:', shoes)

# 2. 딕셔너리 값 접근하기
## 2-1. 대괄호로 접근
print('브랜드:', shoes["brand"])
## 2-2. get() 함수로 접근
print('모델:', shoes.get("model"))

# 3. 키 목록 가져오기
print('키 목록:', shoes.keys())

# 4. 값 추가하기
car = {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
}
print('추가 전:', car)

## 4-1. 대괄호로 추가
car["color"] = "red"
print('color 추가 후:', car)

## 4-2. update()로 추가
car.update({"bgColor": "black"})
print('bgColor 추가 후:', car)

# 5. 값 변경하기
print('변경 전:', car)
car["color"] = "yellow"          # 대괄호로 변경
car.update({"bgColor": "blue"})  # update()로 변경
print('변경 후:', car)

# 6. 값 삭제하기
print('삭제 전:', car)
## 6-1. pop()으로 삭제
car.pop("model")
print('pop() 후:', car)

## 6-2. popitem()으로 마지막 항목 삭제
car.popitem()
print('popitem() 후:', car)