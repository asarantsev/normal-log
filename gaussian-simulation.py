import numpy
from matplotlib import pyplot as plt

N = 100000
step = 0.005
sim = numpy.random.normal(0, 1, N)
mvalues = numpy.arange(step, 1.5, step)
svalues = numpy.arange(step, 2, step)
mresult = []
sresult = []
for m in mvalues:
    for s in svalues:
        if numpy.mean(numpy.log(abs(m + s * sim))) < 0:
            mresult.append(m)
            sresult.append(s)

plt.plot(mresult, sresult, 'go')
plt.xlabel('Mean')
plt.ylabel('Stdev')
plt.show()
    
