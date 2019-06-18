
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
def str_caozuo():
    i=1000
    j=20
    a='kasdmdjs,alkhfasd'
    # 添加
    a='kasdmdjs,'+str(i)+'alkhfasd'
    print(a)
    #find 查找 显示的是m的下标,
    print(a.find("mdjs"))
    #split 切割,以什么切割''里放什么,生成的是列表
    print(a.split(','))
    #replace 替换,把a用1替换
    print(a.replace('a','1'))
#     添加




if __name__ == '__main__':
    # def3()
    # def1()
    # def2()
    str_caozuo()
    # day1()
    # pingjie()
    # yunsuan(6,2)
    # c=fanzhi(3,4)
    # print(c)








