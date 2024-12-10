'''
Ex20-4-Queue.py
큐(queue)
    컴퓨터 기본적인 자료구조의 한가지로,
    먼저 집어 넣은 데이터가 먼저 나오는
    FIFO(First In Frist out) 구조로
    저장하는 형식을 말한다.
'''

# def Queue():
#     queue = []
#     queue.append(1)
#     queue.append(2)
#     queue.append(3)
#     queue.append(4)
#     queue.append(5)
#     while queue:
#         print('Get Value: ', queue.pop(0))
#
# # 실행코드
# Queue()


class Queue:
    def __init__(self):
        self.queue = []  # 빈 리스트로 큐 초기화

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"'{item}' 추가됨")

    def dequeue(self):
        if self.is_empty():
            return "큐가 비어있습니다!"
        item = self.queue.pop(0)
        print(f"'{item}' 제거됨")
        return item

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            return "큐가 비어있습니다!"
        return self.queue[0]

    def display(self):
        if self.is_empty():
            print("큐가 비어있습니다!")
        else:
            print("현재 큐:", self.queue)


# 큐 사용 예제
if __name__ == "__main__":
    # 큐 생성
    q = Queue()

    # 큐에 데이터 추가 (enqueue)
    q.enqueue("첫번째 고객")
    q.enqueue("두번째 고객")
    q.enqueue("세번째 고객")

    # 현재 큐 상태 출력
    q.display()

    # 큐에서 데이터 제거 (dequeue)
    print("\n고객 응대 시작...")
    q.dequeue()  # 첫번째 고객 제거
    q.display()

    # 현재 첫번째 데이터 확인
    print("\n다음 고객 확인...")
    print("다음 고객:", q.peek())

    # 큐 크기 확인
    print("\n대기 중인 고객 수:", q.size())

    # 남은 고객 모두 처리
    print("\n모든 고객 응대...")
    while not q.is_empty():
        q.dequeue()
        q.display()
