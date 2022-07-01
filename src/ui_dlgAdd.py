# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgAdd.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(388, 146)
        font = QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.labSelDate = QLabel(Dialog)
        self.labSelDate.setObjectName(u"labSelDate")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labSelDate)

        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEdit)

        self.labSelEvent = QLabel(Dialog)
        self.labSelEvent.setObjectName(u"labSelEvent")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labSelEvent)

        self.eventEdit = QLineEdit(Dialog)
        self.eventEdit.setObjectName(u"eventEdit")
        self.eventEdit.setMaxLength(15)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.eventEdit)

        self.labMoney = QLabel(Dialog)
        self.labMoney.setObjectName(u"labMoney")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labMoney)

        self.moneyEdit = QLineEdit(Dialog)
        self.moneyEdit.setObjectName(u"moneyEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.moneyEdit)

        self.labNote = QLabel(Dialog)
        self.labNote.setObjectName(u"labNote")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labNote)

        self.noteEdit = QLineEdit(Dialog)
        self.noteEdit.setObjectName(u"noteEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.noteEdit)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u9879\u76ee", None))
        self.labSelDate.setText(QCoreApplication.translate("Dialog", u"\u65e5\u671f\uff1a", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/MM/dd", None))
        self.labSelEvent.setText(QCoreApplication.translate("Dialog", u"\u4e8b\u9879\uff1a", None))
        self.eventEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u7b80\u77ed\u4e8b\u9879\u63cf\u8ff0\uff0c\u5982\u201c\u8d2d\u7269\u201d\u201c\u5de5\u8d44\u201d\uff0c\u965015\u4e2a\u5b57\u4ee5\u5185", None))
        self.labMoney.setText(QCoreApplication.translate("Dialog", u"\u91d1\u989d\uff1a", None))
        self.moneyEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u91d1\u989d\u53d8\u5316\uff0c\u5982\u6536\u516515\u5143\u4e3a+15\uff0c\u652f\u51fa5\u5143\u4e3a-5", None))
        self.labNote.setText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8\uff1a", None))
        self.noteEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u5907\u6ce8\u6587\u5b57\uff0c\u53ef\u7559\u7a7a", None))
    # retranslateUi

