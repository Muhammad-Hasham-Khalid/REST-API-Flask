from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Help(Resource):
  def get(self):
    help = { "Available REST APIs are" : ['/ping', '/info'] }
    return help

class Ping(Resource):
  def get(self):
    return {"status": "Alive"}

class Employee(Resource):
  return {
    "emp1": {'name': "John", "salary": "10K"},
    "emp2": {'name': 'Jack', 'salary': '14K'}
}

api.add_resource(Help, "/")
api.add_resource(Ping, "/ping")
api.add_resource(Employee, "/info")

#/
#/ping
#/info

if __name__ == '__main__':
  app.run(debug=True)