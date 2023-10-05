from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
import os
import sys
import pandas as pd
from pycaret.regression import load_model, predict_model

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from database.models import User, db

# Load trained Pipeline
model = load_model("minha_api")

class Input:
    def __init__(self, Age, Gender_Female, Gender_Male):
        self.Age = Age
        self.Gender_Female = Gender_Female
        self.Gender_Male = Gender_Male

class Output:
    def __init__(self, prediction):
        self.prediction = prediction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres123@db:5432/db_entrega4" 
db.init_app(app)
app.secret_key = 'your_secret_key'
app.static_folder = 'static'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['senha']
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['senha']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('prediction'))
          # Redirect to a logged-in page
        else:
            return 'Login failed'
            
    return render_template('login.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = Input(data['Age'], data['Gender_Female'], data['Gender_Male'])
    data_df = pd.DataFrame([vars(input_data)])  # Convert to DataFrame

    # Make predictions
    predictions = predict_model(model, data=data_df)
    prediction_value = predictions["prediction_label"].iloc[0]

    output = Output(prediction_value)
    return jsonify(vars(output))


app.run(host='0.0.0.0', port=80, debug=True)
