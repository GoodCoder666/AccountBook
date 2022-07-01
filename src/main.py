import sys
from bisect import insort_right
from functools import partial
from os.path import basename
from webbrowser import open_new_tab

from PySide6.QtWidgets import *
from PySide6.QtCore import Slot, QDate
from PySide6.QtGui import QStandardItem, QStandardItemModel

from api import ApiError, openFile, query, saveFile
from dlgAdd import dlgAdd
from dlgCharts import dlgCharts
from ui_dlgHelp import Ui_Dialog as Ui_dlgHelp
from ui_MainWindow import Ui_MainWindow

# Version info
VERSION = '1.0.0'
CHANNEL = 'stable'
BUILD_DATE = '2022-07-01'
FULL_VERSION = f'{VERSION}-{CHANNEL} ({BUILD_DATE}) on {sys.platform}'

app = QApplication(sys.argv)

class AccountBookMainWindow(QMainWindow):
    version_str = '账本 ' + VERSION
    unsaved_tip = '*'
    SUPPORTED_FILTERS = '账本文件(*.abf);;文本文件(*.txt);;所有文件(*.*)'

    def __init__(self, parent=None):
        # Initialize window
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('账本 ' + VERSION)
        self.labStatus = QLabel(self)
        self.ui.statusBar.addWidget(self.labStatus)

        # Initialize table
        self.model = QStandardItemModel(0, 4, self)
        self.model.setHorizontalHeaderLabels(['日期', '事项', '金额', '备注'])
        self.ui.table.setModel(self.model)
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.__data = []
        self.on_actFile_New_triggered()
        self.ui.actEdit_Remove.setEnabled(False)

        # Connect slots
        self.ui.table.selectionModel().selectionChanged.connect(self.__selectionChanged)
        self.model.itemChanged.connect(self.__itemChanged)

    def __updateTable(self, data):
        self.model.itemChanged.disconnect(self.__itemChanged)
        self.model.setRowCount(len(data))
        for row in range(len(data)):
            for col in range(len(data[row])):
                self.model.setItem(row, col, QStandardItem(data[row][col]))
        self.model.itemChanged.connect(self.__itemChanged)

    def __openFile(self, filename):
        try:
            self.__data = openFile(filename)
        except IOError:
            QMessageBox.critical(self, '错误', '文件打开失败。请稍后再试。')
        except ApiError:
            QMessageBox.critical(self, '错误', '文件格式错误。请检查文件完整性。')
        except Exception as e:
            QMessageBox.critical(self, '错误', '未知错误：' + str(e.with_traceback()))
        else:
            self.ui.searchEdit.clear()
            self.__key = ''
            self.__updateTable(self.__data)
            self.labStatus.setText(filename)
            self.setWindowTitle(self.version_str)
            self.__filename = filename

    def __saveFile(self, filename):
        try:
            saveFile(filename, self.__data)
        except IOError:
            QMessageBox.critical(self, '错误', '文件保存错误。请稍后再试。')
        except Exception as e:
            QMessageBox.critical(self, '错误', '未知错误：' + str(e.with_traceback()))
        else:
            self.labStatus.setText('保存成功：' + filename)
            self.setWindowTitle(self.version_str)
            self.__filename = filename

    @Slot()
    def on_actFile_New_triggered(self):
        self.__filename = self.__key = ''
        self.setWindowTitle(self.unsaved_tip + self.version_str)
        self.labStatus.setText('新文件')
        self.model.setRowCount(0)
        self.__data.clear()

    @Slot()
    def on_actFile_Open_triggered(self):
        filename, _ = QFileDialog.getOpenFileName(self, '打开', filter=self.SUPPORTED_FILTERS)
        if filename:
            self.__openFile(filename)

    @Slot()
    def on_actFile_Save_triggered(self):
        if self.__filename:
            self.__saveFile(self.__filename)
        else:
            filename, _ = QFileDialog.getSaveFileName(self, '保存', filter=self.SUPPORTED_FILTERS)
            if filename:
                self.__saveFile(filename)

    @Slot()
    def on_actFile_SaveAs_triggered(self):
        filename, _ = QFileDialog.getSaveFileName(self, '另存为', filter=self.SUPPORTED_FILTERS)
        if filename:
            self.__saveFile(filename)

    @Slot()
    def on_actHelp_About_triggered(self):
        dialog = QDialog(self)
        ui = Ui_dlgHelp()
        ui.setupUi(dialog)
        for link in (ui.githubLink, ui.giteeLink, ui.licenseLink, ui.readmeLink):
            link.clicked.connect(partial(open_new_tab, link.description()))
        ui.labVersion.setText('版本号：' + FULL_VERSION)
        ui.btnUpdate.clicked.connect(partial(open_new_tab, 'https://github.com/GoodCoder666/AccountBook/releases'))
        dialog.exec()

    @Slot()
    def on_actHelp_AboutQt_triggered(self):
        QMessageBox.aboutQt(self, '关于Qt')

    @Slot()
    def on_actEdit_Add_triggered(self):
        dialog = dlgAdd(self)
        if dialog.exec() == QDialog.Accepted:
            row = dialog.getRow()
            insort_right(self.__data, row)
            self.__updateTable(query(self.__data, self.__key))
            self.setWindowTitle(self.unsaved_tip + self.version_str)

    @Slot()
    def on_actEdit_Remove_triggered(self):
        rows = list(set(map(lambda idx: idx.row(), self.ui.table.selectedIndexes())))
        for row in rows:
            self.__data.remove([self.model.item(row, col).text() for col in range(self.model.columnCount())])
        self.model.itemChanged.disconnect(self.__itemChanged)
        self.model.removeRows(rows[0], len(rows))
        self.model.itemChanged.connect(self.__itemChanged)
        self.setWindowTitle(self.unsaved_tip + self.version_str)

    def __selectionChanged(self):
        self.ui.actEdit_Remove.setEnabled(self.ui.table.selectionModel().hasSelection())

    def __itemChanged(self, item: QStandardItem):
        i, j, new = item.row(), item.column(), item.text()
        if (old := self.__data[i][j]) == new: return
        if j == 0 and not QDate.fromString(new, 'yyyy/MM/dd').isValid():
            QMessageBox.critical(self, '错误', '日期格式错误。')
            self.model.itemChanged.disconnect(self.__itemChanged)
            item.setText(old)
            self.model.itemChanged.connect(self.__itemChanged)
            return
        row = self.__data.pop(i)
        row[j] = new
        insort_right(self.__data, row)
        self.__updateTable(query(self.__data, self.__key))
        self.setWindowTitle(self.unsaved_tip + self.version_str)

    @Slot()
    def on_searchEdit_textChanged(self):
        self.__key = self.ui.searchEdit.text()
        self.__updateTable(query(self.__data, self.__key))

    @Slot()
    def on_actStat_Show_triggered(self):
        if self.__data:
            dlgCharts(self.__data, self).exec()
        else:
            QMessageBox.information(self, '提示', '请添加数据以使用统计功能。')

    def closeEvent(self, event):
        if not self.windowTitle().startswith(self.unsaved_tip): return
        filename = basename(self.__filename) if self.__filename else '新文件'
        messageBox = QMessageBox(
            parent=self, icon=QMessageBox.Warning, windowTitle='提示',
            text=f'是否要保存对 {filename} 的更改？', informativeText='如果不保存，你的更改将丢失。',
            standardButtons=QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        messageBox.setButtonText(QMessageBox.Save, '保存')
        messageBox.setButtonText(QMessageBox.Discard, '不保存')
        messageBox.setButtonText(QMessageBox.Cancel, '取消')
        reply = messageBox.exec()
        if reply == QMessageBox.Save:
            self.on_actFile_Save_triggered()
            event.accept()
        elif reply == QMessageBox.Discard:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.__openFile(event.mimeData().text()[8:]) # [8:] is to get rid of 'file:///'

mainform = AccountBookMainWindow()
mainform.show()

sys.exit(app.exec())
