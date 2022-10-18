import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from opcio_arazas import Option

K=360
expiry='20121215'
C=Option('C',K, expiry,1)
P=Option('P',K, expiry,-1)

S=3455
t=0.23
vola=0.3

#print(C.calcPrice(S,t,vola)+P.calcPrice(S,t,vola) - S)
#C-P=S-K put call paritas

spots = range(250,500,5)
prices = [C.calcPrice(s,1,vola) for s in spots]
pays = [C.calcPayoff(s) for s in spots]

plt.plot(spots,pays,spots,prices)
plt.show()