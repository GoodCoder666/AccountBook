# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgHelp.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(540, 280)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_repo = QGroupBox(Dialog)
        self.groupBox_repo.setObjectName(u"groupBox_repo")
        self.gridLayout_2 = QGridLayout(self.groupBox_repo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.githubLink = QCommandLinkButton(self.groupBox_repo)
        self.githubLink.setObjectName(u"githubLink")

        self.gridLayout_2.addWidget(self.githubLink, 0, 1, 1, 1)

        self.giteeLink = QCommandLinkButton(self.groupBox_repo)
        self.giteeLink.setObjectName(u"giteeLink")

        self.gridLayout_2.addWidget(self.giteeLink, 0, 2, 1, 1)

        self.licenseLink = QCommandLinkButton(self.groupBox_repo)
        self.licenseLink.setObjectName(u"licenseLink")

        self.gridLayout_2.addWidget(self.licenseLink, 1, 1, 1, 1)

        self.readmeLink = QCommandLinkButton(self.groupBox_repo)
        self.readmeLink.setObjectName(u"readmeLink")

        self.gridLayout_2.addWidget(self.readmeLink, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_repo, 0, 0, 1, 2)

        self.btnUpdate = QPushButton(Dialog)
        self.btnUpdate.setObjectName(u"btnUpdate")

        self.gridLayout.addWidget(self.btnUpdate, 3, 1, 1, 1)

        self.labVersion = QLabel(Dialog)
        self.labVersion.setObjectName(u"labVersion")

        self.gridLayout.addWidget(self.labVersion, 3, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5173\u4e8e", None))
        self.groupBox_repo.setTitle(QCoreApplication.translate("Dialog", u"\u4ee3\u7801\u4ed3\u5e93", None))
        self.githubLink.setText(QCoreApplication.translate("Dialog", u"GitHub \u9879\u76ee\u5730\u5740", None))
        self.githubLink.setDescription(QCoreApplication.translate("Dialog", u"https://github.com/GoodCoder666/AccountBook", None))
        self.giteeLink.setText(QCoreApplication.translate("Dialog", u"Gitee \u955c\u50cf\u5730\u5740", None))
        self.giteeLink.setDescription(QCoreApplication.translate("Dialog", u"https://gitee.com/goodcoder666/AccountBook", None))
        self.licenseLink.setText(QCoreApplication.translate("Dialog", u"\u7248\u6743\u6761\u6b3e\uff08GPLv3\uff09", None))
        self.licenseLink.setDescription(QCoreApplication.translate("Dialog", u"https://github.com/GoodCoder666/AccountBook/blob/main/LICENSE", None))
        self.readmeLink.setText(QCoreApplication.translate("Dialog", u"README \u5e2e\u52a9\u6587\u4ef6", None))
        self.readmeLink.setDescription(QCoreApplication.translate("Dialog", u"https://github.com/GoodCoder666/AccountBook/blob/main/README.md", None))
        self.btnUpdate.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.labVersion.setText(QCoreApplication.translate("Dialog", u"\u7248\u672c\u53f7\uff1a1.0.0 Stable (x64)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u611f\u8c22\u4f7f\u7528<span style=\" font-weight:700;\">\u8d26\u672c</span>\uff01\u6b22\u8fce\u5728<a href=\"https://github.com/GoodCoder666/AccountBook/issues\"><span style=\" text-decoration: underline; color:#0000ff;\">issues</span></a>\u6307\u51fabug\u95ee\u9898\u6216\u63d0\u51fa\u4fee\u6539\u610f\u89c1\u3002 </p><p>\u521b\u4f5c\u4e0d\u6613\uff0c\u5982\u679c\u60a8\u4e5f\u559c\u6b22<span style=\" font-weight:700;\">\u8d26\u672c</span>\uff0c\u8bf7\u5728<a href=\"https://github.com/GoodCoder666/AccountBook\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a>\u4e0a\u70b9\u4e2aStar\uff0c\u611f\u8c22\u60a8\u7684\u652f\u6301\uff01</p></body></html>", None))
    # retranslateUi

