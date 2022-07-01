from PySide6.QtWidgets import *
from PySide6.QtCore import QDate, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from ui_dlgAdd import Ui_Dialog

class dlgAdd(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.moneyEdit.setValidator(QRegularExpressionValidator(QRegularExpression(r'(\+|\-)[1-9]+[0-9]*')))
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText('确定')
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText('取消')
    
    def getRow(self):
        date = self.ui.dateEdit.text()
        event = self.ui.eventEdit.text()
        money = self.ui.moneyEdit.text()
        note = self.ui.noteEdit.text()
        return [date, event, money, note]

    def accept(self):
        if not self.ui.eventEdit.text():
            QMessageBox.critical(self, "错误", "事件不能为空，请重新填写。")
            return
        if self.ui.moneyEdit.text() in ('', '+', '-'):
            QMessageBox.critical(self, "错误", "金额不能为空，请重新填写。")
            return
        return super().accept()