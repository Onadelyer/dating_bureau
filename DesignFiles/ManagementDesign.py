# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Management.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Management(object):
    def setupUi(self, Management):
        if not Management.objectName():
            Management.setObjectName(u"Management")
        Management.resize(1000, 700)
        self.verticalLayout = QVBoxLayout(Management)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Management)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_clients_by_quarter = QWidget()
        self.tab_clients_by_quarter.setObjectName(u"tab_clients_by_quarter")
        self.verticalLayoutClientsByQuarter = QVBoxLayout(self.tab_clients_by_quarter)
        self.verticalLayoutClientsByQuarter.setObjectName(u"verticalLayoutClientsByQuarter")
        self.clients_by_quarter_table = QTableWidget(self.tab_clients_by_quarter)
        self.clients_by_quarter_table.setObjectName(u"clients_by_quarter_table")
        self.clients_by_quarter_table.setColumnCount(5)

        self.verticalLayoutClientsByQuarter.addWidget(self.clients_by_quarter_table)

        self.tabWidget.addTab(self.tab_clients_by_quarter, "")
        self.tab_clients = QWidget()
        self.tab_clients.setObjectName(u"tab_clients")
        self.verticalLayoutClients = QVBoxLayout(self.tab_clients)
        self.verticalLayoutClients.setObjectName(u"verticalLayoutClients")
        self.client_search_field = QLineEdit(self.tab_clients)
        self.client_search_field.setObjectName(u"client_search_field")

        self.verticalLayoutClients.addWidget(self.client_search_field)

        self.search_client_button = QPushButton(self.tab_clients)
        self.search_client_button.setObjectName(u"search_client_button")

        self.verticalLayoutClients.addWidget(self.search_client_button)

        self.clients_table = QTableWidget(self.tab_clients)
        self.clients_table.setObjectName(u"clients_table")
        self.clients_table.setColumnCount(4)

        self.verticalLayoutClients.addWidget(self.clients_table)

        self.delete_client_button = QPushButton(self.tab_clients)
        self.delete_client_button.setObjectName(u"delete_client_button")

        self.verticalLayoutClients.addWidget(self.delete_client_button, 0, Qt.AlignRight)

        self.tabWidget.addTab(self.tab_clients, "")
        self.tab_matches = QWidget()
        self.tab_matches.setObjectName(u"tab_matches")
        self.verticalLayoutMatches = QVBoxLayout(self.tab_matches)
        self.verticalLayoutMatches.setObjectName(u"verticalLayoutMatches")
        self.match_search_field = QLineEdit(self.tab_matches)
        self.match_search_field.setObjectName(u"match_search_field")

        self.verticalLayoutMatches.addWidget(self.match_search_field)

        self.search_match_button = QPushButton(self.tab_matches)
        self.search_match_button.setObjectName(u"search_match_button")

        self.verticalLayoutMatches.addWidget(self.search_match_button)

        self.matches_table = QTableWidget(self.tab_matches)
        self.matches_table.setObjectName(u"matches_table")
        self.matches_table.setColumnCount(4)

        self.verticalLayoutMatches.addWidget(self.matches_table)

        self.delete_match_button = QPushButton(self.tab_matches)
        self.delete_match_button.setObjectName(u"delete_match_button")

        self.verticalLayoutMatches.addWidget(self.delete_match_button, 0, Qt.AlignRight)

        self.tabWidget.addTab(self.tab_matches, "")
        self.tab_meetings = QWidget()
        self.tab_meetings.setObjectName(u"tab_meetings")
        self.verticalLayoutMeetings = QVBoxLayout(self.tab_meetings)
        self.verticalLayoutMeetings.setObjectName(u"verticalLayoutMeetings")
        self.meeting_search_field = QLineEdit(self.tab_meetings)
        self.meeting_search_field.setObjectName(u"meeting_search_field")

        self.verticalLayoutMeetings.addWidget(self.meeting_search_field)

        self.search_meeting_button = QPushButton(self.tab_meetings)
        self.search_meeting_button.setObjectName(u"search_meeting_button")

        self.verticalLayoutMeetings.addWidget(self.search_meeting_button)

        self.meetings_table = QTableWidget(self.tab_meetings)
        self.meetings_table.setObjectName(u"meetings_table")
        self.meetings_table.setColumnCount(4)

        self.verticalLayoutMeetings.addWidget(self.meetings_table)

        self.delete_meeting_button = QPushButton(self.tab_meetings)
        self.delete_meeting_button.setObjectName(u"delete_meeting_button")

        self.verticalLayoutMeetings.addWidget(self.delete_meeting_button, 0, Qt.AlignRight)

        self.tabWidget.addTab(self.tab_meetings, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Management)

        QMetaObject.connectSlotsByName(Management)
    # setupUi

    def retranslateUi(self, Management):
        Management.setWindowTitle(QCoreApplication.translate("Management", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0456\u043d\u043d\u044f \u0414\u0430\u043d\u0438\u043c\u0438", None))
        self.clients_by_quarter_table.setHorizontalHeaderLabels([
            QCoreApplication.translate("Management", u"\u041a\u0432\u0430\u0440\u0442\u0430\u043b", None),
            QCoreApplication.translate("Management", u"\u041f\u043e\u0432\u043d\u0435 \u0406\u043c'\u044f", None),
            QCoreApplication.translate("Management", u"\u0412\u0456\u043a", None),
            QCoreApplication.translate("Management", u"\u0421\u0442\u0430\u0442\u044c", None),
            QCoreApplication.translate("Management", u"\u0414\u0430\u0442\u0430 \u0414\u043e\u0434\u0430\u0432\u0430\u043d\u043d\u044f", None)])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_clients_by_quarter), QCoreApplication.translate("Management", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438 \u0437\u0430 \u043a\u0432\u0430\u0440\u0442\u0430\u043b\u0430\u043c\u0438", None))
        self.client_search_field.setPlaceholderText(QCoreApplication.translate("Management", u"\u041f\u043e\u0448\u0443\u043a \u041a\u043b\u0456\u0454\u043d\u0442\u0456\u0432...", None))
        self.search_client_button.setText(QCoreApplication.translate("Management", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.clients_table.setHorizontalHeaderLabels([
            QCoreApplication.translate("Management", u"\u041f\u043e\u0432\u043d\u0435 \u0406\u043c'\u044f", None),
            QCoreApplication.translate("Management", u"\u0412\u0456\u043a", None),
            QCoreApplication.translate("Management", u"\u0421\u0442\u0430\u0442\u044c", None),
            QCoreApplication.translate("Management", u"\u0406\u043d\u0442\u0435\u0440\u0435\u0441\u0438", None)])
        self.delete_client_button.setText(QCoreApplication.translate("Management", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u041a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_clients), QCoreApplication.translate("Management", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438", None))
        self.match_search_field.setPlaceholderText(QCoreApplication.translate("Management", u"\u041f\u043e\u0448\u0443\u043a \u041f\u0430\u0440...", None))
        self.search_match_button.setText(QCoreApplication.translate("Management", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.matches_table.setHorizontalHeaderLabels([
            QCoreApplication.translate("Management", u"\u041a\u043b\u0456\u0454\u043d\u0442 \u0410", None),
            QCoreApplication.translate("Management", u"\u041a\u043b\u0456\u0454\u043d\u0442 \u0411", None),
            QCoreApplication.translate("Management", u"\u041e\u0446\u0456\u043d\u043a\u0430 \u0421\u0443\u043c\u0456\u0441\u043d\u043e\u0441\u0442\u0456", None),
            QCoreApplication.translate("Management", u"\u0421\u0442\u0430\u0442\u0443\u0441", None)])
        self.delete_match_button.setText(QCoreApplication.translate("Management", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u041f\u0430\u0440\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_matches), QCoreApplication.translate("Management", u"\u041f\u0430\u0440\u0438", None))
        self.meeting_search_field.setPlaceholderText(QCoreApplication.translate("Management", u"\u041f\u043e\u0448\u0443\u043a \u0417\u0443\u0441\u0442\u0440\u0456\u0447\u0435\u0439...", None))
        self.search_meeting_button.setText(QCoreApplication.translate("Management", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.meetings_table.setHorizontalHeaderLabels([
            QCoreApplication.translate("Management", u"\u0423\u0447\u0430\u0441\u043d\u0438\u043a\u0438", None),
            QCoreApplication.translate("Management", u"\u0414\u0430\u0442\u0430 \u0442\u0430 \u0427\u0430\u0441", None),
            QCoreApplication.translate("Management", u"\u041c\u0456\u0441\u0446\u0435", None),
            QCoreApplication.translate("Management", u"\u0421\u0442\u0430\u0442\u0443\u0441", None)])
        self.delete_meeting_button.setText(QCoreApplication.translate("Management", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0417\u0443\u0441\u0442\u0440\u0456\u0447", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_meetings), QCoreApplication.translate("Management", u"\u0417\u0443\u0441\u0442\u0440\u0456\u0447\u0456", None))
    # retranslateUi

