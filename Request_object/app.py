from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
data = {
  'John': {'salary': '10K', 'technology': 'web development'},
  'Doe': {'salary': '20M', 'technology': 'artificial intelligence'}
}

class Info(Resource):
    def __init__(self):
        #print(dir(request))
        print(request.authorization) # for credentials
        print(request.args) # arguments passed

    def get(self):
        pass

    def post(self):
        pass

api.add_resource(Info, "/info")

if __name__ == '__main__':
    app.run(debug=True)
