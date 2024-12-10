import numpy
import pandas
from matplotlib import pyplot as plt

DF = pandas.read_excel('size-break-points.xlsx')
values = numpy.array(DF.values[:, 2:-1].astype(float))
xaxis = numpy.log(numpy.arange(1, 20, 1))
for k in numpy.arange(0, 1188, 60):
    data = numpy.log(values[k, ::-1]/sum(values[k]))
    plt.plot(xaxis, data, label = 'End of year '+str(1925+int(k/12)))
plt.legend(loc = 'lower left')
plt.xlabel('log ranks')
plt.ylabel('log weights')
plt.show()