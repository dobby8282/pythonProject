'''
파일명: Ex16-3-cls.py

클래스 변수
    클래스를 기반으로 만든 모든 인스턴스가 공유할 수 있는 변수

인스턴스 변수
    해당 인스턴스만 사용하는 값

클래스 메소드
    인스턴스가 없어도 클래스를 이용해 호출할 수 있다.
    cls 키워드를 이용해 클래스 메소드 안에서 클래스 변수 접근 가능.
'''
class Bag:
    count = 0   # 클래스 변수

    def __init__(self):
        Bag.count += 1

    @classmethod # 데코레이터
    def sell(cls):
        cls.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count

    @staticmethod
    def slogan():
        print('명품 주인을 찾습니다.')


# 실행코드
print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방: {}개'.format(Bag.remain_bag()))








