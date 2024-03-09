from flask import render_template, url_for, request, redirect, session, Flask
# from flask import Blueprint
# from flask_paginate import Pagination, get_page_parameter
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

def get_all_courses():
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT * FROM jobsdata"
    cursor.execute(query)

    courses = cursor.fetchall()

    close_database_connection(connection, cursor)

    return courses


@app.route('/courses')
def courses():
    page = request.args.get('page',1 , type=int)
    per_page = 10  # Number of courses per page

    start = (page - 1) * per_page
    end = start + per_page

    courses = get_all_courses()
    courses = list(courses)

    total_pages = (len(courses) + per_page-1) // per_page

    items_on_page = courses[start:end]

    return render_template('cources.html',items=items_on_page,total_pages=total_pages,page=page)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'jobsdb',
}


def connect_to_database():
    return MySQLdb.connect(**db_config)


def close_database_connection(connection, cursor):
    cursor.close()
    connection.close()


if __name__ == "__main__":
    app.run(debug=True)





