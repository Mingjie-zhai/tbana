#!/usr/bin/env python
"""
Calculate relative branching fraction of jpsi->invi over jpsi->mumu
"""

__author__ = "XIAO Suyu <xiaosuyu@ihep.ac.cn>"
__copyright__ = "Copyright (c) XIAO Suyu"
__created__ = "[2018-04-13 Fri 11:14]"

import math
import sys

reso = 0.0
resoEr = 0.0

def get_res(a, b, c, d, e, f):
    res1 = math.sqrt(abs(a**2+b**2-c**2)/2) 
    res2 = math.sqrt(abs(a**2-b**2+c**2)/2) 
    res3 = math.sqrt(abs(b**2-a**2+c**2)/2)
    resEr1 = (math.sqrt((a*d)**2+(b*e)**2+(c*f)**2)) / (2*res1)
    resEr2 = (math.sqrt((a*d)**2+(b*e)**2+(c*f)**2)) / (2*res2)
    resEr3 = (math.sqrt((a*d)**2+(b*e)**2+(c*f)**2)) / (2*res3)
    return res1, res2, res3, resEr1, resEr2, resEr3

# res = get_res(6.03005e-11, 9.54508e-11, 1.10125e-10, 5.74520e-14, 9.00079e-14, 1.00500e-13)

# SE5 SE2-02 SE2-01 
# 20C, 150V
# res = get_res(1.10120e-10, 1.07057e-10, 1.08146e-10, 1.38148e-13, 1.37527e-13,1.29084e-13)
# 20C, 200V
# res = get_res(6.17021e-11, 6.03942e-11, 5.94620e-11, 5.32129e-14, 5.91733e-14, 4.13572e-14)
# 0C, 150V
# res = get_res(8.18048e-11, 8.52622e-11, 8.95913e-11, 7.52901e-14, 4.73842e-14, 1.09924e-13)
# 0C, 200V
# res = get_res(4.84067e-11, 4.52844e-11, 4.64841e-11, 3.89708e-14, 6.12455e-14, 3.93447e-14)
# m30C, 150V
# res = get_res(5.28124e-11, 5.59428e-11, 5.48010e-11, 3.92269e-14, 5.15261e-14, 4.20509e-14)
res = get_res(6.97851e-11, 5.25262e-11, 7.35584e-11, 1.21667e-13, 5.19603e-14, 1.15146e-13)
print 'res = ', res
