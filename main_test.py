import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QTableWidgetItem

# import Process_Spectrum
from spe_test import Ui_MainWindow
# import fnmatch
# import Read_Datas as RD

import Read_Spectrum as RS
import Draw_csv as dc
import FilePaths as fps
from Read_Spectrum import CurrentSamples, CurrentSamples1
import Process_Spectrum as PS


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.Xs = []
        self.Ys = []
        self.xrow = []
        self.count = None
        self.data = None
        self.selected_samples = None
        self.names = None
        self.High = None
        self.Mid = None
        self.LM = None
        self.Low = None
        self.ULow = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initui()
        self.filepaths = []
        self.paths = []

    def initui(self):
        self.ui.button_Select.clicked.connect(self.open_filedialog)
        # self.ui.comboBoxAPP.resize(20, 10)
        self.ui.comboBoxAPP.addItems(fps.apps)
        self.ui.button_Draw.clicked.connect(self.draw)
        self.ui.comboBoxAPP.currentIndexChanged.connect(self.get_list_item)
        self.ui.comboBoxDate.currentIndexChanged.connect(self.get_blew_date)
        self.ui.button_Compare.clicked.connect(self.show_corr)
        self.ui.ButtonClear.clicked.connect(self.clear_list)
        # self.ui.listSample.clicked.connect(self.get_path)
        self.ui.comboBoxDetector.currentIndexChanged.connect(self.change_detector)
        # self.ui.comboBoxDetector.textActivated[str].connect(self.read)
        self.ui.ButtonSaveData.clicked.connect(self.save_data)
        self.ui.buttonX.clicked.connect(self.add_sample)
        self.ui.buttonY.clicked.connect(self.add_sample_y)
        self.ui.ButtonCal.clicked.connect(self.cal_table)

    # 显示相关系数
    def show_corr(self):
        selected_items = [i.text() for i in self.ui.listSample.selectedItems()]
        serials = RS.find_serial(selected_items, self.names)
        self.selected_samples = [CurrentSamples1(self.names, self.data, serial) for serial in serials]
        self.s_dict = vars(self.selected_samples[0])
        self.s_dict1 = vars(self.selected_samples[1])
        # s = [self.s_dict, self.s_dict1]
        # CurrentSamples这个类会读取当前日期下的所有谱图
        # self.selected_samples = [CurrentSamples(self.filepaths, serial) for serial in serials]
        # 特征峰相似度ps (peaks similarity
        ps = PS.coffrelate(self.s_dict, self.s_dict1)
        # ps = PS.coffrelate(self.count, self.selected_samples[0], self.selected_samples[1])
        # 散射峰相似度sim_of_scatter
        sim_of_scatter = PS.cal_cof_of_scatter(self.selected_samples[0], self.selected_samples[1])
        rowcount = self.ui.tableCorrelation.rowCount()
        self.ui.tableCorrelation.insertRow(rowcount)
        self.ui.tableCorrelation.setItem(rowcount, 0, QTableWidgetItem(self.selected_samples[0].name))
        self.ui.tableCorrelation.setItem(rowcount, 1, QTableWidgetItem(self.selected_samples[1].name))
        self.ui.tableCorrelation.setItem(rowcount, 2, QTableWidgetItem(str(ps)))
        # self.ui.tableCorrelation.setItem(rowcount, 3, QTableWidgetItem(str(ps[1])))
        # self.ui.tableCorrelation.setItem(rowcount, 4, QTableWidgetItem(str(ps[2])))
        self.ui.tableCorrelation.setItem(rowcount, 3, QTableWidgetItem(str(sim_of_scatter)))

    # 画出谱图
    def draw(self):
        selected_items = [i.text() for i in self.ui.listSample.selectedItems()]
        serials = RS.find_serial(selected_items, self.names)
        self.selected_samples = [CurrentSamples1(self.names, self.data, serial) for serial in serials]

        # self.selected_samples = [CurrentSamples(self.filepaths, serial) for serial in serials]
        sp_l = RS.to_be_draw(self.selected_samples, 0)
        sp_m = RS.to_be_draw(self.selected_samples, 1)
        sp_h = RS.to_be_draw(self.selected_samples, 2)
        # 谱图能段多了以后需要加一个判断语句
        dc.draw_spectrum('超低能段', sp_l[0], sp_l[1], sp_l[2])
        dc.draw_spectrum('中能段', sp_m[0], sp_m[1], sp_m[2])
        dc.draw_spectrum('高能段', sp_h[0], sp_h[1], sp_h[2])

        # y = self.ui.list_Mid.selectedItems()

    # 得到不同日期下的谱图
    def get_blew_date(self):
        self.selected_app = self.ui.comboBoxAPP.currentText()
        self.selected_date = self.ui.comboBoxDate.currentText()
        self.filepaths = [mcafile for mcafile in fps.findfiles(fps.datas_path
                                                               + '/'
                                                               + self.selected_app
                                                               + '/'
                                                               + self.selected_date, '*.csv')]
        self.names = RS.find_names(self.filepaths)
        if not self.names:
            self.ui.listSample.clear()
        else:
            self.ui.listSample.clear()
            self.ui.listSample.addItems(self.names)
        self.data = self.read()

    def read(self):
        if self.ui.comboBoxDetector.currentText() == 'Amptek':
            d = 1
            # print('Amptek')
        else:
            d = 0
            # print('Ketek')
        self.count = list(RS.count_sp(self.filepaths))  # 当前应用拥有的能段
        if self.count[0] > 0:
            self.ULow = RS.readdata(self.filepaths, 0, d)
        else:
            self.ULow = None
        if self.count[1] > 0:
            self.Low = RS.readdata(self.filepaths, 1, d)
        else:
            self.Low = None
        if self.count[2] > 0:
            self.LM = RS.readdata(self.filepaths, 2, d)
        else:
            self.LM = None
        if self.count[3] > 0:
            self.Mid = RS.readdata(self.filepaths, 3, d)
        else:
            self.Mid = None
        if self.count[4] > 0:
            self.High = RS.readdata(self.filepaths, 4, d)
        else:
            self.High = None
        # print(self.count)
        return self.ULow, self.Low, self.LM, self.Mid, self.High

    # 得到不同应用下的日期，传递给日期选择框
    def get_list_item(self):
        selected_app = self.ui.comboBoxAPP.currentText()
        # print(selected_app)
        datepaths = fps.lookupfiles(selected_app)
        if not datepaths:
            self.ui.comboBoxDate.clear()
        else:
            self.ui.comboBoxDate.clear()
            self.ui.comboBoxDate.addItems(datepaths)

    # 手动打开文件选择框选择谱图
    def open_filedialog(self):
        fname, _ = QFileDialog.getOpenFileNames(self, "CSV文件(*.csv);;All Files(*)")
        print(fname)
        # self.ui.list_Name.clear()
        # self.ui.list_Name.addItems(fname)

    # 清除右侧输出table
    def clear_list(self):
        rowCount = self.ui.tableCorrelation.rowCount()
        k = rowCount - 1
        for i in range(rowCount):
            self.ui.tableCorrelation.removeRow(k)
            k -= 1

    # 选择探测器
    def change_detector(self):
        print('Changed')

    def add_sample(self):
        selected_items = [i.text() for i in self.ui.listSample.selectedItems()]
        for SampleX in selected_items:
            rowcount = self.ui.tableCorrelation.rowCount()

            self.ui.tableCorrelation.insertRow(rowcount)
            self.ui.tableCorrelation.setItem(rowcount, 0, QTableWidgetItem(str(SampleX)))
            self.xrow.append(rowcount)
        # b = []
        # for i in range(self.ui.tableCorrelation.rowCount()):
        #     a = self.ui.tableCorrelation.item(i, 0).text()
        #     b.append(a)
        #     if not a:
        #         break
        serials = RS.find_serial(selected_items, self.names)
        for serial in serials:
            self.Xs.append(CurrentSamples1(self.names, self.data, serial))

    def add_sample_y(self):
        selected_items = [i.text() for i in self.ui.listSample.selectedItems()]
        if not self.ui.tableCorrelation.item(0, 1):
            for i in range(len(selected_items)):
                self.ui.tableCorrelation.setItem(i, 1, QTableWidgetItem(str(selected_items[i])))
        else:
            b = []
            for i in range(self.ui.tableCorrelation.rowCount()):
                item = self.ui.tableCorrelation.item(i, 1)
                if not item:
                    break
                else:
                    a = item.text()
                    b.append(a)
            for i in range(len(selected_items)):
                self.ui.tableCorrelation.setItem(len(b) + i, 1, QTableWidgetItem(selected_items[i]))
        serials = RS.find_serial(selected_items, self.names)
        for serial in serials:
            self.Ys.append(CurrentSamples1(self.names, self.data, serial))
        # self.Ys = [CurrentSamples1(self.names, self.data, serial) for serial in serials]
        # self.Ys.append(self.selected_samples)

    def cal_table(self):
        xs_dict = [vars(x) for x in self.Xs]
        ys_dict = [vars(y) for y in self.Ys]
        ps = [PS.coffrelate(xs_dict[i], ys_dict[i]) for i in range(len(xs_dict))]
        if not self.ui.tableCorrelation.item(0, 2):
            for i in range(len(ps)):
                self.ui.tableCorrelation.setItem(i, 2, QTableWidgetItem(str(ps[i])))
        else:
            b = []
            for i in range(self.ui.tableCorrelation.rowCount()):
                item = self.ui.tableCorrelation.item(i, 2)
                if not item:
                    break
                else:
                    a = item.text()
                    b.append(a)
            for i in range(len(ps)):
                self.ui.tableCorrelation.setItem(len(b) + i, 2, QTableWidgetItem(ps[i]))
    # 保存文件
    def save_data(self):
        print('test')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec())
