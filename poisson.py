# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 12:39:42 2014

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

figsize(12.5, 4)

import scipy.stats as stats
a = np.arange(16)
poi = stats.poisson
lambda_ = [1.5, 4.25]
colours = ['#348ABD', '#A60628']

plt.bar(a, poi.pmf(a, lambda_[0]), color=colours[0],
        label="$\lambda$ = %.1f" % lambda_[0], alpha=0.60,edgecolor=colours[0], lw="3")
plt.bar(a, poi.pmf(a, lambda_[1]), color=colours[1],
        label="$\lambda$ = %.1f" % lambda_[1], alpha=0.60,edgecolor=colours[1], lw="3")


plt.xticks(a + 0.4, a)
plt.legend()
plt.ylabel("probability of $k$")
plt.xlabel("$k$")
plt.title("Probability mass function of a Poisson random variable; differing \
$\lambda$ values")















