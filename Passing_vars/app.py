from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
data = {
  'John': {'salary': '10K', 'technology': 'web development'},
  'Doe': {'salary': '20M', 'technology': 'artificial intelligence'}
}

class Employees(Resource):
    def get(self, ename=None):
        if ename:
            if ename in data.keys():
                return make_response(jsonify(data.get(ename)), 200)
            message = {"message": "Sorry, employee not found."}
            return make_response(jsonify(message), 404)
        return make_response(jsonify(data), 200)

api.add_resource(Employees, '/esinfo', '/esinfo/<string:ename>')

if __name__ == '__main__':
    app.run(debug=True)
