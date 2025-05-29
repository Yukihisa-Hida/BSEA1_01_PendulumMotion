import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math as math
import matplotlib.patches as patches

#フォント設定
plt.rcParams['font.family'] = 'Times New Roman' # font familyの設定
#plt.rcParams['mathtext.fontset'] = 'stix' # math fontの設定
plt.rcParams["font.size"] = 10 # 全体のフォントサイズが変更されます。
#plt.rcParams['xtick.labelsize'] = 9 # 軸だけ変更されます。
#plt.rcParams['ytick.labelsize'] = 24 # 軸だけ変更されます


#軸設定
plt.rcParams['xtick.direction'] = 'in' #x軸の目盛りの向き
plt.rcParams['ytick.direction'] = 'in' #y軸の目盛りの向き
#plt.rcParams['axes.grid'] = True # グリッドの作成
#plt.rcParams['grid.linestyle']='--' #グリッドの線種
plt.rcParams["xtick.minor.visible"] = True  #x軸補助目盛りの追加
plt.rcParams["ytick.minor.visible"] = True  #y軸補助目盛りの追加
#plt.rcParams['xtick.top'] = True  #x軸の上部目盛り
#plt.rcParams['ytick.right'] = True  #y軸の右部目盛り


#軸大きさ
#plt.rcParams["xtick.major.width"] = 1.0             #x軸主目盛り線の線幅
#plt.rcParams["ytick.major.width"] = 1.0             #y軸主目盛り線の線幅
#plt.rcParams["xtick.minor.width"] = 1.0             #x軸補助目盛り線の線幅
#plt.rcParams["ytick.minor.width"] = 1.0             #y軸補助目盛り線の線幅
#plt.rcParams["xtick.major.size"] = 10               #x軸主目盛り線の長さ
#plt.rcParams["ytick.major.size"] = 10               #y軸主目盛り線の長さ
#plt.rcParams["xtick.minor.size"] = 5                #x軸補助目盛り線の長さ
#plt.rcParams["ytick.minor.size"] = 5                #y軸補助目盛り線の長さ
#plt.rcParams["axes.linewidth"] = 1.0                #囲みの太さ


#凡例設定
plt.rcParams["legend.fancybox"] = False  # 丸角OFF
plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = 'black'  # edgeの色を変更
plt.rcParams["legend.markerscale"] = 5 #markerサイズの倍率
# plt.rcParams['lines.linewidth'] = 0
# plt.rcParams['lines.linestyle'] = ''
# plt.rcParams['lines.marker'] = '.'

input_csv = pd.read_csv('./45cm.csv', header=None)    #********使用するcsvファイルの指定********

cut_pre = 90
cut_post = 0

length = len(input_csv[0]) - 1 - cut_pre - cut_post

time = np.arange(0, length * 25, 25)

str_distance = input_csv[2].values.tolist()
str_distance.pop(0)
del str_distance[:cut_pre]

distance = list(map(int, str_distance))

def toRadian(dist):
    return (360 * dist / 1023 - 128.8) / 180 * math.pi

radian = list(map(toRadian, distance))

# print(degree)


plt.figure(dpi=300)

plt.xlim(0, 12000)     #********x軸の範囲(最小値,最大値)********
plt.ylim(-2, 2)    #********y軸の範囲(最小値,最大値)********

plt.plot(time, radian, marker=".", linestyle="None", markerfacecolor='black', markeredgewidth=0)
plt.xlabel("t / ms")     #********x軸ラベルの指定********
plt.ylabel("$\\theta$ / rad")     #********y軸ラベルの指定********
#plt.legend()


# t = []
# for i in range(2400):
#     t.append(i * 5)


# def getTheta(t):
#     T = 1.3 - math.log((t + 1)) / 40
#     A = 91
#     gamma = 0.11
#     omega = 2 * math.pi / T
#     phi = 0

#     return A * math.exp(-gamma * t / 1000) * math.cos(omega * t / 1000 + phi)

# theta = list(map(getTheta, t))

# plt.plot(t, theta, linestyle='-', color="black", marker="None")

plt.show()