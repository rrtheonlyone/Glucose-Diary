from app import db

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reading = db.Column(db.Float, index=True, unique=True)
    food = db.Column(db.String(120), index=True, unique=True)
    time = db.Column(db.DateTime, index=True, unique=True)
    insulin = db.Column(db.Float, index=True, unique=True)

    def __repr__(self):
        return '<Reading %r>' % (self.reading)