from flask import render_template, url_for, request, redirect, session, Flask
import MySQLdb.cursors
import re
import MySQLdb

app = Flask(__name__)

app.secret_key='youssefrikel12'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'webscraping',
}


def connect_to_database():
    return MySQLdb.connect(**db_config)


def close_database_connection(connection, cursor):
    cursor.close()
    connection.close()


if __name__ == "__main__":
    app.run(debug=True)





