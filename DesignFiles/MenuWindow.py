# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        if not MenuWindow.objectName():
            MenuWindow.setObjectName(u"MenuWindow")
        MenuWindow.resize(600, 400)
        self.actionAddData = QAction(MenuWindow)
        self.actionAddData.setObjectName(u"actionAddData")
        self.actionManagement = QAction(MenuWindow)
        self.actionManagement.setObjectName(u"actionManagement")
        self.actionAbout = QAction(MenuWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MenuWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title, 0, Qt.AlignCenter)

        self.AddItems = QPushButton(self.centralwidget)
        self.AddItems.setObjectName(u"AddItems")

        self.verticalLayout.addWidget(self.AddItems, 0, Qt.AlignCenter)

        self.Management = QPushButton(self.centralwidget)
        self.Management.setObjectName(u"Management")

        self.verticalLayout.addWidget(self.Management, 0, Qt.AlignCenter)

        self.About = QPushButton(self.centralwidget)
        self.About.setObjectName(u"About")

        self.verticalLayout.addWidget(self.About, 0, Qt.AlignCenter)

        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MenuWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 21))
        self.menuNavigation = QMenu(self.menubar)
        self.menuNavigation.setObjectName(u"menuNavigation")
        MenuWindow.setMenuBar(self.menubar)

        MenuWindow.addAction(self.actionAddData)
        MenuWindow.addAction(self.actionManagement)
        MenuWindow.addAction(self.actionAbout)
        self.menubar.addAction(self.menuNavigation.menuAction())
        self.menuNavigation.addAction(self.actionAddData)
        self.menuNavigation.addAction(self.actionManagement)
        self.menuNavigation.addAction(self.actionAbout)

        self.retranslateUi(MenuWindow)

        QMetaObject.connectSlotsByName(MenuWindow)
    # setupUi

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(QCoreApplication.translate("MenuWindow", u"\u0413\u043e\u043b\u043e\u0432\u043d\u0435 \u041c\u0435\u043d\u044e", None))
        self.actionAddData.setText(QCoreApplication.translate("MenuWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0414\u0430\u043d\u0456", None))
        self.actionManagement.setText(QCoreApplication.translate("MenuWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0456\u043d\u043d\u044f", None))
        self.actionAbout.setText(QCoreApplication.translate("MenuWindow", u"\u041f\u0440\u043e \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u0443", None))
        self.label_title.setText(QCoreApplication.translate("MenuWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0411\u044e\u0440\u043e \u0417\u043d\u0430\u0439\u043e\u043c\u0441\u0442\u0432", None))
        self.AddItems.setText(QCoreApplication.translate("MenuWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0414\u0430\u043d\u0456", None))
#if QT_CONFIG(shortcut)
        self.AddItems.setShortcut(QCoreApplication.translate("MenuWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.Management.setText(QCoreApplication.translate("MenuWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0456\u043d\u043d\u044f", None))
#if QT_CONFIG(shortcut)
        self.Management.setShortcut(QCoreApplication.translate("MenuWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.About.setText(QCoreApplication.translate("MenuWindow", u"\u041f\u0440\u043e \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u0443", None))
#if QT_CONFIG(shortcut)
        self.About.setShortcut(QCoreApplication.translate("MenuWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.menuNavigation.setTitle(QCoreApplication.translate("MenuWindow", u"\u041d\u0430\u0432\u0456\u0433\u0430\u0446\u0456\u044f", None))
    # retranslateUi

