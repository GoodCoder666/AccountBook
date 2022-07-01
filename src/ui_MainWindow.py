# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 610)
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/images/icons/editor.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actFile_Open = QAction(MainWindow)
        self.actFile_Open.setObjectName(u"actFile_Open")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actFile_Open.setIcon(icon1)
        self.actFile_Save = QAction(MainWindow)
        self.actFile_Save.setObjectName(u"actFile_Save")
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actFile_Save.setIcon(icon2)
        self.actFile_SaveAs = QAction(MainWindow)
        self.actFile_SaveAs.setObjectName(u"actFile_SaveAs")
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/saveas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actFile_SaveAs.setIcon(icon3)
        self.actFile_New = QAction(MainWindow)
        self.actFile_New.setObjectName(u"actFile_New")
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actFile_New.setIcon(icon4)
        self.actHelp_About = QAction(MainWindow)
        self.actHelp_About.setObjectName(u"actHelp_About")
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actHelp_About.setIcon(icon5)
        self.actHelp_AboutQt = QAction(MainWindow)
        self.actHelp_AboutQt.setObjectName(u"actHelp_AboutQt")
        self.actHelp_AboutQt.setIcon(icon5)
        self.actStat_Show = QAction(MainWindow)
        self.actStat_Show.setObjectName(u"actStat_Show")
        icon6 = QIcon()
        icon6.addFile(u":/images/icons/statistics.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actStat_Show.setIcon(icon6)
        self.actEdit_Add = QAction(MainWindow)
        self.actEdit_Add.setObjectName(u"actEdit_Add")
        icon7 = QIcon()
        icon7.addFile(u":/images/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actEdit_Add.setIcon(icon7)
        self.actEdit_Remove = QAction(MainWindow)
        self.actEdit_Remove.setObjectName(u"actEdit_Remove")
        icon8 = QIcon()
        icon8.addFile(u":/images/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actEdit_Remove.setIcon(icon8)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAcceptDrops(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labSearch = QLabel(self.centralwidget)
        self.labSearch.setObjectName(u"labSearch")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labSearch.sizePolicy().hasHeightForWidth())
        self.labSearch.setSizePolicy(sizePolicy)
        self.labSearch.setMinimumSize(QSize(18, 0))
        self.labSearch.setStyleSheet(u"image: url(:/images/icons/search.png);")

        self.horizontalLayout.addWidget(self.labSearch)

        self.searchEdit = QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(u"searchEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.searchEdit)

        self.btnAddItem = QPushButton(self.centralwidget)
        self.btnAddItem.setObjectName(u"btnAddItem")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnAddItem.sizePolicy().hasHeightForWidth())
        self.btnAddItem.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btnAddItem)

        self.btnRemoveItem = QPushButton(self.centralwidget)
        self.btnRemoveItem.setObjectName(u"btnRemoveItem")
        self.btnRemoveItem.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btnRemoveItem.sizePolicy().hasHeightForWidth())
        self.btnRemoveItem.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btnRemoveItem)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table = QTableView(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setSelectionMode(QAbstractItemView.ContiguousSelection)

        self.verticalLayout.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.actFile_New)
        self.menu.addAction(self.actFile_Open)
        self.menu.addAction(self.actFile_Save)
        self.menu.addAction(self.actFile_SaveAs)
        self.menu_2.addAction(self.actStat_Show)
        self.menu_3.addAction(self.actHelp_About)
        self.menu_3.addAction(self.actHelp_AboutQt)
        self.menu_4.addAction(self.actEdit_Add)
        self.menu_4.addAction(self.actEdit_Remove)

        self.retranslateUi(MainWindow)
        self.btnAddItem.clicked.connect(self.actEdit_Add.trigger)
        self.btnRemoveItem.clicked.connect(self.actEdit_Remove.trigger)
        self.actEdit_Remove.enabledChanged.connect(self.btnRemoveItem.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8d26\u672c", None))
        self.actFile_Open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.actFile_Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actFile_Save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.actFile_Save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actFile_SaveAs.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
#if QT_CONFIG(shortcut)
        self.actFile_SaveAs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actFile_New.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.actFile_New.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actHelp_About.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#if QT_CONFIG(shortcut)
        self.actHelp_About.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actHelp_AboutQt.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8eQt", None))
#if QT_CONFIG(shortcut)
        self.actHelp_AboutQt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+H", None))
#endif // QT_CONFIG(shortcut)
        self.actStat_Show.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u7edf\u8ba1", None))
#if QT_CONFIG(shortcut)
        self.actStat_Show.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actEdit_Add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.actEdit_Remove.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
#if QT_CONFIG(shortcut)
        self.actEdit_Remove.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.labSearch.setText("")
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u2026\u2026", None))
        self.btnAddItem.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.btnRemoveItem.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7edf\u8ba1", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
    # retranslateUi

