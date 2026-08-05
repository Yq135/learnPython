import re


# 51
# 编写一个函数计算5/0，使用try/catch捕获异常
def pra51():
    def throwErr():
        return 5 / 0

    try:
        throwErr()
    except ZeroDivisionError:
        print("division by zero")
        print("O不能做分母")
    except Exception:
        print("caught an exception")
    finally:
        print("In finally block for cleanup")


# 52
# 定义一个自定义异常类，它将字符串作为消息属性
def pra52():
    class ServiceError(Exception):
        msg: str

        def __init__(self, msg):
            self.msg = msg

    raise ServiceError("发生了一个错误")


# 53
# 假设我们有一些'username@companyname.com'格式的电子邮件地址，请编写程序打印给定电子邮件地址的用户名，用户名和公司名都由字母组成
# 示例：输入：john@google.com 输出：john
def pra53():
    email = input("请输入电子邮箱:")
    # print(email.split('@')[0])
    pattern = '(\w+)@((\w+\.)+(com))'
    r1 = re.match(pattern, email)
    print(r1.group(1))
    # print(r1.group(2))


# 54
# 假设我们有一些'username@companyname.com'格式的电子邮件地址，请编写程序打印给定电子邮件地址的公司名，用户名和公司名都由字母组成
# 示例：输入：john@google.com 输出：google
def pra54():
    email = input("请输入电子邮箱:")
    pattern = '(\w+)@(\w+).com'
    r1 = re.match(pattern, email)
    print(r1.group(2))


# 55
# 编写一个程序，接收一个由空格分隔的单词序列作为输入，打印只由数字组成的词。
# 示例：输入：2 cats and 3 dogs; 输出：['2','3']
def pra55():
    line = input("请由空格分隔的单词序列:")
    # list = line.split(" ")
    # res = []
    # for s in list:
    #     if s.isdigit():
    #         res.append(s)
    #
    # print(",".join(res))
    print(re.findall('\d+', line))


if __name__ == '__main__':
    pra55()
