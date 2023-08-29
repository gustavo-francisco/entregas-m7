from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres123@localhost:5432/db_entrega2"
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

class Grades(db.Model):
    __tablename__ = "grades"

    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()