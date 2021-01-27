#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
##soon to be deprecated
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
##new way of using jme uncertainty
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *

# Function parameters

# def createJMECorrector(isMC=True,
#                        dataYear=2016,
#                        runPeriod="B",
#                        jesUncert="Total",
#                        jetType="AK4PFchs",
#                        noGroom=False,
#                        metBranchName="MET",
#                        applySmearing=True,
#                        isFastSim=False,
#                        applyHEMfix=False,
#                        splitJER=False,
#                        saveMETUncs=['T1', 'T1Smear']):


# jmeCorrections = createJMECorrector(isMC=True, dataYear=2018,
#                                     jesUncert="All",
#                                     applyHEMfix=True)

#jmeCorrectionFatJet = createJMECorrector(True, 2018, "A", "Total", "AK8PFchs", False, "MET",
#                                         False)

jmeCorrections = createJMECorrector(isMC=True, dataYear=2018, runPeriod="B",
                                    jesUncert="Merged", 
                                    jetType="AK4PFchs",
                                    applyHEMfix=True,
                                    splitJER=False,
                                    metBranchName="MET")

fnames=['root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18NanoAODv7/VBFHToTauTau_M125_13TeV_powheg_pythia8/NANOAODSIM/Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/100000/04B9A063-2245-D84C-A0EF-8AF03AE9B9CC.root']

#p=PostProcessor(".",fnames,"Jet_pt>150","",[jetmetUncertainties2016(),exampleModuleConstr()],provenance=True)
p=PostProcessor(".",fnames,"(nMuon > 0) && (nTau > 0) && (Jet_pt > 20) && (abs(Jet_eta) < 4.7) && ((Jet_jetId == 2) || (Jet_jetId == 6))","keep_and_drop.txt",[jmeCorrections()],provenance=True)

p.run()
