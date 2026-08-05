# 26
# 定义一个函数，可以接受两个字符串作为输入，将它们链接起来，在控制台输出
def pra26():
    def joint(a, b):
        return str(a) + str(b)

    print(joint(12, 36))


# 27
# 定义一个函数，可以接收两个字符串作为输入，在控制台中以最大长度打印字符串。如果两个字符串长度相同，则函数逐行打印所有字符串
def pra27():
    def compareLength(str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        maxlen = max(len1, len2)
        if maxlen == len1:
            print(str1)
        if maxlen == len2:
            print(str2)

    print(compareLength('effw', '324531dxfv'))


# 28
# 定义一个函数，它可以接收一个整数作为输入，如果这个数字是偶数输出"它是偶数"，否则输出"它是奇数"

# 29
# 定义一个函数，它可以打印一个字典，其中健是1到3之间的数字（包括在内），值是健的平方。

# 30
# 定义一个函数，它可以打印一个字典，其中键是1-20之间的数字（包括在内），值是健的平方。

if __name__ == '__main__':
    pra27()
