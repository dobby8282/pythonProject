class MaxHeap:
    """
    최대 힙 클래스 - 항상 부모 노드가 자식 노드보다 큰 값을 가지는 완전 이진 트리
    """
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        """인덱스 i의 부모 노드 인덱스 반환"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """인덱스 i의 왼쪽 자식 노드 인덱스 반환"""
        return 2 * i + 1
    
    def right_child(self, i):
        """인덱스 i의 오른쪽 자식 노드 인덱스 반환"""
        return 2 * i + 2
    
    def swap(self, i, j):
        """힙에서 두 노드의 위치를 교환"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        """
        새로운 원소를 힙에 추가
        1. 새 원소를 힙의 마지막에 추가
        2. 추가된 원소를 부모와 비교하면서 올바른 위치로 이동
        """
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        print(f"{key} 삽입 후 힙: {self.heap}")  # 각 삽입 후 상태 출력
    
    def _sift_up(self, i):
        """
        특정 노드를 부모 노드들과 비교하면서 위로 이동
        부모보다 큰 값을 가진 경우에만 위치를 교환 (최대 힙)
        """
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
    
    def extract_max(self):
        """
        최대값(루트 노드)을 제거하고 반환
        """
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return max_val
    
    def _sift_down(self, i):
        """
        특정 노드를 자식 노드들과 비교하면서 아래로 이동
        자식 중 더 큰 값을 가진 노드와 교환 (최대 힙)
        """
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
            
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
            
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)

# 주어진 숫자들을 차례대로 삽입
heap = MaxHeap()
numbers = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]

print("숫자 삽입 과정:")
for num in numbers:
    heap.insert(num)

print("\n최종 힙 상태:", heap.heap)