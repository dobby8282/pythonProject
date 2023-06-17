'''
파일명: Ex16-1-constructor.py

생성자
    객체를 생성할 때 생성자가 자동으로 호출된다.
    주로 객체 초기화 용으로 사용.

생성자 선언방법
    __init()__

'''
class USB:
    def __init__(self, capacity): # 생성자
        self.capacity = capacity

    def info(self):
        print('{}GB USB'.format(self.capacity))


# 실행코드
usb = USB(128)
usb.info()

usb2 = USB(1024)
usb2.info()






