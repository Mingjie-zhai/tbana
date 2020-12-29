#!/usr/bin/env python
"""
Charge Distribution
"""
 
import sys
import os
import ROOT
from tools import check_outfile_path
from array import array

h_target = ROOT.TH1F('h_target', 'target', 1200, -10000, 10000)
h_gaus = ROOT.TF1('h_gaus', 'gaus', -50000, 50000)
h_CFD50_BV170 = ROOT.TH1F('h_CFD50_BV170', 'CFD50_BV170', 1200, -10000, 10000)
h_CFD50_BV60 = ROOT.TH1F('h_CFD50_BV60', 'CFD50_BV60', 1200, -10000, 10000)
h_CFD50_BV = ROOT.TH1F('h_CFD50_BV', 'CFD50_BV', 200, -10000, 10000)
h_CFD20_BV170 = ROOT.TH1F('h_CFD20_BV170', 'CFD20_BV170', 1200, -10000, 10000)
h_CFD20_BV60 = ROOT.TH1F('h_CFD20_BV60', 'CFD20_BV60', 1200, -10000, 10000)
h_CFD20_BV = ROOT.TH1F('h_CFD20_BV', 'CFD20_BV', 200, -10000, 10000)
h_CFD70_BV170 = ROOT.TH1F('h_CFD70_BV170', 'CFD70_BV170', 1200, -10000, 10000)
h_CFD70_BV60 = ROOT.TH1F('h_CFD70_BV60', 'CFD70_BV60', 1200, -10000, 10000)
h_CFD70_BV = ROOT.TH1F('h_CFD70_BV', 'CFD70_BV', 200, -10000, 10000)

args = sys.argv[1:]

if (len(args) < 2):
    print 'input error'
infile = args[0]
outfile = args[1]
check_outfile_path(outfile)

fin = ROOT.TFile(infile)
t = fin.Get('tree')
entries = t.GetEntriesFast()

fout = ROOT.TFile(outfile, 'RECREATE')

print 'entries = ', entries

def get_distribution(branch_name1, branch_name2, branch_number1, branch_number2, h_target, tmin_his, tmax_his):
    dist_1 = branch_name1[branch_number1]
    dist_2 = branch_name1[branch_number2]
    delta_t = dist_1 - dist_2
    h_target.Fill(delta_t)
    h_target.SetAxisRange(tmin_his, tmax_his, 'X')

def fit_distribution(histo, func, tmin_fit, tmax_fit, n_sigma):  
    # histo.Fit(func, "R", "", -10000, 10000)
    histo.Fit(func, "R", "", tmin_fit, tmax_fit)
    mean1 = func.GetParameter(1)
    sigma1 = func.GetParameter(2)
    t_min1 = mean1 - n_sigma*sigma1
    t_max1 = mean1 + n_sigma*sigma1
    histo.Fit(func, "R", "", t_min1, t_max1)
    mean2 = func.GetParameter(1)
    sigma2 = func.GetParameter(2)
    t_min2 = mean2 - n_sigma*sigma2
    t_max2 = mean2 + n_sigma*sigma2
    histo.Fit(func, "R", "", t_min2, t_max2)
    sigma3 = func.GetParameter(2)
    errsigma3 = func.GetParError(2)

    txt_name = "python/txt/out.txt" 
    txt_out = open(txt_name, 'a')
    out_list = []
    txt_out.writelines('\n')
    out_list.append('%r' % sigma3)
    out_list.append('%r' % errsigma3)
    txt_out.writelines('\n'.join(out_list))
    txt_out.close()

for jentry in xrange(entries):
    ientry = t.LoadTree(jentry)
    if ientry < 0:
        break

    # if ientry > 10:
    #     break

    nb = t.GetEntry(jentry)
    if nb<=0:
        continue

    # amp_max = max(t.pulseHeight)

    if (t.pulseHeight[1]<10 or t.pulseHeight[2]<10 or t.pulseHeight[3]<10):
        continue

    get_distribution(t.timeCFD20, t.timeCFD20, 1, 3, h_CFD20_BV170, 7000, 9800)
    get_distribution(t.timeCFD20, t.timeCFD20, 2, 3, h_CFD20_BV60, 7000, 9800)
    get_distribution(t.timeCFD20, t.timeCFD20, 1, 2, h_CFD20_BV, -1500, 1000)
    get_distribution(t.timeCFD50, t.timeCFD50, 1, 3, h_CFD50_BV170, 7000, 9800)
    get_distribution(t.timeCFD50, t.timeCFD50, 2, 3, h_CFD50_BV60, 7000, 9800)
    get_distribution(t.timeCFD50, t.timeCFD50, 1, 2, h_CFD50_BV, -1500, 1000)
    get_distribution(t.timeCFD70, t.timeCFD70, 1, 3, h_CFD70_BV170, 7000, 9800)
    get_distribution(t.timeCFD70, t.timeCFD70, 2, 3, h_CFD70_BV60, 7000, 9800)
    get_distribution(t.timeCFD70, t.timeCFD70, 1, 2, h_CFD70_BV, -1500, 1000)

############ nsigma = 2 for 101, nsigma = 1 for 102 and 103

print '########## CFD20 BV170 fitting ##########'
fit_distribution(h_CFD20_BV170, h_gaus, -10000, 10000,2)
print '########## CFD20 BV60 fitting ##########'
fit_distribution(h_CFD20_BV60, h_gaus, -10000, 10000,2)
print '########## CFD20 BV fitting ##########'
fit_distribution(h_CFD20_BV, h_gaus, -1000, 1000,2)
print '########## CFD50 BV170 fitting ##########'
fit_distribution(h_CFD50_BV170, h_gaus, -10000, 10000,2)
print '########## CFD50 BV60 fitting ##########'
fit_distribution(h_CFD50_BV60, h_gaus, -10000, 10000,2)
print '########## CFD50 BV fitting ##########'
fit_distribution(h_CFD50_BV, h_gaus, -1000, 1000,2)
print '########## CFD70 BV170 fitting ##########'
fit_distribution(h_CFD70_BV170, h_gaus, -10000, 10000,2)
print '########## CFD70 BV60 fitting ##########'
fit_distribution(h_CFD70_BV60, h_gaus, -10000, 10000,2)
print '########## CFD70 BV fitting ##########'
fit_distribution(h_CFD70_BV, h_gaus, -1000, 1000,2)

h_CFD50_BV170.Write()
h_CFD50_BV60.Write()
h_CFD50_BV.Write()
h_CFD20_BV170.Write()
h_CFD20_BV60.Write()
h_CFD20_BV.Write()
h_CFD70_BV170.Write()
h_CFD70_BV60.Write()
h_CFD70_BV.Write()

fout.Close()






