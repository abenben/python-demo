# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def Var1():
    returns = [-0.01, -0.02, -0.01, 0.04, 0.02, 0.01, -0.03]
    mu = np.mean(returns)
    sigma = np.std(returns)
    valueAtRisk = norm.ppf(0.05, mu, sigma)
    print(valueAtRisk)

def Var2():
    returns = np.random.randn(1000)
    # one-way 5% quantile, critical value is 1.64
    VaR_21 = returns.std() * np.sqrt(21) * 1.645
    print(VaR_21)

def generate_random_index(n=21):
    # could set replace to False as well
    return np.random.choice(np.arange(1000), size=n, replace=False)

def Var3():
    returns = np.random.randn(1000)
    VaR_simulated_21 = []
    n_bootstrap = 10000
    for _ in range(n_bootstrap):
        VaR = returns[generate_random_index(21)].sum()
        VaR_simulated_21.append(VaR)

    v=np.percentile(VaR_simulated_21, q=5)
    print(v)
    plt.hist(VaR_simulated_21)
    plt.show()

if __name__ == '__main__':
    Var1()
    Var2()
    Var3()
    exit()
