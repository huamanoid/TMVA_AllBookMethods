from ROOT import TMVA, TFile, TTree, TCut
from subprocess import call
from os.path import isfile
 
 
# Setup TMVA
TMVA.Tools.Instance()
TMVA.PyMethodBase.PyInitialize()
 
output = TFile.Open('output.root', 'RECREATE')
factory = TMVA.Factory('TMVAClassification', output,
                       '!Silent:Color:DrawProgressBar:Transformations=D,G:AnalysisType=Classification')
 
# Load data 
dataS = TFile.Open('beta/data/signal.root')
dataB = TFile.Open('beta/data/background.root')

signal     = dataS.Get('h1')
background = dataB.Get('h1')
 
dataloader = TMVA.DataLoader('dataset')
#for branch in signal.GetListOfBranches():
#   dataloader.AddVariable(branch.GetName())
 
dataloader.AddVariable('fit_de')
dataloader.AddVariable('fit_mbc')
dataloader.AddVariable('thrust')


dataloader.AddSignalTree(signal, 1.0)
dataloader.AddBackgroundTree(background, 1.0)
dataloader.PrepareTrainingAndTestTree(TCut(''),'nTrain_Signal=144000:nTrain_Background=900000:SplitMode=Random:NormMode=NumEvents')


# Run training, test and evaluation
factory.TrainAllMethods() 
factory.TestAllMethods()
factory.EvaluateAllMethods()


0.887
# Cut optimisation using Monte Carlo sampling
factory.BookMethod(dataloader, TMVA.Types.kCuts, "Cuts",
"!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart" );

0.844
# Cut optmisation using Genetic Algorithm
factory.BookMethod(dataloader, TMVA.Types.kCuts, "CutsGA",
"H:!V:FitMethod=GA:CutRangeMin=-10:CutRangeMax=10:VarProp[1]=FMax:EffSel:\
Steps=30:Cycles=3:PopSize=400:SC_steps=10:SC_rate=5:SC_factor=0.95" );

0.893
# Cut optmisation using Simulated Annealing algorithm
factory.BookMethod(dataloader, TMVA.Types.kCuts, "CutsSA",
"!H:!V:FitMethod=SA:EffSel:MaxCalls=150000:KernelTemp=IncAdaptive:\
InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

0.241
#/ Likelihood classification (naive Bayes) with Spline PDF parametrisation
factory.BookMethod(dataloader, TMVA.Types.kLikelihood, "Likelihood",
"H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:\
NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50" );

0.712
# Likelihood with decorrelation of input variables
factory.BookMethod(dataloader, TMVA.Types.kLikelihood, "LikelihoodD",
"!H:!V:!TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:\
NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=Decorrelate" );

0.912
# Likelihood with unbinned kernel estimator for PDF parametrisation
factory.BookMethod(dataloader, TMVA.Types.kLikelihood, "LikelihoodKDE",
"!H:!V:!TransformOutput:PDFInterpol=KDE:KDEtype=Gauss:KDEiter=Adaptive:\
KDEFineFactor=0.3:KDEborder=None:NAvEvtPerBin=50" );

Unexpectedly high training time
# Probability density estimator range search method (multi-dimensional)
factory.BookMethod(dataloader, TMVA.Types.kPDERS, "PDERS",
"!H:V:NormTree=T:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:\
GaussSigma=0.3:NEventsMin=400:NEventsMax=600" );

Error
# Multi-dimensional PDE using self-adapting phase-space binning
factory.BookMethod(dataloader, TMVA.Types.kPDEFoam, "PDEFoam",
"H:V:SigBgSeparate=F:TailCut=0.001:VolFrac=0.0333:nActiveCells=500:\
nSampl=2000:nBin=5:CutNmin=T:Nmin=100:Kernel=None:Compress=T" );

0.919
# k-Nearest Neighbour method (similar to PDE-RS)
factory.BookMethod(dataloader, TMVA.Types.kKNN, "KNN",
"H:nkNN=20:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:\
UseWeight=T:!Trim" );

0.900
# H-matrix (chi-squared) method
factory.BookMethod(dataloader, TMVA.Types.kHMatrix, "HMatrix", "!H:!V" );

0.866
# Fisher discriminant (also creating Rarity distribution of MVA output)
factory.BookMethod(dataloader, TMVA.Types.kFisher, "Fisher",
"H:!V:Fisher:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=60:\
NsmoothMVAPdf=10" );

0.840
# Fisher discriminant with Gauss-transformed input variables
factory.BookMethod(dataloader, TMVA.Types.kFisher, "FisherG", "VarTransform=Gauss" );

Error
# Fisher discriminant with principle-value-transformed input variables
factory.BookMethod(dataloader, TMVA.Types.kFisher, "FisherG", "VarTransform=PCA" );

0.870
# Boosted Fisher discriminant
factory.BookMethod(dataloader, TMVA.Types.kFisher, "BoostedFisher",
"Boost_Num=20:Boost_Transform=log:\
Boost_Type=AdaBoost:Boost_AdaBoostBeta=0.2");

0.816
# Linear discriminant (same as Fisher, but also performing regression)
factory.BookMethod(dataloader, TMVA.Types.kLD, "LD", "H:!V:VarTransform=None" );

Error
# Function discrimination analysis (FDA), fitting user-defined function
factory.BookMethod(dataloader, TMVA.Types.kFDA, "FDA_MT",
"H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:\
ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MINUIT:\
ErrorLevel=1:PrintLevel=-1:FitStrategy=2:UseImprove:UseMinos:SetBatch" );

0.929
# Artificial Neural Network (Multilayer perceptron) - TMVA version
factory.BookMethod(dataloader, TMVA.Types.kMLP, "MLP",
"H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:\
TestRate=5" );

Unexpectedly high training time
# NN with BFGS quadratic minimisation
factory.BookMethod(dataloader, TMVA.Types.kMLP, "MLPBFGS",
"H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:\
TestRate=5:TrainingMethod=BFGS" );

0.919
# NN (Multilayer perceptron) - ROOT version
factory.BookMethod(dataloader, TMVA.Types.kTMlpANN, "TMlpANN",
"!H:!V:NCycles=200:HiddenLayers=N+1,N:LearningMethod=BFGS:\
ValidationFraction=0.3" );

Error
# NN (Multilayer perceptron) - ALEPH version (depreciated)
factory.BookMethod(dataloader, TMVA.Types.kCFMlpANN, "CFMlpANN",
"!H:!V:NCycles=2000:HiddenLayers=N+1,N" );

Error
# Support Vector Machine
factory.BookMethod(dataloader, TMVA.Types.kSVM, "SVM", "Gamma=0.25:Tol=0.001" );
# Boosted Decision Trees with adaptive boosting

0.922
factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT",
"!H:!V:NTrees=400:nEventsMin=400:MaxDepth=3:BoostType=AdaBoost:\
SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning" );

0.927
#Boosted Decision Trees with gradient boosting
factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTG",
"!H:!V:NTrees=1000:BoostType=Grad:Shrinkage=0.30:UseBaggedGrad:\
GradBaggingFraction=0.6:SeparationType=GiniIndex:nCuts=20:\
PruneMethod=CostComplexity:PruneStrength=50:NNodesMax=5" );

0.850
# Boosted Decision Trees with bagging
factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTB",
"!H:!V:NTrees=400:BoostType=Bagging:SeparationType=GiniIndex:\
nCuts=20:PruneMethod=NoPruning" );

0.011
# Predictive learning via rule ensembles (RuleFit)
factory.BookMethod(dataloader, TMVA.Types.kRuleFit, "RuleFit",
"H:!V:RuleFitModule=RFTMVA:Model=ModRuleLinear:MinImp=0.001:\
RuleMinDist=0.001:NTrees=20:fEventsMin=0.01:fEventsMax=0.5:\
GDTau=-1.0:GDTauPrec=0.01:GDStep=0.01:GDNSteps=10000:GDErrScale=1.02" );


# Run training, test and evaluation
factory.TrainAllMethods() 
factory.TestAllMethods()
factory.EvaluateAllMethods()