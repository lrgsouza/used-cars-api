import jsonpickle as jp
from flask import Flask, render_template, request, url_for, redirect

from oop.car import Car

# Init app
app = Flask(__name__)


# Flask maps HTTP requests to Python functions.
# The process of mapping URLs to functions is called routing.
@app.route('/', methods=['GET'])
def home():
    return "<h1>Used Cars Database System</h1><p>Vehicle Data Query</p>"


@app.route('/cars/model/<model>', methods=['GET'])
def api_car_model(model):
    return jp.encode(Car().readModel(model))

@app.route('/cars/plate/<plate>', methods=['GET'])
def api_car_plate(plate):
    return jp.encode(Car().readPlate(plate))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error="Error 404: Not Found"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html", error="Error 500: Internal Server Error"), 500


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

@app.route('/platerender/<plate>', methods=['GET'])
def byplate(plate):
    cars = Car().readPlate(plate)
    return render_template('plateTemplate.html', cars=cars)

# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
