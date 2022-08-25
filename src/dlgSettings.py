from PySide6.QtWidgets import *
from PySide6.QtCore import Slot
from ui_dlgSettings import Ui_Dialog

class dlgSettings(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText('确定')
        self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText('取消')
        self.btnApply = self.ui.buttonBox.button(QDialogButtonBox.Apply)
        self.btnApply.setText('应用')
        self.btnApply.clicked.connect(self.apply_changes)
        self.ui.comboBox_style.addItems(QStyleFactory.keys())
    
    @Slot(int)
    def on_comboBox_style_currentIndexChanged(self, idx: int):
        self.btnApply.setEnabled(True)

    def accept(self):
        self.apply_changes()
        super().accept()
    
    def apply_changes(self):
        self.btnApply.setEnabled(False)
        style = self.ui.comboBox_style.currentText()
        QApplication.instance().setStyle(style)