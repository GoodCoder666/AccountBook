# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgSettings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(255, 88)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.styleLayout = QHBoxLayout()
        self.styleLayout.setObjectName(u"styleLayout")
        self.labStyle = QLabel(Dialog)
        self.labStyle.setObjectName(u"labStyle")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labStyle.sizePolicy().hasHeightForWidth())
        self.labStyle.setSizePolicy(sizePolicy)

        self.styleLayout.addWidget(self.labStyle)

        self.comboBox_style = QComboBox(Dialog)
        self.comboBox_style.addItem("")
        self.comboBox_style.addItem("")
        self.comboBox_style.setObjectName(u"comboBox_style")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_style.sizePolicy().hasHeightForWidth())
        self.comboBox_style.setSizePolicy(sizePolicy1)

        self.styleLayout.addWidget(self.comboBox_style)


        self.verticalLayout.addLayout(self.styleLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e", None))
        self.labStyle.setText(QCoreApplication.translate("Dialog", u"\u4e3b\u9898\uff1a", None))
        self.comboBox_style.setItemText(0, QCoreApplication.translate("Dialog", u"Windows", None))
        self.comboBox_style.setItemText(1, QCoreApplication.translate("Dialog", u"Fusion", None))

    # retranslateUi

