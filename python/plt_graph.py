 #!/usr/bin/env python
import sys
import os
import math
import ROOT
from array import array

logdir = sys.argv[1:]
print logdir

c = ROOT.TCanvas('c', '', 800, 600)
c.SetFillColor(0)
c.SetFrameFillColor(0)
ROOT.gStyle.SetPadColor(0)
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetOptStat(0)
c.SetLeftMargin(0.15)
c.SetRightMargin(0.15)
c.SetTopMargin(0.1)
c.SetBottomMargin(0.15)
t = ROOT.TText(0, 0, 'a')
t.SetTextSize( 0.05 )
t.SetTextAlign( 12 )
mg = ROOT.TMultiGraph("mg","")


volt = array('d')
charge  = array('d') 

for ii20 in [80., 160., 200., 220., 240., 250.]:
    volt.append(ii20)


for i1 in [22398., 32773., 52603., 69865., 102097., 143540]:
    charge.append(i1)


gr  = ROOT.TGraph(6, volt, charge )
mg.Add(gr)
mg.Draw('alp')

mg.GetYaxis().SetTitle('charge')
mg.GetYaxis().SetRangeUser(0, 150000)
mg.GetXaxis().SetLimits(0, 300)

gr.SetLineWidth(2)
gr.SetLineColor(2)
gr.SetLineStyle(1)
gr.SetMarkerSize(2)
gr.SetMarkerColor(2)
gr.SetMarkerStyle(20)


mg.GetXaxis().SetTitle('Bias voltage/V')
mg.GetXaxis().SetTitleOffset(1.0)
mg.GetYaxis().SetTitleOffset(1.0)
mg.GetXaxis().SetTitleSize(0.05)
mg.GetYaxis().SetTitleSize(0.05)
mg.GetXaxis().SetLabelSize(0.05)
mg.GetYaxis().SetLabelSize(0.05)
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetNdivisions(505)


figfile = 'charge.pdf'

c.SaveAs(figfile)

"""
# 101  50  50
# 102  90  70
# 103 130  90
BV170 = array('d')
BV60 = array('d')
xe = array('d')
ye = array('d')
BV170_res20 = array('d')
BV60_res20 = array('d')
BV170_res50 = array('d')
BV60_res50 = array('d')
BV170_res70 = array('d')
BV60_res70 = array('d')
BV170_charge = array('d')
BV60_charge = array('d')
BV170_noise = array('d')
BV60_noise = array('d')
BV170_SN = array('d')
BV60_SN = array('d')
BV60_pulseHeight = array('d')
BV170_pulseHeight = array('d')
for i in [50.0, 90.0, 130.0]:
    BV170.append(i)
for ii in [50.0, 70.0, 90.0]:
    BV60.append(ii)

xe.append(0)
xe.append(0)
xe.append(0)
ye.append(1)
ye.append(1)
ye.append(1)
print xe
n170 = len(BV170)    
n60 = len(BV60) 

for ii_res20 in [113.03, 65.37, 45.33]:
    BV60_res20.append(ii_res20)
for ii_res50 in [105.49, 66.71, 40.84]:
    BV60_res50.append(ii_res50)
for ii_res70 in [122.64, 71.35, 43.28]:
    BV60_res70.append(ii_res70)

for i_res20 in [162.76, 118.15, 76.74]:
    BV170_res20.append(i_res20)
for i_res50 in [136.18, 104.37, 62.80]:
    BV170_res50.append(i_res50)
for i_res70 in [146.61, 105.31, 64.05]:
    BV170_res70.append(i_res70)

### BV-SiPM - SiPM
# for ii_res20 in [math.sqrt(130.4**2 - 71.8**2), math.sqrt(98.8**2 - 71.8**2), math.sqrt(86.4**2 - 71.8**2)]:
#     BV60_res20.append(ii_res20)
# for ii_res50 in [math.sqrt(122.2**2 - 71.8**2), math.sqrt(91.8**2 - 71.8**2), math.sqrt(82.1**2 - 71.8**2)]:
#     BV60_res50.append(ii_res50)
# for ii_res70 in [math.sqrt(136.3**2 - 71.8**2), math.sqrt(95.2**2 - 71.8**2), math.sqrt(82.3**2 - 71.8**2)]:
#     BV60_res70.append(ii_res70)

# for i_res20 in [math.sqrt(205.9**2 - 71.8**2), math.sqrt(146.0**2 - 71.8**2), math.sqrt(106.9**2 - 71.8**2)]:
#     BV170_res20.append(i_res20)
# for i_res50 in [math.sqrt(181.4**2 - 71.8**2), math.sqrt(127.6**2 - 71.8**2), math.sqrt(94.8**2  - 71.8**2)]:
#     BV170_res50.append(i_res50)
# for i_res70 in [math.sqrt(185.5**2 - 71.8**2), math.sqrt(130.8**2 - 71.8**2), math.sqrt(96.6**2 - 71.8**2)]:
#     BV170_res70.append(i_res70)

#### sigle BV - SiPM
# for ii_res20 in [math.sqrt(167.8**2 - 71.8**2), math.sqrt(100.2**2 - 71.8**2), math.sqrt(104.2**2 - 71.8**2)]:
#     BV60_res20.append(ii_res20)
# for ii_res50 in [math.sqrt(143.1**2 - 71.8**2), math.sqrt(83.3**2 - 71.8**2), math.sqrt(106.9**2 - 71.8**2)]:
#     BV60_res50.append(ii_res50)
# for ii_res70 in [math.sqrt(160.2**2 - 71.8**2), math.sqrt(89.7**2 - 71.8**2), math.sqrt(93.5**2 - 71.8**2)]:
#     BV60_res70.append(ii_res70)

# for i_res20 in [math.sqrt(217.4**2 - 71.8**2), math.sqrt(148.0**2 - 71.8**2), math.sqrt(113.2**2 - 71.8**2)]:
#     BV170_res20.append(i_res20)
# for i_res50 in [math.sqrt(246.6**2 - 71.8**2), math.sqrt(109.6**2 - 71.8**2), math.sqrt(111.6**2  - 71.8**2)]:
#     BV170_res50.append(i_res50)
# for i_res70 in [math.sqrt(174.9**2 - 71.8**2), math.sqrt(115.2**2 - 71.8**2), math.sqrt(116.0**2 - 71.8**2)]:
#     BV170_res70.append(i_res70)

for i_charge in [1.503, 2.307, 3.577]:
    BV170_charge.append(i_charge)
for i_noise in [2.555, 2.396, 2.461]:
    BV170_noise.append(i_noise)
for i_pulseHeight in [6.151, 12.969, 25.664]:
    BV170_pulseHeight.append(i_pulseHeight)
for i_SN in [6.151/2.555, 12.969/2.396, 25.664/2.461]:
    BV170_SN.append(i_SN)

for ii_charge in [3.967, 6.267, 11.381]:
    BV60_charge.append(ii_charge)
for ii_noise in [2.402, 2.327, 2.359]:
    BV60_noise.append(ii_noise)
for ii_pulseHeight in [15.598, 31.652, 54.934]:
    BV60_pulseHeight.append(ii_pulseHeight)
for i_SN in [15.598/2.402, 31.652/2.327, 54.934/2.359]:
    BV60_SN.append(i_SN)

if logdir in [['res']]:
    # gr170_20 = ROOT.TGraph(n170, BV170_charge, BV170_res20)
    # gr60_20 = ROOT.TGraph(n60,    BV60_charge, BV60_res20)
    # gr170_50 = ROOT.TGraph(n170, BV170_charge, BV170_res50)
    # gr60_50 = ROOT.TGraph(n60,    BV60_charge, BV60_res50)
    # gr170_70 = ROOT.TGraph(n170, BV170_charge, BV170_res70)
    # gr60_70 = ROOT.TGraph(n60,    BV60_charge, BV60_res70)

    gr170_20 = ROOT.TGraphErrors(n170, BV170, BV170_res20, xe, ye) 
    gr60_20 =  ROOT.TGraphErrors(n60,  BV60,  BV60_res20 , xe, ye) 
    gr170_50 = ROOT.TGraphErrors(n170, BV170, BV170_res50, xe, ye) 
    gr60_50 =  ROOT.TGraphErrors(n60,  BV60,  BV60_res50 , xe, ye) 
    gr170_70 = ROOT.TGraphErrors(n170, BV170, BV170_res70, xe, ye) 
    gr60_70 =  ROOT.TGraphErrors(n60,  BV60,  BV60_res70 , xe, ye) 
elif logdir in [['charge']]:
    gr170 = ROOT.TGraph(n170, BV170, BV170_charge)
    gr60 = ROOT.TGraph(n60, BV60, BV60_charge)
elif logdir in [['noise']]:
    gr170 = ROOT.TGraph(n170, BV170, BV170_noise)
    gr60 = ROOT.TGraph(n60, BV60, BV60_noise)
elif logdir in [['pulse']]:
    gr170 = ROOT.TGraph(n170, BV170, BV170_pulseHeight)
    gr60 = ROOT.TGraph(n60, BV60, BV60_pulseHeight)
elif logdir in [['SN']]:
    gr170 = ROOT.TGraph(n170, BV170, BV170_SN)
    gr60 = ROOT.TGraph(n60, BV60, BV60_SN)
else:
    print 'input error'

if logdir in [['res']]:
    mg.Add(gr170_20)
    mg.Add(gr60_20)
    mg.Add(gr170_50)
    mg.Add(gr60_50)
    mg.Add(gr170_70)
    mg.Add(gr60_70)
elif logdir in [['charge'], ['pulse'], ['noise'], ['SN']]:
    mg.Add(gr170)
    mg.Add(gr60)
mg.Draw('alp')

if logdir in [['res']]:
    mg.SetTitle('Timing Resolution of NDL Detectors')
    mg.GetYaxis().SetTitle('Timing resolution(ps)')
    # mg.GetYaxis().SetRangeUser(0, 250)
    mg.GetYaxis().SetRangeUser(0, 250)
    # mg.GetXaxis().SetRangeUser(30, 150)
    gr170_20.SetLineWidth(2)
    gr170_20.SetMarkerSize(1.5)
    gr170_20.SetMarkerColor(2)
    gr170_20.SetLineColor(2)
    gr170_20.SetLineStyle(2)
    gr170_20.SetMarkerStyle(20)
    gr170_50.SetLineWidth(2)
    gr170_50.SetMarkerSize(1.5)
    gr170_70.SetLineWidth(2)
    gr170_70.SetMarkerSize(1.5)
    gr60_20.SetLineWidth(2)
    gr60_20.SetMarkerSize(1.5)
    gr60_50.SetLineWidth(2)
    gr60_50.SetMarkerSize(1.5)
    gr60_70.SetLineWidth(2)
    gr60_70.SetMarkerSize(1.5)
    gr170_50.SetMarkerColor(2)
    gr170_50.SetLineColor(2)
    gr170_50.SetLineStyle(1)
    gr170_50.SetMarkerStyle(20)
    gr170_70.SetMarkerColor(2)
    gr170_70.SetLineColor(2)
    gr170_70.SetLineStyle(7)
    gr170_70.SetMarkerStyle(20)
    gr60_20.SetMarkerColor(1)
    gr60_20.SetLineColor(1)
    gr60_20.SetLineStyle(2)
    gr60_20.SetMarkerStyle(22)
    gr60_50.SetMarkerColor(1)
    gr60_50.SetLineColor(1)
    gr60_50.SetLineStyle(1)
    gr60_50.SetMarkerStyle(22)
    gr60_70.SetMarkerColor(1)
    gr60_70.SetLineColor(1)
    gr60_70.SetLineStyle(7)
    gr60_70.SetMarkerStyle(22)

elif logdir in [['charge'], ['pulse'], ['noise'], ['SN']]:
    if logdir in [['charge']]:
        mg.SetTitle('Collected Charge of NDL Detectors')
        mg.GetYaxis().SetTitle('Charge(fC)')
        mg.GetYaxis().SetRangeUser(0, 15)
    elif logdir in [['noise']]:
        mg.SetTitle('Noise of NDL Detectors')
        mg.GetYaxis().SetTitle('Noise(mV)')
        mg.GetYaxis().SetRangeUser(0, 4)
    elif logdir in [['SN']]:
        mg.SetTitle('S/N of NDL Detectors')
        mg.GetYaxis().SetTitle('S/N')
        mg.GetYaxis().SetRangeUser(0, 35)
    else:
        mg.SetTitle('PulseHeight of NDL Detectors')
        mg.GetYaxis().SetTitle('Amplitude(mV)')
        mg.GetYaxis().SetRangeUser(0, 70)
    gr170.SetLineWidth(2)
    gr170.SetMarkerSize(1.5)
    gr170.SetMarkerColor(2)
    gr170.SetLineColor(2)
    gr170.SetMarkerStyle(20)
    gr60.SetLineWidth(2)
    gr60.SetMarkerSize(1.5)
    gr60.SetMarkerColor(1)
    gr60.SetLineColor(1)
    gr60.SetMarkerStyle(22)

mg.GetXaxis().SetTitle('Bias voltage(V)')
# mg.GetXaxis().SetTitle('Charge(fC)')
mg.GetXaxis().SetTitleOffset(1.0)
mg.GetYaxis().SetTitleOffset(1.0)
mg.GetXaxis().SetTitleSize(0.05)
mg.GetYaxis().SetTitleSize(0.05)
mg.GetXaxis().SetLabelSize(0.05)
mg.GetYaxis().SetLabelSize(0.05)
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetNdivisions(505)

if logdir in [['res']]:
    legend = ROOT.TLegend(0.35, 0.58, 0.84, 0.8)
    legend.AddEntry(gr170_20, "BV170 CFD20", "lp")
    legend.AddEntry(gr60_20, "BV60 CFD20", "lp")
    legend.AddEntry(gr170_50, "BV170 CFD50", "lp")
    legend.AddEntry(gr60_50, "BV60 CFD50", "lp")
    legend.AddEntry(gr170_70, "BV170 CFD70", "lp")
    legend.AddEntry(gr60_70, "BV60 CFD70", "lp")
    legend.SetNColumns(2)
elif logdir in [['charge'], ['pulse'], ['noise'],['SN']]:
    legend = ROOT.TLegend(0.6, 0.63, 0.83, 0.77)
    legend.AddEntry(gr170, "BV170", "lp")
    legend.AddEntry(gr60, "BV60", "lp")


t.SetTextFont(72)
if logdir in [['res']]:
    t.DrawText(70, 230, 'HGTD Test Beam')
    t.SetTextFont(42)
#     t.DrawText(107, 230, 'Preliminary')
elif logdir in [ ['pulse']]:
    t.DrawText(51, 62, 'HGTD Test Beam')
    t.SetTextFont(42)
#     t.DrawText(88, 62, 'Preliminary')
elif logdir in [['charge']]:
    t.DrawText(51, 13.2,  'HGTD Test Beam')
    t.SetTextFont(42)
#     t.DrawText(88, 13.2, 'Preliminary')
elif logdir in [['SN']]:
    t.DrawText(51, 31,  'HGTD Test Beam')
    t.SetTextFont(42)
#     t.DrawText(88, 31, 'Preliminary')
elif logdir in [ ['noise']]:
    t.DrawText(51, 3.6,  'HGTD Test Beam')
    t.SetTextFont(42)
#     t.DrawText(88, 3.6, 'Preliminary')

legend.SetBorderSize(0)
legend.SetFillColor(0)
# legend.SetFillsStyle(303)
legend.Draw()

if logdir in [['res']]:
    figfile = 'python/plots/time_res.pdf'
elif logdir in [['charge']]:
    figfile = 'python/plots/charge.pdf'
elif logdir in [['noise']]:
    figfile = 'python/plots/noise.pdf'
elif logdir in [['SN']]:
    figfile = 'python/plots/S_N.pdf'
elif logdir in [['pulse']]:
    figfile = 'python/plots/amp.pdf'
c.SetTicks(1,1)
c.SaveAs(figfile)
"""
