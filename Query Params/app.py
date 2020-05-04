from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
data = {
  'John': {'salary': '10K', 'technology': 'web development'},
  'Doe': {'salary': '20M', 'technology': 'artificial intelligence'}
}

class Help(Resource):
    def get(self):
        return make_response(jsonify({"All Endpoints": ['/esinfo']}), 200)

class Employees(Resource):
    def get(self):
        ename = request.args.get('ename')
        if ename:
            return data[ename]
        return make_response(jsonify(data), 200)

api.add_resource(Help, "/")
api.add_resource(Employees, "/esinfo")

if __name__ == '__main__':
    app.run(debug=True)
