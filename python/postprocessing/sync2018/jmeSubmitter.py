import sys, getopt

import os
import sys
import glob
import pwd
import argparse
import errno
import socket
import signal
import logging
import math

def get_parser(desc):
    parser = argparse.ArgumentParser(description=desc)
    return parser

def parse_command_line(argv):
    parser = get_parser("Run the NanoAODTools postprocessor")

    parser.add_argument('-s','--submit',action='store_true',help='Submit jobs to condor')
    parser.add_argument('-dr','--dryrun',action='store_true',help='Create jobs but dont submit')
    parser.add_argument('-t','--test',action='store_true',help='Do a test (output test.root)')
    parser.add_argument('-jn','--jobName',nargs='?',type=str,const='',help='Job Name for condor submission')
    parser.add_argument('-d','--customDir',nargs='?',type=str,const='',help='Custom input directory')
    parser.add_argument('-sd','--sampledir',nargs='?',type=str,const='',help='The Sample Input directory')
    parser.add_argument('-in','--inFile',nargs='?',type=str,help='.txt file with list of input files')
    # parser.add_argument('-ms','--metShift',nargs='?',type=str,const='',help='Shift the met')
    # parser.add_argument('-es','--doES',nargs='?',type=str,const='',help='Doing TES / EES shifts?')
    # parser.add_argument('-r','--recoilType',nargs='?',type=str,const='',help='Input files are which recoil type?')
    # parser.add_argument('-iswj','--isWJets',nargs='?',type=str,const='',help='Are input files WJets samples?')
    # parser.add_argument('-mt','--metType',nargs='?',type=str,const='',help='MvaMet = 1, Pf Met = -1')
    args = parser.parse_args(argv)

    return args

print "NanoAODTools submit"

def main(argv=None):
    '''
    Submit a job using farmoutAnalysisJobs --fwklite
    '''
    print "NanoAODTools submit"
    args = parse_command_line(argv)
    jobName = args.jobName
    channel = "MuTau"
    period = 13
    dryrun = args.dryrun
    sampledir = args.sampledir
    sample_name = os.path.basename(sampledir)
    print "sample_name:",sample_name
    if sample_name == '' :
        print "SAMPLE_NAME not defined, check for trailing '/' on sampledir path"
        return
        
    sample_dir = '/data/%s/%s/%s' % (pwd.getpwuid(os.getuid())[0], jobName, sample_name)
    submit_dir = '%s/submit' % (sample_dir)
    if os.path.exists(submit_dir):
        print('Submission directory exists for %s %s.' % (jobName, sample_name))
    
    # create dag dir
    dag_dir = '%s/dags/dag' % (sample_dir)
    os.system('mkdir -p %s' % (os.path.dirname(dag_dir)))
    os.system('mkdir -p %s' % (dag_dir+'inputs'))

    # output dir
    output_dir = '/hdfs/store/user/%s/%s/%s/' % (pwd.getpwuid(os.getuid())[0], jobName, sample_name) 


    # create file list
    filesperjob = 1

    # create bash script
    bash_name = '%s/%s_%i_%s.sh' % (dag_dir+'inputs', channel, period, sample_name)
    bashScript = '#!/bin/bash\n input=$(<$INPUT)\n echo \".sh: input is $input\"\n'
    bashScript += "output=$(<$OUTPUT)\n echo \".sh: output is $output\"\n"
#    bashScript += '$CMSSW_BASE/bin/$SCRAM_ARCH/SVFitStandAloneFSA inputfile=$input newOutputFile=1.0 newFile=\'$OUTPUT\'' #% (channel, sample_name, period)
    bashScript += 'python $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/sync2018/nano_postproc.py $output $input '
    bashScript += '--bi $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/sync2018/keep_and_drop_input.txt '
    bashScript += '--bo $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/sync2018/keep_and_drop_output.txt '
    bashScript += '-N 3'
    bashScript += '\n'

    with open(bash_name,'w') as file:
        file.write(bashScript)
    os.system('chmod +x %s' % bash_name)

    # create farmout command
    farmoutString = 'farmoutAnalysisJobs --infer-cmssw-path --fwklite --input-file-list=%s' % (args.inFile)
    farmoutString += ' --submit-dir=%s --output-dag-file=%s --output-dir=%s' % (submit_dir, dag_dir, output_dir)
    farmoutString += ' --input-files-per-job=%i %s %s' % (filesperjob, jobName, bash_name)

    if not args.dryrun:
        print('Submitting %s' % sample_name)
        os.system(farmoutString)
    else:
        print farmoutString

    return

if __name__ == '__main__':
    main()
