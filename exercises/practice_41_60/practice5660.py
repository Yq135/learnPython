# 56
# 打印unicode字符串"hello world"
def pra56():
    u = u"hello world"
    print(u)
    # s= "hello world"


# 57
# 编码与解码
def pra57():
    s = "hello world"
    enc = s.encode('utf-8')
    print(enc)
    dec = enc.decode('utf-8')
    print(dec)


# 58
# 编写一个特殊注释来表明python源代码文件是unicode格式的
def pra58():
    # -*- coding: unicode -*-
    # --------------------------#
    s = "hello world"


# 59
# 写一个程序来计算1/2+2/3+3/4+..+n/(n+1)
# 示例：输入：5 输出：3.55
def pra59():
    num = int(input("输入一个整数："))

    # count = 0.00
    # for j in range(1, num + 1):
    #     count += j / (j + 1)
    # print(count)

    def funa(n):
        if n == 0:
            return 0
        else:
            return n / (n + 1) + funa(n - 1)

    print(funa(num))


# 60
# 编写程序计算：当n>0和F(0)=0时，F(n) = F(n-1)+100通过控制台输入一个给定的n(n>0)
# 示例：输入：5 输出：500
def pra60():
    num = int(input("输入一个整数："))

    def funa(n):
        if n == 0:
            return 1
        else:
            return funa(n - 1) + 100

    print(funa(num))


if __name__ == '__main__':
    pra60()
