rebro = int(input("Введите длинну ребра куба: "))
square = rebro * rebro
perimetr = rebro * 4
obiem = square * rebro
print("Площадь грани куба равна:",square)
print("Периметр грани куба равен:",perimetr)
print("Объём куба равен:",obiem)

God = int(input())
if God % 4 == 0 and (God % 100 != 0) or (God % 400 == 0):
      print('Год',God," - високосный")
else:
 print('Год',God," - невисокосный")