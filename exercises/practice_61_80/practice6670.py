import random


# 66
# 随机生成一个1-100内的整数
def pra66():
    print(random.randint(1, 100))


# 67
# 生成一个值在10到100之间的随机浮点数
def pra67():
    print(random.random() * 100)


# 68
# 编写一个程序输出0和10之间的随机偶数
def pra68():
    # li1 = range(0, 11)
    # li2 = list(filter(lambda x: x % 2 == 0, li1))
    # print(li2[random.randint(0, 5)])
    print(random.choice([i for i in range(11) if i % 2 == 0]))


# 69
# 编写一个程序输出一个随机数，它可以被5和7整除，在0和1000之间
def pra69():
    print(random.choice([i for i in range(1000 + 1) if i % 7 == 0 and i % 5 == 0]))


# 70
# 编写一个程序生成一个包含100-200之间的5个随机数列表
def pra70():
    # li = []
    # for i in range(5):
    #     li.append(random.randint(100,200))
    #
    # for x in li:
    #     print(x)
    print(random.sample(range(100, 200), 5))


if __name__ == '__main__':
    pra70()
