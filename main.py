import sys
from UGUI.GUI import *
from UEvent.savefile import *
from UEvent.selectfiledir import *
from PySide6.QtGui import QIcon,QImage,QPixmap
from UEvent.run import *
if __name__ == '__main__':
    ui.setWindowIcon(QPixmap('./logo.png'))
    ui.imageShowText.setScaledContents(True)
    ui.saveFileBtn.clicked.connect(selectOutputFileCB)
    ui.selectFileBtn.clicked.connect(selectDirCB)
    ui.runBtn.clicked.connect(runBtnCB)
    sys.exit(app.exec())
