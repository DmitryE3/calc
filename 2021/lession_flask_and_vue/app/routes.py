from app import app, db
from flask import jsonify, request
from app.models import Books

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return "Ping!"

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    """
    function to display and add new books
    :return:
    """
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        book = Books(author=post_data.get('author'), book_name=post_data.get('title'), read=post_data.get('read'))
        db.session.add(book)
        db.session.commit()
        response_object['message'] = 'Book added!'
    else:

        response_object['books'] = BOOKS
    return jsonify(response_object)
