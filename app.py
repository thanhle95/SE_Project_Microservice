from dataclasses import dataclass
from threading import Timer

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import consumer

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(200))
    block_id = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    capacity = db.Column(db.Integer)


@app.route('/')
def index():
    return "hello"


def subcribeQueue():
    consumer.subcribe()


if __name__ == '__main__':
    r = Timer(1.0, subcribeQueue)
    r.start()
    app.run(debug=True, host='0.0.0.0')
