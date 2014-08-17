# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 15:34:47 2014

@author: Koangel
"""

import pymc as pm

a = [1,2,3,4,5]
val = pm.Poisson("obs", 0.1, value=a, observed=True)
print val.value
val.random()
print val.value

val1 = pm.Poisson("obs1", 0.1)
print val1.value
val1.random()
print val1.value