from Servises.BasicService import BasicService
from Models.Match import Match
from Models.Client import Client
from Servises.ClientDatabase import ClientDatabase
from datetime import datetime
from typing import List
from Servises.Database import Database

class MatchDatabase(BasicService):
    def __init__(self):
        self.collection = Database.get_collection('matches')
        self.client_db = ClientDatabase()

    def read_all(self) -> List[Match]:
        matches = []
        cursor = self.collection.find()
        for doc in cursor:
            match = Match.from_dict(doc, self.client_db)
            matches.append(match)
        return matches

    def insert(self, match: Match) -> None:
        self.collection.insert_one(match.to_dict())

    def delete(self, client_a_name: str, client_b_name: str) -> None:
        self.collection.delete_one({
            'client_a_full_name': client_a_name,
            'client_b_full_name': client_b_name
        })
