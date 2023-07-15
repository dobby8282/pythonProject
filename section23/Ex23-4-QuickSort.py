'''
파일명: Ex23-4-QuickSort.py

4. 퀵 정렬(Quick Sort)
    분할 정복 알고리즘의 일종, 기준점(pivot)을 설정하고
    pivot 보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 분할한 후
    각 부분 리스트에 대해 재귀적으로 퀵 정렬을 수행하는 알고리즘
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    '''
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    pivot = 6
    
    left = [5, 3, 1, 2, 4]
    right = [8, 7]
    equal = [6]
    
    return ->  [1, 2, 3, 4, 5] + [6] + [7, 8]  
        1. quick_sort(left) ->  [1, 2, 3, 4] + [5] + []
            arr = [5, 3, 1, 2, 4]
            pivot = 5
            left = [3, 1, 2, 4]
            right = []
            equal = [5]
            1-1 quick_sort(left) -> [1, 2, 3, 4]
                arr = [3, 1, 2, 4]
                pivot = 3
                left = [1, 2]
                right = [4]
                equal = [3]
                1-1-1 quick_sort(left) -> left + equal + right -> [1, 2] 
                    arr = [1, 2]
                    pivot = 1
                    left = []
                    right = [2]
                    equal = [1]
                1-1-2 quick_sort(equal) -> [3]
                1-1-3 quick_sort(right) -> [4]
            1-2 quick_sort(equal) -> [5]
            1-2 quick_sort(right) -> []
        2 quick_sort(equal) -> [6]
        3 quick_sort(right) -> [7, 8]
    
    '''
    pivot = arr[0]

    left, right, equal = [], [], []

    for a in arr:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)

    return quick_sort(left) + equal + quick_sort(right)

# 실행코드
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(quick_sort(arr))


