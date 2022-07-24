# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_matplotlibwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MatplotlibWidget(object):
    def setupUi(self, MatplotlibWidget):
        if not MatplotlibWidget.objectName():
            MatplotlibWidget.setObjectName(u"MatplotlibWidget")
        MatplotlibWidget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(MatplotlibWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameMatplotlib = QFrame(MatplotlibWidget)
        self.frameMatplotlib.setObjectName(u"frameMatplotlib")
        self.frameMatplotlib.setFrameShape(QFrame.StyledPanel)
        self.frameMatplotlib.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frameMatplotlib)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnStart = QPushButton(MatplotlibWidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnStop = QPushButton(MatplotlibWidget)
        self.btnStop.setObjectName(u"btnStop")

        self.horizontalLayout.addWidget(self.btnStop)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MatplotlibWidget)

        QMetaObject.connectSlotsByName(MatplotlibWidget)
    # setupUi

    def retranslateUi(self, MatplotlibWidget):
        MatplotlibWidget.setWindowTitle(QCoreApplication.translate("MatplotlibWidget", u"MatplotlibWidget", None))
        self.btnStart.setText(QCoreApplication.translate("MatplotlibWidget", u"start", None))
        self.btnStop.setText(QCoreApplication.translate("MatplotlibWidget", u"stop", None))
    # retranslateUi
