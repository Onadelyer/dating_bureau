from datetime import datetime
from Models.Client import Client
from Servises.ClientDatabase import ClientDatabase

class Match:
    """Клас для зберігання даних про співпадіння між клієнтами"""
    def __init__(self, client_a: Client, client_b: Client, matched_on: datetime = None):
        self.client_a = client_a
        self.client_b = client_b
        self.matched_on = matched_on or datetime.now()
        self.compatibility_score = self.calculate_compatibility()
        self.status = "new"

    def calculate_compatibility(self) -> float:
        # Приклад простого алгоритму сумісності
        common_interests = set(self.client_a.interests) & set(self.client_b.interests)
        total_interests = set(self.client_a.interests) | set(self.client_b.interests)
        score = len(common_interests) / len(total_interests) if total_interests else 0.0
        return round(score, 2)

    def update_status(self, new_status: str) -> None:
        self.status = new_status

    def to_dict(self) -> dict:
        return {
            'client_a_full_name': self.client_a.full_name,
            'client_b_full_name': self.client_b.full_name,
            'matched_on': self.matched_on,
            'compatibility_score': self.compatibility_score,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data: dict, client_db: ClientDatabase):
        client_a = client_db.find_by_name(data['client_a_full_name'])
        client_b = client_db.find_by_name(data['client_b_full_name'])
        matched_on = data.get('matched_on', datetime.now())
        if isinstance(matched_on, str):
            matched_on = datetime.fromisoformat(matched_on)
        match = cls(client_a, client_b, matched_on)
        match.compatibility_score = data.get('compatibility_score', 0.0)
        match.status = data.get('status', 'new')
        return match

