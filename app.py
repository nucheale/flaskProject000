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
    return render_template('register.html', current_date='4 апреля 2024', current_time='15:15')


if __name__ == '__main__':
    app.run(debug=True)
