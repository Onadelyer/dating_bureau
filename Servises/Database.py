from pymongo import MongoClient

class Database:
    _client = None
    _db = None

    @staticmethod
    def initialize():
        Database._client = MongoClient('mongodb://localhost:27017/')
        Database._db = Database._client['dating_bureau']

    @staticmethod
    def get_collection(collection_name):
        if Database._db is None:
            raise Exception("Database not initialized. Call Database.initialize() first.")
        return Database._db[collection_name]

    @staticmethod
    def close():
        if Database._client:
            Database._client.close()
