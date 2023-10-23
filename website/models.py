from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Predict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stress = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sr = db.Column(db.Integer)
    rr = db.Column(db.Integer)
    t = db.Column(db.Integer)
    lm = db.Column(db.Integer)
    bo = db.Column(db.Integer)
    rem = db.Column(db.Integer)
    srh = db.Column(db.Integer)
    hr = db.Column(db.Integer)

    def __repr__(self):
        return f'Predict(id={self.id}, stress={self.stress}, date={self.date}, user_id={self.user_id}, sr={self.sr}, rr={self.rr}, t={self.t}, lm={self.lm}, bo={self.bo}, rem={self.rem}, srh={self.srh}, hr={self.hr})'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    state = db.Column(db.String(150))
    city = db.Column(db.String(150))
    zipcode = db.Column(db.String(150))
    work = db.Column(db.String(150))
    marital = db.Column(db.String(150))
    predicts = db.relationship('Predict')

    def __repr__(self):
        return f'User(id={self.id}, email={self.email}, user={self.id})'

    

