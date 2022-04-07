import random
class Human:
    def __init(self, name="Human", job=None, home=None,car=None):
        self.name=name
        self.money=100
        self.gladness=50
        self.satiety=50
        self.job=job
        self.home=home
        self.car=car
    def get_home(self):
        self.home=House()
    def get_job(self):
        if self.can.drive:
            pass
        else:
            self.to_repair()
            return

        self.job=Job()
    def get_car(self):
        self.car=Auto(brands_of_car)

    def eat(self):
        if self.home.food<=0:
            self.shopping()
        else:
            pass

    def work(self):
        pass
    def shopping(self,manege):
        pass
    def chill(self):
        pass
    def to_repair(self):
        pass
    def clean_home(self):
        pass
    def days_index(self):
        pass
    def is_alive(self):
        pass
    def alive(self):
        pass
class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list(brand_list))
        self.fuel=brand_list[self.brand]['fuel']
        self.strength=brand_list[self.brand]['strength']
        self.consuption=brand_list[self.brand]['consuption']
    brands_of_car={'BMW':{'fuel': 100, 'strength': 100, 'consuption': 6 },
                    'Lada': {'fuel': 50, 'strength': 40, 'consuption': 10},
                    'Volvo': {'fuel': 70, 'strength': 150, 'consuption': 8},
                    'Ferrari': {'fuel': 80, 'strength': 120, 'consuption': 14},

                    }
    def drive(self):
        if self.strength>0 and self.fuel>=self.consuption:
            self.fuel-=self.consuption
            return True
        else:
            print("The car can not move")
            return False

class House:
    def __init__(self):
        self.mess=0
        self.food=0

class Job:
    def __init__(self, job_list):
        self.job=random.choise(list(job_list))
        self.salary=job_list[self.job]['salary']
        self.gladness_less=job_list[self.job]['gladness_less']
    job_list = {
        "Java developer":{"salary":50, "gladness_less":10},
        'Python developer':{"salary":40, "gladness_less":3},
        'C++ developer':{"salary":45, "gladness_less":25},
        'Rust developer':{"salary":70, "gladness_less":1}
    }