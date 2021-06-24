import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data = [
  {
    'id': 0,
    'First Name': 'Eric',
    'Last Name': 'Colvin'
  },
  {
    'id':1,
    'First Name': 'John',
    'Last Name': 'Doe'
  },
]

@app.route('/', methods=['GET'])
def home():
  return jsonify(data)

app.run()
