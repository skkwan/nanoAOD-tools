# Parse YAML for batch submit
# Usage:
#   python parseYamlForBatchSubmit.py 
# Or, if you want to submit:
#   python parseYamlForBatchSubmit.py --execute

import argparse
import glob
import os
import yaml

# Set up argument parser
parser = argparse.ArgumentParser(description='Script for submitting multiple CRAB jobs at a time.')

parser.add_argument("--execute",
                    help="Execute the crab submit commands.",
                    dest='execute', action = 'store_true')
parser.add_argument("--dryrun", 
                    help="Dryrun only.",
                    dest='execute', action = 'store_false')
parser.set_defaults(feature=True)


args = parser.parse_args()

list_file = open('yamlForBatchSubmit.yml')
list = yaml.safe_load(list_file)


for d in list['toSubmit']:
    # print(d,list["toSubmit"][d])
    
    # Look for cfg.py files matching this regex
    cfgList = glob.glob('crab_'+d+'*_cfg.py')

    # Check that there is only one cfg.py file which can be run, for each dataset
    assert(len(cfgList) == 1), '[ERROR:] Ambiguity in which cfg.py to run for dataset %s, found multiple instances: \n %s' % (d, cfgList)

    # Only one cfg file: extract the string
    cfgName = cfgList[0]

    # Build the CRAB submit command
    cmd = 'crab submit -c %s' % cfgName
    cmd.decode('ascii')
    if (args.execute):
        print('Executing: %s' % cmd)
        os.system(cmd)
    else:
        print('args.execute == False (Default value), do not submit any jobs')

