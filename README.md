# TMVA_AllBookMethods

Factory                  : Evaluate classifier: Cuts
                         : 
<WARNING>                : You have asked for histogram MVA_EFF_BvsS which does not seem to exist in *Results* .. better don't use it 
<WARNING>                : You have asked for histogram EFF_BVSS_TR which does not seem to exist in *Results* .. better don't use it 
TFHandler_Cuts           : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       Cuts           : 0.951
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              Cuts           : 0.542 (0.564)       0.887 (0.876)      0.953 (0.955)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
Factory                  : Evaluate classifier: LikelihoodKDE
                         : 
LikelihoodKDE            : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_LikelihoodKDE  : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       LikelihoodKDE  : 0.961
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              LikelihoodKDE  : 0.659 (0.656)       0.912 (0.913)      0.963 (0.964)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         Factory                  : Evaluate classifier: CutsGA
                         : 
<WARNING>                : You have asked for histogram MVA_EFF_BvsS which does not seem to exist in *Results* .. better don't use it 
<WARNING>                : You have asked for histogram EFF_BVSS_TR which does not seem to exist in *Results* .. better don't use it 
TFHandler_CutsGA         : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       CutsGA         : 0.937
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              CutsGA         : 0.101 (0.097)       0.844 (0.861)      0.951 (0.956)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         
                         
                         
                         
                         
                         Factory                  : Evaluate classifier: CutsSA
                         : 
<WARNING>                : You have asked for histogram MVA_EFF_BvsS which does not seem to exist in *Results* .. better don't use it 
<WARNING>                : You have asked for histogram EFF_BVSS_TR which does not seem to exist in *Results* .. better don't use it 
<WARNING>                :  unable to fill 1 efficiency bins 
TFHandler_CutsSA         : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       CutsSA         : 0.947
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              CutsSA         : 0.558 (0.565)       0.893 (0.880)      0.955 (0.956)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         
                         
 
Factory                  : Evaluate classifier: Likelihood
                         : 
Likelihood               : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_Likelihood     : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       Likelihood     : 0.728
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              Likelihood     : 0.138 (0.134)       0.241 (0.241)      0.724 (0.722)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html        
                         
                         
                         
                         
                         


Factory                  : Evaluate classifier: LikelihoodD
                         : 
TFHandler_LikelihoodD    : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:    -1.6832     1.0062   [    -3.0928    0.78118 ]
                         :  fit_mbc:     148.69     1.0099   [     146.75     150.53 ]
                         :   thrust:     3.2120     1.0513   [   -0.74820     4.1232 ]
                         : -----------------------------------------------------------
LikelihoodD              : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_LikelihoodD    : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:    -1.6832     1.0062   [    -3.0928    0.78118 ]
                         :  fit_mbc:     148.69     1.0099   [     146.75     150.53 ]
                         :   thrust:     3.2120     1.0513   [   -0.74820     4.1232 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       LikelihoodD    : 0.896
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              LikelihoodD    : 0.223 (0.215)       0.712 (0.705)      0.907 (0.907)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html      
                         
                         
                         
                         
                         
                         
                         
Factory                  : Evaluate classifier: KNN
                         : 
KNN                      : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_KNN            : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       KNN            : 0.959
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              KNN            : 0.655 (0.674)       0.919 (0.922)      0.960 (0.960)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         



Factory                  : Evaluate classifier: HMatrix
                         : 
HMatrix                  : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_HMatrix        : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       HMatrix        : 0.956
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              HMatrix        : 0.605 (0.606)       0.900 (0.901)      0.966 (0.966)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         
                         
                         

Factory                  : Evaluate classifier: Fisher
                         : 
Fisher                   : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
                         : Also filling probability and rarity histograms (on request)...
TFHandler_Fisher         : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       Fisher         : 0.945
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              Fisher         : 0.367 (0.382)       0.866 (0.869)      0.969 (0.969)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         
                         
                         
Factory                  : Evaluate classifier: FisherG
                         : 
TFHandler_FisherG        : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:  -0.096403     1.0016   [    -3.2206     5.7307 ]
                         :  fit_mbc:   -0.11507    0.99635   [    -3.1839     5.7307 ]
                         :   thrust:    0.13843    0.94576   [    -3.2650     5.7307 ]
                         : -----------------------------------------------------------
FisherG                  : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_FisherG        : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:  -0.096403     1.0016   [    -3.2206     5.7307 ]
                         :  fit_mbc:   -0.11507    0.99635   [    -3.1839     5.7307 ]
                         :   thrust:    0.13843    0.94576   [    -3.2650     5.7307 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       FisherG        : 0.935
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              FisherG        : 0.175 (0.192)       0.840 (0.843)      0.958 (0.958)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         

Factory                  : Evaluate classifier: BoostedFisher
                         : 
BoostedFisher            : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_BoostedFisher  : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       BoostedFisher  : 0.947
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              BoostedFisher  : 0.369 (0.375)       0.870 (0.874)      0.969 (0.969)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         
                         
                         
Factory                  : Evaluate classifier: LD
                         : 
LD                       : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_LD             : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       LD             : 0.935
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              LD             : 0.309 (0.312)       0.816 (0.817)      0.965 (0.966)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html     
                         
                         
                         
                         
                         
                         
Factory                  : Test method: MLP for Classification performance
                         : 
MLP                      : [dataset] : Evaluation of MLP on testing sample (32023 events)
                         : Elapsed time for evaluation of 32023 events: 0.0545 sec       
Factory                  : Evaluate all methods
Factory                  : Evaluate classifier: MLP
                         : 
TFHandler_MLP            : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.29003    0.52939   [   -0.99999    0.99995 ]
                         :  fit_mbc:   0.033560    0.54248   [   -0.99994    0.99775 ]
                         :   thrust:    0.64182    0.43892   [   -0.99990     1.0000 ]
                         : -----------------------------------------------------------
MLP                      : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_MLP            : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.29003    0.52939   [   -0.99999    0.99995 ]
                         :  fit_mbc:   0.033560    0.54248   [   -0.99994    0.99775 ]
                         :   thrust:    0.64182    0.43892   [   -0.99990     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       MLP            : 0.971
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              MLP            : 0.677 (0.676)       0.929 (0.930)      0.977 (0.978)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         
                         

Factory                  : Evaluate classifier: TMlpANN
                         : 
TMlpANN                  : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_TMlpANN        : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       TMlpANN        : 0.966
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              TMlpANN        : 0.670 (0.667)       0.919 (0.921)      0.973 (0.974)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
Info in <TMultiLayerPerceptron::Train>: Using 730799 train and 313201 test entries.





Factory                  : Evaluate classifier: BDT
                         : 
BDT                      : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_BDT            : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       BDT            : 0.971
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              BDT            : 0.671 (0.669)       0.922 (0.924)      0.976 (0.977)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html   
                         
                         
                         
                         
                         
Factory                  : Evaluate classifier: BDTG
                         : 
BDTG                     : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_BDTG           : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       BDTG           : 0.971
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              BDTG           : 0.672 (0.663)       0.927 (0.929)      0.977 (0.977)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
                         
                         
                         
                         
                         
                         
Factory                  : Evaluate classifier: BDTB
                         : 
BDTB                     : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_BDTB           : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       BDTB           : 0.903
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              BDTB           : 0.000 (0.000)       0.000 (0.850)      0.934 (0.934)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!






Factory                  : Evaluate classifier: RuleFit
                         : 
RuleFit                  : [dataset] : Loop over test events and fill histograms with classifier response...
                         : 
TFHandler_RuleFit        : Variable        Mean        RMS   [        Min        Max ]
                         : -----------------------------------------------------------
                         :   fit_de:   -0.44504    0.26467   [   -0.79999    0.19990 ]
                         :  fit_mbc:     5.3694   0.036418   [     5.3000     5.4341 ]
                         :   thrust:    0.82091    0.21946   [ 5.1980e-05     1.0000 ]
                         : -----------------------------------------------------------
                         : 
                         : Evaluation results ranked by best signal efficiency and purity (area)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet       MVA                       
                         : Name:         Method:          ROC-integ
                         : dataset       RuleFit        : 0.436
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
                         : Testing efficiency compared to training efficiency (overtraining check)
                         : -------------------------------------------------------------------------------------------------------------------
                         : DataSet              MVA              Signal efficiency: from test sample (from training sample) 
                         : Name:                Method:          @B=0.01             @B=0.10            @B=0.30   
                         : -------------------------------------------------------------------------------------------------------------------
                         : dataset              RuleFit        : 0.000 (0.000)       0.011 (0.011)      0.217 (0.219)
                         : -------------------------------------------------------------------------------------------------------------------
                         : 
Dataset:dataset          : Created tree 'TestTree' with 32023 events
                         : 
Dataset:dataset          : Created tree 'TrainTree' with 1044000 events
                         : 
Factory                  : Thank you for using TMVA!
                         : For citation information, please visit: http://tmva.sf.net/citeTMVA.html
