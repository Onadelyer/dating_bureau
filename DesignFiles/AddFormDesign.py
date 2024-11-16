# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_AddForm(object):
    def setupUi(self, AddForm):
        if not AddForm.objectName():
            AddForm.setObjectName(u"AddForm")
        AddForm.resize(800, 600)
        self.verticalLayout = QVBoxLayout(AddForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(AddForm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_client = QWidget()
        self.tab_client.setObjectName(u"tab_client")
        self.formLayoutClient = QFormLayout(self.tab_client)
        self.formLayoutClient.setObjectName(u"formLayoutClient")
        self.label_client_name = QLabel(self.tab_client)
        self.label_client_name.setObjectName(u"label_client_name")

        self.formLayoutClient.setWidget(0, QFormLayout.LabelRole, self.label_client_name)

        self.client_name = QLineEdit(self.tab_client)
        self.client_name.setObjectName(u"client_name")

        self.formLayoutClient.setWidget(0, QFormLayout.FieldRole, self.client_name)

        self.label_client_age = QLabel(self.tab_client)
        self.label_client_age.setObjectName(u"label_client_age")

        self.formLayoutClient.setWidget(1, QFormLayout.LabelRole, self.label_client_age)

        self.client_age = QSpinBox(self.tab_client)
        self.client_age.setObjectName(u"client_age")
        self.client_age.setMinimum(18)
        self.client_age.setMaximum(100)

        self.formLayoutClient.setWidget(1, QFormLayout.FieldRole, self.client_age)

        self.label_client_gender = QLabel(self.tab_client)
        self.label_client_gender.setObjectName(u"label_client_gender")

        self.formLayoutClient.setWidget(2, QFormLayout.LabelRole, self.label_client_gender)

        self.client_gender = QComboBox(self.tab_client)
        self.client_gender.addItem("")
        self.client_gender.addItem("")
        self.client_gender.addItem("")
        self.client_gender.setObjectName(u"client_gender")

        self.formLayoutClient.setWidget(2, QFormLayout.FieldRole, self.client_gender)

        self.label_client_interests = QLabel(self.tab_client)
        self.label_client_interests.setObjectName(u"label_client_interests")

        self.formLayoutClient.setWidget(3, QFormLayout.LabelRole, self.label_client_interests)

        self.client_interests = QLineEdit(self.tab_client)
        self.client_interests.setObjectName(u"client_interests")

        self.formLayoutClient.setWidget(3, QFormLayout.FieldRole, self.client_interests)

        self.label_client_contact_info = QLabel(self.tab_client)
        self.label_client_contact_info.setObjectName(u"label_client_contact_info")

        self.formLayoutClient.setWidget(4, QFormLayout.LabelRole, self.label_client_contact_info)

        self.client_contact_info = QLineEdit(self.tab_client)
        self.client_contact_info.setObjectName(u"client_contact_info")

        self.formLayoutClient.setWidget(4, QFormLayout.FieldRole, self.client_contact_info)

        self.label_client_preferred_age = QLabel(self.tab_client)
        self.label_client_preferred_age.setObjectName(u"label_client_preferred_age")

        self.formLayoutClient.setWidget(5, QFormLayout.LabelRole, self.label_client_preferred_age)

        self.horizontalLayoutPreferredAge = QHBoxLayout()
        self.horizontalLayoutPreferredAge.setObjectName(u"horizontalLayoutPreferredAge")
        self.client_preferred_age_min = QSpinBox(self.tab_client)
        self.client_preferred_age_min.setObjectName(u"client_preferred_age_min")
        self.client_preferred_age_min.setMinimum(18)
        self.client_preferred_age_min.setMaximum(100)

        self.horizontalLayoutPreferredAge.addWidget(self.client_preferred_age_min)

        self.label_dash = QLabel(self.tab_client)
        self.label_dash.setObjectName(u"label_dash")

        self.horizontalLayoutPreferredAge.addWidget(self.label_dash)

        self.client_preferred_age_max = QSpinBox(self.tab_client)
        self.client_preferred_age_max.setObjectName(u"client_preferred_age_max")
        self.client_preferred_age_max.setMinimum(18)
        self.client_preferred_age_max.setMaximum(100)

        self.horizontalLayoutPreferredAge.addWidget(self.client_preferred_age_max)


        self.formLayoutClient.setLayout(5, QFormLayout.FieldRole, self.horizontalLayoutPreferredAge)

        self.label_client_preferred_gender = QLabel(self.tab_client)
        self.label_client_preferred_gender.setObjectName(u"label_client_preferred_gender")

        self.formLayoutClient.setWidget(6, QFormLayout.LabelRole, self.label_client_preferred_gender)

        self.client_preferred_gender = QComboBox(self.tab_client)
        self.client_preferred_gender.addItem("")
        self.client_preferred_gender.addItem("")
        self.client_preferred_gender.addItem("")
        self.client_preferred_gender.setObjectName(u"client_preferred_gender")

        self.formLayoutClient.setWidget(6, QFormLayout.FieldRole, self.client_preferred_gender)

        self.label_client_bio = QLabel(self.tab_client)
        self.label_client_bio.setObjectName(u"label_client_bio")

        self.formLayoutClient.setWidget(7, QFormLayout.LabelRole, self.label_client_bio)

        self.client_bio = QTextEdit(self.tab_client)
        self.client_bio.setObjectName(u"client_bio")

        self.formLayoutClient.setWidget(7, QFormLayout.FieldRole, self.client_bio)

        self.add_client_button = QPushButton(self.tab_client)
        self.add_client_button.setObjectName(u"add_client_button")

        self.formLayoutClient.setWidget(8, QFormLayout.FieldRole, self.add_client_button)

        self.tabWidget.addTab(self.tab_client, "")
        self.tab_match = QWidget()
        self.tab_match.setObjectName(u"tab_match")
        self.formLayoutMatch = QFormLayout(self.tab_match)
        self.formLayoutMatch.setObjectName(u"formLayoutMatch")
        self.label_match_client_a = QLabel(self.tab_match)
        self.label_match_client_a.setObjectName(u"label_match_client_a")

        self.formLayoutMatch.setWidget(0, QFormLayout.LabelRole, self.label_match_client_a)

        self.match_client_a = QComboBox(self.tab_match)
        self.match_client_a.setObjectName(u"match_client_a")

        self.formLayoutMatch.setWidget(0, QFormLayout.FieldRole, self.match_client_a)

        self.label_match_client_b = QLabel(self.tab_match)
        self.label_match_client_b.setObjectName(u"label_match_client_b")

        self.formLayoutMatch.setWidget(1, QFormLayout.LabelRole, self.label_match_client_b)

        self.match_client_b = QComboBox(self.tab_match)
        self.match_client_b.setObjectName(u"match_client_b")

        self.formLayoutMatch.setWidget(1, QFormLayout.FieldRole, self.match_client_b)

        self.add_match_button = QPushButton(self.tab_match)
        self.add_match_button.setObjectName(u"add_match_button")

        self.formLayoutMatch.setWidget(2, QFormLayout.FieldRole, self.add_match_button)

        self.tabWidget.addTab(self.tab_match, "")
        self.tab_meeting = QWidget()
        self.tab_meeting.setObjectName(u"tab_meeting")
        self.formLayoutMeeting = QFormLayout(self.tab_meeting)
        self.formLayoutMeeting.setObjectName(u"formLayoutMeeting")
        self.label_meeting_participants = QLabel(self.tab_meeting)
        self.label_meeting_participants.setObjectName(u"label_meeting_participants")

        self.formLayoutMeeting.setWidget(0, QFormLayout.LabelRole, self.label_meeting_participants)

        self.meeting_participants = QListWidget(self.tab_meeting)
        self.meeting_participants.setObjectName(u"meeting_participants")

        self.formLayoutMeeting.setWidget(0, QFormLayout.FieldRole, self.meeting_participants)

        self.label_meeting_date = QLabel(self.tab_meeting)
        self.label_meeting_date.setObjectName(u"label_meeting_date")

        self.formLayoutMeeting.setWidget(1, QFormLayout.LabelRole, self.label_meeting_date)

        self.meeting_date = QDateTimeEdit(self.tab_meeting)
        self.meeting_date.setObjectName(u"meeting_date")
        self.meeting_date.setCalendarPopup(True)

        self.formLayoutMeeting.setWidget(1, QFormLayout.FieldRole, self.meeting_date)

        self.label_meeting_location = QLabel(self.tab_meeting)
        self.label_meeting_location.setObjectName(u"label_meeting_location")

        self.formLayoutMeeting.setWidget(2, QFormLayout.LabelRole, self.label_meeting_location)

        self.meeting_location = QLineEdit(self.tab_meeting)
        self.meeting_location.setObjectName(u"meeting_location")

        self.formLayoutMeeting.setWidget(2, QFormLayout.FieldRole, self.meeting_location)

        self.add_meeting_button = QPushButton(self.tab_meeting)
        self.add_meeting_button.setObjectName(u"add_meeting_button")

        self.formLayoutMeeting.setWidget(3, QFormLayout.FieldRole, self.add_meeting_button)

        self.tabWidget.addTab(self.tab_meeting, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(AddForm)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AddForm)
    # setupUi

    def retranslateUi(self, AddForm):
        AddForm.setWindowTitle(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0414\u0430\u043d\u0456", None))
        self.label_client_name.setText(QCoreApplication.translate("AddForm", u"\u041f\u043e\u0432\u043d\u0435 \u0406\u043c'\u044f:", None))
        self.label_client_age.setText(QCoreApplication.translate("AddForm", u"\u0412\u0456\u043a:", None))
        self.label_client_gender.setText(QCoreApplication.translate("AddForm", u"\u0421\u0442\u0430\u0442\u044c:", None))
        self.client_gender.setItemText(0, QCoreApplication.translate("AddForm", u"\u0427\u043e\u043b\u043e\u0432\u0456\u043a", None))
        self.client_gender.setItemText(1, QCoreApplication.translate("AddForm", u"\u0416\u0456\u043d\u043a\u0430", None))
        self.client_gender.setItemText(2, QCoreApplication.translate("AddForm", u"\u0406\u043d\u0448\u0435", None))

        self.label_client_interests.setText(QCoreApplication.translate("AddForm", u"\u0406\u043d\u0442\u0435\u0440\u0435\u0441\u0438 (\u0447\u0435\u0440\u0435\u0437 \u043a\u043e\u043c\u0443):", None))
        self.label_client_contact_info.setText(QCoreApplication.translate("AddForm", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430 \u0406\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0456\u044f:", None))
        self.label_client_preferred_age.setText(QCoreApplication.translate("AddForm", u"\u0411\u0430\u0436\u0430\u043d\u0438\u0439 \u0412\u0456\u043a\u043e\u0432\u0438\u0439 \u0414\u0456\u0430\u043f\u0430\u0437\u043e\u043d:", None))
        self.label_dash.setText(QCoreApplication.translate("AddForm", u"-", None))
        self.label_client_preferred_gender.setText(QCoreApplication.translate("AddForm", u"\u0411\u0430\u0436\u0430\u043d\u0430 \u0421\u0442\u0430\u0442\u044c:", None))
        self.client_preferred_gender.setItemText(0, QCoreApplication.translate("AddForm", u"\u0427\u043e\u043b\u043e\u0432\u0456\u043a", None))
        self.client_preferred_gender.setItemText(1, QCoreApplication.translate("AddForm", u"\u0416\u0456\u043d\u043a\u0430", None))
        self.client_preferred_gender.setItemText(2, QCoreApplication.translate("AddForm", u"\u0411\u0443\u0434\u044c-\u044f\u043a\u0430", None))

        self.label_client_bio.setText(QCoreApplication.translate("AddForm", u"\u0411\u0456\u043e\u0433\u0440\u0430\u0444\u0456\u044f:", None))
        self.add_client_button.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u041a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_client), QCoreApplication.translate("AddForm", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u041a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.label_match_client_a.setText(QCoreApplication.translate("AddForm", u"\u041a\u043b\u0456\u0454\u043d\u0442 A:", None))
        self.label_match_client_b.setText(QCoreApplication.translate("AddForm", u"\u041a\u043b\u0456\u0454\u043d\u0442 B:", None))
        self.add_match_button.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u041f\u0430\u0440\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_match), QCoreApplication.translate("AddForm", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u041f\u0430\u0440\u0443", None))
        self.label_meeting_participants.setText(QCoreApplication.translate("AddForm", u"\u0423\u0447\u0430\u0441\u043d\u0438\u043a\u0438:", None))
        self.label_meeting_date.setText(QCoreApplication.translate("AddForm", u"\u0414\u0430\u0442\u0430 \u0442\u0430 \u0427\u0430\u0441:", None))
        self.label_meeting_location.setText(QCoreApplication.translate("AddForm", u"\u041c\u0456\u0441\u0446\u0435:", None))
        self.add_meeting_button.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0417\u0443\u0441\u0442\u0440\u0456\u0447", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_meeting), QCoreApplication.translate("AddForm", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0417\u0443\u0441\u0442\u0440\u0456\u0447", None))
    # retranslateUi

