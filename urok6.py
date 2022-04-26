#Slava Ukraini, geroiam slava


class A:
    def display(self):
        self.var = 20
class B:
    def calculate(self):
        self.var = 10



class AB(A, B):
    def test(self):
        print(self.var)

result = AB()

result.calculate()
result.display()
result.test()