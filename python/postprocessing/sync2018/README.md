# Workflow for my NanoAODTools

## Installation
Follow the NanoAODTools install (with a CMSSW area- I used CMSSW_10_6_0) and copy this sync2018/ folder into `python/postprocessing`.

## To run
Edit `runPostProc.sh` to point to the correct NanoAOD input files, and check that the output directory 
(ideally somewhere in EOS) is correct.

What `runPostProc.sh` does is that it makes one new `skim_postproc.py` per input NanoAOD file, runs it (in parallel, nominally)
and moves the `.root` file to the output directory. 
```
# after updating runPostProc.sh
cmsenv
voms-proxy-init --voms cms --valid 194:00  
source runPostProc.sh
```

To delete all the temporary Python files, run
```
make clean
```

## What to do next
This should interface with my LUNA framework for skimming NanoAOD files.

