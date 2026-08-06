from random import shuffle


# 76
# 编写一个程序洗牌和打印列表[3,6,7,8]
def pra76():
    list = [3, 6, 7, 8]
    shuffle(list)
    print(list)


# 77
# 请编写一个程序,生成主语在['I','You']中,动词在['play','love']中,对象在['Hockey','Football']中的所有句子
def pra77():
    li1 = ['I', 'You']
    li2 = ['play', 'love']
    li3 = ['Hockey', 'Football']
    # res = []
    for s1 in li1:
        for s2 in li2:
            for s3 in li3:
                print('%s %s %s.' % (s1, s2, s3))


# 78
# 写一个程序,删除列表中的所有偶数后打印,列表：[5,6,77,45,22,12,24]
def pra78():
    li = [5, 6, 77, 45, 22, 12, 24]
    res = list(filter(lambda x: x % 2 != 0, li))
    print(res)


# 79
# 编写程序，删除[12,24,35,70,88,120,155]中可以被5和7整除的数后打印列表
def pra79():
    li = [12, 24, 35, 70, 88, 120, 155]
    res = list(filter(lambda x: x % 5 != 0 and x % 7 != 0, li))
    print(res)


# 80
# 编写一个程序，去掉[12,24,35,70,88,120,155]中的第0,2,4,5位置上的元素后打印列表
def pra80():
    li = [12, 24, 35, 70, 88, 120, 155]
    del_index = [0, 2, 4, 5]
    del_index.reverse()
    for i in del_index:
        li.pop(i)
    print(li)


# 编写一个程序，去掉[12,24,35,70,88,120,155]中的第0,2,4,6位置上的元素后打印列表
def pra80_1():
    li = [12, 24, 35, 70, 88, 120, 155]
    res = [x for (i, x) in enumerate(li) if i % 2 != 0]
    print(res)


if __name__ == '__main__':
    pra80_1()
