from Servises.BasicService import BasicService
from Models.Match import Match
from Models.Client import Client
from Servises.ClientDatabase import ClientDatabase
from datetime import date
from typing import List

class MatchDatabase(BasicService):
    def __init__(self):
        self.file_path = "Database/matches.txt"
        self.client_db = ClientDatabase()

    def read_from_file(self) -> List[Match]:
        matches = []
        clients = self.client_db.read_from_file()
        client_dict = {client.full_name: client for client in clients}

        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    data = line.strip().split('~')
                    if len(data) == 5:
                        client_a_name = data[0]
                        client_b_name = data[1]
                        matched_on = date.fromisoformat(data[2])
                        compatibility_score = float(data[3])
                        status = data[4]
                        client_a = client_dict.get(client_a_name)
                        client_b = client_dict.get(client_b_name)
                        if client_a and client_b:
                            match = Match(client_a, client_b, matched_on)
                            match.compatibility_score = compatibility_score
                            match.status = status
                            matches.append(match)
        except FileNotFoundError:
            pass
        return matches

    def write_all(self, matches: List[Match]) -> None:
        with open(self.file_path, "w") as file:
            for match in matches:
                data = [
                    match.client_a.full_name,
                    match.client_b.full_name,
                    match.matched_on.isoformat(),
                    str(match.compatibility_score),
                    match.status
                ]
                line = '~'.join(data)
                file.write(line + '\n')
