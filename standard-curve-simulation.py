import numpy
from matplotlib import pyplot as plt

K = 100
Xaxis = [numpy.log(k) for k in range(1, K+1)]
NSIMS = 3
for sim in range(NSIMS):
    interJumpTimes = numpy.random.exponential(1, K)
    jumpTimes = -numpy.log(numpy.cumsum(interJumpTimes))
    plt.plot(Xaxis, jumpTimes)
plt.show()