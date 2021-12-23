# @author:  fangfei
# @time  :  2021/12/21/0021  14:57
# @file  :  demo_错误与异常.py
# @desc  : 


def div(a, b):
    return a / b


f = open('data.txt')
_list = [0, 1, 2]

try:
    print(div(1, 1))
    print(_list[0])
    f.readlines()

# except ZeroDivisionError as e:
#     print('这块有一个异常处理')
#     print(e)
# except IndexError as e1:
#     print(e1)
except Exception as e:
    print(f'抛出异常：{e}')

else:   # 没有异常时执行
    print("没有异常时执行else语句")

finally:    # finally最终都会被执行，无论是否有异常
    f.close()
    print('finally最终都会被执行，无论是否有异常')


def set_age(num):
    if num <= 0 or num > 200:
        raise ValueError(f"年龄{num}设置错误")
    else:
        print(f"年龄{num}设置正确")


set_age(500)
