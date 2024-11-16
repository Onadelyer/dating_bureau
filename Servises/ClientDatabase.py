from Servises.BasicService import BasicService
from Models.Client import Client
from typing import List, Tuple

class ClientDatabase(BasicService):
    def __init__(self):
        self.file_path = "Database/clients.txt"

    def read_from_file(self) -> List[Client]:
        clients = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    data = line.strip().split('~')
                    if len(data) == 9:
                        full_name = data[0]
                        age = int(data[1])
                        gender = data[2]
                        interests = data[3].split(',')
                        contact_info = data[4]
                        preferred_age_range = (int(data[5]), int(data[6]))
                        preferred_gender = data[7]
                        bio = data[8]
                        client = Client(full_name, age, gender, interests, contact_info, preferred_age_range, preferred_gender, bio)
                        clients.append(client)
        except FileNotFoundError:
            pass
        return clients

    def write_all(self, clients: List[Client]) -> None:
        with open(self.file_path, "w") as file:
            for client in clients:
                data = [
                    client.full_name,
                    str(client.age),
                    client.gender,
                    ','.join(client.interests),
                    client.contact_info,
                    str(client.preferred_age_range[0]),
                    str(client.preferred_age_range[1]),
                    client.preferred_gender,
                    client.bio
                ]
                line = '~'.join(data)
                file.write(line + '\n')
