import numpy as np


def ChiSquareTest(a, b, c, d):
    N = a + b + c + d
    E11 = (a + c) * (a + b) / N
    E12 = (b + d) * (a + b) / N
    E21 = (a + c) * (c + d) / N
    E22 = (b + d) * (c + d) / N
    chi2 = (abs(a - E11) - 0.5)**2 / E11 + (abs(b - E12) - 0.5)**2 / E12 + (abs(c - E21) - 0.5)**2 / E21 + (abs(d - E22) - 0.5)**2 / E22
    return chi2


def FisherExactTest(a0, b0, c0, d0):
    times = a0 + c0
    Pr = [0 for i in range(times + 1)]
    Pr[0] = PrCalc(a0, b0, c0, d0)
    a = a0 + c0
    b = b0 - c0
    c = 0
    d = d0 + c0
    pSum = 0
    for i in range(1, times + 1):
        a -= 1
        b += 1
        c += 1
        d -= 1
        if a >= 0 and b >= 0 and c >= 0 and d >= 0:
            Pr[i] = PrCalc(a, b, c, d)
            if Pr[i] <= Pr[0]:
                pSum += Pr[i]
    return pSum


def PrCalc(a, b, c, d):
    N = a + b + c + d
    Pr = np.math.factorial(a + b) * np.math.factorial(c + d) * np.math.factorial(a + c) * np.math.factorial(b + d) / (np.math.factorial(a) * np.math.factorial(b) * np.math.factorial(c) * np.math.factorial(d) * np.math.factorial(N))
    return Pr


a, b, c, d = (input("请输入列联表各值：").split())
a = int(a)
b = int(b)
c = int(c)
d = int(d)

print('Chi-square test的检验统计量为：' + repr(ChiSquareTest(a, b, c, d)) + '\nFisher exact test的值为：' + repr(FisherExactTest(a, b, c, d)))
