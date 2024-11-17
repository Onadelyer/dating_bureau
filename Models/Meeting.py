from datetime import datetime
from typing import List
from Models.Client import Client
from Servises.ClientDatabase import ClientDatabase

class Meeting:
    """Клас для зберігання даних про зустрічі між клієнтами"""
    def __init__(self, participants: List[Client], scheduled_date: datetime, location: str):
        self.participants = participants
        self.scheduled_date = scheduled_date
        self.location = location
        self.status = "scheduled"
        self.notes = ""

    def reschedule(self, new_date: datetime) -> None:
        self.scheduled_date = new_date
        self.status = "rescheduled"

    def cancel(self) -> None:
        self.status = "cancelled"

    def add_notes(self, notes: str) -> None:
        self.notes += notes

    def to_dict(self) -> dict:
        return {
            'participants_names': [client.full_name for client in self.participants],
            'scheduled_date': self.scheduled_date,
            'location': self.location,
            'status': self.status,
            'notes': self.notes
        }

    @classmethod
    def from_dict(cls, data: dict, client_db: ClientDatabase):
        participants = []
        for name in data['participants_names']:
            client = client_db.find_by_name(name)
            if client:
                participants.append(client)
        scheduled_date = data.get('scheduled_date', datetime.now())
        meeting = cls(participants, scheduled_date, data['location'])
        meeting.status = data.get('status', 'scheduled')
        meeting.notes = data.get('notes', '')
        return meeting