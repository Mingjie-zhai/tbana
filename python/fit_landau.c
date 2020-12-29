#include "TH1.h"
#include "TF1.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TMath.h"

Double_t langaufun(Double_t *x, Double_t *par) {

      // Numeric constants
      Double_t invsq2pi = 0.3989422804014;   // (2 pi)^(-1/2)
      Double_t mpshift  = -0.22278298;       // Landau maximum location

      // Control constants
      Double_t np = 100.0;      // number of convolution steps
      Double_t sc =   5.0;      // convolution extends to +-sc Gaussian sigmas

      // Variables
      Double_t xx;
      Double_t mpc;
      Double_t fland;
      Double_t sum = 0.0;
      Double_t xlow,xupp;
      Double_t step;
      Double_t i;


      // MP shift correction
      mpc = par[1] - mpshift * par[0];

      // Range of convolution integral
      xlow = x[0] - sc * par[3];
      xupp = x[0] + sc * par[3];

      step = (xupp-xlow) / np;

      // Convolution integral of Landau and Gaussian by sum
      for(i=1.0; i<=np/2; i++) {
         xx = xlow + (i-.5) * step;
         fland = TMath::Landau(xx,mpc,par[0]) / par[0];
         sum += fland * TMath::Gaus(x[0],xx,par[3]);

         xx = xupp - (i-.5) * step;
         fland = TMath::Landau(xx,mpc,par[0]) / par[0];
         sum += fland * TMath::Gaus(x[0],xx,par[3]);
      }

      return (par[2] * step * sum * invsq2pi / par[3]);
}

void fit_landau() {

   std::string signal_pdf_rootfile;
   std::stringstream hist_title;
   const Int_t numberOfParams = 4;

   // signal_pdf_rootfile =   "../event/101.root" ;
   // signal_pdf_rootfile =   "../event/102.root" ;
   // signal_pdf_rootfile =   "../event/103.root" ;
   signal_pdf_rootfile =   "event/event_10mV_101.root" ;

   // hist_title << "h_charge_BV60" ;
   // Double_t fitMinLimit = -4;
   // Double_t fitMaxLimit = 39;
   // Double_t startingParams[numberOfParams] = {1,11,1000,0.72};
   // hist_title << "h_pulseHeight_BV60" ;
   // Double_t fitMinLimit = 1;
   // Double_t fitMaxLimit = 149;
   // Double_t startingParams[numberOfParams] = {2,60,300,7.2};
   // hist_title << "h_charge_BV170" ;
   // Double_t fitMinLimit = -3;
   // Double_t fitMaxLimit = 39;
   // Double_t startingParams[numberOfParams] = {1,2,200,3};
   // hist_title << "h_pulseHeight_BV170" ;
   // Double_t fitMinLimit = 1;
   // Double_t fitMaxLimit = 149;
   // Double_t startingParams[numberOfParams] = {1,10,500,1.72};

//   hist_title << "h_pulseHeight_sipm" ;
//   Double_t fitMinLimit = 20;
//   Double_t fitMaxLimit = 100;
//   Double_t startingParams[numberOfParams] = {3,50,5000000000,10.72};

   hist_title << "h_noise_sipm" ;
   Double_t fitMinLimit = 1.5;
   Double_t fitMaxLimit = 3.5;
   Double_t startingParams[numberOfParams] = {0.2,2.2,20000,3.0};

   TFile *f1 = new TFile(signal_pdf_rootfile.c_str());
   TH1F* hSNR = dynamic_cast<TH1F*>(gDirectory->Get(hist_title.str().c_str()));

//    TLegend* legFit = new TLegend(0.51,0.62,0.93,0.88);
//    legFit->SetFillStyle(0);
//    // legFit->SetLineColorAlpha(0,0);
//    legFit->SetTextColor(kBlack);
//    legFit->SetMargin(0.1);

   TF1 *fLandauXGaus = new TF1("fLandauXGaus",langaufun,fitMinLimit,fitMaxLimit,numberOfParams);
   fLandauXGaus->SetParameters(startingParams);
   fLandauXGaus->SetParNames("Width","MPV","Area","GSigma");
   // hSNR->Rebin(10);
   hSNR->Fit(fLandauXGaus,"RS","",  fitMinLimit, fitMaxLimit);   // fit within specified range, save param results

   TLegend* legFit = new TLegend(0.51,0.62,0.93,0.88);
   legFit->SetFillStyle(0);
   // legFit->SetLineColorAlpha(0,0);
   legFit->SetTextColor(kBlack);
   legFit->SetMargin(0.1);

   for(Int_t iParam=0;iParam<numberOfParams;iParam++){
      legFit->AddEntry("NULL",Form("%s = %3.3f #pm %3.3f",fLandauXGaus->GetParName(iParam),fLandauXGaus->GetParameter(iParam),fLandauXGaus->GetParError(iParam)) , "");
   }
   legFit->Draw();

   // SetMPVPerConfigPerChannel(configName, variableName,channelID, fLandauXGaus->GetParameter(1), fLandauXGaus->GetParError(1));

  //-------------------------------------------------------------------------------------------------------------------------------------//
  //Customisation
//   hSNR->GetXaxis()->SetRangeUser(fitMinLimit,fitMaxLimit);
//   canFit->SaveAs("landau.pdf");
}
