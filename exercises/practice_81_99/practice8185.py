import numpy as np


# 81
# 编写一个程序使用列表生成一个358的三位数组，每个元素为0
def pra81():
    # li = [3, 5, 8]
    # res = []
    # 一、手搓
    # def zeroList(n):
    #     li = [0 for x in range(n)]
    #     return li
    #
    # for x in range(li[0]):
    #     row = [zeroList(li[2]) for y in range(li[1])]
    #     res.append(row)
    # 二、简化
    # res = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
    # 三、numpy
    res = np.zeros((3, 5, 8), dtype=int)

    print(res)


# 82
# 编写一个程序，去掉[12,24,35,70,88,120,155]中的第0，第4，第5位数字后，打印列表
def pra82():
    li = [12, 24, 35, 70, 88, 120, 155]
    res = [x for (i, x) in enumerate(li) if i not in [0, 4, 5]]
    print(res)


# 83
# 编写一个程序，在[12,24,35,70,88,120,155]中删除值24后打印列表
def pra83():
    li = [12, 24, 35, 70, 88, 120, 155]
    li.remove(24)
    print(li)


# 84
# 对于两个列表[1,3,6,78,35,55]和[12,24,35,70,88,120,155]，编写一个程序生成一个元素为两个列表交集的列表并打印
def pra84():
    li1 = [1, 3, 6, 78, 35, 55]
    li2 = [12, 24, 35, 70, 88, 120, 155]
    res = [n for n in li1 if n in li2]
    print(res)

    # 二、用集合
    set1 = set(li1)
    set2 = set(li2)
    set1 &= set2
    li = list(set1)
    print(li)


# 85
# 对于给定列表[12,24,35,24,70,88,120,155,88,120,155],编写一个程序删除所有重复的值保留原始顺序，打印这个列表
def pra85():
    li = [12, 24, 35, 24, 70, 88, 120, 155, 88, 120, 155]
    set1 = set()
    res = []
    for i in li:
        if i in set1:
            continue
        else:
            set1.add(i)
            res.append(i)
    print(res)


if __name__ == '__main__':
    pra85()
