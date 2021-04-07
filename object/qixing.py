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

runing = EBicycle(20)
runing.run(110)
