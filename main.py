# 10-m
class Oyinchi:
    def __init__(self, ism):
        self.ism = ism

    def info(self):
        print(f"Ism: {self.ism}")

class ProOyinchi(Oyinchi):
    def __init__(self,ism, reyting):
        super().__init__(ism)
        self.reyting = reyting

    def info(self):
        super().info()
        print(f"Reyting: {self.reyting}")


p = ProOyinchi("Ali", 2500)
p.info()
