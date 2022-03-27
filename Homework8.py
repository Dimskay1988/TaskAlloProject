# class Transport:
#     def drive(self):
#         print("Это транспорт, он едет")
#
# class Bike(Transport):
#     def wheel(self):
#         print("Тут всего 2 колеса")
#
# b = Bike()
# b.drive()
# b.wheel()
#
# class Stone(Transport):
#     def drive(self):
#         print("Это камень, он неподвижен")
#
# s = Stone()
# s.drive()


<<<<<<< HEAD
<<<<<<< HEAD
class Phone():
=======
class Phone:
>>>>>>> feature/homework8
=======
class Phone:
>>>>>>> feature/homework10
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

<<<<<<< HEAD
<<<<<<< HEAD
    def sayone(self):
        print(f"This is {self.brand}")

    def saytwo(self):
        print(f"His model - {self.model}")

=======
=======
>>>>>>> feature/homework10
    def say_one(self):
        print(f"This is {self.brand}")

        def say_two(self):
            print(f"His model - {self.model}")
<<<<<<< HEAD
>>>>>>> feature/homework8
=======
>>>>>>> feature/homework10

class Smartphone(Phone):
    def __init__(self, brand, model, OS):
        super().__init__(brand, model)
        self.OS = OS

<<<<<<< HEAD
<<<<<<< HEAD
    def sayOS(self):
        print(f"OS - {self.OS}")


mobile = Phone("Nokia", 3310)
mobile.sayone()
mobik = Smartphone("Xiaomi", "Redmi", "Android")
mobik.sayOS()
=======
=======
>>>>>>> feature/homework10
    def say_OS(self):
        print(f"OS - {self.OS}")

mobile = Phone("Nokia", 3310)
mobile.say_one()
mobik = Smartphone("Xiaomi", "Redmi", "Android")
mobik.say_OS()
<<<<<<< HEAD
>>>>>>> feature/homework8
=======
>>>>>>> feature/homework10
