import math as m
class Yuan:
    def __init__(self,Banjing):
        self.Banjing = Banjing

    def zhouchang(self):
        return round(self.Banjing*2*m.pi,2)
    def mainji(self):
        return round(self.Banjing**2*m.pi,2)
    def qiubiaomianji(self):
        return round(self.Banjing**2*4*m.pi,2)
    def tiji(self):
        return round(self.Banjing**3*4/3*m.pi,2)

r1=Yuan(3)
print(r1.zhouchang())
print(r1.mainji())
print(r1.qiubiaomianji())
print(r1.tiji())