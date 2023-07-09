'''
파일명: Ex23-2-SelectionSort.py

선택정렬(Selection Sort)
    주어진 리스트에서 최소값을 찾아
    맨 앞에 있는 값과 교체하는 알고리즘
'''

# 선택 정렬 알고리즘
def selection_sort(arr):

    for i in range(len(arr)):

        min_idx = i

        for j in range(i + 1, len(arr)):
            '''
            arr = [1, 2, 4, 5, 3]
            i = 2
            j = 4
            min_idx = 4
            '''

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# 실행코드
arr = [5, 3, 4, 1, 2]
print(selection_sort(arr))