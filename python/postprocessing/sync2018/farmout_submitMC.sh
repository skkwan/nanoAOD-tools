#!/bin/sh
#voms-proxy-init --voms cms --valid 100:00
jobID="2021_May18_fwklite"
header="--job-count=1 --fwklite --assume-input-files-exist --job-generates-output-name --vsize-limit=8000 --input-files-per-job=1"

farmoutAnalysisJobs  $1  $header --input-dbs-path=/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM  ${jobID}_VBFHToTauTau $CMSSW_BASE $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/sync2018/farmout_postprocTemplate.py
