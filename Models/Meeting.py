from datetime import datetime
from typing import List
from Models.Client import Client

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
