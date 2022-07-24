import tkinter as tk
from tkinter import filedialog
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

from matplotlib.font_manager import FontProperties

# 实例化
root = tk.Tk()
root.withdraw()
# 获取文件夹路径
# filepaths = filedialog.askopenfilenames(title='请选择一个或多个谱图', initialdir=os.getenv(
#     'XrfV2DataRoot') + r'\\temp\\PhecdaHE\\SpectrumFolder\\纸张',
#                                         filetypes=[('CSV谱图', '.csv'), ('MCA谱图', '.mca, kmca'), ('All Files', '*')])
filepaths = filedialog.askopenfilenames(title='请选择一个或多个谱图',
                                        filetypes=[('CSV谱图', '.csv'), ('MCA谱图', '.mca, kmca'), ('All Files', '*')])
# filepaths = 'D:/PHECDA-zhijianDatasV2/temp/PhecdaHE/SpectrumFolder/纸张/2022-06-09/'
count_ULow = 0
count_Mid = 0
count_High = 0
for h in filepaths:
    if '[超低能]' in h:
        count_ULow += 1
    if '[中能]' in h:
        count_Mid += 1
    if '[高能]' in h:
        count_High += 1

i = 0
j = 0
k = 0
files = []
Spectrum_Low = np.zeros((count_ULow, 1500))
Energy_Low = np.zeros((count_ULow, 1500))
BG_Low = np.zeros((count_ULow, 1500))
NET_Low = np.zeros((count_ULow, 1500))
Spectrum_Mid = np.zeros((count_Mid, 4000))
Energy_Mid = np.zeros((count_Mid, 4000))
BG_Mid = np.zeros((count_Mid, 4000))
NET_Mid = np.zeros((count_Mid, 4000))
Spectrum_High = np.zeros((count_High, 4000))
Energy_High = np.zeros((count_High, 4000))
BG_High = np.zeros((count_High, 4000))
NET_High = np.zeros((count_High, 4000))
Name = []
for filepath in filepaths:
    with open(filepath, encoding='utf-8') as file_x:
        data = np.loadtxt(file_x, str, skiprows=11, delimiter=",").astype(float)

        if '[超低能]' in filepath:
            temp = os.path.basename(filepath).replace('[超低能]', '')
            temp = temp.replace('.csv', '')
            Name.append(temp)
            Energy_Low[i, ...] = data[0:, 1]
            Spectrum_Low[i, ...] = data[0:, 3]
            BG_Low[i, ...] = data[0:, 4]
            NET_Low[i, ...] = data[0:, 5]
            i += 1
        if '[中能]' in filepath:
            temp = os.path.basename(filepath).replace('[中能]', '')
            temp = temp.replace('.csv', '')
            # Name.append(temp)
            # Name.replace()
            Energy_Mid[j, ...] = data[0:, 1]
            Spectrum_Mid[j, ...] = data[0:, 3]
            BG_Mid[j, ...] = data[0:, 4]
            NET_Mid[j, ...] = data[0:, 5]
            j += 1
        # elif '[中能]' not in filepath:
        #     Energy_Mid[j, ...] = data[0:, 1]
        #     Spectrum_Mid[j, ...] = data[0:, 3]
        #     BG_Mid[j, ...] = data[0:, 4]
        #     NET_Mid[j, ...] = data[0:, 5]

        if '[高能]' in filepath:
            temp = os.path.basename(filepath).replace('[高能]', '')
            temp = temp.replace('.csv', '')
            # Name.append(temp)
            Energy_High[k, ...] = data[0:, 1]
            Spectrum_High[k, ...] = data[0:, 3]
            BG_High[k, ...] = data[0:, 4]
            NET_High[k, ...] = data[0:, 5]
            k += 1


# for h in filepaths:
#     if '[高能]' in h:
#         if Energy_High[0, 4001] is 0:
#             Spectrum_High = Spectrum_High[:, 0:4000]
#             BG_High = BG_High[:, 0:4000]
#             Energy_High = Energy_High[:, 0:4000]
#             NET_High = NET_High[:, 0:4000]


class Sample:

    def __init__(self, serial):
        self.name = Name[serial]
        if count_ULow > 0:
            self.sl = Spectrum_Low[serial, :]
            self.bl = BG_Low[serial, :]
            self.nl = NET_Low[serial, :]
            self.el = Energy_Low[serial, :]
        if count_Mid > 0:
            self.sm = Spectrum_Mid[serial, :]
            self.nm = NET_Mid[serial, :]
            self.bm = BG_Mid[serial, :]
            self.em = Energy_Mid[serial, :]
        if count_High > 0:
            self.sh = Spectrum_High[serial, :]
            self.bh = BG_High[serial, :]
            self.nh = NET_High[serial, :]
            self.eh = Energy_High[serial, :]


colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化
if count_ULow > 0:
    fig1 = plt.figure()
    plt.title('超低能', fontsize=25)
    for i in range(len(BG_Low)):
        # font = FontProperties(fname="SimHei.ttf", size=14)  # 设置字体
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.plot(Energy_Low[i], NET_Low[i], label=str(i)+'#纸样品')  # , color=mcolors.TABLEAU_COLORS[colors[i]]
        temp_l = i
    plt.legend(['1#样品', '2#样品', '3#样品', '4#样品'], prop={"size":20})
    plt.xlabel('Energy(keV)')
    plt.ylabel('Count(cps)')
    plt.show()
# label = str(step * (i + 1) * tau)[:3]
if count_Mid > 0:
    fig2 = plt.figure()
    plt.title('中能', fontsize=25)
    for i in range(len(BG_Mid)):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.plot(Energy_Mid[i], NET_Mid[i],
                 label=str(i)+'#纸样品')  # , color=mcolors.TABLEAU_COLORS[colors[i]]
    plt.legend(['1#样品', '2#样品', '3#样品', '4#样品'], prop={"size":20})
    plt.xlabel('Energy(keV)')
    plt.ylabel('Count(cps)')
    plt.show()

if count_High > 0:
    fig3 = plt.figure()
    plt.title('高能', fontsize=25)
    for i in range(len(BG_High)):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.plot(Energy_High[i], NET_High[i],
                 label=str(i)+'#纸样品')  # , color=mcolors.TABLEAU_COLORS[colors[i]]
    plt.legend(['1#样品', '2#样品', '3#样品', '4#样品'], prop={"size":20})
    plt.xlabel('Energy(keV)')
    plt.ylabel('Count(cps)')
    plt.show()
