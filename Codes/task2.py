def McNemarTest(b, c):
    chi2 = (abs(b - c) - 1)**2 / (b + c)
    return chi2


a, b, c, d = (input("请输入列联表各值：").split())
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print('McNemar test的检验统计量为：' + repr(McNemarTest(b, c)))
