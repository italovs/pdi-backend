from flask import Blueprint
from flask.templating import render_template
from ast import literal_eval
from os import environ

BERTHS = literal_eval(environ.get('BERTHS'))

main = Blueprint('main', __name__)

@main.route("/")
def index():
  return render_template("index.html", ids = BERTHS)

@main.route("/berth/<id>", methods=['GET'])
def berth(id):
  return render_template("berth.html", id = id)
