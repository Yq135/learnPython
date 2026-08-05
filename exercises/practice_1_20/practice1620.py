from operator import itemgetter, attrgetter


# 16
# 使用列表推导输出列表中的每个奇数，该列表由一系列逗号分隔的数字输入
def pra16():
    list = input("输入一系列逗号分隔的数字:").split(",")
    res = []
    for i in list:
        if int(i) % 2 != 0:
            res.append(i)
    print(",".join(res))


# 17
# 编写一个程序，按升序对（名称，年龄，高度）元组进行排序，其中name是字符串，age和height是数字，元组由控制台输入
# 优先级 name>age>height
# 示例：Tom,19,80; John,20,90; Jony,17,91; Json,21,85
def pra17():
    inputStr = input()
    strList = inputStr.split(";")
    tupleList = []
    for str in strList:
        tuple1 = tuple(str.split(","))
        tupleList.append(tuple1)
    # from operator import itemgetter, attrgetter
    print(sorted(tupleList, key=itemgetter(0, 1, 2)))


# 18
# 使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字
def pra18():
    def genNumber(n):
        for i in range(n + 1):
            if i % 7 == 0:
                yield i

    for i in genNumber(100):
        print(i)


# 19
# 编写一个程序，计算每个单词在输入的句子中出现的频率，按字母顺序对健进行排序后输出
# 示例：New to Python or choosing between Python 2 and Python 3? Read  Python 2 or Python 3.
def pra19():
    line = input("输入一个句子：")
    wordList = [x for x in line.split()]
    wordDict = {}
    for word in wordList:
        count = wordDict.get(word)
        if count:
            count += 1
            wordDict[word] = count
        else:
            wordDict[word] = 1
    res = sorted(wordDict.keys())
    for r in res:
        print("%s:%d" % (r, wordDict[r]))
        # print(f"{r}:{wordDict[r]}")


# 20
# 写一个可以计算数字平方值的方法，使用**
def pra20():
    s = input("输入一个数字：")
    print(int(s) ** 2)


if __name__ == '__main__':
    pra20()
