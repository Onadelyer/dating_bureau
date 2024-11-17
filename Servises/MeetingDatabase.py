from Servises.BasicService import BasicService
from Models.Meeting import Meeting
from Models.Client import Client
from Servises.ClientDatabase import ClientDatabase
from datetime import datetime
from typing import List
from Servises.Database import Database

class MeetingDatabase(BasicService):
    def __init__(self):
        self.collection = Database.get_collection('meetings')
        self.client_db = ClientDatabase()

    def read_all(self) -> List[Meeting]:
        meetings = []
        cursor = self.collection.find()
        for doc in cursor:
            meeting = Meeting.from_dict(doc, self.client_db)
            meetings.append(meeting)
        return meetings

    def insert(self, meeting: Meeting) -> None:
        self.collection.insert_one(meeting.to_dict())

    def delete(self, participants_names: List[str], scheduled_date: datetime) -> None:
        self.collection.delete_one({
            'participants_names': participants_names,
            'scheduled_date': scheduled_date
        })
