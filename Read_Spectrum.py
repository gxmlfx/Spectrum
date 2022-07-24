# import fnmatch
import os
# from os.path import join, isdir
# import Draw_csv as DS
import numpy as np
from FilePaths import filepaths

# datas_path = os.getenv('XrfV2DataRoot') + r'temp\PhecdaHE\SpectrumFolder/'  # 读取环境变量里datas的位置

'''
datas_path = '/Users/gxmlfx/PhcdaHe/SpectrumFolder/'  # Unix目录

# mcas = glob.glob(datas_path + '*/*/*.csv')
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
        filepaths.append(mcafile) '''


def count_sp(paths):
    count_ULow = 0
    count_Low = 0
    count_LM = 0
    count_Mid = 0
    count_High = 0
    for h in paths:
        if '[超低能]' in h or '[ULow Energy]' in h:
            count_ULow += 1
        if '[低能]' in h or '[Low Energy]' in h:
            count_Low += 1
        if '[中低能]' in h or '[LM Energy]' in h:
            count_LM += 1
        if '[中能]' in h or '[Mid Energy]' in h:
            count_Mid += 1
        if '[高能]' in h or '[High Energy]' in h:
            count_High += 1
    return count_ULow, count_Low, count_LM, count_Mid, count_High


def readdata(paths, s, d):
    num_of_spec_seg = count_sp(paths)

    name_s = []
    i = 0
    if s == 0:
        count = num_of_spec_seg[0]
        str1 = '[超低能]'
        str2 = '[ULow Energy]'
        length = 1500
    elif s == 1:
        count = num_of_spec_seg[1]
        str1 = '[低能]'
        str2 = '[Low Energy]'
        length = 1500
    elif s == 2:
        count = num_of_spec_seg[2]
        str1 = '[中低能]'
        str2 = '[LM Energy]'
        length = 4000
    elif s == 3:
        count = num_of_spec_seg[3]
        str1 = '[中能]'
        str2 = '[Mid Energy]'
        length = 4000
    elif s == 4:
        count = num_of_spec_seg[4]
        str1 = '[高能]'
        str2 = '[High Energy]'
        if d == 0:  # Ketek
            length = 6000
        elif d == 1:  # Amptek
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


class Sample:
    def __init__(self, serial, energy_seg, currentfilepaths):
        self.name = readdata(currentfilepaths, energy_seg)[0][serial]
        self.en = readdata(currentfilepaths, energy_seg)[1][serial]
        self.sp = readdata(currentfilepaths, energy_seg)[2][serial]
        self.bg = readdata(currentfilepaths, energy_seg)[3][serial]
        self.net = readdata(currentfilepaths, energy_seg)[4][serial]


# 问题：目前会读取paths里的全部文件
class CurrentSamples:
    def __init__(self, paths, serial):
        names = find_names(paths)
        ulow = readdata(paths, 0)
        mid = readdata(paths, 1)
        high = readdata(paths, 2)
        serial_low = find_serial(names, ulow[0])
        serial_mid = find_serial(names, mid[0])
        serial_high = find_serial(names, high[0])
        self.name = names[serial]
        self.le = ulow[1][serial_low[serial]]
        self.ls = ulow[2][serial_low[serial]]
        self.lb = ulow[3][serial_low[serial]]
        self.ln = ulow[4][serial_low[serial]]

        self.me = mid[1][serial_mid[serial]]
        self.ms = mid[2][serial_mid[serial]]
        self.mb = mid[3][serial_mid[serial]]
        self.mn = mid[4][serial_mid[serial]]

        self.he = high[1][serial_high[serial]]
        self.hs = high[2][serial_high[serial]]
        self.hb = high[3][serial_high[serial]]
        self.hn = high[4][serial_high[serial]]


class CurrentSamples1:
    def __init__(self, names, seg, serial):
        self.name = names[serial]
        if seg[0] is not None:
            serial_ulow = find_serial(names, seg[0][0])
            self.ue = seg[0][1][serial_ulow[serial]]
            self.us = seg[0][2][serial_ulow[serial]]
            self.ub = seg[0][3][serial_ulow[serial]]
            self.un = seg[0][4][serial_ulow[serial]]
        if seg[1] is not None:
            serial_low = find_serial(names, seg[1][0])
            self.le = seg[1][1][serial_low[serial]]
            self.ls = seg[1][2][serial_low[serial]]
            self.lb = seg[1][3][serial_low[serial]]
            self.ln = seg[1][4][serial_low[serial]]
        if seg[2] is not None:
            serial_lm = find_serial(names, seg[2][0])
            self.lme = seg[2][1][serial_lm[serial]]
            self.lms = seg[2][2][serial_lm[serial]]
            self.lmb = seg[2][3][serial_lm[serial]]
            self.lmn = seg[2][4][serial_lm[serial]]
        if seg[3] is not None:
            serial_mid = find_serial(names, seg[3][0])
            self.me = seg[3][1][serial_mid[serial]]
            self.ms = seg[3][2][serial_mid[serial]]
            self.mb = seg[3][3][serial_mid[serial]]
            self.mn = seg[3][4][serial_mid[serial]]
        if seg[4] is not None:
            serial_high = find_serial(names, seg[4][0])
            self.he = seg[4][1][serial_high[serial]]
            self.hs = seg[4][2][serial_high[serial]]
            self.hb = seg[4][3][serial_high[serial]]
            self.hn = seg[4][4][serial_high[serial]]


# 根据中能段文件寻找同样品其他能段文件
def find_names(paths):
    mids = [xx for xx in paths if '中能' in xx or 'Mid Energy' in xx]
    temp_s = [os.path.basename(path) for path in mids]
    names = [temp[0:temp.find('[')] for temp in temp_s]
    return names


def find_other_seg(name, paths):
    name1 = [path1 for path1 in paths if path1.find(name) != -1]
    return name1


def find_serial(name, seg):
    serial = [seg.index(i) for i in name]
    return serial


# 将实例化的多个样品转换为画图函数需要的列表
def to_be_draw(serial_list, es):
    name = []
    serial_ue = []
    serial_us = []
    serial_le = []
    serial_ls = []
    serial_lme = []
    serial_lms = []
    serial_me = []
    serial_ms = []
    serial_he = []
    serial_hs = []
    for index, i in enumerate(serial_list):
        name.append(serial_list[index].name)
        serial_ue.append(serial_list[index].ue)
        serial_us.append(serial_list[index].us)
        serial_le.append(serial_list[index].le)
        serial_ls.append(serial_list[index].ls)
        serial_lme.append(serial_list[index].lme)
        serial_lms.append(serial_list[index].lms)
        serial_me.append(serial_list[index].me)
        serial_ms.append(serial_list[index].ms)
        serial_he.append(serial_list[index].he)
        serial_hs.append(serial_list[index].hs)
    sel_en = []
    sel_sp = []
    if es == 0:
        sel_en = serial_ue
        sel_sp = serial_us
    elif es == 1:
        sel_en = serial_le
        sel_sp = serial_ls
    elif es ==2:
        sel_en = serial_lme
        sel_sp = serial_lms
    elif es == 3:
        sel_en = serial_me
        sel_sp = serial_ms
    elif es == 4:
        sel_en = serial_he
        sel_sp = serial_hs
    return name, sel_en, sel_sp


if __name__ == "__main__":
    # ULow = readdata(filepaths, 0)
    # Mid = readdata(filepaths, 1)
    # High = readdata(filepaths, 2)
    # x = CurrentSamples(filepaths, 0)
    # y = CurrentSamples(filepaths, 1)
    # xy = [CurrentSamples(filepaths, serial) for serial in [0, 1]]
    # sp_l = to_be_draw(xy, 0)
    # DS.draw_spectrum('ULow', sp_l[0], sp_l[1], sp_l[2])
    paths = filepaths[21:]
    # x = find_serial(['GSS9', 'GSS5'], paths)
    # for index, i in enumerate(paths):
    #     if 'GSS9' in i:
    #
    #         print(index)

    NameList = ['GSS9', 'GSS5']
    paths1 = [paths[index] for name in NameList for index, i in enumerate(paths) if name in i]
    # paths1 = []
    # for name in NameList:
    #     for index , i in enumerate(paths):
    #         if name in i:
    #             paths1.append(paths[index])

    print('运行正常')
