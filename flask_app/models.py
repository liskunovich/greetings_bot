from manage import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    tg_username = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

