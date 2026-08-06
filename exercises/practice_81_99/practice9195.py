import itertools


# 91
# 编写一个程序，打印[1,2,3]的所有排列
def pra91():
    li = [1, 2, 3]
    iter = itertools.permutations(li)
    for s in iter:
        print(s)


# 92
# 写一个程序来解决经典难题：鸡兔同笼，鸡和兔子一共有35个头和94只脚。返回有多少只兔子，多少只鸡
def pra92():
    def func(x, y):
        for i in range(1, x + 1):
            j = x - i
            if 2 * i + 4 * j == y:
                return i, j

    x, y = func(35, 94)
    print(f"鸡:{x},兔子:{y}")


# 93
# 给定一个字符，用它构造一个底边长5个字符，高3个字符的等腰三角形
def pra93():
    s = input("输入一个字符：")

    # print("  %s  " % s)
    # print(" %s%s%s " % (s, s, s))
    # print("%s%s%s%s%s" % (s, s, s, s, s))
    # print("  "+s)
    # print(" "+s+s+s)
    # print(s*5)
    def func(h, char):
        for i in range(1, h + 1):
            print(" " * (h - i) + char * ((i - 1) * 2 + 1))

    func(3, s)


# 94
# 已知一个字符串为"hello_world_yoyo"，如何得到一个队列["hello","world","yoyo"]
def pra94():
    s = input("输入一个字符串：")
    print(s.split("_"))


# 95
# 打印99乘法表
def pra95():
    # for i in range(1, 10):
    #     li = ["%s * %s = %s" % (i, j, i * j) for j in range(1, i + 1)]
    #     print("  ".join(li))
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d*%d=%-2d" % (i, j, i * j), end="  ")  # 平常end默认"\n"
            j += 1
        print()
        i += 1


if __name__ == '__main__':
    pra95()
