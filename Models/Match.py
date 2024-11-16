from datetime import date
from Models.Client import Client

class Match:
    """Клас для зберігання даних про співпадіння між клієнтами"""
    def __init__(self, client_a: Client, client_b: Client, matched_on: date = None):
        self.client_a = client_a
        self.client_b = client_b
        self.matched_on = matched_on or date.today()
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
