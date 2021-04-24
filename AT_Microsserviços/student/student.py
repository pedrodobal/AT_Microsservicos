from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://admin:admin@db/student'
CORS(app)

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    discipline = db.Column(db.String(100))
    question = db.Column(db.String(500))
    
class TaskUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    task_id = db.Column(db.Integer)
    
    UniqueConstraint('user_id', 'task_id', name='user_task_unique')

@app.route('/')
def index():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')