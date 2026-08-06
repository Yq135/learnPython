import re


# 96
# 输入一个姓名，判断是否姓王
def pra96():
    name = input("输入一个姓名:")
    if "王" == name[0]:
        print("是姓王")
    else:
        print("不姓王")


# 97
# 统计字符串中字母w出现的次数
# 示例：Hello,welcome to my world.
def pra97():
    line = input("输入一个字符串:")
    li = re.findall("[wW]", line)
    print("w出现了%d次" % len(li))
    count = 0
    for s in line:
        if 'w' == s:
            count += 1
    print("w出现了%d次" % len(li))


# 98
# 返回列表 a=[1,-6,2,-5,9,4,20,-3]中的数字绝对值
def pra98():
    a = [1, -6, 2, -5, 9, 4, 20, -3]
    res = [abs(x) for x in a]
    print(res)


if __name__ == '__main__':
    pra98()
