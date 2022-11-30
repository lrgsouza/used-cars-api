from flask import Flask, request, jsonify,  render_template, request, url_for, redirect
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


@app.route('/home', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        car = Car()
        car.brand = request.form['brand']
        car.model = request.form['model']
        car.year = request.form['year']
        car.fuel = request.form['fuel']
        car.km = request.form['km']
        car.engine = request.form['engine']
        car.plate = request.form['plate']
        car.sold = False
        car.create()
        return redirect(url_for('index'))

    cars = Car().readPlate('VCZ8Z16')
    return render_template('index.html', cars=cars)

@app.route('/platerender/<plate>', methods=('GET'))
def byplate(plate):
    cars = Car().readPlate(plate)
    return render_template('plateTemplate.html', cars=cars)

# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
