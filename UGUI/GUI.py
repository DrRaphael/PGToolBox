import sys
from PySide6 import QtCore,QtWidgets,QtGui
from UGUI.home import *

class GUI(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None ):
        super(GUI,self).__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
ui = GUI()
ui.show()
