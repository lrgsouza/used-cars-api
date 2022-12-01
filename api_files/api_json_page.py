from flask import Blueprint, request
import jsonpickle as jp

from oop.car import Car
from helper.util import regexStr

app = Blueprint('json_page', __name__)


# Flask maps HTTP requests to Python functions.
@app.route('/api/model/<model>', methods=['GET'])
def api_car_model(model):
    return jp.encode(Car().readByDict(dict(model=model)))


@app.route('/api/plate/<plate>', methods=['GET'])
def api_car_plate(plate):
    return jp.encode(Car().readByDict(dict(plate=plate)))


@app.route('/api/search/', methods=['GET'])
def api_car_details():
    car_dict = {}
    brand = request.args.get('brand')
    model = request.args.get('model')
    year = request.args.get('year')
    fuel = request.args.get('fuel')
    engine = request.args.get('engine')
    plate = request.args.get('plate')
    minKm = request.args.get('min_km')
    maxKm = request.args.get('max_km')
    minPrice = request.args.get('min_price')
    maxPrice = request.args.get('max_price')

    if model:
        car_dict['model'] = regexStr(model)
    if brand:
        car_dict['brand'] = regexStr(brand)
    if year:
        car_dict['year'] = int(year)
    if fuel:
        car_dict['fuel'] = fuel
    if engine:
        car_dict['engine'] = engine
    if plate:
        car_dict['plate'] = regexStr(plate)

    km_dict = {}
    if minKm:
        km_dict['$gte'] = int(minKm)
    if maxKm:
        km_dict['$lte'] = int(maxKm)

    if km_dict:
        car_dict['km'] = km_dict

    price_dict = {}
    if minPrice:
        price_dict['$gte'] = int(minPrice)
    if maxPrice:
        price_dict['$lte'] = int(maxPrice)

    if price_dict:
        car_dict['price'] = price_dict

    res = Car().readByDict(car_dict)

    cars = []
    for car in res:
        cars.append(car)

    return jp.encode(cars)
