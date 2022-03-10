from functools import reduce

list_1 = [[1,4,6,5,3],[4,3,6,9],[9,7,4,6,2]]

new_list = reduce(lambda a, b: a + b, list_1)
"""Это лябмда функция, по слиянию списков через reduce"""
print(new_list)

def decorator_with_args(func):
    """Это декоратор"""
    print('*** Декоратор ***')
    def decorat(*args, **kwargs):
        print('Оборачиваем фукнцию: {}'.format(func))
        returned = func(*args, **kwargs)
        print('Выходим из обёртки')
        return returned
    return decorat

@decorator_with_args
def cal_sum(lstt):
    """Это функция по слиянию через append"""
    new_list_2 = []
    for lst in lstt:
        for i in lst:
            new_list_2.append(i)
    return new_list_2

uni_list = cal_sum(list_1)
print(uni_list)

@decorator_with_args
def cal_sum_2(lstt):
    """Это функция по слиянию через сумму"""
    new_list_2 = []
    for lst in lstt:
        new_list_2 = new_list_2+lst
    return new_list_2

uni_list_2 = cal_sum_2(list_1)
print(uni_list_2)

@decorator_with_args
def cal_sum_reduce(lstt):
    """А это уже с лямбдой и редюсом"""
    return reduce(lambda a, b: a + b, lstt)

uni_list_3 = cal_sum_reduce(list_1)
print(uni_list_3)
