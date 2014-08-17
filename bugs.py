# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 12:16:24 2014

@author: Koangel
"""

import json, matplotlib
s = json.load(open("styles/bmh_matplotlibrc.json"))
matplotlib.rcParams.update(s)

# The code below can be passed over, as it is currently not important, plus it
# uses advanced topics we have not covered yet. LOOK AT PICTURE, MICHAEL!
from IPython.core.pylabtools import figsize
from matplotlib import pyplot as plt

figsize(12.5, 4)
colours = ["#348ABD", "#A60628"]

prior = [0.20, 0.80]

posterior = [1./3, 2./3]

plt.bar([0, .7], prior, alpha=0.70, width=0.25,
        color=colours[0], label="prior distribution",
        lw="3", edgecolor=colours[0])

plt.bar([0 + 0.25, .7 + 0.25], posterior, alpha=0.7,
        width=0.25, color=colours[1],
        label="posterior distribution",
        lw="3", edgecolor=colours[1])
        
plt.xticks([0.20, .95], ["Bugs Absent", "Bugs Present"])
plt.title("Prior and Posterior probability of bugs present")
plt.ylabel("Probability")
plt.legend(loc="upper left");

















