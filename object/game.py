"""
一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200.
定义一个fight方法：
my_hp=my_hp-enemy_power
enemy_final_hp=enemy_hp-my_power
两个hp进行对比，血量剩余多的人获胜
"""
"""
##简单的函数表达
import random##导入random随机方法
def fight(enemy_hp,enemy_power):
    my_hp = 1000
    my_power = 200
#    enemy_hp = 1000
#    enemy_power = 200
    while True:##循环对打多轮
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        print(my_hp)
        print(enemy_hp)
        ##三目表达式
        ##print("我赢了")if my_final_hp >enemy_final_hp else print("敌人赢了")
        if my_hp > enemy_hp:
            print("我赢了")
            break##退出循环

        else:
            print("敌人赢了")
            break

#fight()
if __name__ == '__main__':
## 生成一些血量，每次随机的去选择血量
    hp = [x for x in  range(990,1100)]##[]是列表，for循环：for in range
    enemy_hp = random.choice(hp)##敌人的血量赋予随机数
    print(enemy_hp)
    enemy_power = random.randint(190,210)##敌人的攻击力赋予随机数
    print(enemy_power)
    fight(enemy_hp,enemy_power)
"""
"""
##将上面的简单函数模式改为面向对象模式
class game:
    #属性：血量，攻击力
    def __init__(self):
        self.my_hp = 1000
        self.my_power = 200
        self.enemy_hp = 1000
        self.enemy_power = 100
    #方法：fight打架
    def fight(self):
        while True:  ##循环对打多轮
            self.my_hp = self.my_hp- self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            print(self.enemy_hp)
            ##三目表达式
            ##print("我赢了")if my_final_hp >enemy_final_hp else print("敌人赢了")
            if self.my_hp > self.enemy_hp:
                print("我赢了")
                break  ##退出循环

            else:
                print("敌人赢了")
                break
#调用类的方法，需要实例化一下去调用，例如实例化一下a
a = game()
a.fight()
"""
"""
按上面的类进行一个继承,角色：后裔
后裔继承了game的hp和power。并多了一个护甲属性
重新定义另外一个defense属性：
final_hp = hp + defense - enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量先为零的人输掉比赛
定义一个新的方法back_home，游戏结束之后回城
"""
class game:
    #属性：血量，攻击力
    def __init__(self):
        self.my_hp = 1000
        self.my_power = 200
        self.enemy_hp = 1000
        self.enemy_power = 100
    #方法：fight打架
    def fight(self):
        while True:  ##循环对打多轮
            self.my_hp = self.my_hp- self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            print(self.enemy_hp)
            ##三目表达式
            ##print("我赢了")if my_final_hp >enemy_final_hp else print("敌人赢了")
            if self.my_hp > self.enemy_hp:
                print("我赢了")
                break  ##退出循环
            else:
                print("敌人赢了")
                break
class houyi(game):
    def __init__(self):
        self.defense = 100
        super().__init__()##调用父类的属性
    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            print(self.enemy_hp)
            if self.my_hp > self.enemy_hp:
                print("我赢了")
                break
            else:
                print("敌人赢了")
                break
        #定义一个新的方法，游戏结束之后回城
    def back_home(self):
        print("准备回城")

#调用类的方法，需要实例化一下去调用，例如实例化一下b
b = houyi()
b.fight()
b.back_home()