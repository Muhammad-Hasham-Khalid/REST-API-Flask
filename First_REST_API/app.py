from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app) # for api we have to pass our current app

employee_info = {
    "emp1": {
        'name': "John",
        "salary": "10K"
    },
    "emp2": {
        'name': 'Jack',
        'salary': '14K'
    }
}

class Employee(Resource):
    def get(self):
        return employee_info

api.add_resource(Employee, '/info')

if __name__ == '__main__':
    app.run(debug=True)