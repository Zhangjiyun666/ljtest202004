
class BaBa():
    money = "500W"
    def make_money(self):
        print("爸爸有钱，拿去花！")

class ErZi(BaBa):
    # pass                # 占位符号：为了让代码不报错
    money = "500E"
    def make_money(self):
        print("儿子终于实现了小目标！")

# 子类可以继承父类的属性和方法
ez = ErZi()
print(ez.money)
ez.make_money()

# 重写：子类把父类的属性和方法重新实现
