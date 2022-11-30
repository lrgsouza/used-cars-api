from flask import Blueprint
from flask import render_template, request, url_for, redirect

from oop.car import Car

app = Blueprint('html_page', __name__)


# Flask maps HTTP requests to Python functions.
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        car = Car()
        car.plate = request.form['plate']
        car.brand = request.form['plate']
        car.model = request.form['model']
        car.year = request.form['year']
        car.fuel = request.form['fuel']
        car.km = request.form['km']
        car.engine = request.form['engine']
        car.sold = False
        car.create()
        return redirect(url_for('html_page.home'))
    return render_template('register.html')


@app.route('/model/<model>', methods=['GET'])
def byModel(model):
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
        return render_template('delete.html', num=res)
    return render_template('delete.html', num=-1)


@app.route('/find/<model>', methods=['GET'])
def find(model):
    cars = Car().readModel(model)
    carros = []
    for car in cars:
        carros.append(car)
    return render_template('showCarsTemplate.html', cars=carros, model=model, len=len(carros))
