from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PECI/Projeto/database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=True)
    ptId = db.Column(db.Integer, primary_key=True)

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    if user.ptId == 1: # testar isto
        # ...
        return render_template('page_that_shows.html')
    else:
        # ...
        return render_template('page_that_doesnt.html')