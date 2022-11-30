from db.database import Database
from bson import ObjectId


class Car(Database):
    def __init__(self, brand, model, year, fuel, km, engine, plate, sold):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel
        self.km = km
        self.engine = engine
        self.plate = plate
        self.sold = sold
        super(Car, self).__init__(collection="Cars")

    def __init__(self):
        super(Car, self).__init__(collection="Cars")

    def create(self):
        res = self.collection.insert_one({"brand": self.brand, "model": self.model, "year": self.year,
                                          "fuel": self.fuel, "km": self.km, "engine": self.engine,
                                          "plate": self.plate, "sold": self.sold})
        return res.inserted_id

    def readPlate(self, plate):
        res = self.collection.find_one({"plate": plate})
        return res

    def readModel(self, model):
        res = self.collection.find({"model": model})
        return res

    def read(self,plate):
        res = self.collection.find_one({"plate": plate})
        return res

    def update(self):
        res = self.collection.update_one({"_id": ObjectId(id)}, {
            "$set": {"brand": self.brand, "model": self.model, "year": self.year,
                     "fuel": self.fuel, "km": self.km, "engine": self.engine,
                     "plate": self.plate, "sold": self.sold}})
        return res.modified_count

    def delete(self):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count
