# crab_template_cfg.py
# Variables like 'REQUEST_NAME' are replaced using a configuration .yml
# and the parseYaml.py wrapper

from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config

config = Configuration()

config.section_("General")
config.General.workArea     = 'crab_projects'
config.General.requestName  = 'REQUEST_NAME'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'PSet.py'
config.JobType.scriptExe  = 'CRAB_BASH_SCRIPT'
# config.JobType.scriptArgs = ['script=CRAB_SCRIPT_PYTHON_NAME']
# hadd nano will not be needed once nano tools are in cmssw
config.JobType.inputFiles = ['CRAB_PYTHON_SCRIPT_PATH', '../../../scripts/haddnano.py']
config.JobType.sendPythonFolder = True

config.section_("Data")
config.Data.inputDataset = 'DAS_NAME'
config.Data.inputDBS     = 'INPUT_DBS'
config.Data.splitting    = 'FileBased'
config.Data.unitsPerJob  = 1

config.Data.outLFNDirBase    = '/store/user/skkwan/NanoPost'
config.Data.publication      = True
config.Data.outputDatasetTag = 'OUTPUT_TAG'

config.section_("Site")
config.Site.storageSite = "T2_US_Wisconsin"

