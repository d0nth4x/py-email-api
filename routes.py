# coding=utf-8

from flask import Blueprint
from flask.ext.jsonpify import jsonify
from html import HTML

from auth import *
from mail import send_mail
from database import *

from pprint import pprint

routes_blueprint = Blueprint('routes_blueprint', __name__,)


# @routes_blueprint.route('/',methods = ['POST'])
# @requires_auth
# def index():
#

@routes_blueprint.route('/example', methods=['GET'])
@requires_auth
def example():
    body = "example body"
    title = "example title"

    send_mail(['admin@localhost'], title, body, False)

    return jsonify(status=0, msg='ok!')
