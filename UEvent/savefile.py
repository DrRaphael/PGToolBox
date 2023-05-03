from UGUI.GUI import *
from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog

filedialog = QFileDialog(ui)



def selectOutputFileCB():
    result = filedialog.getSaveFileName(ui,"输出路径",filter='*.jpg')
    filepath = result[0]
    filed = (filepath[-4:])
    if filed != '.jpg':
        filepath = filepath + '.jpg'
    ui.outputfilePathText.setText(filepath)


