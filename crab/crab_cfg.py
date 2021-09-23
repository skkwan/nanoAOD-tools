from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config

config = Configuration()

config.section_("General")
config.General.workArea = 'crab_projects'
config.General.requestName = 'NanoPost_test'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_script.sh'
# hadd nano will not be needed once nano tools are in cmssw
config.JobType.inputFiles = ['crab_script.py', '../scripts/haddnano.py']
config.JobType.sendPythonFolder = True

config.section_("Data")
config.Data.inputDataset = '/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM'
#config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 10

config.Data.outLFNDirBase = '/store/user/skkwan/NanoPost'
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoPost_Test_VBFHToTauTau'

config.section_("Site")
config.Site.storageSite = "T2_US_Wisconsin"

