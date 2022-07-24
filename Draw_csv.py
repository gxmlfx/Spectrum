import matplotlib.pyplot as plt
from Read_Spectrum import to_be_draw

plt.rcParams["font.family"] = 'Songti SC'


def draw_spectrum(title, name, en, sp):
    plt.figure(title)
    plt.title(title, fontsize=18)
    for i in range(len(name)):
        # plt.figure(i)
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.plot(en[i], sp[i])  # , color=mcolors.TABLEAU_COLORS[colors[i]]
        plt.legend(name, prop={"size": 10})
    plt.xlabel('Energy(keV)')
    plt.ylabel('Count(cps)')
    plt.show()


# draw_spectrum('test', RD.get_data(RD.filepaths, 0), RD.get_data(RD.filepaths, 0)[0])
if __name__ == "__main__":
    x = to_be_draw([1, 2, 3, 4], 1)
    draw_spectrum('test', x[0], x[1], x[2])
