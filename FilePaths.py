import fnmatch
import os
from os.path import join, isdir

# datas_path = os.getenv('XrfV2DataRoot') + r'temp\PhecdaHE\SpectrumFolder/'  # 读取环境变量里datas的位置
datas_path = '/Users/gxmlfx/PhcdaHe/SpectrumFolder/'  # Unix目录
# mcas = glob.glob(datas_path + '*/*/*.csv')
apps = [apps for apps in os.listdir(datas_path) if isdir(join(datas_path, apps))]
# apps = []
# for temp in os.listdir(datas_path):
#     if isdir(join(datas_path, temp)):
#         apps.append(temp)


# 先查找日期，进而通过日期查找文件
def lookupfiles(app):
    for root, dirs, files in os.walk(datas_path + app):
        for dir in dirs:
            yield dir


# 通过扩展名查找文件
def findfiles(path, extensions):
    for root, dirs, file_names in os.walk(path):
        for file in fnmatch.filter(file_names, extensions):
            yield os.path.join(root, file)


# 查找所有谱图文件并将目录保存进filepaths
filepaths = []
for subdir in apps:
    # print(subdir)
    # filepaths = [mcafile for mcafile in findfiles(datas_path + subdir, '*.csv')]
    for mcafile in findfiles(datas_path + subdir, '*.csv'):
        filepaths.append(mcafile)
