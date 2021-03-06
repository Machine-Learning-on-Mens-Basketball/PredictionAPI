import os
from flask import Flask
from flask_restful import Api, Resource
from app.main.controllers.predict_controller import PredictController

app = Flask(__name__)
api = Api(app)

api.add_resource(PredictController, '/predict')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)