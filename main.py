#!/usr/bin/python
# coding=utf-8

import sys
from flask import Flask, request, Response
from flask_restful import Resource, Api
from json import dumps
# from flask.ext.jsonpify import flask_jsonpify
from flask.ext.jsonpify import jsonify
from html import HTML

from pprint import pprint

from auth import *
from mail import send_mail
from database import *
from routes import routes_blueprint


reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.register_blueprint(routes_blueprint)


@app.route("/")
@requires_auth
def index():
    return jsonify(foo="bar")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
