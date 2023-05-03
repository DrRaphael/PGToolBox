# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1069, 711)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.imageShowText = QLabel(self.frame_3)
        self.imageShowText.setObjectName(u"imageShowText")
        self.imageShowText.setMinimumSize(QSize(800, 600))

        self.horizontalLayout_2.addWidget(self.imageShowText)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.selectFileBtn = QPushButton(self.frame_4)
        self.selectFileBtn.setObjectName(u"selectFileBtn")
        self.selectFileBtn.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.selectFileBtn, 0, 3, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.outputfilePathText = QLineEdit(self.frame_4)
        self.outputfilePathText.setObjectName(u"outputfilePathText")

        self.gridLayout.addWidget(self.outputfilePathText, 1, 2, 1, 1)

        self.orderCBox = QComboBox(self.frame_4)
        self.orderCBox.addItem("")
        self.orderCBox.addItem("")
        self.orderCBox.addItem("")
        self.orderCBox.addItem("")
        self.orderCBox.setObjectName(u"orderCBox")

        self.gridLayout.addWidget(self.orderCBox, 2, 2, 1, 1)

        self.srcText = QLineEdit(self.frame_4)
        self.srcText.setObjectName(u"srcText")

        self.gridLayout.addWidget(self.srcText, 0, 2, 1, 1)

        self.runBtn = QPushButton(self.frame_4)
        self.runBtn.setObjectName(u"runBtn")

        self.gridLayout.addWidget(self.runBtn, 6, 0, 1, 4)

        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 3, 2, 1, 1)

        self.saveFileBtn = QPushButton(self.frame_4)
        self.saveFileBtn.setObjectName(u"saveFileBtn")
        self.saveFileBtn.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.saveFileBtn, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.previewCheckBox = QCheckBox(self.frame_4)
        self.previewCheckBox.setObjectName(u"previewCheckBox")
        self.previewCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.previewCheckBox, 4, 0, 1, 4)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.orderCBox)
        self.label_5.setBuddy(self.srcText)
        self.label_3.setBuddy(self.comboBox_2)
        self.label.setBuddy(self.srcText)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PGToolBox", None))
        self.imageShowText.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6392\u5e8f\u65b9\u5f0f\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u8def\u5f84\uff1a", None))
        self.selectFileBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u62fc\u63a5\u65b9\u5411\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.orderCBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d\u589e\u5e8f", None))
        self.orderCBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d\u964d\u5e8f", None))
        self.orderCBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u589e\u5e8f", None))
        self.orderCBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u964d\u5e8f", None))

        self.runBtn.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6c34\u5e73", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5782\u76f4", None))

        self.saveFileBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.previewCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u9884\u89c8(\u4f1a\u635f\u5931\u6027\u80fd\uff09", None))
    # retranslateUi

