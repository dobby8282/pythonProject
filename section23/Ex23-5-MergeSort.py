'''
파일명: Ex23-5-MergeSort.py

병합정렬(Merge Sort)
    분할 정복 알고리즘의 일종으로, 리스트를 절반으로 나눈 후
    각각을 재귀적으로 합병 정렬하고, 다시 합치면서 정렬하는 알고리즘
'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    '''
    arr = [5, 2, 8, 6, 1, 9, 3, 7]
    mid = 4

    (1) 재귀 
    left = merge_sort([5, 2, 8, 6]) -> [2, 5, 6, 8]
    arr = [5, 2, 8, 6]
    mid = 2
        (1-1) 재귀
        left = merge_sort([5, 2]) -> [2, 5]
        arr = [5, 2]
        mid = 1
            (1-1-1) 재귀 
            left = merge_sort([5]) -> [5]
            arr = [5]

            (1-1-2) 재귀
            right = merge_sort([2]) -> [2]
            arr = [2]

            merge([5],[2]) -> [2, 5]

        (1-2) 재귀
        right = merge_sort([8, 6]) -> [6, 8]

    (2) 재귀
    right = merge_sort([1, 9, 3, 7]) -> [1, 3, 7, 9]

    merge([2, 5, 6, 8], [1, 3, 7, 9]) -> [1, 2, 3, 5, 6, 7, 8, 9]

    '''

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

    '''
    left = [2, 5]
    right = [6, 8]
    result = []
    i = 0
    j = 0
    '''

    i = j = 0
    while i < len(left) and j < len(right):

        '''
        result = [2, 5, 6, 8]
        left = [2, 5]
        right = [6, 8]

        i = 2
        j = 0

        '''

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)
