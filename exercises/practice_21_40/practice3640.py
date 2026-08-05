# 36
# 定义一个函数，它可以生成一个列表，其中值是1-20之间的数字的平方（包括在内），打印列表中除了前5个元素外的所有值
def pra36():
    list = []
    for i in range(1, 21):
        list.append(i ** 2)
    print(list[5:])


# 37
# 定义一个函数，它可以生成一个元组，其中值是1-20之间的数字的平方（包括在内）
def pra37():
    list = []
    for i in range(1, 21):
        list.append(i ** 2)
    print(tuple(list))


# 38
# 对于给定的元组(1,2,3,4,5,6,7,8,9,10),编写一个程序，在第一行输出前半部分值，在一行输出后半部分值
def pra38():
    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    spIndex = int(len(tuple1) / 2)
    print(tuple1[:spIndex])
    print(tuple1[spIndex:])


# 39
# 编写程序生成生成并输出一个元组，其值是给定元组(1,2,3,4,5,6,7,8,9,10)中的偶数
def pra39():
    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    result = []
    for i in tuple1:
        if i % 2 == 0:
            result.append(i)
    print(tuple(result))


# 40
# 写一个程序，接受一个字符串作为输入，如果字符串是"yes""YES""Yes"打印"Yes"，否则打印"No"


if __name__ == '__main__':
    pra39()
