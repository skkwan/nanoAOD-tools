# runPostProc.sh
# Usage: source runPostProc.sh
# Remember to do voms-proxy-init beforehand and double-check SAMPLES and the output directory


SAMPLES=$1

# Access the .list list of samples to run over
echo ">>> postProc.sh: Reading from ${SAMPLES}..."


while IFS=, read -r SAMPLE INPUT_DIR YEAR CONFIG_DIR XSEC LUMI SCALE
do {
    INPUT_DIR="/afs/cern.ch/work/s/skkwan/public/hToAA/syncNanoAOD/${INPUT_DIR}"
    echo ">>> postProc.sh: Reading input list of files: ${INPUT_DIR}"
    
    TEMP_DIR="scripts_${SAMPLE}/"
    mkdir -p ${TEMP_DIR}
    
    while IFS=$'\n', read -r F
    do	{
	    
	    # 	# Extract the file name
	    prefix="root://cmsxrootd.fnal.gov/"
	    G=${F#"$prefix"}
	    
	    H="${G##*/}"
	    I="${H%.root}"
	    echo "${SAMPLE}_${I}"

	    # Make a temporary directory and temporary .py to call the NanoAODTools
	    TEMP="${TEMP_DIR}TEMP_${SAMPLE}_${I}_postproc.py"
	    LOG="${TEMP_DIR}log_${SAMPLE}_${I}.log"
	    keepdrop="../keep_and_drop.txt" # since the .py scripts will be nested in one directory
	    cp postproc_template.py ${TEMP}
	    grep -rl 'in.root' ${TEMP}           | xargs sed -i "s|in.root|$F|g"
	    # grep -rl 'keep_and_drop.txt' ${TEMP} | xargs sed -i "s|keep_and_drop.txt|${keepdrop}|g"
	    # grep -rl 'out.root' ${TEMP}          | xargs sed -i "s|out.root|${OUT}|g"
	    
	    if [[ "${SAMPLE}" == *"SingleMuon-Run2018"* ]]; then
		grep -rl 'isMC=True' ${TEMP}     | xargs sed -i "s|isMC=True|isMC=False|g"
	    fi

	    # To-do: add output directory as argument
	    nohup python ${TEMP} > ${LOG} & 
	    wait 
	    # 	echo "Done running ${TEMP}, now moving the output file"
	    mv ${I}_Skim.root ${TEMP_DIR}/
	}
    done < ${INPUT_DIR}
    } &
    
done < ${SAMPLES}
