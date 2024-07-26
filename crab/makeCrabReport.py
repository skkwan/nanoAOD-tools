import os
import yaml

config_file = open("datasetConfig2018.yml")

config = yaml.safe_load(config_file)

year=2018

reportname="report.txt"
os.system("rm -r report.txt")

for eraType in ["mc_2018"]:
#for eraType in ["embed_2018", "data_2018_A", "data_2018_B", "data_2018_C", "data_2018_D"]:
   for name in config[eraType]["datasets"]:
      # Report
      command = f"echo '-------- {name} ----------------------------- ' | tee -a {reportname}"
      os.system(command)
      command = f'crab status -d crab_projects/crab_NanoPost_{name}_{config[eraType]["prodtag"]} | tee -a {reportname}'
      print(command)
      os.system(command)
      os.system(f"echo '\n\n' | tee -a {reportname}")

# crab_NanoPost_Cascade_GluGluH125toA1A2to3A1_A1to2Bor2Tau_MA1-15_MA2-70_RunIISummer20UL18NanoAODv9