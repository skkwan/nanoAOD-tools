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

def main(argv=None):
    jmeCorrections = createJMECorrector(isMC=True, dataYear=2018, runPeriod="B",
                                        jesUncert="Total", 
                                        jetType="AK4PFchs",
                                        noGroom="True",
                                        applyHEMfix=True,
                                        splitJER=False,
                                        metBranchName="MET")

    fnames=[os.getenv('INPUT')]
    
    for f in fnames:
        print("Printing file names...")
        print(f)

        # p=PostProcessor(".",
        #                 ["/hdfs/store/user/skkwan/ACDEB11A-E534-5043-899F-9880E41725DC.root"], 
        #                 cut="(nMuon > 0) && (nTau > 0)",
        #                 branchsel="keep_and_drop_input.txt",
        #                 outputbranchsel="keep_and_drop_output.txt",
        #                 maxEntries=10,
        #                 modules=[jmeCorrections()],
        #                 postfix="_postproc",
        #                 provenance=True)
        
        # p.run()
        
        


if __name__ == '__main__':
    main()
    sys.exit(0)
