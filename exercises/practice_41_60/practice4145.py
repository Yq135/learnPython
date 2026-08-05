# 41
# 编写一个程序，使用过滤函数过滤列表中的偶数，列表[1,2,3,4,5,6,7,8,9,10]
def pra41():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    li = filter(lambda x: x % 2 == 0, list)
    for tm in li:
        print(tm)


# 42
# 编写一个程序，使用map函数构造一个列表，其中的元素是[1,2,3,4,5,6,7,8,9,10]列表元素的平方
def pra42():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # li = [x**2 for x in list]
    li = map(lambda x: x ** 2, list)
    for tm in li:
        print(tm)


# 43
# 编写一个程序，使用map函数和filter生成一个列表，其中的元素是[1,2,3,4,5,6,7,8,9,10]列表中偶数的平方
def pra43():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    li = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, list))
    for tm in li:
        print(tm)


# 44
# 编写一个程序，使用map函数生成一个列表，其中的元素\是1-20之间的数字的平方（包括在内）
def pra44():
    # list = [x for x in range(1, 21)]
    # li = map(lambda x: x ** 2, list)
    li = map(lambda x: x ** 2, range(1, 21))
    for tm in li:
        print(tm)


# 45
# 定义一个名为American的类，它有一个名为printNationality的静态方法
def pra45():
    class American(object):

        @staticmethod
        def printNationality():
            print("American")
            print("这个American的静态方法")

    am = American
    am.printNationality()
    American.printNationality()


if __name__ == '__main__':
    pra45()
