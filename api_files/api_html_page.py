from flask import Blueprint
from flask import render_template, request, url_for, redirect

from oop.car import Car

app = Blueprint('html_page', __name__)


# Flask maps HTTP requests to Python functions.
@app.route('/home', methods=['GET', 'POST'])
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


@app.route('/model/<model>', methods=['GET'])
def byplate(model):
    cars = Car().readModel(model)
    carros = []
    for car in cars:
        carros.append(car)
    return render_template('tableTemplate.html', cars=carros, model=model, len=len(carros))


@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        model = request.form['model']
        cars = Car().readModel(model)
        carros = []
        for car in cars:
            carros.append(car)
        return render_template('filter.html', cars=carros)
    return render_template('filter.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        plate = request.form['plate']
        Car().delete(plate)
        return redirect(url_for('delete'))
    return render_template('delete.html')