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

volt_2 = array('d')
volt_1 = array('d')
res_504_20C  = array('d') 
res_504_0C  = array('d') 
res_504_m30C  = array('d') 
res_202_20C   = array('d')
res_202_0C   = array('d')
res_202_m30C   = array('d')
res_201_20C = array('d')
res_201_0C = array('d')
res_201_m30C = array('d')

for i in [150., 200.]:
    volt_2.append(i)
for ii in [150.]:
    volt_1.append(ii)
for i1 in [77.11, 44.27]:
    res_504_20C.append(i1)
for i2 in [78.62, 42.98]:
    res_202_20C.append(i2)
for i3 in [74.26, 41.09]:
    res_201_20C.append(i3)
for i4 in [54.48, 33.41]:
    res_504_0C.append(i4)
for i5 in [61.03, 35.02]:
    res_202_0C.append(i5)
for i6 in [65.59, 30.56]:
    res_201_0C.append(i6)
for i7 in [38.18]:
    res_504_m30C.append(i7)
for i8 in [36.49]:
    res_202_m30C.append(i8)
for i9 in [40.89]:
    res_201_m30C.append(i9)

gr_504_20  = ROOT.TGraph(2, volt_2, res_504_20C )
gr_504_0   = ROOT.TGraph(2, volt_2, res_504_0C  )
gr_504_m30 = ROOT.TGraph(1, volt_1, res_504_m30C)
gr_202_20  = ROOT.TGraph(2, volt_2, res_202_20C )
gr_202_0   = ROOT.TGraph(2, volt_2, res_202_0C  )
gr_202_m30 = ROOT.TGraph(1, volt_1, res_202_m30C)
gr_201_20  = ROOT.TGraph(2, volt_2, res_201_20C )
gr_201_0   = ROOT.TGraph(2, volt_2, res_201_0C  )
gr_201_m30 = ROOT.TGraph(1, volt_1, res_201_m30C)

mg.Add(gr_504_20 )
mg.Add(gr_504_0  )
mg.Add(gr_504_m30)
mg.Add(gr_202_20 )
mg.Add(gr_202_0  )
mg.Add(gr_202_m30)
mg.Add(gr_201_20 )
mg.Add(gr_201_0  )
mg.Add(gr_201_m30)

mg.Draw('alp')

mg.GetYaxis().SetTitle('Timing resolution/ps')
mg.GetYaxis().SetRangeUser(25, 90)
# mg.GetXaxis().SetRangeUser(100, 250)
# mg.GetHistogram().SetMaximum(90.)
# mg.GetHistogram().SetMaximum(25.)
mg.GetXaxis().SetLimits(135, 215)
# mg.GetYaxis().SetLimits(25, 90)
gr_504_20.SetLineWidth(2)
gr_504_20.SetLineColor(2)
gr_504_20.SetLineStyle(10)
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
gr_202_20.SetLineStyle(10)
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
gr_201_20.SetLineWidth(2)
gr_201_20.SetLineColor(6)
gr_201_20.SetLineStyle(10)
gr_201_20.SetMarkerSize(2)
gr_201_20.SetMarkerColor(6)
gr_201_20.SetMarkerStyle(23)
gr_201_0.SetLineWidth(2)
gr_201_0.SetLineColor(6)
gr_201_0.SetLineStyle(9)
gr_201_0.SetMarkerSize(2)
gr_201_0.SetMarkerColor(6)
gr_201_0.SetMarkerStyle(23)
gr_201_m30.SetLineWidth(2)
gr_201_m30.SetLineColor(6)
gr_201_m30.SetLineStyle(8)
gr_201_m30.SetMarkerSize(2)
gr_201_m30.SetMarkerColor(6)
gr_201_m30.SetMarkerStyle(23)

mg.GetXaxis().SetTitle('Bias voltage/V')
mg.GetXaxis().SetTitleOffset(1.0)
mg.GetYaxis().SetTitleOffset(1.0)
mg.GetXaxis().SetTitleSize(0.05)
mg.GetYaxis().SetTitleSize(0.05)
mg.GetXaxis().SetLabelSize(0.05)
mg.GetYaxis().SetLabelSize(0.05)
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetNdivisions(505)

legend = ROOT.TLegend(0.56, 0.7, 0.84, 0.89)
legend.AddEntry(gr_504_20 , "SE5-04" , "lp")
legend.AddEntry(gr_202_20 , "SE2-02" , "lp")
legend.AddEntry(gr_201_20 , "SE2-01" , "lp")

legend.SetBorderSize(0)
legend.SetFillColor(0)
# legend.SetFillsStyle(303)
legend.Draw()

figfile = 'beta_res.pdf'

c.SaveAs(figfile)
