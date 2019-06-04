

import os
# 声明全局变量
vard=['dafdf']
def nihao():
    global vard
    vard=25
    print(vard)
if __name__ == '__main__':
    nihao()

# os 目录操作模块,用于操作目录和权限
# 获取当前路径
getcwd = os.getcwd()
print(getcwd)
# 获取上级路径
abspath = os.path.abspath('..')
print(abspath)
#创建并打开open函数
# 写入式覆盖
text_io = open('wenjianming.text', 'w+')
text_io.write('你好')

# 写入式追加
text_io = open('wenjianming.text', 'a+')
text_io.write('干什么')

# 写入式只读不能写入
text_io = open('wenjianming.text', 'r')
# 多行读取
print(text_io.readlines())
