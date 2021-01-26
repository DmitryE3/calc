from app import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200))
    book_name = db.Column(db.String(200))
    read = db.Column(db.Boolean())