import re


# 01
# 编写一个程序，找到2000年至3200年中，所有可以被7整除但不能被5整除的所有数字，结果以逗号分割打印在一行上
def par01():
    li = []
    for i in range(2000, 3200 + 1):
        if i % 7 == 0 & i % 5 != 0:
            li.append(str(i))
    print(",".join(li))


# 02
# 编写一个可以计算给定数阶乘的程序，结果以逗号分割打印在一行上
def par02():
    def fact(x):
        if x == 0:
            return 1
        return x * fact(x - 1)

    num = int(input("请输入一个整数："))
    print(fact(num))


# 03
# 使用给定的整数n,编写一个程序生成一个包含（i，ixi）的字典，该字典包含从1到n之间的整数（两者都包含），打印这个字典
# 示例： 输入5，返回{1:1, 2:4, 3:9, 4:16, 5:25}
def par03():
    def square_dict(x):
        d = dict()
        for i in range(1, x + 1):
            d[i] = i * i
        return d

    num = int(input("请输入一个整数："))
    print(square_dict(num))


# 04
# 编写一个程序，该程序接收控制台以逗号分割的整数序列，并生成包含每个数字的列表和元组
# 示例：输入 24岁，67年,12点,12日,98年,8月 ；输出：['24','67','12','12','98','8']('24','67','12','12','98','8')
def par04():
    def str2List(string):
        # li = string.split(',')
        # for i in range(0, len(li)):
        #     li[i] = re.search('\d*', li[i]).group()
        li = re.findall(r'[0-9]+', string)
        print(li)
        print(tuple(li))

    string = input("请输入一个逗号分割的整数序列：")
    str2List(string)


# 05
# 定义一个至少有两个方法的类：一个getString：从控制台获取字符串，一个printString：打印大写字母的字符串，并写出简单的测试函数来测试类方法
def par05():
    class PrintUpperString(object):
        s: str

        def getString(self):
            global ss
            ss = input("输入一串字符串：")

        def printString(self):
            print(ss.upper())

    def par05test():
        pus = PrintUpperString()
        pus.getString()
        pus.printString()

    par05test()


if __name__ == "__main__":
    par05()
