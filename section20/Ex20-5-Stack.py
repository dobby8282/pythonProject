'''
파일명: Ex20-5-Stack.py
스택(Stack)
    한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형구조로
    후입선출(LIFO - Last In First Out)로 되어 있다.
    자료를 넣는 것을 '밀어 넣다' 하여 Push라 하고
    반대로 넣어둔 자료를 꺼내는 것을 Pop 이라고 하는데
    이때 꺼내지는 자료는 가장 최근에 Push한 자료부터 나오게 된다.

'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        print(self.stack)

# 실행 코드
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.print_stack()

while not stack.is_empty():
    print('stack pop: ', stack.pop())
