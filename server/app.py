# Пишем одностраничное приложение с Flask и Vue.js:
# https://tproger.ru/translations/developing-app-with-flask-and-vue-js/

# Introduction по Vue: https://ru.vuejs.org/v2/guide/index.html

# Git commands overview: https://github.com/cyberspacedk/Git-commands

# Про npm: https://docs.npmjs.com/about-npm/index.html

# Docker за час: https://www.youtube.com/watch?v=QF4ZF857m44

# PostgreSQL - Скачать для Windows: https://www.postgresql.org/download/windows/
# PostgreSQL - бстро разбираемся: https://www.youtube.com/watch?v=WpojDncIWOw

import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': [True]
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': [False]
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': [True]
    }
]



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS - для безопасности
CORS(app, resources={r'/*': {'origins': '*'}})

# Первоначальная проверка сервера
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# Список книг и их добавление
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

# Обработка маршрута PUT из RESTful (удаление книги, например)
@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

# Удаление книги
def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

if __name__ == '__main__':
    app.run()