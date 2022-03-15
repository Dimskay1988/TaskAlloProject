class Inform:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def hum_info(cls, name, age):
        return cls(name, 12)

    @staticmethod
    def hum_info1(age):
        return age + 1


Man = Inform.hum_info("Valera", 25)
print(Man.name, Man.age)
print(Man.hum_info1(22))
