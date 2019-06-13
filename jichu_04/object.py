
# 声明一个类,大写字母开头
class Human(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eate(self):
        print(self.name+'吃饭')
    def sleep(self):
        print(self.name+'睡觉')
    def info(self):
        print('%s%s%s'%(self.name,self.age,self.sex))





# 继承
class Tester(Human):
    # 继承后可以继续初始化并添加参数
    def __init__(self,name,age,sex,job):
        self.name = name
        self.age = age
        self.sex = sex
        self.job=job


    def do_test(self):
        print(self.name+'测试员在工作')
    #     继承后新方法名可以和父级方法名重复
    def info(self):
        print('%s %s %s %s' % (self.name, self.age, self.sex,self.job))

if __name__ == '__main__':
    human = Human('军', '10', '男')
    human.sleep()
    human.eate()
    human.info()
    tester = Tester('所有人', '20', '男','测试')
    tester.sleep()
    tester.info()
    print(tester.sex)


