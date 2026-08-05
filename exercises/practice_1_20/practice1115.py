import re


# 11
# 编写一个程序，接收一系列以逗号分隔的4位二进制数作为输入，然后检查他们是否可以被5整除，可被5整除的数字以逗号分隔顺序打印
# 示例：输入：0100,0011,1010,1001 ；输出：1010
def pra11():
    list = input("输入以逗号分隔的4位二进制数：").split(",")
    res = []
    for bn in list:
        # num = 0
        # length = len(bn)
        # for i in range(length):
        #     num += int(bn[i]) *  2 ** (length - 1 - i)
        num = int(bn, 2)
        if num % 5 == 0:
            res.append(bn)
    print(",".join(res))


# 12
# 编写一个程序，找到1000到3000之间所有位数均为偶数的数字，比如2000，2002等；获得的数字都以逗号分隔顺序打印在一行上
def pra12():
    res = []
    for num in range(2000, 3000):
        # flg = True
        # for i in str(num):
        #     if int(i) % 2 == 0:
        #         flg = True
        #     else:
        #         flg = False
        #         break
        # if flg:
        #     res.append(str(num))
        if int(str(num)[0]) % 2 == 0 and int(str(num)[1]) % 2 == 0 and \
                int(str(num)[2]) % 2 == 0 and int(str(num)[3]) % 2 == 0:
            res.append(str(num))
    print(",".join(res))


# 13
# 编写一个接收句子并计算字母和数字个数的程序
# 示例： 输入：Hello world! 123 ; 输出：字母10 数字3
def pra13():
    line = input("输入一个句子：")
    wordCount = 0
    numCount = 0
    for s in line:
        if re.match("[0-9]", s):  # s.isdigit()
            numCount += 1
        if re.match("[a-zA-Z]", s):  # s.isalpha()
            wordCount += 1
    # print("字母"+str(wordCount)+"数字"+str(numCount))
    print(f"字母{wordCount}数字{numCount}")


# 14
# 编写一个接收句子并计算大写字母和小写字母数量的程序
# 示例： 输入：Hello world! ; 输出：UPPER CASE 1; LOWER CASE 9
def pra14():
    line = input("输入一个句子：")
    # dict = {"UPPER CASE": 0, "LOWER CASE": 0}
    upper_case = 0
    lower_case = 0
    for s in line:
        if re.match("[A-Z]", s):  # s.isupper()
            upper_case += 1
        if re.match("[a-z]", s):  # s.islower()
            lower_case += 1
    print(f"UPPER CASE {upper_case};LOWER CASE {lower_case}")


# 15
# 编写一个程序，计算a+aa+aaa+aaaa的值，给定的数字作为啊的值
# 示例：输入：9，输出：11106
def pra15():
    s = input("输入一个整数：")
    # num1 = int(s)
    # num2 = int(s+s)
    # num3 = int(s+s+s)
    # num4 = int(s+s+s+s)
    # sum = num1 + num2 + num3 + num4
    li = []
    for i in range(1, 5):
        # numstr = ''
        # for j in range(i):
        #     numstr += s
        numstr = s * i
        li.append(numstr)
    sum = 0
    for str in li:
        sum += int(str)
    print(sum)


if __name__ == '__main__':
    # pra15()
    s = input()
    print(s * 5)
