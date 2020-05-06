
# 新建一个类：
class Person():
    # 构造方法：实例化类的时候来新建成员变量
    def __init__(self, mz, sg, tz, xb):
        self.mingzi = mz
        self.shenggao = sg
        self.tizhong = tz
        self.xingbie = xb

    # 成员方法：类里面的方法
    # self:固定
    def pao(self):
        print("人可以跑")
        print(self.xingbie)

# 调用类：实例化
p = Person("张三", 180, 100, "女")        # Person()实例化Person类，返回类对象并且赋值给p变量
print(p.mingzi)     # 调用属性
p.pao()             # 调用方法
# print(p.pao())