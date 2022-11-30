from flask import Blueprint
import jsonpickle as jp

from oop.car import Car

app = Blueprint('json_page', __name__)


# Flask maps HTTP requests to Python functions.
@app.route('/cars/model/<model>', methods=['GET'])
def api_car_model(model):
    return jp.encode(Car().readModel(model))


@app.route('/cars/plate/<plate>', methods=['GET'])
def api_car_plate(plate):
    return jp.encode(Car().readPlate(plate))