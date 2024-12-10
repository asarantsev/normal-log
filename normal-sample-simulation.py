import numpy
from matplotlib import pyplot as plt

N = 100
NSIMS = 3
Xaxis = [numpy.log(k) for k in range(1, N+1)]
for sim in range(NSIMS):
    data = numpy.random.normal(0, 1, N)
    data = sorted(data, reverse = True)
    plt.plot(Xaxis, data)
plt.xlabel('Log Ranks')
plt.ylabel('Log Weights')
plt.show()
