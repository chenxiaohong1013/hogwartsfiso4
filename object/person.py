"""
面向对象：
创建一个person类
属性：姓名，性别，年龄，存款金额
方法：吃，睡，跑，赚钱
父类person
子类funny继承父类person
"""

class person:
    ##静态属性
    name = None
    gender = "男"
    age = 10
    ##私有属性
    __money = 1000
    def __init__(self,name,gender,age):
        self.name = name
        self.gender =gender
        self.age = age
##动态方法
    def eat(self):
        print(f"{self.name}会吃")
    def sleep(self):
        print("睡")
    def running(self):
        print("跑")
    ##调用私有属性
    def have_money(self):
        return  self.__money
    ##私有的方法
    def __get_money(self):
        return self.__money+2000
##子类继承父类person
class funny(person):
    # 继承person类的属性和方法
    #子类增加属性
    skill: str
    def __init__(self,name,gender,age,skill):
        super().__init__(name,gender,age)
        self.skill = skill
    #子类增加方法
    def fun(self):
        print(f"{self.name}很搞笑")

fun1 = funny("沈腾","男","33","gaox")
print(fun1.gender)
fun1.fun()
print(fun1.skill)



""" 
a=person(name="qq",gender="nv",age="20")
print(a.gender)
a.eat()

a2=person(name="3s",gender="nan",age="23")
print(a2.running)
print(a2.name)
print(a2.gender)
print(a2.have_money())
print(a2._Person__money)
"""