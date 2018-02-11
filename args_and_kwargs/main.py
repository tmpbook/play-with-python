# 搞懂 *args 和 **kwargs ️️❤️ 临书
''' 一 '''
def aoo(*args, g):
    print(args)

foo(1, 2, 3, g=6)
# out:
# (1, 2, 3)

''' 二 '''
def boo(f, **kwargs):
    print(kwargs)

boo(f=1, app=12, gen=23)
# out:
# {'gen': 23, 'app': 12}

''' 三 '''
def coo(*arg, **kwarg):
    print(arg)
    print(kwarg)

coo(1, 2, 3, a=1, b=2, c=3)
# out:
# (1, 2, 3)
# {'b': 2, 'a': 1, 'c': 3}

''' 四 '''
def doo(a, b, c):
    print(a, b, c)

abc = [1, 2, 3]
doo(*abc)
# out:
# 1 2 3

''' 五 '''
# **Python3 新语法**
first, *other = [1,2,3,4]
# first 的值是：1
# other 的值：[2, 3, 4]
first, *other, penult, last = [1,2,3,4]
# other 的值是 [2]
