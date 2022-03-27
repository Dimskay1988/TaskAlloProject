class MyError(Exception):
    pass

while True:
    try:
        x = float(input("Введите первое число \n"))
        y = float(input("Введите второе число \n"))
    except ValueError:
        print("Вы ввели неверное значение")
        break
    operation = input("Введите знак операции: \n")
    if operation == "+":
        result = x + y
        print(sum)
    elif operation == "-":
        result = x - y
    elif operation == "*":
        try:
            result = x * y
            if result == 15:
                raise MyError
        except MyError:
            print("Так нельзя")
            break
        result = x * y
    elif operation == "/":
        try:
            result = x / y
        except ZeroDivisionError:
            print("Деление на ноль невозможно!")
            break
    try:
        print(result)
    except NameError or MyError:
        print("Вы ввели неверный знак операции")
    break
