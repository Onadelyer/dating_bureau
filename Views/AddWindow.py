from PySide6.QtWidgets import QWidget, QMessageBox
from DesignFiles.AddFormDesign import Ui_AddForm  # Імпортуємо правильний клас
from Servises.ClientDatabase import ClientDatabase
from Servises.MatchDatabase import MatchDatabase
from Servises.MeetingDatabase import MeetingDatabase
from Models.Client import Client
from Models.Match import Match
from Models.Meeting import Meeting
from datetime import datetime

class AddWindow(QWidget, Ui_AddForm):  # Використовуємо правильний клас
    def __init__(self, parent=None):
        """Ініціалізація компонентів та методів вікна"""
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.client_db = ClientDatabase()
        self.match_db = MatchDatabase()
        self.meeting_db = MeetingDatabase()

        self.init_comboboxes()
        self.add_client_button.clicked.connect(self.add_client_method)
        self.add_match_button.clicked.connect(self.add_match_method)
        self.add_meeting_button.clicked.connect(self.add_meeting_method)

    def init_comboboxes(self):
        """Ініціалізація комбо-боксів з іменами клієнтів"""
        clients = self.client_db.read_from_file()
        client_names = [client.full_name for client in clients]
        self.match_client_a.clear()
        self.match_client_b.clear()
        self.meeting_participants.clear()
        self.match_client_a.addItems(client_names)
        self.match_client_b.addItems(client_names)
        self.meeting_participants.addItems(client_names)

    def add_client_method(self):
        """Додавання нового клієнта"""
        full_name = self.client_name.text().strip()
        age = self.client_age.value()
        gender = self.client_gender.currentText()
        interests = self.client_interests.text().split(',')
        contact_info = self.client_contact_info.text().strip()
        preferred_age_min = self.client_preferred_age_min.value()
        preferred_age_max = self.client_preferred_age_max.value()
        preferred_gender = self.client_preferred_gender.currentText()
        bio = self.client_bio.toPlainText().strip()

        if not full_name or not interests or not contact_info or not bio:
            QMessageBox.warning(self, "Помилка", "Будь ласка, заповніть всі поля")
            return

        preferred_age_range = (preferred_age_min, preferred_age_max)
        client = Client(
            full_name, age, gender, interests, contact_info, preferred_age_range, preferred_gender, bio,
            date_added=datetime.now()  # Додано поле date_added
        )
        clients = self.client_db.read_from_file()
        clients.append(client)
        self.client_db.write_all(clients)
        QMessageBox.information(self, "Успіх", "Клієнта успішно додано")
        self.init_comboboxes()

    def add_match_method(self):
        """Додавання нового співпадіння"""
        client_a_name = self.match_client_a.currentText()
        client_b_name = self.match_client_b.currentText()
        clients = self.client_db.read_from_file()
        client_dict = {client.full_name: client for client in clients}

        client_a = client_dict.get(client_a_name)
        client_b = client_dict.get(client_b_name)

        if not client_a or not client_b:
            QMessageBox.warning(self, "Помилка", "Невірно вибрані клієнти")
            return

        match = Match(client_a, client_b)
        matches = self.match_db.read_from_file()
        matches.append(match)
        self.match_db.write_all(matches)
        QMessageBox.information(self, "Успіх", "Співпадіння успішно додано")

    def add_meeting_method(self):
        """Додавання нової зустрічі"""
        participant_items = self.meeting_participants.selectedItems()
        participants = []
        clients = self.client_db.read_from_file()
        client_dict = {client.full_name: client for client in clients}

        for item in participant_items:
            client = client_dict.get(item.text())
            if client:
                participants.append(client)

        if not participants:
            QMessageBox.warning(self, "Помилка", "Виберіть хоча б одного учасника")
            return

        scheduled_date = self.meeting_date.dateTime().toPython()
        location = self.meeting_location.text().strip()
        if not location:
            QMessageBox.warning(self, "Помилка", "Вкажіть місце проведення")
            return

        meeting = Meeting(participants, scheduled_date, location)
        meetings = self.meeting_db.read_from_file()
        meetings.append(meeting)
        self.meeting_db.write_all(meetings)
        QMessageBox.information(self, "Успіх", "Зустріч успішно заплановано")
