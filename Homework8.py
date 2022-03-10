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


class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def sayone(self):
        print(f"This is {self.brand}")

    def saytwo(self):
        print(f"His model - {self.model}")


class Smartphone(Phone):
    def __init__(self, brand, model, OS):
        super().__init__(brand, model)
        self.OS = OS

    def sayOS(self):
        print(f"OS - {self.OS}")


mobile = Phone("Nokia", 3310)
mobile.sayone()
mobik = Smartphone("Xiaomi", "Redmi", "Android")
mobik.sayOS()