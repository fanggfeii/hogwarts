# @author:  fangfei
# @time  :  2021/12/22/0022  15:10
# @file  :  demo_三目运算符.py
# @desc  : 

'''
exp1 if contion else exp2

使用 if else 实现三目运算符（条件运算符）的格式如下：
exp1 if contion else exp2

condition 是判断条件，exp1 和 exp2 是两个表达式。
如果 condition 成立（结果为真），就执行 exp1，并把 exp1 的结果作为整个表达式的结果；
如果 condition 不成立（结果为假），就执行 exp2，并把 exp2 的结果作为整个表达式的结果。
'''

a = int(input("Input a: "))
b = int(input("Input b: "))
print("a大于b") if a > b else (print("a小于b") if a < b else print("a等于b"))
