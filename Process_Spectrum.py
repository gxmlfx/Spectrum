from bisect import bisect

import matplotlib.pyplot as plt
import numpy as np

# from Read_Datas import Sample, count_ULow
from Read_Spectrum import filepaths
# from Read_Spectrum import Sample
import Read_Spectrum as RS


# import FilePaths as fps

# ULow = readdata(filepaths, 0)
# Mid = readdata(filepaths, 1)
# High = readdata(filepaths, 2)


# class Sample:
#     def __init__(self, serial, energy_seg):
#         if energy_seg == 0:
#             self.name = ULow[0][serial]
#             self.en = ULow[1][serial]
#             self.sp = ULow[2][serial]
#             self.bg = ULow[3][serial]
#             self.net = ULow[4][serial]
#         if energy_seg == 1:
#             self.name = Mid[0][serial]
#             self.en = Mid[1][serial]
#             self.sp = Mid[2][serial]
#             self.bg = Mid[3][serial]
#             self.net = Mid[4][serial]
#         if energy_seg == 2:
#             self.name = High[0][serial]
#             self.en = High[1][serial]
#             self.sp = High[2][serial]
#             self.bg = High[3][serial]
#             self.net = High[4][serial]


class Element:
    _ID = 0

    def __init__(self, element, ka, kb, la, lb):
        self.element = element
        self.ka = ka
        self.kb = kb
        self.la = la
        self.lb = lb
        self.id = self._ID
        self.__class__._ID += 1


Ca = Element('Ca', 3.691, 4.013, 0.341, 0.345)
Al = Element('Al', 1.487, 1.553, None, None)
# Si = Element('Si', 1.74, 1.829, None, None)
K = Element('K', 3.313, 3.590, None, None)
Ti = Element('Ti', 4.509, 4.932, 0.452, 0.458)
Fe = Element('Fe', 6.4, 7.058, 0.705, 0.718)
Zn = Element('Zn', 8.632, 9.572, 1.012, 1.035)
Ga = Element('Ga', 9.243, 10.265, 1.098, 1.125)
Sr = Element('Sr', 14.142, 15.837, 1.807, 1.872)
elements = [Ca.ka, Ti.ka, Fe.ka, Fe.kb, Zn.ka, Sr.ka]


# 查找并选取最高峰为基峰位置
# 查找元素位置附近的极值点作为计数率，返回的是计数率
def find_ele(sample, str1, ele=Ca.ka):
    str2 = str1[:-1] + 'n'
    original_location = bisect(sample[str1], ele)
    diff = np.mean(sample[str2][original_location -2:original_location +2])
    return diff


# 元素计数率与参考峰的比值
def ele_ratio(characteristic_ele, str1, sample, benchmark_ele=Ca.ka):
    benchmark = find_ele(sample, str1, benchmark_ele)
    characteristic = find_ele(sample, str1, characteristic_ele)
    ratio = benchmark/characteristic
    return ratio


# 将ele_ratio的比值数据整合为列表
def ratio_list(sample, str1, benchmark=Ca.ka):  # 改变benchmark即可改变基峰元素
    ration_list = [ele_ratio(i, str1, sample, benchmark) for index, i in enumerate(elements[1:])]
    return ration_list


# 计算相似度
def coffrelate(sample1, sample2):
    seg = ['ue', 'le', 'lme', 'me', 'he']
    co = [np.corrcoef(ratio_list(sample1, i), ratio_list(sample2, i))[0, 1]
          for index , i in enumerate(seg)
          if seg[index] in sample1 and seg[index] in sample2]
    co = list(map(float, co))
    co_sum = 0
    for i in co:
        h = float(i)
        co_sum += h * (h / sum(co))
    return '%.3f' % co_sum


from deriv import cal_deriv  # 计算离散点的导数


# 查找散射峰
def find_scatter(samples):
    sample_en = samples.me[1000:]
    sample_sp = samples.mb[1000:]
    return sample_en, sample_sp


# 计算散射峰相关系数
def cal_cof_of_scatter(sample1, sample2):
    cof_of_scatter = np.corrcoef(find_scatter(sample1)[1], find_scatter(sample2)[1])[0, 1]
    return '%.3f' % cof_of_scatter


if __name__ == "__main__":
    # jj = '中能段'
    # # x = coffrelate()
    # num_ele = len(elements)
    # num_sam = len(RS.Mid[0])
    # rm = np.zeros((num_ele - 1, num_sam))
    #
    # for index1, ele in enumerate(elements):
    #     for index2, sp in enumerate(RS.Mid[0]):
    #         rm[index1 - 1, index2] = ele_ratio(Ca.ka, ele, Sample(index2, 1).net)
    #
    # # plt.plot(Sample(0, 1).en, Sample(0, 1).sp, color='red')
    # # plt.plot(Sample(1, 1).en, Sample(1, 1).sp, color='blue')
    # pcc = [np.corrcoef(rm[:, i], rm[:, i + 1])[0, 1] for i in range(num_sam - 1)]
    x = RS.CurrentSamples(filepaths, 0)
    y = RS.CurrentSamples(filepaths, 1)
    x1 = RS.CurrentSamples(filepaths, 4)
    z = coffrelate(x, y)
    z1 = cal_cof_of_scatter(x, y)
