import pymongo


class Database:
    def __init__(self, collection, dataset=None):
        database = 'usedcarsdb'
        connectionString = "mongodb+srv://usedcars:zfvyKT4HG0ng7e58@cluster.7yhbdp2.mongodb.net/?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]

        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)
