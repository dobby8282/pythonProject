'''
파일명: Ex20-1-Linear.py

자료구조
    데이터를 저장하고 조직화하는 방법론

선형리스트(LinearList)
    간단한 자료구조 중 하나로, 데이터를 일렬로 나열한 것이다.

'''

class LinearList():
    def __init__(self):
        self.linear = []


    def add_data(self, data):
        linear = self.linear
        linear.append(None)
        lLen = len(linear)
        linear[lLen - 1] = data

    def insert_data(self, position, data):
        linear = self.linear

        if position < 0 or position > len(linear):
            print('데이터를 삽입할 범위를 벗어났습니다.')
            return

        linear.append(None)
        linearSize = len(linear)

        for i in range(linearSize - 1, position, -1):
            linear[i] = linear[i - 1]
            linear[i - 1] = None

        linear[position] = data

    def delete_data(self, position):
        linear = self.linear

        if position < 0 or position > len(linear):
            print('데이터를 삭제할 범위를 벗어났습니다.')

        linear[position] = None
        linearSize = len(linear)

        for i in range(position + 1, linearSize):
            linear[i - 1] = linear[i]
            linear[i] = None

        del(linear[linearSize - 1])

    def print_list(self):
        linear = self.linear
        for list in linear:
            print(list)

# 실행코드
linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)

linear.insert_data(3, 99)

linear.delete_data(2)

linear.print_list()














