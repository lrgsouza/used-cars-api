from db.database import Database

LIMIT = 50

class Car(Database):
    def __init__(self, brand, model, year, fuel, km, engine, plate, sold, price, transmission):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel
        self.km = km
        self.engine = engine
        self.plate = plate
        self.sold = sold
        self.price = price
        self.transmission = transmission
        super(Car, self).__init__(collection="Cars")

    def __init__(self):
        super(Car, self).__init__(collection="Cars")

    def create(self):
        res = self.collection.insert_one({"brand": self.brand, "model": self.model, "year": self.year,
                                          "fuel": self.fuel, "km": self.km, "engine": self.engine,
                                          "plate": self.plate, "sold": self.sold, "price": self.price,
                                          "transmission": self.transmission})
        return res.inserted_id

    def readByDict(self, args: dict):
        return self.collection.find(args).limit(LIMIT)

    def readPlate(self, plate):
        res = self.collection.find_one({"plate": plate})
        return res

    def update(self):
        res = self.collection.update_one({"plate": self.plate}, {
            "$set": {"brand": self.brand, "model": self.model, "year": self.year,
                     "fuel": self.fuel, "km": self.km, "engine": self.engine,
                     "plate": self.plate, "sold": self.sold, "price": self.price,
                     "transmission":self.transmission}})
        return res.modified_count

    def delete(self, plate):
        res = self.collection.delete_one({"plate": plate})
        return res.deleted_count
