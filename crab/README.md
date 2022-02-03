# README.md for CRAB NanoAODTools submission

## Basic steps
1. Edit `datasetConfig2018.yml` which lists all the input DAS datasets and says
   which NanoAODTools script to use, the CRAB production tag, etc.

   Edit `crab_template_cfg.py` which contains the parameters passed to CRAB, e.g.
   which T2 storage to use, multi-core options, and so on.

2. Make sure the arguments to JetMetHelper are correct in the NanoAODTools scripts,
   e.g. In `datasetConfig2018.yml`, it says MC will invoke `crab_script_2018MC.py`, so
   if you want the Merged JER uncertainties, make sure it says "Merged" in that `.py` file.
3. Now create one CRAB `_cfg.py` per dataset, by running this:
   ```
   python parseYaml.py
   ```
4. Set up
   ```
   cmsenv
   voms-proxy-init
   cd crabJobConfigs/2018
   ```
5. To submit multiple CRAB `_cfg.py` (hereafter referred to as "jobs": one job per `_cfg.py` file)
   edit `yamlForBatchSubmit.yml`. E.g. only run one dataset to see if it works first, by
   commenting out the other lines in this file.

   And make sure that the "string" at the top of `yamlForBatchSubmit.yml` is accurate.
6. Submit one CRAB job per uncommented line in `yamlForBatchSubmit.yml`.
   ``` 
   python parseYamlForBatchSubmit.py --execute
   # May need to type GRID password again even if you did voms-proxy-init earlier
   ```

## Troubleshooting CRAB jobs

* Wall clock time exceeded
  * Could be due to broken paths in /hdfs (e.g. to outdated or duplicate datasets) which
    need to be marked as invalid.

* Multi-threading in CRAB config:
  ```
  config.JobType.maxJobRuntimeMin = 300
  config.JobType.numCores = 8
  config.JobType.maxMemoryMB = 9000
  ```