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

jmeCorrections = createJMECorrector(isMC=True, dataYear=2018, runPeriod="B",
                                    jesUncert="Total", 
                                    jetType="AK4PFchs",
                                    noGroom="True",
                                    applyHEMfix=True,
                                    splitJER=False,
                                    metBranchName="MET")

# farmout's inputFileNames will substitute with "1.root", "2.root" so no parentheses are needed
stems=[$inputFileNames]
fnames=[]

for f in stems:
    fnames.append("root://cmsxrootd.fnal.gov/" + f)

p=PostProcessor(".",
                ["/hdfs/store/user/skkwan/ACDEB11A-E534-5043-899F-9880E41725DC.root"], 
                cut="(nMuon > 0) && (nTau > 0)",
                branchsel="keep_and_drop_input.txt",
                outputbranchsel="keep_and_drop_output.txt",
                maxEntries=10,
                modules=[jmeCorrections()],
                postfix="_postproc",
                provenance=True)

p.run()
