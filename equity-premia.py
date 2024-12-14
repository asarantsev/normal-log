import numpy
import pandas
from matplotlib import pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from statsmodels.graphics.tsaplots import plot_acf

def plots(series):
    qqplot(series, line = 's')
    plt.show()
    plot_acf(series)
    plt.show()
    plot_acf(abs(series))
    plt.show()

data = pandas.read_excel('data.xlsx', sheet_name = 'data')
vix = data.values[:, 1]
returns = data.values[:, 2]
rates = data.values[:, 3]
premia = returns - rates/12
npremia = premia/vix
plots(premia)
plots(npremia)


