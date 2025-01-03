# 파이썬 람다(Lambda) 함수

## 1. 람다 함수란?
람다 함수는 이름 없는 익명 함수로, 단일 표현식을 사용하여 간단한 함수를 만드는 방법입니다.

### 기본 문법
```python
lambda 인자 : 표현식
```

## 2. 일반 함수와 람다 함수 비교

### 일반 함수
```python
def add(x, y):
    return x + y

print(add(5, 3))  # 출력: 8
```

### 람다 함수
```python
add = lambda x, y: x + y
print(add(5, 3))  # 출력: 8
```

## 3. 람다 함수의 주요 용도

### 3.1 map() 함수와 함께 사용
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 출력: [1, 4, 9, 16, 25]
```

### 3.2 filter() 함수와 함께 사용
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 출력: [2, 4, 6]
```

### 3.3 sort() 함수와 함께 사용
```python
students = [
    {'name': '철수', 'grade': 85},
    {'name': '영희', 'grade': 92},
    {'name': '민수', 'grade': 78}
]
students.sort(key=lambda student: student['grade'], reverse=True)
print(students)  # 성적 순으로 정렬됨
```

## 4. 람다 함수의 장단점

### 장점
- 코드가 간결해짐
- 일회성 함수를 만들 때 유용
- 함수형 프로그래밍에 적합

### 단점
- 복잡한 로직을 구현하기 어려움
- 디버깅이 어려울 수 있음
- 가독성이 떨어질 수 있음

## 5. 연습문제

1. 다음 리스트의 각 요소를 제곱하는 람다 함수를 작성하세요:
```python
numbers = [1, 2, 3, 4, 5]
# 결과: [1, 4, 9, 16, 25]
```

2. 다음 리스트에서 짝수만 필터링하는 람다 함수를 작성하세요:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 결과: [2, 4, 6, 8, 10]
```

## 6. 답안
```python
# 문제 1 답안
squared = list(map(lambda x: x**2, numbers))

# 문제 2 답안
even = list(filter(lambda x: x % 2 == 0, numbers))
```