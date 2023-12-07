# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):

        data = "hello world"
        return jsonify({'data': data})
