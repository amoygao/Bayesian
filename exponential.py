# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 13:20:01 2014

@author: Koangel
"""

import json, matplotlib
s = json.load(open("styles/bmh_matplotlibrc.json"))
matplotlib.rcParams.update(s)

# The code below can be passed over, as it is currently not important, plus it
# uses advanced topics we have not covered yet. LOOK AT PICTURE, MICHAEL!
from IPython.core.pylabtools import figsize
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

figsize(12.5, 4)

a = np.linspace(0, 4, 100)
lambdas = [0.5, 1]
colours = ['#348ABD', '#A60628']

expo = stats.expon

for l, c in zip(lambdas, colours):
    plt.plot(a, expo.pdf(a, scale=1./l), lw=3,color=c, label="$\lambda=%.1f$" % l)
    plt.fill_between(a, 0, expo.pdf(a, scale=1.0/l), color=c, alpha=.33)
    
plt.legend()
plt.ylabel("PDF at $z$")
plt.xlabel("$z$")
plt.ylim(0, 1.2)
plt.title("Probability density function of an Exponential random variable;\
 differing $\lambda$")



















