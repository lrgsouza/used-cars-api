from flask import Flask, request, jsonify
from oop.car import Car
from bson import json_util, ObjectId
import json

# Init app
app = Flask(__name__)

def parse_json(data):
    return json.loads(json_util.dumps(data))

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Flask maps HTTP requests to Python functions.
# The process of mapping URLs to functions is called routing.
@app.route('/', methods=['GET'])
def home():
    return "<h1>Used Cars Database System</h1><p>Vehicle Data Query</p>"


@app.route('/cars/model/<model>', methods=['GET'])
def api_car_model(model):
    return parse_json(Car().readModel(model))


@app.route('/cars/plate/<plate>', methods=['GET'])
def api_car_plate(plate):
    return parse_json(Car().readPlate(plate))


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found</p>", 404


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
