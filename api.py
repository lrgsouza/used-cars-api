from flask import Flask, request, jsonify,  render_template, request, url_for, redirect
from oop.car import Car
import jsonpickle as jp
import json
# Init app
app = Flask(__name__)


# Flask maps HTTP requests to Python functions.
# The process of mapping URLs to functions is called routing.
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


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('/'))
    return render_template('register.html')

@app.route('/api/model/<model>', methods=['GET'])
def byplate(model):
    cars = Car().readModel(model)
    carros = []
    for car in cars:
        carros.append(car)
    return render_template('tableTemplate.html', cars=carros, model=model, len=len(carros))

@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        car_dict = {}
        model = request.form['model']
        brand = request.form['brand']
        if model:
            car_dict['model'] = model
        if brand:
            car_dict['brand'] = brand
        # cars = Car().readModel(model)
        print(car_dict)
        cars = Car().readByDict(car_dict)
        carros = []
        for car in cars:
            carros.append(car)
        return render_template('tableTemplate.html', cars=carros, model=model, len=len(carros))
    return render_template('filter.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        plate = request.form['plate']
        res = Car().delete(plate)
        return render_template('delete.html',num=res)
    return render_template('delete.html',num=-1)

# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)
