from flask import Flask, render_template
from my_database import Database
from config_data import config

app = Flask(__name__)

db = Database(config.DATABASE_FILE)
db.create_tables()


@app.route('/')
def index():
    return render_template('index.html', h1='Заголовок')


@app.route('/register')
def register():
    return render_template('register.html', current_date='DATE', current_time='TIME')


if __name__ == '__main__':
    app.run(debug=True)
