from dataclasses import dataclass
from threading import Timer

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Section(db.Model):
    id: int
    course_id: int
    block_id: int
    start_date: str
    end_date: str
    capacity: str

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(200))
    block_id = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    capacity = db.Column(db.Integer)


@app.route('/')
def index():
    return "hello"


@app.route("/api/section", methods=['GET'])
def get_all_section():
    return jsonify(Section.query.all())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
