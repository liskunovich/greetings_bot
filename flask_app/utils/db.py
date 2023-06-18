from manage import app, db
from ..models import User


def insert_user_data(name: str, city: str, tg_username: str) -> None:
    with app.app_context():
        db.session.add(User(name=name, city=city, tg_username=tg_username[1::]))
        db.session.commit()


def get_user_data(username: str) -> dict:
    with app.app_context():
        user = User.query.filter_by(tg_username=username).first()
        if user:
            return {
                'name': user.name,
                'city': user.city,
            }
        return {}
