#!/usr/bin/env python
"""
Charge Distribution
"""
 
import sys
import os
import ROOT
from tools import check_outfile_path
from array import array



h_charge = ROOT.TH1F('h_charge', 'charge', 600, -100000, 500000)
h_pulseHeight = ROOT.TH1F('h_charge', 'charge', 500, 0, 500)

charge = [0,0,0,0]
pulseHeight = [0,0,0,0]
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
t_out = ROOT.TTree('tree', 'tree')


print 'entries = ', entries
for jentry in xrange(entries):
    ientry = t.LoadTree(jentry)
    if ientry < 0:
        break

    nb = t.GetEntry(jentry)
    if nb<=0:
        continue

    if ( t.pulseHeight[2]<20):
        continue

    i=0
    for ch in t.charge:
        charge[i] = ch
        i = i +1
    h_charge.Fill(t.charge[2])

    i=0
    for pu in t.pulseHeight:
        pulseHeight[i] = pu
        i = i +1
    h_pulseHeight.Fill(t.pulseHeight[2])
    t_out.Fill()


t_out.Write()
h_charge.Write()

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
#c.SetLogy()

h_charge.SetLineColor(1)
h_charge.Draw('')
h_charge.GetYaxis().SetTitle('Event')
h_charge.GetXaxis().SetTitle('charge')
h_charge.GetXaxis().SetTitleOffset(1.0)
h_charge.GetYaxis().SetTitleOffset(1.5)
h_charge.GetXaxis().SetTitleSize(0.05)
h_charge.GetYaxis().SetTitleSize(0.05)
h_charge.GetXaxis().SetLabelSize(0.05)
h_charge.GetYaxis().SetLabelSize(0.05)
h_charge.GetYaxis().SetNdivisions(505)
"""
h_pulseHeight.SetLineColor(1)
h_pulseHeight.Draw('')
h_pulseHeight.GetYaxis().SetTitle('Event')
h_pulseHeight.GetXaxis().SetTitle('pulseHeight')
h_pulseHeight.GetXaxis().SetTitleOffset(1.0)
h_pulseHeight.GetYaxis().SetTitleOffset(1.0)
h_pulseHeight.GetXaxis().SetTitleSize(0.05)
h_pulseHeight.GetYaxis().SetTitleSize(0.05)
h_pulseHeight.GetXaxis().SetLabelSize(0.05)
h_pulseHeight.GetYaxis().SetLabelSize(0.05)
h_pulseHeight.GetYaxis().SetNdivisions(505)
"""

figfile = '1.pdf'
c.SaveAs(figfile)


fout.Close()




