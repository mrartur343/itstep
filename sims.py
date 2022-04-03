class Human:
    def __init__(self, name="Human"):
        self.name=name
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers=[]

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passagers")
            for passagers in self.passangers:
                print(passagers.name)
        else:
            print(f"There are no passagers in {self.brand}")
nick = Human('Nick')
kate = Human('Kate')
car = Car('Mersedess')

car.add_passanger(Nick)
car.add_passanger(Kate)
car.print_passangers_name