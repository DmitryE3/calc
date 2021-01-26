from app import db


class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_beer = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(3000))
    recipe_grain = db.Column(db.String(3000))
    recipe_extract = db.Column(db.String(3000))
    charact = db.Column(db.String(200))
    cooking = db.Column(db.String(3000))
    amount_of_ingredients = db.Column(db.String(200))
    times = db.Column(db.String(1000))
    author = db.Column(db.String(64))
    private = db.Column(db.Boolean, default=False, nullable=False)
