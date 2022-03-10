from typing import List

first_list = ["nik9", "mike123", "john45", "n1k0la1"]
modify_list = [i + "1" for i in first_list]
print(modify_list)

def modify_list_2 (new_list: list) -> list:
    final_list = [i + "2" for i in new_list]
    return final_list

first_list = modify_list_2(first_list)
print(first_list)

# from datetime import datetime

# a = []

# def actual_time(neew_time: list) -> str:
#      my_time = datetime.today().strftime('%d.%m.%Y %H:%M')
#      date = datetime.today().strftime('%d.%m.%Y')
#      neew_time = [my_time for i in range(0,3)]
#      return neew_time [1]

# actual_time(a)

actual_time(my_time)
