# parseYaml.py

import yaml
import os

config_file = open("datasetConfig2018.yml")

config = yaml.safe_load(config_file)


#-------------------------------------------------------#

for eraType in ["mc_2018", "embed_2018", "data_2018_A", "data_2018_B", "data_2018_C", "data_2018_D"]:
   for d in config[eraType]["datasets"]:

      dir = "crabJobConfigs/" + str(config[eraType]["year"]) + "/" 

      newCRABConfFile  = dir + "crab_" + d + "_" + config[eraType]["prodtag"] + "_cfg.py"  
      print(newCRABConfFile)

      requestName      = config["requestname"] + "_" + d + "_" + config[eraType]["prodtag"]  
      crabBashScript   = config[eraType]["bash"]        # used for scriptExe in CRAB
      crabPythonScript = config[eraType]["script"]      # crab python script: one per era (will say which jmeCorrection to use)
      dasName          = config[eraType]["datasets"][d] # DAS name
      inputDBS         = config[eraType]["inputDBS"]    # inputDBS
      outputTag        = 'NanoPost_' + d + "_" + config[eraType]["prodtag"]  

      # Make one new template file per dataset
      with open('crab_template_cfg.py', 'r') as templatefile:
         t1 = templatefile.read()
         with open(newCRABConfFile, 'w+') as writefile:

            t2 = t1.replace('REQUEST_NAME',            requestName)
            t3 = t2.replace('CRAB_BASH_SCRIPT',        crabBashScript)
            t4 = t3.replace('CRAB_PYTHON_SCRIPT_PATH', crabPythonScript)
            t5 = t4.replace('DAS_NAME',                dasName)
            t6 = t5.replace('INPUT_DBS',               inputDBS)
            t7 = t6.replace('OUTPUT_TAG',              outputTag)

            writefile.write(t7)

#-------------------------------------------------------#

