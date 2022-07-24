# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spe.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_rootWindw(object):
    def setupUi(self, rootWindw):
        if not rootWindw.objectName():
            rootWindw.setObjectName(u"rootWindw")
        rootWindw.resize(575, 490)
        self.verticalLayout_7 = QVBoxLayout(rootWindw)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_3.setSpacing(-1)
#endif
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(rootWindw)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_4)

        self.list_App = QListWidget(rootWindw)
        self.list_App.setObjectName(u"list_App")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.list_App.sizePolicy().hasHeightForWidth())
        self.list_App.setSizePolicy(sizePolicy1)
        self.list_App.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_5.addWidget(self.list_App)

        self.verticalLayout_5.setStretch(0, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(rootWindw)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.label_5)

        self.list_Name = QListWidget(rootWindw)
        self.list_Name.setObjectName(u"list_Name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.list_Name.sizePolicy().hasHeightForWidth())
        self.list_Name.setSizePolicy(sizePolicy3)
        self.list_Name.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_6.addWidget(self.list_Name)

        self.verticalLayout_6.setStretch(0, 2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.line = QFrame(rootWindw)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(rootWindw)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.list_Low = QListWidget(rootWindw)
        self.list_Low.setObjectName(u"list_Low")
        self.list_Low.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.list_Low)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_2 = QFrame(rootWindw)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(rootWindw)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.list_Mid = QListWidget(rootWindw)
        self.list_Mid.setObjectName(u"list_Mid")
        self.list_Mid.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.list_Mid)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line_3 = QFrame(rootWindw)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(rootWindw)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.list_High = QListWidget(rootWindw)
        self.list_High.setObjectName(u"list_High")
        self.list_High.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_3.addWidget(self.list_High)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_Select = QPushButton(rootWindw)
        self.button_Select.setObjectName(u"button_Select")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_Select.sizePolicy().hasHeightForWidth())
        self.button_Select.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.button_Select)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_Draw = QPushButton(rootWindw)
        self.button_Draw.setObjectName(u"button_Draw")
        sizePolicy4.setHeightForWidth(self.button_Draw.sizePolicy().hasHeightForWidth())
        self.button_Draw.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.button_Draw)

        self.button_Compare = QPushButton(rootWindw)
        self.button_Compare.setObjectName(u"button_Compare")
        sizePolicy4.setHeightForWidth(self.button_Compare.sizePolicy().hasHeightForWidth())
        self.button_Compare.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.button_Compare)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)


        self.retranslateUi(rootWindw)

        QMetaObject.connectSlotsByName(rootWindw)
    # setupUi

    def retranslateUi(self, rootWindw):
        rootWindw.setWindowTitle(QCoreApplication.translate("rootWindw", u"\u9009\u62e9\u9700\u8981\u7684\u8c31\u56fe", None))
        self.label_4.setText(QCoreApplication.translate("rootWindw", u"\u8bf7\u9009\u62e9\u5e94\u7528", None))
        self.label_5.setText(QCoreApplication.translate("rootWindw", u"\u8c31\u56fe\u6587\u4ef6\u540d", None))
        self.label.setText(QCoreApplication.translate("rootWindw", u"\u4f4e\u80fd\u6bb5", None))
        self.label_2.setText(QCoreApplication.translate("rootWindw", u"\u4e2d\u80fd\u6bb5", None))
        self.label_3.setText(QCoreApplication.translate("rootWindw", u"\u9ad8\u80fd\u6bb5", None))
        self.button_Select.setText(QCoreApplication.translate("rootWindw", u"\u4ece\u6587\u4ef6\u9009\u62e9...", None))
        self.button_Draw.setText(QCoreApplication.translate("rootWindw", u"\u7ed8\u5236\u8c31\u56fe", None))
        self.button_Compare.setText(QCoreApplication.translate("rootWindw", u"\u76f8\u4f3c\u5ea6\u6bd4\u8f83", None))
    # retranslateUi

