# Run jmeSubmitter.py

cmsenv

jobname="Jul-16-2021-try1-all-events-sync"

python jmeSubmitter.py --sampledir VBFHToTauTau --jobName ${jobname} --inFile nanoAODfilepaths/2018/VBFHToTauTau.list  # --dryrun
