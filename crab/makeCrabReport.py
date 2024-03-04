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
      command = "echo '-------- {} ----------------------------- ' | tee -a {}".format(name, reportname)
      os.system(command)
      command = "crab status -d crabJobConfigs/{}/crab_projects/crab_NanoPost_{}_{} | tee -a {}".format(year, name, config[eraType]["prodtag"], reportname)
      print(command)
      os.system(command)
      os.system("echo '\n\n' | tee -a {}".format(reportname))
