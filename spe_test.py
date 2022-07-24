# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spe_test.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(967, 628)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.comboBoxAPP = QComboBox(self.groupBox)
        self.comboBoxAPP.addItem("")
        self.comboBoxAPP.setObjectName(u"comboBoxAPP")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxAPP.sizePolicy().hasHeightForWidth())
        self.comboBoxAPP.setSizePolicy(sizePolicy1)
        self.comboBoxAPP.setMinimumSize(QSize(100, 20))
        self.comboBoxAPP.setBaseSize(QSize(200, 100))
        self.comboBoxAPP.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout.addWidget(self.comboBoxAPP)

        self.comboBoxDate = QComboBox(self.groupBox)
        self.comboBoxDate.addItem("")
        self.comboBoxDate.setObjectName(u"comboBoxDate")
        sizePolicy1.setHeightForWidth(self.comboBoxDate.sizePolicy().hasHeightForWidth())
        self.comboBoxDate.setSizePolicy(sizePolicy1)
        self.comboBoxDate.setMinimumSize(QSize(120, 20))
        self.comboBoxDate.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout.addWidget(self.comboBoxDate)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.listSample = QListWidget(self.groupBox)
        self.listSample.setObjectName(u"listSample")
        self.listSample.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.listSample)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonX = QPushButton(self.groupBox)
        self.buttonX.setObjectName(u"buttonX")

        self.horizontalLayout_2.addWidget(self.buttonX)

        self.buttonY = QPushButton(self.groupBox)
        self.buttonY.setObjectName(u"buttonY")

        self.horizontalLayout_2.addWidget(self.buttonY)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.comboBoxDetector = QComboBox(self.groupBox)
        self.comboBoxDetector.addItem("")
        self.comboBoxDetector.addItem("")
        self.comboBoxDetector.setObjectName(u"comboBoxDetector")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBoxDetector.sizePolicy().hasHeightForWidth())
        self.comboBoxDetector.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.comboBoxDetector)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_Draw = QPushButton(self.groupBox)
        self.button_Draw.setObjectName(u"button_Draw")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.button_Draw.sizePolicy().hasHeightForWidth())
        self.button_Draw.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.button_Draw)

        self.button_Select = QPushButton(self.groupBox)
        self.button_Select.setObjectName(u"button_Select")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.button_Select.sizePolicy().hasHeightForWidth())
        self.button_Select.setSizePolicy(sizePolicy6)

        self.horizontalLayout_3.addWidget(self.button_Select)

        self.button_Compare = QPushButton(self.groupBox)
        self.button_Compare.setObjectName(u"button_Compare")
        sizePolicy5.setHeightForWidth(self.button_Compare.sizePolicy().hasHeightForWidth())
        self.button_Compare.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.button_Compare)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(3)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy7)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ButtonClear = QPushButton(self.groupBox_2)
        self.ButtonClear.setObjectName(u"ButtonClear")
        self.ButtonClear.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_5.addWidget(self.ButtonClear)

        self.ButtonCal = QPushButton(self.groupBox_2)
        self.ButtonCal.setObjectName(u"ButtonCal")
        self.ButtonCal.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.ButtonCal.sizePolicy().hasHeightForWidth())
        self.ButtonCal.setSizePolicy(sizePolicy5)
        self.ButtonCal.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_5.addWidget(self.ButtonCal)

        self.ButtonSaveData = QPushButton(self.groupBox_2)
        self.ButtonSaveData.setObjectName(u"ButtonSaveData")
        sizePolicy5.setHeightForWidth(self.ButtonSaveData.sizePolicy().hasHeightForWidth())
        self.ButtonSaveData.setSizePolicy(sizePolicy5)
        self.ButtonSaveData.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_5.addWidget(self.ButtonSaveData)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.tableCorrelation = QTableWidget(self.groupBox_2)
        if (self.tableCorrelation.columnCount() < 6):
            self.tableCorrelation.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCorrelation.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCorrelation.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCorrelation.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCorrelation.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCorrelation.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCorrelation.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableCorrelation.setObjectName(u"tableCorrelation")
        self.tableCorrelation.setSortingEnabled(False)

        self.gridLayout.addWidget(self.tableCorrelation, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 967, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XRF\u8c31\u56fe\u6570\u636e\u5206\u6790", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open ...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u548c\u9009\u62e9\u8c31\u56fe", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u5e94\u7528", None))
        self.comboBoxAPP.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))

        self.comboBoxDate.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6837\u54c1", None))
        self.buttonX.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u4e3aX", None))
        self.buttonY.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u4e3aY", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u6d4b\u5668", None))
        self.comboBoxDetector.setItemText(0, QCoreApplication.translate("MainWindow", u"Ketek", None))
        self.comboBoxDetector.setItemText(1, QCoreApplication.translate("MainWindow", u"Amptek", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a\u5f53\u524d\u4eea\u5668\u7684\u63a2\u6d4b\u5668\u540e\u8bf7\u52ff\u518d\u66f4\u6539\u8be5\u9009\u9879", None))
        self.button_Draw.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u8c31\u56fe", None))
        self.button_Select.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u6587\u4ef6\u9009\u62e9...", None))
        self.button_Compare.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u5ea6\u6bd4\u8f83", None))
#if QT_CONFIG(whatsthis)
        self.groupBox_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u533a\u57df", None))
        self.ButtonClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.ButtonCal.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.ButtonSaveData.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58...", None))
        ___qtablewidgetitem = self.tableCorrelation.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6837\u54c1\u540dA", None));
        ___qtablewidgetitem1 = self.tableCorrelation.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6837\u54c1\u540dB", None));
        ___qtablewidgetitem2 = self.tableCorrelation.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5cf0\u76f8\u4f3c\u5ea6 (Debug)", None));
        ___qtablewidgetitem3 = self.tableCorrelation.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u6563\u5c04\u5cf0\u76f8\u4f3c\u5ea6 (Debug)", None));
        ___qtablewidgetitem4 = self.tableCorrelation.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u4f3c\u5ea6", None));
        ___qtablewidgetitem5 = self.tableCorrelation.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

