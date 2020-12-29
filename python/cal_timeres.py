#!/usr/bin/env python
"""
Calculate relative branching fraction of jpsi->invi over jpsi->mumu
"""

__author__ = "XIAO Suyu <xiaosuyu@ihep.ac.cn>"
__copyright__ = "Copyright (c) XIAO Suyu"
__created__ = "[2018-04-13 Fri 11:14]"

import math
import sys

args = sys.argv[1:]

if '101' in args:
  inputfile = 'python/txt/101.txt'
elif '102' in args:
  inputfile = 'python/txt/102.txt'
elif '103' in args:
  inputfile = 'python/txt/103.txt'

# if '20' in args:
#   i_res = 0
# elif '50' in args:
#   i_res = 6
# elif '70' in args:
#   i_res = 12

reso = 0.0
resoEr = 0.0

data_res = []
for line in open(inputfile):
    data_res.append(line)
for i in range(len(data_res)):
    data_res[i] = float(data_res[i])

print len(data_res)

def get_res(a, b, c, d, e, f):
    res1 = math.sqrt(abs(a**2+b**2-c**2)/2) 
    res2 = math.sqrt(abs(a**2-b**2+c**2)/2) 
    res3 = math.sqrt(abs(b**2-a**2+c**2)/2)
    resEr1 = (math.sqrt((a*d)**2+(b*e)**2+(c*f)**2)) / (2*res1)
    resEr2 = (math.sqrt((a*d)**2+(b*e)**2+(c*f)**2)) / (2*res2)
    resEr3 = (math.sqrt((a*d)**2+(b*e)**2+(c*f)**2)) / (2*res3)
    return res1, res2, res3, resEr1, resEr2, resEr3

# print get_res(2, 2, 2.5)
resCFD20 = get_res(data_res[0],  data_res[2],  data_res[4] , data_res[1],  data_res[3],  data_res[5] )
resCFD50 = get_res(data_res[6],  data_res[8],  data_res[10], data_res[7],  data_res[9],  data_res[11])
resCFD70 = get_res(data_res[12], data_res[14], data_res[16], data_res[13], data_res[15], data_res[17])

print 'res for CFD20 SiPM BV170 BV60 = ', resCFD20
print 'res for CFD50 SiPM BV170 BV60 = ', resCFD50
print 'res for CFD70 SiPM BV170 BV60 = ', resCFD70
# print "\nItems",        "\t\tBV170 \tBV60 \tSiPM"
# print "CFD20",          resCFD20

