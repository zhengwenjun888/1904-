def def1():
    print('test1')
def def2():
    print('test2')
def def3():
    print('test3')

def day1():
    # 声明变量
    a='Hello word'
    b=123
    c=1.22
    d=[]
    e=()
    f={}
    print(a)
    # 打印类型
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
# 数据类型转换b,e
    print(type(str(b)))
    print(type(str(e)))
def pingjie():
    a='你好'
    b=123
    print(a+str(b))
    print('%s%s'%(a,b))
def yunsuan(a,b):
    print(a+b)
    print(a-b)
    print(a/b)
def fanzhi(a,b):
    c=a*b
    return c




if __name__ == '__main__':
    # def3()
    # def1()
    # def2()

    # day1()
    pingjie()
    yunsuan(6,2)
    c=fanzhi(3,4)
    print(c)








