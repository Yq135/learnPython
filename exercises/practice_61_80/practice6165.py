# 61
# 斐波那契数列的计算公式如下：如果n=0,f(n)=0;如果n=1,f(n)=1;如果n>1,f(n)=f(n-1)+f(n-2);
# 编写一个程序，在控制台输入给定n的情况下计算f(n)的值，输入：7，输出：13
def pra61():
    num = int(input("输入一个整数："))

    def funa(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return funa(n - 1) + funa(n - 2)

    print(funa(num))


# 62
# 使用generator编写一个程序，由控制台输入n，以逗号分隔的形式输出0到n之间的偶数
# 示例：输入：10，输出：0,2,4,6,8,10
def pra62():
    num = int(input("输入一个整数："))

    def getEnevNum(n):
        for i in range(n + 1):
            if i % 2 == 0:
                yield i

    ge = getEnevNum(num)
    # for i in range(num+1):
    #     print(next(ge))
    li = []
    for i in ge:
        li.append(str(i))
    print(",".join(li))


# 63
# 请编写一个生成器程序，由控制台输入n，以逗号分隔的形式输出0到n之间可以被5和7整除的数字
# 示例：输入：100，输出：0,35,70
def pra63():
    num = int(input("输入一个整数："))

    def generatorFunc(n):
        for i in range(n + 1):
            if i % 5 == 0 and i % 7 == 0:
                yield i

    ge = generatorFunc(num)
    li = []
    for i in ge:
        li.append(str(i))
    print(",".join(li))


# 64
# 请写assert语句来验证列表[2,4,6,8]中的每个数字都是偶数
def pra64():
    list = [2, 4, 6, 8]
    list1 = [2, 4, 7, 8, 9]
    for i in list:
        assert i % 2 == 0
    for i in list1:
        assert i % 2 == 0


# 65
# 请编写一个程序，从控制台接收基本的数学表达式，输出计算结果
# 示例：输入 35+3，输出：38
def pra65():
    line = input("输入一个数学表达式：")
    print(eval(line))


if __name__ == '__main__':
    pra65()
