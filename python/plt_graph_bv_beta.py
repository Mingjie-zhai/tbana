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

mg = ROOT.TMultiGraph("mg","")

volt_60_20 = array('d')
volt_60_0 = array('d')
volt_60_m30 = array('d')
volt_170_20 = array('d')
volt_170_0 = array('d')
volt_170_m30 = array('d')
res_504_20C  = array('d') 
res_504_0C  = array('d') 
res_504_m30C  = array('d') 
res_202_20C   = array('d')
res_202_0C   = array('d')
res_202_m30C   = array('d')

for ii20 in [120., 130., 140.]:
    volt_170_20.append(ii20)
for ii0 in [110., 120., 130.]:
    volt_170_0.append(ii0)
for iim30 in [100., 110.]:
    volt_170_m30.append(iim30)
for iii20 in [80., 90., 100.]:
    volt_60_20.append(iii20)
for iii0 in [70., 80., 90.]:
    volt_60_0.append(iii0)
for iiim30 in [50., 60., 70.]:
    volt_60_m30.append(iiim30)

for i1 in [61.09, 48.16, 42.84]:
    res_504_20C.append(i1)
for i2 in [54.68, 43.93, 33.99]:
    res_504_0C.append(i2)
for i4 in [46.26, 35.33]:
    res_504_m30C.append(i4)
for i5 in [58.64, 44.66, 33.24]:
    res_202_20C.append(i5)
for i7 in [56.25, 45.19, 32.34]:
    res_202_0C.append(i7)
for i8 in [70.02, 45.31, 35.88]:
    res_202_m30C.append(i8)

gr_504_20  = ROOT.TGraph(3, volt_170_20, res_504_20C )
gr_504_0   = ROOT.TGraph(3, volt_170_0, res_504_0C  )
gr_504_m30 = ROOT.TGraph(2, volt_170_m30, res_504_m30C)
gr_202_20  = ROOT.TGraph(3, volt_60_20, res_202_20C )
gr_202_0   = ROOT.TGraph(3, volt_60_0, res_202_0C  )
gr_202_m30 = ROOT.TGraph(3, volt_60_m30, res_202_m30C)

mg.Add(gr_504_20 )
mg.Add(gr_504_0  )
mg.Add(gr_504_m30)
mg.Add(gr_202_20 )
mg.Add(gr_202_0  )
mg.Add(gr_202_m30)

mg.Draw('alp')

mg.GetYaxis().SetTitle('Timing resolution/ps')
mg.GetYaxis().SetRangeUser(20, 90)
# mg.GetXaxis().SetRangeUser(100, 250)
# mg.GetHistogram().SetMaximum(90.)
# mg.GetHistogram().SetMaximum(25.)
mg.GetXaxis().SetLimits(40, 150)
# mg.GetYaxis().SetLimits(25, 90)
gr_504_20.SetLineWidth(2)
gr_504_20.SetLineColor(2)
gr_504_20.SetLineStyle(1)
gr_504_20.SetMarkerSize(2)
gr_504_20.SetMarkerColor(2)
gr_504_20.SetMarkerStyle(20)
gr_504_0.SetLineWidth(2)
gr_504_0.SetLineColor(2)
gr_504_0.SetLineStyle(9)
gr_504_0.SetMarkerSize(2)
gr_504_0.SetMarkerColor(2)
gr_504_0.SetMarkerStyle(20)
gr_504_m30.SetLineWidth(2)
gr_504_m30.SetLineColor(2)
gr_504_m30.SetLineStyle(8)
gr_504_m30.SetMarkerSize(2)
gr_504_m30.SetMarkerColor(2)
gr_504_m30.SetMarkerStyle(20)
gr_202_20.SetLineWidth(2)
gr_202_20.SetLineColor(4)
gr_202_20.SetLineStyle(1)
gr_202_20.SetMarkerSize(2)
gr_202_20.SetMarkerColor(4)
gr_202_20.SetMarkerStyle(22)
gr_202_0.SetLineWidth(2)
gr_202_0.SetLineColor(4)
gr_202_0.SetLineStyle(9)
gr_202_0.SetMarkerSize(2)
gr_202_0.SetMarkerColor(4)
gr_202_0.SetMarkerStyle(22)
gr_202_m30.SetLineWidth(2)
gr_202_m30.SetLineColor(4)
gr_202_m30.SetLineStyle(8)
gr_202_m30.SetMarkerSize(2)
gr_202_m30.SetMarkerColor(4)
gr_202_m30.SetMarkerStyle(22)

mg.GetXaxis().SetTitle('Bias voltage/V')
mg.GetXaxis().SetTitleOffset(1.0)
mg.GetYaxis().SetTitleOffset(1.0)
mg.GetXaxis().SetTitleSize(0.05)
mg.GetYaxis().SetTitleSize(0.05)
mg.GetXaxis().SetLabelSize(0.05)
mg.GetYaxis().SetLabelSize(0.05)
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetNdivisions(505)

# legend = ROOT.TLegend(0.56, 0.63, 0.84, 0.89)
legend = ROOT.TLegend(0.56, 0.73, 0.84, 0.89)
legend.AddEntry(gr_504_20 , "BV170-08" , "lp")
# legend.AddEntry(gr_504_0 , "BV170, 0C" , "lp")
# legend.AddEntry(gr_504_m30 , "BV170, -30C" , "lp")
legend.AddEntry(gr_202_20 , "BV60-01" , "lp")
# legend.AddEntry(gr_202_0 , "BV60, 0C" , "lp")
# legend.AddEntry(gr_202_m30 , "BV60, -30C" , "lp")

legend.SetBorderSize(0)
legend.SetFillColor(0)
# legend.SetFillsStyle(303)
legend.Draw()

figfile = 'bv_beta_res.pdf'

c.SaveAs(figfile)
