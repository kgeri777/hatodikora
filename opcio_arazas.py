import numpy as np
from scipy.stats import norm

class Option:
    def __init__(self, right:str, strike:float, expiry:str, pos:int):
        #call or put
        self.right = right
        self.pos = pos
        self.strike = strike
        self.expiry = expiry
        self.vola = np.nan

    def calcPrice(self, S: float, timeToExp: float, vola: float, rate=0):
        if not np.isnan(vola):
            IV = vola
        else:
            IV = self.vola if not np.isnan(self.vola) else self.initVola
        if np.isnan(IV):
            print("Vola is not set!")
            return np.nan
        t = timeToExp
        if t > 0:
            d1 = (np.log(S / self.strike) + (rate + IV ** 2 / 2) * t) / (IV * np.sqrt(t))
            d2 = d1 - IV * np.sqrt(t)
            if self.right == 'C':
                return (S * norm.cdf(d1) - norm.cdf(d2) * self.strike * np.exp(-rate * t)) * self.pos
            else:
                return (norm.cdf(-d2) * self.strike * np.exp(-rate * t) - S * norm.cdf(-d1)) * self.pos
        elif t == 0:
            return self.calcPayoff(S)
        else:
            print("expired!")
            return np.nan


    def calcVola(self,S, time, price, rate=0):
        vola_hi=0.3
        while self.calcPrice(self, S, time, vola_hi, rate=0) < price:
            vola_hi *= 2
        vola_low = vola_hi / 2
        while abs(vola_hi - vola_low) > 0.0001:
            vola = 0.5 * (vola_low + vola_hi)
            price_updated = self.calcPrice(S,time,vola,rate)
            if price_updated < price:
                vola_low = vola
            else:
                vola_hi = vola
        return vola





    def initVola(self):
        self.vola = 0.2


    def calcPayoff(self,spot:float):
        if self.right == 'C':
            return max(spot-self.strike,0)*self.pos
        elif self.right == 'P':
            return max(self.strike-spot, 0) * self.pos
        else:
            print('Wrong option type')
            return None

    def calcDelta(self, S, timeToExp, vola, rate=0):
        if not np.isnan(vola):
            IV = vola
        else:
            IV = self.vola if not np.isnan(self.vola) else self.initVola
        if np.isnan(IV):
            print("Vola is not set!")
            return np.nan
        t = timeToExp
        if t > 0:
            d1 = (np.log(S / self.strike) + (rate + IV ** 2 / 2) * t) / (IV * np.sqrt(t))
            if self.right == 'C':
                return norm.cdf(d1) * self.pos
            else:
                return (norm.cdf(d1) - 1) * self.pos
        else:
            print("expired!")
            return np.nan








opt = Option('C',100,'20121202',1)
print(opt.calcPrice(110,0.5,0.3,0.04))