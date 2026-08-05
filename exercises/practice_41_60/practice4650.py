# 46
# 定义一个名为American的类及其子类NewYorker。使用类子类（parentClass）来定义子类
import math


def pra46():
    class American(object):
        @staticmethod
        def printNationality():
            print("American")

    class NewYorker(American):
        @staticmethod
        def printNationality():
            print("NewYorker")

    new = NewYorker
    new.printNationality()


# 47
# 定义一个名为Circle的类，可以用半径来构造，Circle有一个可以计算面积的方法
def pra47():
    class Circle(object):
        radius: int = 1

        def __init__(self, r=None):
            self.radius = r

        def getArea(self):
            return self.radius ** 2 * math.pi

    c1 = Circle(2)
    print(c1.getArea())


# 48
# 定义一个名为Rectangle的类，可以用长和款来构造，Rectangle有一个可以计算面积的方法
def pra48():
    class Rectangle(object):
        l: int = 1
        w: int = 1

        def __init__(self, l=None, w=None):
            self.l = l
            self.w = w

        def getArea(self):
            return self.l * self.w

    r1 = Rectangle(2, 4)
    print(r1.getArea())


# 49
# 定义一个名为Shape的类及其子类Square。Square类有一个init函数，它以长度作为参数。这俩都有一个area函数，可以打印面积
def pra49():
    class Shape(object):
        def area(self):
            return 0

    class Square(Shape):
        l: int = 0

        def __init__(self, l=None):
            self.l = l

        def area(self):
            return self.l * self.l

    s1 = Square(2)
    print(s1.area())


# 50
# 引发RuntimeError异常
def pra50():
    raise RuntimeError("代码运行异常")


if __name__ == '__main__':
    pra50()
