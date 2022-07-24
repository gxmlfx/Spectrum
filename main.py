from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import os
import sys
# import fnmatch
# import Read_Datas as RD
import Read_Spectrum as RS
import Draw_csv as dc
import FilePaths as fps


class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        qfile_stats = QFile('ui/spe.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()
        self.ui = QUiLoader().load('ui/spe.ui')
        self.ui.button_Select.clicked.connect(self.open_filedialog)
        self.ui.list_App.addItems(fps.apps)
        self.ui.button_Draw.clicked.connect(self.draw)
        self.ui.list_App.itemClicked.connect(self.get_list_item)

    # def show_corr(self):


    def draw(self):
        selected_low = []
        selected_mid = []
        selected_high = []
        # sp_l = self.ui.list_Low.selectedItems()
        selected_low = [i.text() for i in self.ui.list_Low.selectedItems()]
        # for i in self.ui.list_Low.selectedItems():
        #     selected_low.append(i.text())
        serial_low = RS.find_serial(selected_low, 0)
        sp_l = RS.to_be_draw(serial_low, 0)

        for j in self.ui.list_Mid.selectedItems():
            selected_mid.append(j.text())
        serial_mid = RS.find_serial(selected_mid, 1)
        sp_m = RS.to_be_draw(serial_mid, 1)

        for k in self.ui.list_High.selectedItems():
            selected_high.append(k.text())
        serial_high = RS.find_serial(selected_high, 2)
        sp_h = RS.to_be_draw(serial_high, 2)
        if sp_l[1].size > 0:
            dc.draw_spectrum('超低能段', sp_l[0], sp_l[1], sp_l[2])
        if sp_m[1].size > 0:
            dc.draw_spectrum('中能段', sp_m[0], sp_m[1], sp_m[2])
        if sp_h[1].size > 0:
            dc.draw_spectrum('高能段', sp_h[0], sp_h[1], sp_h[2])
        # y = self.ui.list_Mid.selectedItems()

    def get_list_item(self):
        selected = self.ui.list_App.selectedItems()[0].text()
        # print(selected)
        filepaths = []
        for mcafile in fps.findfiles(fps.datas_path + '/' + selected, '*.csv'):
            filepaths.append(mcafile)
        if not filepaths:
            self.ui.list_Name.clear()
            self.ui.list_Low.clear()
            self.ui.list_Mid.clear()
            self.ui.list_High.clear()
        else:
            self.ui.list_Name.clear()
            self.ui.list_Name.addItems(filepaths)
            self.ui.list_Low.clear()
            self.ui.list_Low.addItems(RS.readdata(filepaths, 0)[0])
            self.ui.list_Mid.clear()
            self.ui.list_Mid.addItems(RS.readdata(filepaths, 1)[0])
            self.ui.list_High.clear()
            self.ui.list_High.addItems(RS.readdata(filepaths, 2)[0])

    def open_filedialog(self):
        fname, _ = QFileDialog.getOpenFileNames(self.ui, '选择谱图', os.getcwd(), "CSV文件(*.csv);;All Files(*)")
        # self.ui.list_Low.addItem(fname)
        print(fname)
        self.ui.list_Name.clear()
        self.ui.list_Name.addItems(fname)
        # self.ui.list_Name.addItems(filepaths)


app = QApplication([])
stats = Stats()
stats.ui.show()
sys.exit(app.exec())
