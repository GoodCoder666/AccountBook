# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgCharts.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QGridLayout,
    QLabel, QSizePolicy, QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 490)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labEndDate = QLabel(Dialog)
        self.labEndDate.setObjectName(u"labEndDate")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labEndDate.sizePolicy().hasHeightForWidth())
        self.labEndDate.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.labEndDate, 1, 2, 1, 1)

        self.labStartDate = QLabel(Dialog)
        self.labStartDate.setObjectName(u"labStartDate")
        sizePolicy.setHeightForWidth(self.labStartDate.sizePolicy().hasHeightForWidth())
        self.labStartDate.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.labStartDate, 1, 0, 1, 1)

        self.startDateEdit = QDateEdit(Dialog)
        self.startDateEdit.setObjectName(u"startDateEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.startDateEdit.sizePolicy().hasHeightForWidth())
        self.startDateEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.startDateEdit, 1, 1, 1, 1)

        self.endDateEdit = QDateEdit(Dialog)
        self.endDateEdit.setObjectName(u"endDateEdit")
        sizePolicy1.setHeightForWidth(self.endDateEdit.sizePolicy().hasHeightForWidth())
        self.endDateEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.endDateEdit, 1, 3, 1, 1)

        self.graphTab = QTabWidget(Dialog)
        self.graphTab.setObjectName(u"graphTab")
        self.statTotal = QWidget()
        self.statTotal.setObjectName(u"statTotal")
        self.gridLayout_Total = QGridLayout(self.statTotal)
        self.gridLayout_Total.setObjectName(u"gridLayout_Total")
        self.totalView = QChartView(self.statTotal)
        self.totalView.setObjectName(u"totalView")
        self.totalView.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing)

        self.gridLayout_Total.addWidget(self.totalView, 0, 0, 1, 1)

        self.graphTab.addTab(self.statTotal, "")
        self.statEvent = QWidget()
        self.statEvent.setObjectName(u"statEvent")
        self.gridLayout_Event = QGridLayout(self.statEvent)
        self.gridLayout_Event.setObjectName(u"gridLayout_Event")
        self.eventView = QChartView(self.statEvent)
        self.eventView.setObjectName(u"eventView")
        self.eventView.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing)

        self.gridLayout_Event.addWidget(self.eventView, 0, 0, 1, 1)

        self.graphTab.addTab(self.statEvent, "")
        self.statDate = QWidget()
        self.statDate.setObjectName(u"statDate")
        self.gridLayout_Date = QGridLayout(self.statDate)
        self.gridLayout_Date.setObjectName(u"gridLayout_Date")
        self.dateView = QChartView(self.statDate)
        self.dateView.setObjectName(u"dateView")
        self.dateView.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing)

        self.gridLayout_Date.addWidget(self.dateView, 0, 0, 1, 1)

        self.graphTab.addTab(self.statDate, "")

        self.gridLayout.addWidget(self.graphTab, 0, 0, 1, 4)


        self.retranslateUi(Dialog)

        self.graphTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7edf\u8ba1\u4fe1\u606f", None))
        self.labEndDate.setText(QCoreApplication.translate("Dialog", u"\u7ed3\u675f\u65e5\u671f\uff1a", None))
        self.labStartDate.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u65e5\u671f\uff1a", None))
        self.startDateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/MM/dd", None))
        self.endDateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/MM/dd", None))
        self.graphTab.setTabText(self.graphTab.indexOf(self.statTotal), QCoreApplication.translate("Dialog", u"\u603b\u6536\u652f", None))
        self.graphTab.setTabText(self.graphTab.indexOf(self.statEvent), QCoreApplication.translate("Dialog", u"\u4e8b\u9879\u6536\u652f", None))
        self.graphTab.setTabText(self.graphTab.indexOf(self.statDate), QCoreApplication.translate("Dialog", u"\u6bcf\u65e5\u6536\u652f", None))
    # retranslateUi

