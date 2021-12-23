# @author:  fangfei
# @time  :  2021/12/21/0021  6:30
# @file  :  demo_读取文件.py
# @desc  : 

# with语句块，可以将文件打开后，操作完成后，自动关闭这个文件
with open('data.txt') as f:
    # print(f.readlines())
    print(f.readline(2))  # 2为可选参数 为字符长度
    # while True:
    #     line = f.readline()
    #
    #     if line:
    #         print(line)
    #     else:
    #         break

