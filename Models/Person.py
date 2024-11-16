class Person:
    """Базовий клас для збереження даних про людей"""
    def __init__(self, full_name: str, age: int):
        self._full_name = full_name
        self._age = age

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, value: str) -> None:
        self._full_name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value
