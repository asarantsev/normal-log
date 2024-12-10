import numpy
from matplotlib import pyplot as plt

K = 100
Xaxis = numpy.log(numpy.array(range(1, K+1)))
NSIMS = 3
for sim in range(NSIMS):
    interJumpTimes = numpy.random.exponential(1, K)
    jumpTimes = numpy.log(numpy.cumsum(interJumpTimes))
    plt.plot(Xaxis, -jumpTimes)
plt.plot(Xaxis, -Xaxis, 'black', linestyle = 'dashed')
plt.xlabel('log ranks')
plt.ylabel('log weights')
plt.title('Upper Left End')
plt.show()

N = 500
Xaxis = numpy.log(numpy.array(range(N-K, N)))
for sim in range(NSIMS):
    interJumpTimes = numpy.random.exponential(1, K)
    jumpTimes = numpy.log(numpy.cumsum(interJumpTimes))
    plt.plot(Xaxis[::-1], jumpTimes)
Function = numpy.array([numpy.log(N-numpy.exp(k)) for k in Xaxis])
plt.plot(Xaxis, Function, 'black', linestyle = 'dashed')
plt.xlabel('log ranks')
plt.ylabel('log weights')
plt.title('Lower Right End')
plt.show()
    