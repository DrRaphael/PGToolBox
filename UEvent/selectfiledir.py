from UGUI.GUI import *
from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog
fd = QFileDialog(ui)

def selectDirCB():
    print("here")
    result = fd.getExistingDirectory(ui,"路径")
    filepath = result
    if filepath !="":
        ui.srcText.setText(filepath)
    print(filepath)


