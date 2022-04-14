import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask('ValeraProj')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/Ivent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class EventParticipants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f"<users {self.id}>"


@app.route('/')
def index():
    return '<b>Index Page</b>'


@app.route('/user', methods=["POST"])
def add():
    data = request.get_json()
    db.session.add(EventParticipants(id=data['id'], name=data['name'], email=data['email']))
    db.session.commit()
    return data


@app.route('/user', methods=["GET"])
def get_all_users():
    participants = EventParticipants.query.all()
    new_list = []
    for item in participants:
        new_list.append({"id": item.id, "name": item.name, "email": item.email})
    return json.dumps(new_list)


if __name__ == "__main__":
    app.run(debug=True)
