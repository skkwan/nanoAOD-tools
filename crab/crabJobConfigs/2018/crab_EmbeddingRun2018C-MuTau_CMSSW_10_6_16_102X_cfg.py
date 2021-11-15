# crab_template_cfg.py
# Variables like 'NanoPost_EmbeddingRun2018C-MuTau_CMSSW_10_6_16_102X' are replaced using a configuration .yml
# and the parseYaml.py wrapper

from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config

config = Configuration()

config.section_("General")
config.General.workArea     = 'crab_projects'
config.General.requestName  = 'NanoPost_EmbeddingRun2018C-MuTau_CMSSW_10_6_16_102X'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName   = 'PSet.py'
config.JobType.scriptExe  = 'crab_bash_2018EmbeddedC.sh'
# config.JobType.scriptArgs = ['script=CRAB_SCRIPT_PYTHON_NAME']
# hadd nano will not be needed once nano tools are in cmssw
config.JobType.inputFiles = ['crab_script_2018EmbC.py', '../../../scripts/haddnano.py']
config.JobType.sendPythonFolder = True

config.section_("Data")
config.Data.inputDataset = '/EmbeddingRun2018C/skkwan-CMSSW_10_6_16_102X_EmbeddingRun2018C_MuTauFinalState-inputDoubleMu-b351189ddbae69df39b0343b8e904fcc/USER'
config.Data.inputDBS     = 'phys03'
config.Data.splitting    = 'FileBased'
config.Data.unitsPerJob  = 1
#config.Data.splitting    = 'Automatic'

config.Data.outLFNDirBase    = '/store/user/skkwan/NanoPost'
config.Data.publication      = True
config.Data.outputDatasetTag = 'NanoPost_EmbeddingRun2018C-MuTau_CMSSW_10_6_16_102X'

config.section_("Site")
config.Site.storageSite = "T2_US_Wisconsin"

