from Servises.BasicService import BasicService
from Models.Client import Client
from typing import List, Dict
from datetime import datetime
from Servises.Database import Database

class ClientDatabase(BasicService):
    def __init__(self):
        self.collection = Database.get_collection('clients')

    def read_all(self) -> List[Client]:
        clients = []
        cursor = self.collection.find()
        for doc in cursor:
            client = Client.from_dict(doc)
            clients.append(client)
        return clients

    def insert(self, client: Client) -> None:
        self.collection.insert_one(client.to_dict())

    def delete(self, full_name: str) -> None:
        self.collection.delete_one({'full_name': full_name})

    def find_by_name(self, full_name: str) -> Client:
        doc = self.collection.find_one({'full_name': full_name})
        if doc:
            return Client.from_dict(doc)
        return None
