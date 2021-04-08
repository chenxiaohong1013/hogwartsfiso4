"""
写一个Bicycle(自行车)类，
1.有run（骑行）方法，调用时显示骑行里程km（骑行里程为传入的数字）
再写一个电动自行车类EBicycle继承Bicycle，
1.添加电池电量battery_level属性通过参数传入
2.同时有两个方法：
   a。fill_charge（vol）用来充电，vol为电量
   b。run（km）方法用于骑行，每骑行10km消耗电量1度，
       当电量耗尽时调用Bicycle的run方法骑行，
通过传入的骑行里程数，显示骑行结果（就是当电量耗尽，需要你真正骑行的里程数）

"""

import yaml##调用yaml工具实现数据控制的，如果不需要这段可以去掉
class Bicycle():
    def run(self,km):
        print(f"骑行了{km}千米")
class EBicycle(Bicycle):
        battery_level:int
        def __init__(self, battery):
            self.battery_level = battery
        def fill_charge(self,vol):
            self.battery_level += vol
        def run(self,km):
            a = km - self.battery_level*10
            if a>0:
                print("电不够用")
                print(f"使用电骑行：{self.battery_level * 10}")
                print(f"还需要脚蹬{a}千米")
                Bicycle().run(a)

            else:
                print("电够用")
                print(f"骑行了{km}千米")
with open('../xinjiancyyaml/data.yaml',encoding='utf-8') as f:##调用yaml工具，文件是data.yaml
    test = yaml.safe_load(f)
rr = test['defualt']
print(rr['env'])
runing = EBicycle(rr['battery'])
runing.run(rr['km'])
