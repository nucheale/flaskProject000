from flask import Flask, render_template, request, redirect, jsonify
from my_database import Database
from config_data import config
from datetime import datetime

app = Flask(__name__)

db = Database(config.DATABASE_FILE)
db.create_tables()


@app.route('/')
def index():
    return render_template('index.html', h1='Заголовок')


now = datetime.now()
formatted_datetime = now.strftime('%d.%m.%Y %H:%M')


@app.route('/register', methods=['GET', 'POST'])
def register():
    incorrect_username = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if db.user_exists(username):
            incorrect_username = 'Пользователь с таким логином уже существует'
            # return "user_exists"
        else:
            db.add_new_user(username, email, password, now)
            return redirect('/success_register')

    return render_template('register.html', current_datetime=formatted_datetime, incorrect_username=incorrect_username)


# @app.route('/check_username')
# def check_username():
#     username = request.form['username']
#     if db.user_exists(username):
#         return jsonify({'message': 'Пользователь с таким логином уже существует'})
#     else:
#         return jsonify({'message': ''})


@app.route('/success_register')
def success():
    return 'USER REGISTERED'


@app.route('/login', methods=['GET', 'POST'])
def login():
    incorrect_data = None
    if request.method == 'POST':
        username_email = request.form['username_email']
        password = request.form['password']
        if db.user_login(username_email, password):
            return redirect('/success_login')
        else:
            incorrect_data = 'Введена неверная пара логин/пароль'

    return render_template('login.html', current_datetime=formatted_datetime, incorrect_data=incorrect_data)


@app.route('/success_login')
def success_login():
    return 'success_login'


if __name__ == '__main__':
    app.run(debug=True)
