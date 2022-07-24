import tkinter as tk
from tkinter import filedialog
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import pandas as pd
import platform
from matplotlib.font_manager import FontProperties

# 实例化
root = tk.Tk()
root.withdraw()
SYSTEM_PLATFORM = platform.system()
if SYSTEM_PLATFORM == 'Darwin' or "Linux":
    filepaths = filedialog.askopenfilenames(title='请选择一个或多个谱图',
                                            filetypes=[('All Files', '*')])
elif SYSTEM_PLATFORM == 'windows':
    filepaths = filedialog.askopenfilenames(title='请选择一个或多个谱图',
                                            initialdir=os.getenv('XrfV2DataRoot') +
                                                       r'\\temp\\PhecdaHE\\SpectrumFolder\\纸张',
                                            filetypes=[('All Files', '*')])
count_ULow = 0
count_Low = 0
count_Mid = 0
count_High = 0
count_LM = 0
for h in filepaths:
    if '[超低能]' in h or '[ULow Energy]' in h:
        count_ULow += 1
    if '[低能]' in h or '[Low Energy]' in h:
        count_Low += 1
    if '[中能]' in h or '[Mid Energy]' in h:
        count_Mid += 1
    if '[高能]' in h or '[High Energy]' in h:
        count_High += 1
    if '[中低能]' in h or '[LM Energy]' in h:
        count_LM += 1

i = 0
j = 0
k = 0
lm = 0
ul = 0
files = []
Spectrum_ULow = np.zeros((count_ULow, 1500))
Spectrum_Low = np.zeros((count_Low, 1500))
Spectrum_LM = np.zeros((count_LM, 4000))
Spectrum_Mid = np.zeros((count_Mid, 4000))
Spectrum_High = np.zeros((count_High, 6000))
Name_L = []
Name_M = []
Name_H = []
Name_UL = []
Name_LM = []
for filepath in filepaths:
    with open(filepath, encoding='utf-8') as file_x:
        data = pd.read_csv(filepath, delimiter=',')
        if '[超低能]' in filepath or '[ULow Energy]' in filepath:
            data2 = np.asarray(data.iloc[11:1511, :]).T
            temp_UL = os.path.basename(filepath)
            temp_UL = temp_UL[0:temp_UL.find('[')]
            Name_UL.append(temp_UL)
            Spectrum_ULow[ul] = data2
            ul += 1
        if '[低能]' in filepath or '[Low Energy]' in filepath:
            data1 = np.asarray(data.iloc[11:1511, :]).T
            temp_L = os.path.basename(filepath)
            temp_L = temp_L[0:temp_L.find('[')]
            Name_L.append(temp_L)
            Spectrum_Low[i] = data1
            i += 1
        if '[中低能]' in filepath or '[LM Energy]' in filepath:
            data5 = np.asarray(data.iloc[11:4011, :]).T
            temp_LM = os.path.basename(filepath)
            temp_LM = temp_LM[0:temp_LM.find('[')]
            Name_LM.append(temp_LM)
            Spectrum_LM[i] = data5
            i += 1

        if '[中能]' in filepath or '[Mid Energy]' in filepath:
            data2 = np.asarray(data.iloc[11:4011, :]).T
            temp_M = os.path.basename(filepath)
            temp_M = temp_M[0:temp_M.find('[')]
            # temp = temp.replace('.csv', '')
            Name_M.append(temp_M)
            Spectrum_Mid[j] = data2
            j += 1
        if '[高能]' in filepath or '[High Energy]' in filepath:
            data3 = np.asarray(data.iloc[11:6011, :]).T
            if 4000 < np.shape(data3)[1] < 6000:
                data4 = data3[:, 0:4000]
                Spectrum_High = Spectrum_High[:, 0:4000]
                Spectrum_High[k] = data4
            else:
                Spectrum_High[k] = data3
            temp_H = os.path.basename(filepath)
            temp_H = temp_H[0:temp_H.find('[')]
            Name_H.append(temp_H)
            k += 1


class Sample:

    def __init__(self, serial):
        self.name = Name_L[serial]
        if count_ULow > 0:
            self.ul = Spectrum_ULow[serial, :]
        if count_Low > 0:
            self.l = Spectrum_Low[serial, :]
        if count_Mid > 0:
            self.m = Spectrum_Mid[serial, :]
        if count_High > 0:
            self.h = Spectrum_High[serial, :]
        if count_LM > 0:
            self.lm = Spectrum_LM[serial, :]


colors = list(mcolors.TABLEAU_COLORS.keys())  # 颜色变化


def draw_spectrum(title, spectrum, name):
    fig = plt.figure(title)
    plt.title(title, fontsize=18)
    for i in range(len(name)):
        # plt.rcParams['font.sans-serif'] = ['Songti']  # 用来正常显示中文标签
        # plt.rcParams['font.sans-serif']=['Helvetica'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.plot(spectrum[i])  # , color=mcolors.TABLEAU_COLORS[colors[i]]
        plt.legend(name, prop={"size": 10})
    plt.xlabel('Energy(keV)')
    plt.ylabel('Count(cps)')
    plt.show()


if count_ULow > 0:
    draw_spectrum('超低能', Spectrum_ULow, Name_UL)
if count_Low > 0:
    draw_spectrum('低能', Spectrum_Low, Name_L)
if count_LM > 0:
    draw_spectrum('中低能', Spectrum_LM, Name_UL)
if count_Mid > 0:
    draw_spectrum('中能', Spectrum_Mid, Name_M)
if count_High > 0:
    draw_spectrum('高能', Spectrum_High, Name_H)
