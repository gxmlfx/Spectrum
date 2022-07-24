# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowSpec.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(592, 490)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listAPP = QListWidget(Form)
        self.listAPP.setObjectName(u"listAPP")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listAPP.sizePolicy().hasHeightForWidth())
        self.listAPP.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.listAPP)

        self.tableSpecSeg = QTableWidget(Form)
        if (self.tableSpecSeg.columnCount() < 3):
            self.tableSpecSeg.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableSpecSeg.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableSpecSeg.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableSpecSeg.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableSpecSeg.setObjectName(u"tableSpecSeg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableSpecSeg.sizePolicy().hasHeightForWidth())
        self.tableSpecSeg.setSizePolicy(sizePolicy1)
        self.tableSpecSeg.setRowCount(0)
        self.tableSpecSeg.setColumnCount(3)

        self.horizontalLayout_2.addWidget(self.tableSpecSeg)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.button_Select = QPushButton(Form)
        self.button_Select.setObjectName(u"button_Select")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_Select.sizePolicy().hasHeightForWidth())
        self.button_Select.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.button_Select)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_Draw = QPushButton(Form)
        self.button_Draw.setObjectName(u"button_Draw")
        sizePolicy2.setHeightForWidth(self.button_Draw.sizePolicy().hasHeightForWidth())
        self.button_Draw.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.button_Draw)

        self.button_Compare = QPushButton(Form)
        self.button_Compare.setObjectName(u"button_Compare")
        sizePolicy2.setHeightForWidth(self.button_Compare.sizePolicy().hasHeightForWidth())
        self.button_Compare.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.button_Compare)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableSpecSeg.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u8d85\u4f4e\u80fd", None));
        ___qtablewidgetitem1 = self.tableSpecSeg.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u4e2d\u80fd", None));
        ___qtablewidgetitem2 = self.tableSpecSeg.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u9ad8\u80fd", None));
        self.button_Select.setText(QCoreApplication.translate("Form", u"\u4ece\u6587\u4ef6\u9009\u62e9...", None))
        self.button_Draw.setText(QCoreApplication.translate("Form", u"\u7ed8\u5236\u8c31\u56fe", None))
        self.button_Compare.setText(QCoreApplication.translate("Form", u"\u76f8\u4f3c\u5ea6\u6bd4\u8f83", None))
    # retranslateUi

