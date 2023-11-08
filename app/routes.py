from flask import Blueprint
from flask.templating import render_template
from app import BERTHS

main = Blueprint('main', __name__)

@main.route("/")
def index():
  return render_template("index.html", ids = BERTHS)

@main.route("/berth/<id>", methods=['GET'])
def berth(id):
  return render_template("berth.html", id = id)

@main.route("/berths", methods=['GET'])
def berths():
  berths_values = []
  for berth in BERTHS:
    berths_values.append(str(berth))

  berths_json = {
    "berths": berths_values
  }
  return berths_json
