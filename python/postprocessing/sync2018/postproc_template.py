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
                                    jesUncert="Total", 
                                    jetType="AK4PFchs",
                                    noGroom="True",
                                    applyHEMfix=True,
                                    splitJER=False,
                                    metBranchName="MET")

fnames=['in.root']

#p=PostProcessor(".",fnames,"Jet_pt>150","",[jetmetUncertainties2016(),exampleModuleConstr()],provenance=True)
p=PostProcessor(".", fnames, cut="(nMuon > 0) && (nTau > 0)",
                branchsel="keep_and_drop.txt",
                modules=[jmeCorrections()],
                provenance=True)

p.run()
