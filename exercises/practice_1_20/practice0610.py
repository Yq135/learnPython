import math


# 06
# 编写一个程序，根据给定的公式计算并打印值：假设C=50, H=30, D是一个变量，他的是以逗号分割的序列输入到程序中
# 示例：输入：100，150，180；程序输出：18，22，24
def par06():
    c = 50
    h = 30
    l = input("请输入一组数字：").split(",")
    res = []
    for d in l:
        res.append(str(round(math.sqrt(2 * c * float(d) / h))))
    print(",".join(res))


# 07
# 编写一个程序，X,Y作为输入，生成一个二维数组，数组的第i行和第j列的元素值应该是ixj。i=0,1,2, X-1, j= 0,1,2,J-1
# 示例：输入：3, 5 ; 程序输出为：[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]
def par07():
    x = int(input("输入二维数组的行："))
    y = int(input("输入二维数组的列："))
    l1 = []
    for i in range(0, x):
        l2 = []
        for j in range(0, y):
            l2.append(i * j)
        l1.append(l2)
    print(l1)


# 08
# 编写一个程序，以逗号分割的单词序列作为输入，按照字母顺序对每个单词进行排序，并通过逗号分隔的序列来打印单词。
# 示例： 输入： without,hello,bag,world ; 输出： bag,hello,without,world
def par08():
    s = input("输入单词序列：")
    l = s.split(",")
    l.sort()
    print(",".join(l))


# 09
# 编写一个程序，接收一行序列作为输入，并将句子中的所有字符大写后打印
def par09():
    lines = []
    while True:
        s = input("输入一行序列字符串：")
        if s != None:
            lines.append(s.upper())
        else:
            break
        for s1 in lines:
            print(s1)


# 10
# 编写一个程序，以一系列空格分割的单词作为输入，并在删除所有重复单词后，按字母顺序排序后打印这些单词。
# 示例：输入：hello world and practice makes perfect and hello world agin
#      输出：again and hello makes perfect practice world
def par10():
    s = input("输入一系列空格分割的单词：")
    lines = s.split(" ")
    set1 = set(lines)
    li2 = list(set1)
    li2.sort()
    print(" ".join(li2))


if __name__ == "__main__":
    par10()
