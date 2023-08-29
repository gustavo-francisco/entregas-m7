from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from database.models import User, db, Grades

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres123@localhost:5432/db_entrega2" 
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
            return redirect(url_for('notas'))
          # Redirect to a logged-in page
        else:
            return 'Login failed'
            
    return render_template('login.html')

@app.route('/notas', methods=['GET', 'POST'], endpoint='notas')
def grades():
    if 'user_id' in session:
        user_id = session['user_id']

        if request.method == 'POST':
            if 'action' in request.form:
                action = request.form['action']
                if action == 'add_note':
                    nova_nota = request.form['nova_nota']
                    nova_nota_float = float(nova_nota)

                    nova_grade = Grades(grade=nova_nota_float, user_id=user_id)
                    db.session.add(nova_grade)
                    db.session.commit()
                    
                elif action == 'remove_note':
                    nota_removida = float(request.form['nota_removida'])
                    nota_removida_str = str(nota_removida)  # Converter para string

                    grade_a_remover = Grades.query.filter_by(grade=nota_removida_str, user_id=user_id).first()

                    if grade_a_remover:
                        db.session.delete(grade_a_remover)
                        db.session.commit()
                        
        user = User.query.get(user_id)
        grades = Grades.query.filter_by(user_id=user_id).all()

        return render_template('notas.html', user=user, grades=grades)

    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)