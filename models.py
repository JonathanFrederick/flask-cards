from app import db
from passlib.apps import custom_app_context as pw_context


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    pw_hash = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.hash_pw(password)

    def hash_pw(self, password):
        self.pw_hash = pw_context.encrypt(password)

    def verify_pw(self, password):
        return pw_context.verify(password, self.pw_hash)

    def __repr__(self):
        return 'User: {}'.format(self.username)
