from UGUI.GUI import *
import shutil
from pictool.ImageProcess import *
from PIL import Image,ImageQt
import threading
g_flag = 0
def perImageCB(sche,Pimagenow):
    global g_flag
    sche = int(sche * 100)
    try:
        ui.progressBar.setValue(int(sche))
        if (ui.previewCheckBox.isChecked()==True) or (sche == 99) :
            qimg = ImageQt.ImageQt(Pimagenow)
            qpixmap = QPixmap(qimg)
            ui.imageShowText.setPixmap(qpixmap)
    except:
        pass



def showImageCB(targetFilePath):
    shutil.copy(targetFilePath, ui.outputfilePathText.text())


def imageProcThread():
    filePath = ui.srcText.text() + '/'
    if ui.orderCBox.currentText()=='文件名增序':
        direct = 'LR'
    else:
        direct = 'RL'
    concatImageHorizontal(dirpath=filePath, direct=direct, perCb=perImageCB, showCB=showImageCB)
    ui.progressBar.setValue(int(100))


def runBtnCB():
    print("Here")
    imageThread = threading.Thread(target=imageProcThread)
    imageThread.start()
