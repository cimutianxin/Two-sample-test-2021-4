import numpy as np
import random


def wilcoxonRankSumTest2(a, b):
    n1 = sum(a)
    n2 = sum(b)
    R1 = 0
    R2 = 0
    combinedSample = [0 for i in range(len(a))]
    averageRank = [0 for i in range(len(a))]
    rank = [0 for i in range(len(a))]
    for i in range(len(a)):
        combinedSample[i] = a[i] + b[i]
        if i != 0:
            rank[i] = rank[i - 1] + combinedSample[i]
            averageRank[i] = (rank[i] + rank[i - 1]) / 2 + 0.5
        else:
            rank[i] = combinedSample[i]
            averageRank[i] = rank[i] / 2 + 0.5
        R1 += a[i] * averageRank[i]
        R2 += b[i] * averageRank[i]
    if (n1 < n2 or (n1 == n2 and R1 < R2)):
        if R1 != n1 * (n1 + n2 + 1) / 2:
            T = (abs(R1 - n1 * (n1 + n2 + 1) / 2) - 0.5) / ((n1 * n2 / 12) * (n1 + n2 + 1))**0.5
        else:
            T = 0
    if (n1 > n2 or (n1 == n2 and R1 > R2)):
        if R2 != n2 * (n1 + n2 + 1) / 2:
            T = (abs(R2 - n2 * (n1 + n2 + 1) / 2) - 0.5) / ((n1 * n2 / 12) * (n1 + n2 + 1))**0.5
        else:
            T = 0

    return T


def wilcoxonRankSumTest1(a, b):
    X = np.zeros((len(a) + len(b), 2))
    for i in range(len(a)):
        X[i, 0] = 1
        X[i, 1] = a[i]
    for j in range(len(b)):
        X[j + len(a), 0] = 2
        X[j + len(a), 1] = b[j]
    X = X[np.lexsort(X.T)]

    rangeOfRank = 1
    rankArray = []
    for i in range(1, len(X)):
        if X[i, 0] == X[i - 1, 0]:
            rangeOfRank += 1
        else:
            rankArray.append(rangeOfRank)
            rangeOfRank = 1
    rankArray.append(rangeOfRank)

    aNext = []
    bNext = []
    tick = True
    for i in range(len(rankArray)):
        if tick:
            aNext.append(rankArray[i])
            bNext.append(0)
        else:
            bNext.append(rankArray[i])
            aNext.append(0)
        tick = not tick

    return wilcoxonRankSumTest2(aNext, bNext)


def t_test(a, b):
    var_a = sum(a) / len(a)
    var_b = sum(b) / len(b)
    s_1_temp = 0
    s_2_temp = 0
    for i in range(len(a)):
        s_1_temp += (a[i] - var_a)**2
    for i in range(len(b)):
        s_2_temp += (b[i] - var_b)**2
    s_1Squared = s_1_temp / len(a)
    s_2Squared = s_2_temp / len(b)
    t = abs((var_a - var_b)) / ((((len(a) - 1) * s_1Squared + (len(a) - 1) * s_1Squared) / (len(a) + len(b) - 2)) * (1 / len(a) + 1 / len(b)))**0.5
    return t


# 输入数据
# a = list(map(int,input("A组:").split()))
# b = list(map(int,input("B组:").split()))

# 正态模拟
# simuZa = np.round(np.random.normal(10, 1, size=10), 3)
# simuZb = np.round(np.random.normal(10, 1, size=10), 3)

# x, y为列表类型数据
x = [15, 23, 21, 31, 22, 14, 18, 11, 21, 34]
y = [19, 12, 34, 16, 20, 10, 24, 23, 14, 13]

# 三个函数
# wilcoxonRankSumTest1(x, y)计算未经排序处理的数据
# wilcoxonRankSumTest2(x, y)计算经过排序处理的数据，比如课本例子
# t_test(x, y)
print(x, '\n', y, '\n')
print('wilcoxonRankSumTest', wilcoxonRankSumTest1(x, y), '\n')
print('t-test', t_test(x, y), '\n')
print('根据以上检验统计量需要再计算p值')
