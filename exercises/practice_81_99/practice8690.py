# 86
# 定义一个类Person和它的两个子类：Male和Female
# 所有的类都有一个getGender方法，它可以打印：Male为男性类，Female为女性类
def pra86():
    class Person(object):
        def getGender(self):
            pass

    class Male(Person):
        def getGender(self):
            print("Male为男性类")

    class Female(Person):
        def getGender(self):
            print("Female为女性类")

    man = Male()
    man.getGender()
    woman = Female()
    woman.getGender()


# 87
# 编写一个程序，计算并打印由控制台输入的字符串中的每个字符的数量
# 示例：输入：abcdefgabcd, 输出：a,2 b,2 c,2 d,2 e,1 f,1 g,1
def pra87():
    line = input("输入一串字符串：")
    countDict = {}
    # for s in line:
    #     if s in countDict:
    #         countDict[s] = countDict[s]+1
    #     else:
    #         countDict[s] = 1
    # for key in countDict.keys():
    #     print("%s,%d" % (key, countDict[key]))
    for s in line:
        countDict[s] = countDict.get(s, 0) + 1
    print(" ".join(["%s,%d" % (k, v) for k, v in countDict.items()]))


# 88
# 两个列表：x=['11','uu','kk','hh'],y=[1,2,3,4,5,6],对这两个列表进行数据对其
def pra88():
    x = ['11', 'uu', 'kk', 'hh']
    y = [1, 2, 3, 4, 5, 6]
    # dic = {}
    # for i in range(len(x)):
    #     if y[i]:
    #         dic[x[i]] = y[i]
    #     else:
    #         break
    # for key in dic.keys():
    #     print("%s,%d" % (key, dic[key]))
    for i, j in zip(x, y):
        print(i, j)


# 89
# 请编写一个程序，从控制台输入一个字符串，将字符串以相反的顺序打印出来
# 示例：输入：rise to vote sir ; 输出：ris etov ot esir
def pra89():
    line = input("输入一串字符串：")
    # res =[]
    # size = len(line)
    # for i in range(len(line)):
    #     res.append(line[size-1])
    #     size -=1
    # print("".join(res))
    res = line[::-1]
    print(res)

#90
#编写一个程序，从控制台接收一个字符串，并打印具有偶数索引的字符
#示例：输入H1e2l3l4o5w6o7r8l9d 输出：Helloworld
def pra90():
    line = input("输入一串字符串：")
    # res = []
    # for i in line:
    #     if line.index(i) %2 ==0:
    #         res.append(i)
    # print("".join(res))
    res = line[::2]
    print(res)

if __name__ == '__main__':
    pra90()
