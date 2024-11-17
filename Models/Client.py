from Models.Person import Person
from typing import List, Tuple
from datetime import datetime

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
        bio: str,
        date_added: datetime = None  # Нове поле
    ):
        super().__init__(full_name, age)
        self.gender = gender
        self.interests = interests
        self.contact_info = contact_info
        self.preferred_age_range = preferred_age_range
        self.preferred_gender = preferred_gender
        self.bio = bio
        self.date_added = date_added or datetime.now()  # Встановлюємо поточну дату, якщо не задано

    def update_profile(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def matches(self, other_client: 'Client') -> bool:
        # Простий приклад перевірки сумісності
        age_match = self.preferred_age_range[0] <= other_client.age <= self.preferred_age_range[1]
        gender_match = other_client.gender == self.preferred_gender
        interest_match = bool(set(self.interests) & set(other_client.interests))
        return age_match and gender_match and interest_match

    def to_dict(self) -> dict:
        return {
            'full_name': self.full_name,
            'age': self.age,
            'gender': self.gender,
            'interests': self.interests,
            'contact_info': self.contact_info,
            'preferred_age_range': self.preferred_age_range,
            'preferred_gender': self.preferred_gender,
            'bio': self.bio,
            'date_added': self.date_added
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            full_name=data['full_name'],
            age=data['age'],
            gender=data['gender'],
            interests=data['interests'],
            contact_info=data['contact_info'],
            preferred_age_range=tuple(data['preferred_age_range']),
            preferred_gender=data['preferred_gender'],
            bio=data['bio'],
            date_added=data.get('date_added', datetime.now())
        )