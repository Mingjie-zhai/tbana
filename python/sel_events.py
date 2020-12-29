#!/usr/bin/env python
"""
Charge Distribution
"""
 
import sys
import os
import ROOT
from tools import check_outfile_path
from array import array

h_charge_BV60 = ROOT.TH1F('h_charge_BV60', 'charge_BV60', 25, -5, 40)
h_risetime_BV60 = ROOT.TH1F('h_risetime_BV60', 'risetime_BV60', 110, 0, 2000)
h_risetime_BV170 = ROOT.TH1F('h_risetime_BV170', 'risetime_BV170', 110, 0, 2000)
h_risetime_sipm = ROOT.TH1F('h_risetime_sipm', 'risetime_sipm', 110, 0, 2000)
h_charge_sipm = ROOT.TH1F('h_charge_sipm', 'charge_sipm', 25, -5, 40)
h_pulseHeight_BV60 = ROOT.TH1F('h_pulseHeight_BV60', 'pulseHeight_BV60', 25, 0, 150)
h_pulseHeight_sipm = ROOT.TH1F('h_pulseHeight_sipm', 'pulseHeight_sipm', 25, 0, 150)
h_charge_BV170 = ROOT.TH1F('h_charge_BV170', 'charge_BV170', 25, -5, 40)
h_pulseHeight_BV170 = ROOT.TH1F('h_pulseHeight_BV170', 'pulseHeight_BV170', 25, 0, 150)

h_noise_BV60 = ROOT.TH1F('h_noise_BV60', 'noise_BV60', 25, 1, 4)
h_noise_sipm = ROOT.TH1F('h_noise_sipm', 'noise_sipm', 25, 1, 4)
h_gaus60_noise = ROOT.TF1('h_gaus60_noise', 'gaus', 1, 4)
h_gaussipm_noise = ROOT.TF1('h_gaussipm_noise', 'gaus', 1, 4)
h_noise_BV170 = ROOT.TH1F('h_noise_BV170', 'noise_BV170', 25, 1, 4)
h_gaus170_noise = ROOT.TF1('h_gaus170_noise', 'gaus', 1, 4)

h_time60_CFD20 = ROOT.TH1F('h_time60_CFD20', 'time60_CFD20', 25, 7000, 9500)
h_gaus60_CFD20 = ROOT.TF1('h_gaus60_CFD20', 'gaus', 7000, 9500)
h_time170_CFD20 = ROOT.TH1F('h_time170_CFD20', 'time170_CFD20', 25, 7000, 9500)
h_gaus170_CFD20 = ROOT.TF1('h_gaus170_CFD20', 'gaus', 7000, 9500)
h_time60_CFD50 = ROOT.TH1F('h_time60_CFD50', 'time60_CFD50', 25, 7000, 9500)
h_gaus60_CFD50 = ROOT.TF1('h_gaus60_CFD50', 'gaus', 7000, 9500)
h_time170_CFD50 = ROOT.TH1F('h_time170_CFD50', 'time170_CFD50', 25, 7000, 9500)
h_gaus170_CFD50 = ROOT.TF1('h_gaus170_CFD50', 'gaus', 7000, 9500)
h_time60_CFD70 = ROOT.TH1F('h_time60_CFD70', 'time60_CFD70', 25, 7000, 9500)
h_gaus60_CFD70 = ROOT.TF1('h_gaus60_CFD70', 'gaus', 7000, 9500)
h_time170_CFD70 = ROOT.TH1F('h_time170_CFD70', 'time170_CFD70', 25, 7000, 9500)
h_gaus170_CFD70 = ROOT.TF1('h_gaus170_CFD70', 'gaus', 7000, 9500)

h_timeBV_CFD20 = ROOT.TH1F('h_timeBV_CFD20', 'timeBV_CFD20', 30, -50000, 50000)
h_timeBV_CFD50 = ROOT.TH1F('h_timeBV_CFD50', 'timeBV_CFD50', 30, -50000, 50000)
h_timeBV_CFD70 = ROOT.TH1F('h_timeBV_CFD70', 'timeBV_CFD70', 30, -50000, 50000)
h_gaus_CFD20 = ROOT.TF1('h_gaus_CFD20', 'gaus', -50000, 50000)
h_gaus_CFD50 = ROOT.TF1('h_gaus_CFD50', 'gaus', -50000, 50000)
h_gaus_CFD70 = ROOT.TF1('h_gaus_CFD70', 'gaus', -50000, 50000)

charge = array('f',[0.]*8)
pulseHeight = array('f',[0.]*8)
noise = array('f',[0.]*8)
riseTime1090 = array('f',[0.]*8)

charge_BV60 = array('f',[0.])
pulseHeight_BV60 = array('f',[0.])
noise_BV60 = array('f',[0.])
riseTime1090_BV60 = array('f',[0.])

charge_sipm = array('f',[0.])
pulseHeight_sipm = array('f',[0.])
noise_sipm = array('f',[0.])
riseTime1090_sipm = array('f',[0.])

charge_BV170 = array('f',[0.])
pulseHeight_BV170 = array('f',[0.])
noise_BV170 = array('f',[0.])
riseTime1090_BV170 = array('f',[0.])

cut_time20_BV60_unirrad = array('f',[0.])
cut_time20_BV170_unirrad = array('f',[0.])
cut_time20_BV_unirrad = array('f',[0.])
cut_time50_BV60_unirrad = array('f',[0.])
cut_time50_BV170_unirrad = array('f',[0.])
cut_time50_BV_unirrad = array('f',[0.])
cut_time70_BV60_unirrad = array('f',[0.])
cut_time70_BV170_unirrad = array('f',[0.])
cut_time70_BV_unirrad = array('f',[0.])

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

t_out_BV60 = ROOT.TTree('BV60', 'BV60')
t_out_BV60.Branch('cut_time20_BV60_unirrad', cut_time20_BV60_unirrad, 'cut_time20_BV60_unirrad/F')
t_out_BV60.Branch('cut_time50_BV60_unirrad', cut_time50_BV60_unirrad, 'cut_time50_BV60_unirrad/F')
t_out_BV60.Branch('cut_time70_BV60_unirrad', cut_time70_BV60_unirrad, 'cut_time70_BV60_unirrad/F')
t_out_BV60.Branch('charge_BV60', charge_BV60, 'charge_BV60/F')
t_out_BV60.Branch('pulseHeight_BV60', pulseHeight_BV60, 'pulseHeight_BV60/F')
t_out_BV60.Branch('noise_BV60', noise_BV60, 'noise_BV60/F')
t_out_BV60.Branch('riseTime1090_BV60', riseTime1090_BV60, 'riseTime1090_BV60/F')

t_out_BV170 = ROOT.TTree('BV170', 'BV170')
t_out_BV170.Branch('cut_time20_BV170_unirrad', cut_time20_BV170_unirrad, 'cut_time20_BV170_unirrad/F')
t_out_BV170.Branch('cut_time50_BV170_unirrad', cut_time50_BV170_unirrad, 'cut_time50_BV170_unirrad/F')
t_out_BV170.Branch('cut_time70_BV170_unirrad', cut_time70_BV170_unirrad, 'cut_time70_BV170_unirrad/F')
t_out_BV170.Branch('cut_time20_BV_unirrad', cut_time20_BV_unirrad, 'cut_time20_BV_unirrad/F')
t_out_BV170.Branch('cut_time50_BV_unirrad', cut_time50_BV_unirrad, 'cut_time50_BV_unirrad/F')
t_out_BV170.Branch('cut_time70_BV_unirrad', cut_time70_BV_unirrad, 'cut_time70_BV_unirrad/F')
t_out_BV170.Branch('charge_BV170', charge_BV170, 'charge_BV170/F')
t_out_BV170.Branch('pulseHeight_BV170', pulseHeight_BV170, 'pulseHeight_BV170/F')
t_out_BV170.Branch('noise_BV170', noise_BV170, 'noise_BV170/F')
t_out_BV170.Branch('riseTime1090_BV170', riseTime1090_BV170, 'riseTime1090_BV170/F')

print 'entries = ', entries
for jentry in xrange(entries):
    ientry = t.LoadTree(jentry)
    if ientry < 0:
        break

#    if ientry > 1000:
#         break

    nb = t.GetEntry(jentry)
    if nb<=0:
        continue

    time20_sipm = t.timeCFD20[3]
    time50_sipm = t.timeCFD50[3]
    time70_sipm = t.timeCFD70[3]

    time20_BV60_unirrad = t.timeCFD20[2]
    cut_time20_BV60_unirrad[0] =  time20_BV60_unirrad - time20_sipm
    # BV60_unirrad = cut_time20_BV60_unirrad[0]
    BV60_unirrad = ( 7000. < cut_time20_BV60_unirrad[0] < 9500. )

    time50_BV60_unirrad = t.timeCFD50[2]
    cut_time50_BV60_unirrad[0] =  time50_BV60_unirrad - time50_sipm
    # BV60_unirrad = cut_time50_BV60_unirrad[0]
    BV60_unirrad = ( 7000. < cut_time50_BV60_unirrad[0] < 9500. )

    time70_BV60_unirrad = t.timeCFD70[2]
    cut_time70_BV60_unirrad[0] =  time70_BV60_unirrad - time70_sipm
    # BV60_unirrad = cut_time70_BV60_unirrad[0]
    BV60_unirrad = ( 7000. < cut_time70_BV60_unirrad[0] < 9500. )
###################################
    time20_BV170_unirrad = t.timeCFD20[1]
    cut_time20_BV170_unirrad[0] =  time20_BV170_unirrad - time20_sipm
    # BV170_unirrad = cut_time20_BV170_unirrad[0]
    BV170_unirrad = ( 7000. < cut_time20_BV170_unirrad[0] < 9500. )

    time50_BV170_unirrad = t.timeCFD50[1]
    cut_time50_BV170_unirrad[0] =  time50_BV170_unirrad - time50_sipm
    # BV170_unirrad = cut_time50_BV170_unirrad[0]
    BV170_unirrad = ( 7000. < cut_time50_BV170_unirrad[0] < 9500. )

    time70_BV170_unirrad = t.timeCFD70[1]
    cut_time70_BV170_unirrad[0] =  time70_BV170_unirrad - time70_sipm
    # BV170_unirrad = cut_time70_BV170_unirrad[0]
    BV170_unirrad = ( 7000. < cut_time70_BV170_unirrad[0] < 9500. )
 ################################################
    cut_time20_BV_unirrad[0] =  time20_BV170_unirrad - time20_BV60_unirrad
    BV_unirrad = cut_time20_BV_unirrad[0]
    # BV_unirrad = ( -20000. < cut_time20_BV170_unirrad[0] < 20000. )

    cut_time50_BV_unirrad[0] =  time50_BV170_unirrad - time50_BV60_unirrad
    BV_unirrad = cut_time50_BV_unirrad[0]
    # BV_unirrad = ( -20000. < cut_time50_BV170_unirrad[0] < 20000. )

    cut_time70_BV_unirrad[0] =  time70_BV170_unirrad - time70_BV60_unirrad
    BV_unirrad = cut_time70_BV_unirrad[0]
    # BV_unirrad = ( -20000. < cut_time70_BV170_unirrad[0] < 20000. )


    if (t.pulseHeight[1]<10 or t.pulseHeight[2]<10 or t.pulseHeight[3]<10):
        continue
    if (BV60_unirrad): 
        i=0 
        for c in t.charge:
            charge[i] = c
            i = i +1
        charge_BV60[0] = charge[2]
        h_charge_BV60.Fill(t.charge[2])
     
        ii = 0
        for cc in t.pulseHeight:
            pulseHeight[ii] = cc
            ii = ii +1
        pulseHeight_BV60[0] = pulseHeight[2]
        h_pulseHeight_BV60.Fill(t.pulseHeight[2])

        n = 0
        for cn in t.noise:
            noise[n] = cn
            n = n +1
        noise_BV60[0] = noise[2]
        h_noise_BV60.Fill(t.noise[2])

        nn = 0
        for cn in t.riseTime1090:
            riseTime1090[nn] = cn
            nn = nn +1
        riseTime1090_BV60[0] = riseTime1090[2]
        h_risetime_BV60.Fill(t.riseTime1090[2])

        h_time60_CFD20.Fill(cut_time20_BV60_unirrad[0])
        h_time60_CFD50.Fill(cut_time50_BV60_unirrad[0])
        h_time60_CFD70.Fill(cut_time70_BV60_unirrad[0])
      
        t_out_BV60.Fill()

    if (BV170_unirrad): 
        i=0 
        for c in t.charge:
            charge[i] = c
            i = i +1
        charge_BV170[0] = charge[1]
        h_charge_BV170.Fill(t.charge[1])
     
        ii = 0
        for cc in t.pulseHeight:
            pulseHeight[ii] = cc
            ii = ii +1
        pulseHeight_BV170[0] = pulseHeight[1]
        h_pulseHeight_BV170.Fill(t.pulseHeight[1])

        nn = 0
        for cnn in t.noise:
            noise[nn] = cnn
            nn = nn +1
        noise_BV170[0] = noise[1]
        h_noise_BV170.Fill(t.noise[1])

        nn = 0
        for cn in t.riseTime1090:
            riseTime1090[nn] = cn
            nn = nn +1
        riseTime1090_BV170[0] = riseTime1090[1]
        h_risetime_BV170.Fill(t.riseTime1090[1])

        h_time170_CFD20.Fill(cut_time20_BV170_unirrad[0])
        h_time170_CFD50.Fill(cut_time50_BV170_unirrad[0])
        h_time170_CFD70.Fill(cut_time70_BV170_unirrad[0])
      
    if (BV_unirrad): 
        i=0 
        for c in t.charge:
            charge[i] = c
            i = i +1
        charge_sipm[0] = charge[3]
        h_charge_sipm.Fill(t.charge[3])
     
        ii = 0
        for cc in t.pulseHeight:
            pulseHeight[ii] = cc
            ii = ii +1
        pulseHeight_sipm[0] = pulseHeight[3]
        h_pulseHeight_sipm.Fill(t.pulseHeight[3])

        nn = 0
        for cnn in t.noise:
            noise[nn] = cnn
            nn = nn +1
        noise_sipm[0] = noise[3]
        h_noise_sipm.Fill(t.noise[3])

        nn = 0
        for cn in t.riseTime1090:
            riseTime1090[nn] = cn
            nn = nn +1
        riseTime1090_sipm[0] = riseTime1090[3]
        h_risetime_sipm.Fill(t.riseTime1090[3])
        h_timeBV_CFD20.Fill(cut_time20_BV_unirrad[0])
        h_timeBV_CFD50.Fill(cut_time50_BV_unirrad[0])
        h_timeBV_CFD70.Fill(cut_time70_BV_unirrad[0])

        t_out_BV170.Fill()

print 'CFD20 res'
h_time60_CFD20.Fit(h_gaus60_CFD20, "R", "", 7000, 9500)
mean_BV60_20 = h_gaus60_CFD20.GetParameter(1)
sigma_BV60_20 = h_gaus60_CFD20.GetParameter(2)
t_min_update = mean_BV60_20 - 3*sigma_BV60_20
t_max_update = mean_BV60_20 + 3*sigma_BV60_20
h_time60_CFD20.Fit(h_gaus60_CFD20, "R", "", t_min_update, t_max_update)
h_time170_CFD20.Fit(h_gaus170_CFD20, "R", "", 7000, 9500)
h_timeBV_CFD20.Fit(h_gaus_CFD20, "R", "", -16000, 20000)

print 'CFD50 res'
h_time60_CFD50.Fit(h_gaus60_CFD50, "R", "", 7000, 9500)
h_time170_CFD50.Fit(h_gaus170_CFD50, "R", "", 7000, 9500)
h_timeBV_CFD50.Fit(h_gaus_CFD50, "R", "", -16000, 20000)

print 'CFD70 res'
h_time60_CFD70.Fit(h_gaus60_CFD70, "R", "", 7000, 9500)
h_time170_CFD70.Fit(h_gaus170_CFD70, "R", "", 7000, 9500)
h_timeBV_CFD70.Fit(h_gaus_CFD70, "R", "", -16000, 20000)

h_noise_BV60.Fit(h_gaus60_noise, "R", "",   1, 4)
h_noise_BV170.Fit(h_gaus170_noise, "R", "", 1, 4)
mean_60 = h_gaus60_noise.GetParameter(1)
mean_170 = h_gaus170_noise.GetParameter(1)

txt_name = "out.txt"
txt_out = open(txt_name, 'a')
# txt_out.writelines(time)
out_list = []
out_list.append('%r' % mean_60)
out_list.append('%r' % mean_170)
txt_out.writelines('\n'.join(out_list))
txt_out.close()

t_out_BV60.Write()
h_time60_CFD20.Write()
h_time60_CFD50.Write()
h_time60_CFD70.Write()
h_charge_BV60.Write()
h_noise_BV60.Write()
h_risetime_BV60.Write()
h_pulseHeight_BV60.Write()

t_out_BV170.Write()
h_time170_CFD20.Write()
h_time170_CFD50.Write()
h_time170_CFD70.Write()
h_timeBV_CFD20.Write()
h_timeBV_CFD50.Write()
h_timeBV_CFD70.Write()
h_charge_BV170.Write()
h_noise_BV170.Write()
h_risetime_BV170.Write()
h_pulseHeight_BV170.Write()
h_charge_sipm.Write()
h_noise_sipm.Write()
h_risetime_sipm.Write()
h_pulseHeight_sipm.Write()

fout.Close()






