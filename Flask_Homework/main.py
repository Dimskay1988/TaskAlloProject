import json

from flask import Flask, request

app = Flask(__name__)

############################### Включается после того, как файл есть и сохранен
# with open('data.json', 'r', encoding='utf-8') as fh:
#     users = json.load(fh)
###############################

############################### Включается изначально, когда НЕТУ json файла
users = [
    {
        "id": 1,
        "name": "Valera",
    }, {
        "id":2,
        "name": "Vlad",
    },
]
##############################

with open('data.json', 'w') as file:
    names_json = json.dumps(users)
    file.write(names_json)


@app.route('/')
def index():
    return '<b>Index Page</b>'


@app.route('/privet')
def privet():
    return '<b>The England ionship final.</b>'


@app.route('/user/')
def get_all_users():
    return json.dumps(users)


@app.route('/user/', methods=['POST'])
def create_user():
    data = request.get_json()
    users.append(data)
    print(data)
    with open('data.json', 'w') as file:
        names_json = json.dumps(users)
        file.write(names_json)
    return data


if __name__ == "__main__": app.run()
