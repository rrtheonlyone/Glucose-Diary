from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')
db = SQLAlchemy(app)

class GetReadings(Resource):
    def get(self):
        return {'Reading': '6.4'}

api.add_resource(GetReadings, '/')

if __name__ == '__main__':
    app.run(debug=True)