from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask('ValeraProj')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Ivents.db'
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

@app.route('/add', methods=("POST", "GET"))
def add():
    data = request.get_json()
    db.session.add(User(id=data['id'], name=data['name'], email=data['email']))
    db.session.commit()
    return data

if __name__ == "__main__":
    app.run(debug=True)
