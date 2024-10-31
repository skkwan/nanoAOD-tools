#!/usr/bin/env python
import os
import sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
##soon to be deprecated                                                                                
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
##new way of using jme uncertainty                                                                  
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
# this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles, runsAndLumis

jmeCorrections = createJMECorrector(isMC=True, dataYear="UL2016", runPeriod="A",
                                    jesUncert="Merged",
                                    jetType="AK4PFchs",
                                    noGroom="True",
                                    applyHEMfix=True,
                                    splitJER=False,
                                    metBranchName="MET")

p = PostProcessor(".",
                  inputFiles(),
                  modules=[jmeCorrections()],
                  provenance=True,
                  fwkJobReport=True,
                  jsonInput=runsAndLumis())

p.run()

print("DONE")
