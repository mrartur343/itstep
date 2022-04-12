import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.study = 0
        self.cash = 100
        self.alive = True

    def to_study(self):
        print("Time to study!")
        self.gladness -= 3
        self.study += 0.12

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3
    def to_work(self):
        print("Time to work")
        self.cash += 5
        self.gladness -= 3
        self.study -= 0.05

    def to_buy(self):
        print("Buy book!")
        self.cash -= 3
        self.study=3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.study -= 0.1
        self.cash -=0.2

    def is_alive(self):
        if self.study < -0.5:
            print("Вас вигнали з університету")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.study >= 100:
            print("Ви закінчили університет")
            self.alive = False
        elif self.cash <= -20:
            print("Ви у боргах")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness={self.gladness}")
        print(f"Study={round(self.study,2)}")
        print(f"Cash={round(self.cash,2)} гривень")

    def live(self, day):
        day = "Day " + str(day) + ' (year ' + str(
            year) + ") of " + self.name + "file"
        print(f"{day:=^55}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_buy()
        elif live_cube == 5:
            self.to_work()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Student ")
for year in range(150):
    for day in range(365):
        if nick.alive == False:
            break
        nick.live(day)
if nick.alive == True:
    print('Студент навчяется 150 років 0_o')
