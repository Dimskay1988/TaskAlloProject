import json

users = [{'name': 'Van','age': 300},{'name': 'Rickardo','age': 25}]

with open('data.json', 'w') as file:
    names_json = json.dumps(users)
    file.write(names_json)

import csv

with open('data.csv', 'w') as file:
     writer = csv.writer(file)
     writer.writerow(users[0].values())
     writer.writerow(users[1].values())

import openpyxl

file_ext = ".xlsx"
file_name = str("Myexceldocument")
file_name = file_name + file_ext
wb = openpyxl.Workbook()
sheet = wb.create_sheet(title = 'Первый лист', index = 0)
sheet = wb['Первый лист']
sheet.column_dimensions['A'].width = 15
sheet.append(['Nickname', 'Age'])
sheet.append(['Nagibator228', '13'])
sheet.append(['Patriot', '31'])
sheet.append(['OrdinaryMen', '25'])
sheet["A5"].value = 'Всё'
wb.save(file_name)

f = open("Valera.txt", "w", encoding = 'utf-8')
f.close()

with open('Valera.txt', 'r+') as file:
    print(file.read())
    file.write('Hi!!!! This is my text!\n')





