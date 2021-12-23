# @author:  fangfei
# @time  :  2021/12/22/0022  15:19
# @file  :  demo_推导式.py
# @desc  :


# 列表推导式:[表达式 for 变量 in 列表]    或者  [表达式 for 变量 in 列表 if 条件]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print({x ** 2 for x in li})
print([x**2 for x in li if x > 5 if x < 9])
print(dict([(x, x*10) for x in li]))
print([(x, x*10) for x in li])

# 生成平方列表。如【1,4,9】
_list1 = []
for i in range(1, 4):
    _list1.append(i**2)
print(_list1)

_list2 = [i**2 for i in range(1, 4)]
print(_list2)

_list3 = [i**2 for i in range(1, 4) if i != 1]
print(_list3)

_list4 = [i*j for i in range(1, 4) for j in range(1, 4)]
print(_list4)


# 字典推导式
_dict = {i: i*2 for i in range(1, 4 )}
print(_dict)
