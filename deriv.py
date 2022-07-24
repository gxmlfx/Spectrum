# 计算离散点导数
def cal_deriv(x, y):  # x, y的类型均为列表

    # x列表两数之差
    diff_x = [j - i for i, j in zip(x[0::], x[1::])]
    diff_y = [j - i for i, j in zip(y[0::], y[1::])]
    # slopes = []  # 用来存储斜率
    slopes = [diff_y[i] / diff_x[i] for i in range(len(diff_y))]
    # 用来存储一阶导数，根据离散点导数的定义，计算并存储结果
    deriv = [(0.5 * (i + j)) for i, j in zip(slopes[0::], slopes[1::])]
    deriv.insert(0, slopes[0])  # (左)端点的导数即为与其最近点的斜率
    deriv.append(slopes[-1])  # (右)端点的导数即为与其最近点的斜率
    return deriv  # 返回存储一阶导数结果的列表


if __name__ == "__main__":
    x = [1 / 60, 1 / 30, 1 / 20, 1 / 15, 1 / 12, 1 / 10, 7 / 60, 2 / 15, 3 / 20, 1 / 6, 11 / 60]
    y = [99.8014, 99.80255, 99.80633, 99.81218, 99.82422, 99.83488, 99.85151, 99.87169, 99.89393, 99.91125, 99.92673]
    z = cal_deriv(x, y)
    print(z)
