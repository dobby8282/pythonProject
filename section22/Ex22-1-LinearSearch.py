'''
파일명: Ex22-1-LinearSearch.py

선형 검색(Linear Search)
    간단한 검색 알고리즘, 데이터를 처음부터 끝까지
    순차적으로 비교하여 값을 찾는다.
'''

def linear_search(arr, x):
    size = len(arr)
    for i in range(size):
        if arr[i] == x:
            return i

    return -1 # 찾고자 하는 값이 없는 경우 -1

# 실행코드
arr = [1, 3, 5, 7, 8]
print(linear_search(arr, 5))