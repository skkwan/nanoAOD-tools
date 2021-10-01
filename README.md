# nanoAOD-tools
Tools for working with NanoAOD (adapted by skkwan). Forked from NanoAODTools.

## Checkout instructions: CMSSW

    ```	    
    cmsrel CMSSW_10_6_0
    cd CMSSW_10_6_0/src
    git clone git@github.com:skkwan/nanoAOD-tools.git PhysicsTools/NanoAODTools
    cd PhysicsTools/NanoAODTools
    cmsenv	
    scram b
    ```	  

## CRAB instructions (currently only operational for 2018 MC)
   
### Do this once each time you change the CRAB config file template (or are setting up)
   1. In `crab/`, `datasetConfig2018.yml` lists the input dataset names and their DAS, as well as
      which crab config and crab bash script template to use. 
      
      The template crab config file is called `crab_template_cfg.py`.
  
   2. Create a unique crab config file:
      ```
      cd crab/
      python parseYaml.py
      ```
      This should create a bunch of config files in `crab/crabJobConfigs/2018`.

### Next, to submit jobs:
   1. In `crabJobConfigs/2018`, `yamlForBatchSubmit.yml` lists the samples you want to submit 
      in one go (also re-iterates the input DAS datasets). Comment/uncomment as needed.
   2. In `crabJobConfigs/2018`, submit the jobs with
      ```
      # get voms certificate
      cmsenv
      python parseYamlForBatchSubmit.py # as a check that the cfg files exist
      python parseYamlForBatchSubmit.py --execute    # to run this for real
      ````
   3. The jobs will be created in a sub-directory `crab_projects/`.