from Servises.BasicService import BasicService
from Models.Meeting import Meeting
from Models.Client import Client
from Servises.ClientDatabase import ClientDatabase
from datetime import datetime
from typing import List

class MeetingDatabase(BasicService):
    def __init__(self):
        self.file_path = "Database/meetings.txt"
        self.client_db = ClientDatabase()

    def read_from_file(self) -> List[Meeting]:
        meetings = []
        clients = self.client_db.read_from_file()
        client_dict = {client.full_name: client for client in clients}

        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    data = line.strip().split('~')
                    if len(data) >= 4:
                        participant_names = data[0].split(',')
                        scheduled_date = datetime.fromisoformat(data[1])
                        location = data[2]
                        status = data[3]
                        notes = data[4] if len(data) > 4 else ''
                        participants = [client_dict.get(name) for name in participant_names if client_dict.get(name)]
                        if participants:
                            meeting = Meeting(participants, scheduled_date, location)
                            meeting.status = status
                            meeting.notes = notes
                            meetings.append(meeting)
        except FileNotFoundError:
            pass
        return meetings

    def write_all(self, meetings: List[Meeting]) -> None:
        with open(self.file_path, "w") as file:
            for meeting in meetings:
                participant_names = ','.join([client.full_name for client in meeting.participants])
                data = [
                    participant_names,
                    meeting.scheduled_date.isoformat(),
                    meeting.location,
                    meeting.status,
                    meeting.notes
                ]
                line = '~'.join(data)
                file.write(line + '\n')
