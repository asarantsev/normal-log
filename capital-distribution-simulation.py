import numpy
from matplotlib import pyplot as plt

T = 400
N = 100

def curve(rho, slope):
    g = 0.062
    s = 0.202
    data = numpy.random.multivariate_normal([0, g], [[1, -rho*s], [-rho*s, s**2]], T)
    Y = data[:, 0]
    Z = data[:, 1]
    nu = 0.6573
    Gamma = numpy.random.gamma(shape = 1/nu, scale = nu, size = T)
    lnv = [3]
    for t in range(T-1):
        lnv.append(lnv[t] * 0.882 + 0.346 - 0.0621 + 0.0621*Gamma[t] + 0.1392*numpy.sqrt(Gamma[t])*Y[t])
    VIX = numpy.exp(lnv)
    Returns = VIX*Z
    record = []
    for k in range(N):
        eps = numpy.random.normal(0, 1, T)
        C = [0]
        for t in range(T):
            C.append((1 - slope*Returns[t])*C[t] + VIX[t]*eps[t])
        record.append(C[-1])
    record = sorted(record, reverse = True)
    return record

logs = numpy.array([numpy.log(k) for k in range(1, N+1)])
plt.plot(logs, curve(0, 0.1), label = 'slope 0.1, correlation 0%')
plt.plot(logs, curve(0.5, 0.1), label = 'slope 0.1, correlation -50%')
plt.plot(logs, curve(0, 0.2), label = 'slope 0.2, correlation 0%')
plt.plot(logs, curve(0.5, 0.2), label = 'slope 0.2, correlation -50%')
plt.legend(loc = 'lower left')
plt.show()