# class geometric_progressy:
#     @staticmethod
#     def geoprog(i, d):
#         while True:
#             yield i
#             i *= d
#
# iter = geometric_progressy
# iter = iter.geoprog(1, 2)
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))

import re

class regularka:
    @staticmethod
    def matching(text):
        match = re.fullmatch(r'\w+.\w+@\w+.\w+', text)
        print('YES' if match else 'NO')
    @staticmethod
    def finding(text):
        search = re.findall(r'\w+.\w+@\w+.\w+', text)
        print(search)

Email = regularka
First = Email.matching("Example-2155@gmail.com")
Second = Email.matching("This is just text")

Searching = Email.finding("Добрый день! На электронную почту TradeOOO-Organization@yahoo.com пришло сообщение от CyberVasyan2077@CD.red")
