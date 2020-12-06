# 2020/11/29
# author:xieyudong
class Father:
    def __init__(self,money,hourseName,car):
        self.money = money
        self.hourse = hourseName
        self.car = car
    def eat(self,vegetables,noddles):
        print(f"father{vegetables}and{noddles}")
class Son(Father):
    def eat(self,meat,Fruits):
        print(f"son_jichenle_father{self.money},{self.hourse},{self.car},like_eat{meat}and{Fruits}")
s1 = Son(1000,"别墅","infinity")
print(s1.eat("meat","pear"))
