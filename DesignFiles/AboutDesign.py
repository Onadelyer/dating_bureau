# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(400, 300)
        self.verticalLayout = QVBoxLayout(About)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_about_text = QLabel(About)
        self.label_about_text.setObjectName(u"label_about_text")
        self.label_about_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_about_text)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"\u041f\u0440\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u0443", None))
        self.label_about_text.setText(QCoreApplication.translate("About", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u0430 \u0434\u043b\u044f \u0431\u044e\u0440\u043e \u0437\u043d\u0430\u0439\u043e\u043c\u0441\u0442\u0432\n"
"\u0420\u043e\u0437\u0440\u043e\u0431\u043b\u0435\u043d\u0430 \u0434\u043b\u044f \u0443\u043f\u0440\u0430\u0432\u043b\u0456\u043d\u043d\u044f \u0432\u0456\u0434\u043d\u043e\u0441\u0438\u043d\u0430\u043c\u0438 \u0437 \u043a\u043b\u0456\u0454\u043d\u0442\u0430\u043c\u0438 \u0442\u0430 \u043f\u0456\u0434\u0431\u043e\u0440\u0443 \u043f\u0430\u0440.\n"
"\n"
"\u0413\u0430\u0440\u044f\u0447\u0456 \u043a\u043b\u0430\u0432\u0456\u0448\u0456:\n"
"CTRL+M - \u0412\u0456\u0434\u043a\u0440\u0438\u0442\u0438 \u0432\u0456\u043a\u043d\u043e \u0434\u043e\u0434\u0430\u0432\u0430\u043d\u043d\u044f \u0434\u0430\u043d\u0438\u0445\n"
"CTRL+S - \u0412\u0456\u0434\u043a\u0440\u0438\u0442\u0438 \u0432\u0456\u043a\u043d\u043e \u0443\u043f\u0440\u0430\u0432\u043b\u0456\u043d\u043d\u044f\n"
"F1 - \u0412\u0456\u0434\u043a\u0440\u0438\u0442\u0438 \u0432\u0456\u043a\u043d\u043e \"\u041f\u0440\u043e"
                        " \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u0443\"", None))
    # retranslateUi

