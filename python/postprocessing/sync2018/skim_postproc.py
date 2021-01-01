#!/usr/bin/env python
#from exampleModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from importlib import import_module
import os
import sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True


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


jmeCorrections = createJMECorrector(True, 2018, "A", "Total", "AK4PFchs", False, "MET",
                                    False)

jmeCorrectionFatJet = createJMECorrector(True, 2018, "A", "Total", "AK8PFchs", False, "MET",
                                         False)

fnames=['root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18NanoAODv7/VBFHToTauTau_M125_13TeV_powheg_pythia8/NANOAODSIM/Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/100000/04B9A063-2245-D84C-A0EF-8AF03AE9B9CC.root']

#p=PostProcessor(".",fnames,"Jet_pt>150","",[jetmetUncertainties2016(),exampleModuleConstr()],provenance=True)
p=PostProcessor(".",fnames,"","keep_and_drop.txt",[jmeCorrections(), jmeCorrectionFatJet()],provenance=True)

p.run()
