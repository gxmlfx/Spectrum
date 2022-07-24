import fnmatch
import os
import numpy as np
import glob
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd
from os.path import isfile, join, isdir

# datas_path = os.getenv('XrfV2DataRoot') + r'temp\PhecdaHE\SpectrumFolder/'  # 读取环境变量里datas的位置


datas_path = '/Users/gxmlfx/PhcdaHe/SpectrumFolder/'  # Unix目录

mcas = glob.glob(datas_path + '*/*/*.csv')
apps = [apps for apps in os.listdir(datas_path) if isdir(join(datas_path, apps))]


# 通过扩展名查找文件
def findfiles(path, extensions):
    for root, dirs, file_names in os.walk(path):
        for file in fnmatch.filter(file_names, extensions):
            yield os.path.join(root, file)


# 查找所有谱图文件并将目录保存进filepaths
filepaths = []
for subdir in os.listdir(datas_path):
    # print(subdir)
    for mcafile in findfiles(datas_path + subdir, '*.csv'):
        filepaths.append(mcafile)


def readdata(paths, count):
    name_s = []
    i = 0
    if count == count_ULow:
        str1 = '[超低能]'
        str2 = '[ULow Energy]'
        length = 1500
    elif count == count_Mid:
        str1 = '[中能]'
        str2 = '[Mid Energy]'
        length = 4000
    elif count == count_High:
        str1 = '[高能]'
        str2 = '[High ENergy]'
        length = 4000

    spectrum_s = np.zeros((count, length))
    energy_s = np.zeros((count, length))
    bg_s = np.zeros((count, length))
    net_s = np.zeros((count, length))
    for filepath in paths:
        with open(filepath, encoding='utf-8') as file_x:
            data = np.loadtxt(file_x, str, skiprows=11, delimiter=",").astype(float)
            if str1 in filepath or str2 in filepath:
                temp_s = os.path.basename(filepath)
                temp_s = temp_s[0:temp_s.find('[')]
                name_s.append(temp_s)
                energy_s[i, ...] = data[0:, 1]
                spectrum_s[i, ...] = data[0:, 3]
                bg_s[i, ...] = data[0:, 4]
                net_s[i, ...] = data[0:, 5]
                i += 1
    return name_s, energy_s, spectrum_s, bg_s, net_s


# 计数有几个低中高能谱

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


def count_sp(paths):
    count_ULow = 0
    count_Mid = 0
    count_High = 0
    for h in paths:
        if '[超低能]' in h:
            count_ULow += 1
        if '[中能]' in h:
            count_Mid += 1
        if '[高能]' in h:
            count_High += 1
    return count_ULow, count_Mid, count_High


def get_data(paths, s):
    spec = readdata(paths, count_sp(paths)[s])
    return spec


ULow = get_data(filepaths, 0)
Mid = readdata(filepaths, count_Mid)
High = readdata(filepaths, count_High)

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
Name_L = []
Name_M = []
Name_H = []
for filepath in filepaths:
    with open(filepath, encoding='utf-8') as file_x:
        data = np.loadtxt(file_x, str, skiprows=11, delimiter=",").astype(float)
        # data1 = pd.read_csv(filepath, delimiter=',',error_bad_lines = False)
        # name = [row.split()[1] for row in file_x]
        if '[超低能]' in filepath:
            temp_L = os.path.basename(filepath)
            temp_L = temp_L[0:temp_L.find('[')]
            Name_L.append(temp_L)
            Energy_Low[i, ...] = data[0:, 1]
            Spectrum_Low[i, ...] = data[0:, 3]
            BG_Low[i, ...] = data[0:, 4]
            NET_Low[i, ...] = data[0:, 5]
            i += 1
        if '[中能]' in filepath:
            temp_M = os.path.basename(filepath)
            temp_M = temp_M[0:temp_M.find('[')]
            Name_M.append(temp_M)
            # Name.replace()
            # Name = [temp]
            Energy_Mid[j, ...] = data[0:, 1]
            Spectrum_Mid[j, ...] = data[0:, 3]
            BG_Mid[j, ...] = data[0:, 4]
            NET_Mid[j, ...] = data[0:, 5]
            j += 1
        if '[高能]' in filepath:
            temp_H = os.path.basename(filepath)
            temp_H = temp_H[0:temp_H.find('[')]
            Name_H.append(temp_H)
            Energy_High[k, ...] = data[0:, 1]
            Spectrum_High[k, ...] = data[0:, 3]
            BG_High[k, ...] = data[0:, 4]
            NET_High[k, ...] = data[0:, 5]
            k += 1


class Sample:
    _ID = 0

    def __init__(self, serial):
        self.name = Name_M[serial]
        self.sl = Spectrum_Low[serial, :]
        self.sm = Spectrum_Mid[serial, :]
        self.sh = Spectrum_High[serial, :]
        self.bl = BG_Low[serial, :]
        self.bm = BG_Mid[serial, :]
        self.bh = BG_High[serial, :]
        self.nl = NET_Low[serial, :]
        self.nm = NET_Mid[serial, :]
        self.nh = NET_High[serial, :]
        self.el = Energy_Low[serial, :]
        self.em = Energy_Mid[serial, :]
        self.eh = Energy_High[serial, :]
        self.id = self._ID
        self.__class__._ID += 1

    @property
    def ID(self):
        return self._ID
