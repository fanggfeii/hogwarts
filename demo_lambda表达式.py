# @author:  fangfei
# @time  :  2021/12/22/0022  14:47
# @file  :  demo_lambda表达式.py
# @desc  :

func_1 = lambda x: x*3
# _func = lambda x, y: x+y
'''
之所以有下划线，是因为你把lambda表达式赋给了另一个变量。
但lambda表达式本就是一个匿名的函数，PEP8规范并不推荐将lambda表达式赋值给一个变量，
再通过变量调用函数这种方式。
'''


def func_2(x): return x*3


def func_3(x):
    return x*3


print(func_1(5))

