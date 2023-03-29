from flask import Flask, jsonify, request
from flask_cors import cross_origin
from jwaab import answerMe

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>namaste mai head master hoon</p>"


@app.route("/headmasterji", methods=['POST'])
@cross_origin()
def jwaab():
    print(request.get_json(), 'data')

    response = jsonify(message="jwaab ")
    print(answerMe(request.get_json().swaal))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
