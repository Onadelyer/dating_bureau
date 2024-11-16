from Models.Person import Person
from typing import List, Tuple

class Client(Person):
    """Клас для зберігання даних про клієнтів бюро знайомств"""
    def __init__(
        self, 
        full_name: str, 
        age: int, 
        gender: str, 
        interests: List[str], 
        contact_info: str, 
        preferred_age_range: Tuple[int, int], 
        preferred_gender: str, 
        bio: str
    ):
        super().__init__(full_name, age)
        self.gender = gender
        self.interests = interests
        self.contact_info = contact_info
        self.preferred_age_range = preferred_age_range
        self.preferred_gender = preferred_gender
        self.bio = bio

    def update_profile(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def matches(self, other_client: 'Client') -> bool:
        # Простий приклад перевірки сумісності
        age_match = self.preferred_age_range[0] <= other_client.age <= self.preferred_age_range[1]
        gender_match = other_client.gender == self.preferred_gender
        interest_match = bool(set(self.interests) & set(other_client.interests))
        return age_match and gender_match and interest_match
