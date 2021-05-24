#!/bin/bash
 input=$INPUT
 echo ".sh: input is $input"
output=$OUTPUT
 echo ".sh: output is $output"
python $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/sync2018/nano_postproc.py $output $input --bi $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/sync2018/keep_and_drop_input.txt --bo $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/sync2018/keep_and_drop_output.txt -N 3
