import random
import time
import zlib
from timeit import Timer


# 71
# 编写一个程序生成一个随机列表，其中包含100到200间的五个偶数
def pra71():
    list = [x for x in range(100, 201) if x % 2 == 0]
    print(random.sample(list, 5))


# 72
# 编写一个程序，随机生成一个列表，其中包含1到1000间可以被5和7整除的数字
def pra72():
    list = [x for x in range(1001) if x % 5 == 0 and x % 7 == 0]
    print(random.sample(list, 5))


# 73
# 随机打印一个7到15之间的整数
def pra73():
    print(random.randint(7, 15))


# 74
# 编写一个程序来压缩和解压字符串"hello world! hello world! hello world! hello world! hello world!"
def pra74():
    # import zlib
    s = b"hello world! hello world! hello world! hello world! hello world!"
    z = zlib.compress(s)
    print(z)
    d = zlib.decompress(z)
    print(d)


# 75
# 编写一个程序打印100次"1+1" 执行的运行时间
def pra75():
    # startTime = time.localtime()
    # for i in range(100):
    #     print("1+1")
    # endTime = time.localtime()
    # print('总计耗时：', endTime-startTime, 'ms')
    ti = Timer("for i in range(100): 1+1")
    print(ti.timeit())


if __name__ == '__main__':
    pra75()
