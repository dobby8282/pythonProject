'''
파일명: Ex16-5-inheritance.py

상속(inheritance)
    상위클래스(부모클래스, 슈퍼클래스)가 가지고 있는 기능을
    그대로 물려받아 하위클래스(자식클래스, 서브클래스)에서
    사용할 수 있다. (확장개념)

상속방법
class 상위클래스
    본문
    
class 하위클래스(상위클래스)
    본문

'''
# 부모클래스
class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print('원두: {}'.format(self.bean))

# 자식클래스
class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print('물: {}ml'.format(self.water))

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()

print(coffee.bean)
coffee.coffee_info()








