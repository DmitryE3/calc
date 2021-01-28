from app import app, db
from flask import jsonify, request
from app.models import Books

BOOKS = []
#     {
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ]


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
        BOOKS = []
        books = Books.query.all()
        for book in books:
            BOOKS.append({
                'id': book.id,
                'title': book.book_name,
                'author': book.author,
                'read': book.read
            })
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        book = Books(id=book_id, author=post_data.get('author'), book_name=post_data.get('title'), read=post_data.get('read'))
        db.session.add(book)
        db.session.commit()
        response_object['message'] = 'Book updated!'
    elif request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


def remove_book(book_id):
    book = Books.query.filter_by(id=book_id).all()
    print(book)
    if book:
        for i in book:
            db.session.delete(i)
            db.session.commit()
        return True
    return False