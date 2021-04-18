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

#Model
0.929
# Artificial Neural Network (Multilayer perceptron) - TMVA version
factory.BookMethod(dataloader, TMVA.Types.kMLP, "MLP",
"H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:\
TestRate=5" );
0.931
factory.BookMethod(dataloader, TMVA.Types.kMLP, "MLP",
"H:!V:NeuronType=tanh:VarTransform=N:NCycles=1000:HiddenLayers=N+7:\
TestRate=5" );
0.928
factory.BookMethod(dataloader, TMVA.Types.kMLP, "MLP",
"H:!V:NeuronType=tanh:VarTransform=N:NCycles=1500:HiddenLayers=N+10:\
TestRate=5" );


0.927
#Boosted Decision Trees with gradient boosting
factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTG",
"!H:!V:NTrees=1000:BoostType=Grad:Shrinkage=0.30:UseBaggedGrad:\
GradBaggingFraction=0.6:SeparationType=GiniIndex:nCuts=20:\
PruneMethod=CostComplexity:PruneStrength=50:NNodesMax=5" );
0.926
factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTG",
"!H:!V:NTrees=3000:BoostType=Grad:Shrinkage=0.30:UseBaggedGrad:\
GradBaggingFraction=0.6:SeparationType=GiniIndex:nCuts=20:\
PruneMethod=CostComplexity:PruneStrength=50:NNodesMax=4" );

0.922
factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT",
"!H:!V:NTrees=400:nEventsMin=400:MaxDepth=3:BoostType=AdaBoost:\
SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning" );
0.923
factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT",
"!H:!V:NTrees=1000:nEventsMin=400:MaxDepth=7:BoostType=AdaBoost:\
SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning" );


0.919
# NN (Multilayer perceptron) - ROOT version
factory.BookMethod(dataloader, TMVA.Types.kTMlpANN, "TMlpANN",
"!H:!V:NCycles=200:HiddenLayers=N+1,N:LearningMethod=BFGS:\
ValidationFraction=0.3" );
0.929
factory.BookMethod(dataloader, TMVA.Types.kTMlpANN, "TMlpANN",
"!H:!V:NCycles=1000:HiddenLayers=N+1,N:LearningMethod=BFGS:\
ValidationFraction=0.3" );

factory.BookMethod(dataloader, TMVA.Types.kTMlpANN, "TMlpANN",
"!H:!V:NCycles=1100:HiddenLayers=N+3,N:LearningMethod=BFGS:\
ValidationFraction=0.3" );



0.919
# k-Nearest Neighbour method (similar to PDE-RS)
factory.BookMethod(dataloader, TMVA.Types.kKNN, "KNN",
"H:nkNN=20:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:\
UseWeight=T:!Trim" );
0.924
factory.BookMethod(dataloader, TMVA.Types.kKNN, "KNN",
"H:nkNN=50:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:\
UseWeight=T:!Trim" );


# Run training, test and evaluation
factory.TrainAllMethods() 
factory.TestAllMethods()
factory.EvaluateAllMethods()