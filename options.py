import math

#Black-Scholes model simulator

#inputs
S = 100 #Stock price
K = 100 #strike price
r = 0.05 #risk-free rate (%)
T = 1 #time to exp (year)
om = 0.2 #volatility

#deriv
d1 = (math.log(S/K) + (r + om**2 / 2) * T) / (om * math.sqrt(T))
d2 = d1 - om * math.sqrt(T)

def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

#calc
Call = round(S * N(d1) - K * math.exp(-r * T) * N(d2), 2)

#output
print("Call Price: $", Call)