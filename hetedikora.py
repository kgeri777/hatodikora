import numpy as np
import matplotlib.pyplot as plt
class GBrown:

    def __init__(self):
        pass
    def generate(self, S_0 , mu, sigma, T, N):
        dt = T/N
        X = np.exp(((mu - sigma**2/2) * dt) + sigma * np.random.normal(0,np.sqrt(dt), N))
        return S_0 * np.cumprod(X)

gb = GBrown()
sigma = 0.35
N = 250
S_0 = 100
spots = gb.generate(S_0, 0 ,sigma, 1, N)
times= np.arange(0, 1, 1/N)
plt.plot(times, spots)
plt.show()

from opcio_arazas import Option
opt=Option("C",S_0,None,1)
vola= 0.35
prices=[]
deltas=[]
for (t,S) in zip(times,spots):
    price=opt.calcPrice(S,1-t,vola)
    delta = opt.calcDelta(S, 1 - t, vola)
    prices.append(price)
    deltas.append(delta)

plt.plot(times,np.array(prices))
plt.show()



