from flask import Blueprint
from flask import render_template, request, url_for, redirect

from oop.car import Car

app = Blueprint('html_page', __name__)


# Flask maps HTTP requests to Python functions.
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('homePageTemplate.html')


@app.route('/filtering', methods=['GET', 'POST'])
def filtering():
    if request.method == 'POST':
        car_dict = {}
        model = request.form['model']
        brand = request.form['brand']
        if model:
            car_dict['model'] = model
        if brand:
            car_dict['brand'] = brand
        print(car_dict)
        cars = Car().readByDict(car_dict)
        carros = []
        for car in cars:
            carros.append(car)
        return render_template('tableTemplate.html', cars=carros, model=model, len=len(carros))
    return render_template('filter.html')


@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        car_dict = {}
        brand = request.form['brand']
        model = request.form['model']
        year = request.form['year']
        fuel = request.form['fuel']
        engine = request.form['engine']
        plate = request.form['plate']
        minKm = request.form['min_km']
        maxKm = request.form['max_km']

        if model:
            car_dict['model'] = model
        if brand:
            car_dict['brand'] = brand
        if year:
            car_dict['year'] = int(year)
        if fuel:
            car_dict['fuel'] = fuel
        if engine:
            car_dict['engine'] = engine
        if plate:
            car_dict['plate'] = plate

        km_dict = {}
        if minKm:
            km_dict['$gte'] = int(minKm)
        if maxKm:
            km_dict['$lte'] = int(maxKm)

        if km_dict:
            car_dict['km'] = km_dict

        res = Car().readByDict(car_dict)

        cars = []
        for car in res:
            cars.append(car)

        car_dict['min_km'] = minKm
        car_dict['max_km'] = maxKm
        return render_template('showCarsTemplate.html', cars=cars, len=len(cars), search=car_dict)
    return render_template('showCarsTemplate.html', cars=[], len=0, search=[])


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        plate = request.form['plate']
        Car().delete(plate)

    return redirect('/register')


@app.route('/find/<model>', methods=['GET'])
def find(model):
    cars = Car().readModel(model)
    carros = []
    for car in cars:
        carros.append(car)
    return render_template('showCarsTemplate.html', cars=carros, len=len(carros))


@app.route('/findOne/<plate>', methods=['GET', 'POST'])
def findOne(plate):
    car = Car().readPlate(plate)
    if car:
        return render_template('updateCarTemplate.html', car=car)
    return redirect('/register')


@app.route('/update', methods=['POST'])
def update():
    car = Car()
    car.plate = request.form['plate']
    car.brand = request.form['brand']
    car.model = request.form['model']
    car.year = request.form['year']
    car.fuel = request.form['fuel']
    car.km = request.form['km']
    car.engine = request.form['engine']
    car.sold = request.form['sold']
    car.update()
    redir = '/findOne/' + str(car.plate)
    return redirect(redir)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        car = Car()
        car.plate = request.form['plate']
        car.brand = request.form['brand']
        car.model = request.form['model']
        car.year = request.form['year']
        car.fuel = request.form['fuel']
        car.km = request.form['km']
        car.engine = request.form['engine']
        car.sold = request.form['sold']
        car.create()

        redir = '/findOne/' + str(car.plate)
        return redirect(redir)
    return render_template('registerCarTemplate.html')
