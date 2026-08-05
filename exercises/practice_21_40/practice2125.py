# 21
# 编写一个程序来打印一些Python内置函数文档(doc)，例如abs(),int()
def pra21():
    print(int.__doc__)


# 22
# 定义一个类，它具有类参数并具有相同的实例参数
def pra22():
    class BeanP():
        name: str = "jack"
        age: int
        heignt: int

        def __init__(self, name=None, age=None, height=None):
            if name:
                self.name = name
            if age:
                self.age = age
            if height:
                self.heignt = height

    p = BeanP('kaiy', 18, 180)
    print(p.name)
    n = BeanP()
    print(n.name)


# 23
# 定义一个可以计算两数之和的函数
def pra23():
    def sum1(a, b):
        return int(a) + int(b)

    print(sum1(12, 36))


# 24
# 定义一个可以将整数转换为字符串并在控制台打印的函数
def pra24():
    def printInt(num):
        print(str(num))

    printInt(24)


# 25
# 定义一个函数，它可以接收两个字符串形式的整数并计算他们的和，然后再控制台输出
def pra25():
    def sum2(a, b):
        return int(a) + int(b)

    print(sum2("12", "36"))


if __name__ == '__main__':
    pra25()
