#Slava Ukraini, geroiam slava


class Display:
    def display(self):
        self.var = 20
class Computer:
    def calculate(self):
        self.var = 10



class SmartPhone(Display, Computer):
    def test(self):
        print(self.var)

iphone = SmartPhone()
iphone.calculate()
iphone.display()
iphone.test()