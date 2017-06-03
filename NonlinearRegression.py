import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
from math import e

def bc(x, Bu, Rm, Lamda):
    return Bu*e**(-1*e**((Rm*e*(Lamda-x)/Bu)+1))

class Nonlinear_Regression():

    def __init__(self, datafile, formula):
        self.data = pd.read_csv(datafile,'\t',header=-1)
        self.formula = formula

    def fit(self, initial=(73,4,1), iter=1000):
        popt, pcov = curve_fit(self.formula, self.data[0], self.data[1], p0=(73,4,1), maxfev=iter)
        print(popt)
        print(pcov)

    def show(self):
        plt.plot(np.linspace(0,30,500),self.formula(np.linspace(0,30,500),*popt))
        plt.scatter(self.data[0],self.data[1],color='b') 
        plt.show()

if __name__ == '__main__':
    a=Nonlinear_Regression('data_table.txt', bc)
    a.fit()
    a.show()
'''
data_table.txt
1	24.19884963
2	42.89235826
3	55.66967954
4	66.06409203
5	80.03286771
6	95.43960559
7	115.1602301
8	135.4971241
9	151.1503698
10	166.1873459
11	177.7321282
12	188.0032868
13	195.2752671
14	200.7395234
15	205.2177486
16	207.9704191
17	210.1889893
18	212.7362366
19	213.7633525
20	216.2284306
21	218.200493
22	219.2276089
23	220.4190633
24	221.6516023
25	221.9391947
26	222.1857025
27	223.3771569
28	224.7740345
29	224.8972884
'''
