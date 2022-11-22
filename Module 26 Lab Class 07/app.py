"My cute API"
"CURD operation using flask"

from flask import Flask, request

database = {'Ariful' : '100','Sumon' : '200','Kalam' : '300'}

#initialize flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to my cute API'

@app.route('/getdata/', methods=['GET'])
def get_data():
    return database

@app.route('/adddata/', methods=['PUT'])
def add_data():
    key, value = list(request.args.items())[0]
    database[key] = value
    return f"{key} added"

@app.route('/deletedata/', methods=['DELETE'])
def delete_data():
    key, value = list(request.args.items())[0]
    database.pop(value)
    return f"{key} Deleted"

if __name__ == '__main__':
    app.run()