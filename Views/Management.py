from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from DesignFiles.ManagementDesign import Ui_Management
from Servises.ClientDatabase import ClientDatabase
from Servises.MatchDatabase import MatchDatabase
from Servises.MeetingDatabase import MeetingDatabase
from Models.Client import Client
from Models.Match import Match
from Models.Meeting import Meeting
from datetime import datetime

class Management(QWidget, Ui_Management):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.client_db = ClientDatabase()
        self.match_db = MatchDatabase()
        self.meeting_db = MeetingDatabase()

        self.fill_clients_table(self.client_db.read_all())
        self.fill_matches_table(self.match_db.read_all())
        self.fill_meetings_table(self.meeting_db.read_all())

        self.search_client_button.clicked.connect(self.search_client_method)
        self.search_match_button.clicked.connect(self.search_match_method)
        self.search_meeting_button.clicked.connect(self.search_meeting_method)
        self.delete_client_button.clicked.connect(self.delete_client_method)
        self.delete_match_button.clicked.connect(self.delete_match_method)
        self.delete_meeting_button.clicked.connect(self.delete_meeting_method)
        self.fill_clients_by_quarter_table()

    def fill_clients_table(self, clients: list[Client]) -> None:
        """Заповнення таблиці клієнтів"""
        self.clients_table.clearContents()
        self.clients_table.setRowCount(len(clients))
        for i, client in enumerate(clients):
            self.clients_table.setItem(i, 0, QTableWidgetItem(client.full_name))
            self.clients_table.setItem(i, 1, QTableWidgetItem(str(client.age)))
            self.clients_table.setItem(i, 2, QTableWidgetItem(client.gender))
            self.clients_table.setItem(i, 3, QTableWidgetItem(', '.join(client.interests)))

    def fill_matches_table(self, matches: list[Match]) -> None:
        """Заповнення таблиці співпадінь"""
        self.matches_table.clearContents()
        self.matches_table.setRowCount(len(matches))
        for i, match in enumerate(matches):
            self.matches_table.setItem(i, 0, QTableWidgetItem(match.client_a.full_name))
            self.matches_table.setItem(i, 1, QTableWidgetItem(match.client_b.full_name))
            self.matches_table.setItem(i, 2, QTableWidgetItem(str(match.compatibility_score)))
            self.matches_table.setItem(i, 3, QTableWidgetItem(match.status))

    def fill_meetings_table(self, meetings: list[Meeting]) -> None:
        """Заповнення таблиці зустрічей"""
        self.meetings_table.clearContents()
        self.meetings_table.setRowCount(len(meetings))
        for i, meeting in enumerate(meetings):
            participants = ', '.join([client.full_name for client in meeting.participants])
            self.meetings_table.setItem(i, 0, QTableWidgetItem(participants))
            self.meetings_table.setItem(i, 1, QTableWidgetItem(meeting.scheduled_date.strftime("%Y-%m-%d %H:%M")))
            self.meetings_table.setItem(i, 2, QTableWidgetItem(meeting.location))
            self.meetings_table.setItem(i, 3, QTableWidgetItem(meeting.status))

    def search_client_method(self):
        """Пошук клієнтів"""
        search_text = self.client_search_field.text().strip()
        if not search_text:
            QMessageBox.warning(self, "Помилка", "Введіть текст для пошуку")
            return
        clients = [client for client in self.client_db.read_from_file() if search_text.lower() in client.full_name.lower()]
        self.fill_clients_table(clients)

    def search_match_method(self):
        """Пошук співпадінь"""
        search_text = self.match_search_field.text().strip()
        if not search_text:
            QMessageBox.warning(self, "Помилка", "Введіть текст для пошуку")
            return
        matches = [match for match in self.match_db.read_from_file() if search_text.lower() in match.client_a.full_name.lower() or search_text.lower() in match.client_b.full_name.lower()]
        self.fill_matches_table(matches)

    def search_meeting_method(self):
        """Пошук зустрічей"""
        search_text = self.meeting_search_field.text().strip()
        if not search_text:
            QMessageBox.warning(self, "Помилка", "Введіть текст для пошуку")
            return
        meetings = [meeting for meeting in self.meeting_db.read_from_file() if search_text.lower() in ', '.join([client.full_name for client in meeting.participants]).lower()]
        self.fill_meetings_table(meetings)

    def delete_client_method(self):
        """Видалення клієнта"""
        row = self.clients_table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Помилка", "Виберіть клієнта для видалення")
            return
        full_name = self.clients_table.item(row, 0).text()
        clients = [client for client in self.client_db.read_from_file() if client.full_name != full_name]
        self.client_db.write_all(clients)
        self.fill_clients_table(clients)

    def delete_match_method(self):
        """Видалення співпадіння"""
        row = self.matches_table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Помилка", "Виберіть співпадіння для видалення")
            return
        client_a_name = self.matches_table.item(row, 0).text()
        client_b_name = self.matches_table.item(row, 1).text()
        matches = [match for match in self.match_db.read_from_file() if not ((match.client_a.full_name == client_a_name and match.client_b.full_name == client_b_name) or (match.client_a.full_name == client_b_name and match.client_b.full_name == client_a_name))]
        self.match_db.write_all(matches)
        self.fill_matches_table(matches)

    def delete_meeting_method(self):
        """Видалення зустрічі"""
        row = self.meetings_table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Помилка", "Виберіть зустріч для видалення")
            return
        participants_text = self.meetings_table.item(row, 0).text()
        scheduled_date_text = self.meetings_table.item(row, 1).text()
        scheduled_date = datetime.strptime(scheduled_date_text, "%Y-%m-%d %H:%M")
        meetings = [meeting for meeting in self.meeting_db.read_from_file() if not (', '.join([client.full_name for client in meeting.participants]) == participants_text and meeting.scheduled_date == scheduled_date)]
        self.meeting_db.write_all(meetings)
        self.fill_meetings_table(meetings)

    def group_clients_by_quarter(self):
        """Групування клієнтів за кварталами року"""
        clients = self.client_db.read_from_file()
        quarters = {1: [], 2: [], 3: [], 4: []}
        for client in clients:
            month = client.date_added.month
            quarter = (month - 1) // 3 + 1
            quarters[quarter].append(client)
        return quarters
    
    def fill_clients_by_quarter_table(self):
        """Заповнення таблиці клієнтів за кварталами"""
        quarters = self.group_clients_by_quarter()
        self.clients_by_quarter_table.clearContents()
        total_rows = sum(len(clients) for clients in quarters.values())
        self.clients_by_quarter_table.setRowCount(total_rows)
        row = 0
        for quarter, clients in sorted(quarters.items()):
            for client in clients:
                self.clients_by_quarter_table.setItem(row, 0, QTableWidgetItem(f"Квартал {quarter}"))
                self.clients_by_quarter_table.setItem(row, 1, QTableWidgetItem(client.full_name))
                self.clients_by_quarter_table.setItem(row, 2, QTableWidgetItem(str(client.age)))
                self.clients_by_quarter_table.setItem(row, 3, QTableWidgetItem(client.gender))
                self.clients_by_quarter_table.setItem(row, 4, QTableWidgetItem(client.date_added.strftime("%Y-%m-%d")))
                row += 1