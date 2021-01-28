# runPostProc.sh
# Usage: source runPostProc.sh
# Remember to do voms-proxy-init beforehand and double-check SAMPLES and the output directory


cmsenv

SAMPLES="/afs/cern.ch/work/s/skkwan/public/hToAA/syncNanoAOD/nanoAODfilepaths/2018/VBFHToTauTau.list"

# Access the .list list of samples to run over
while IFS=$'\n', read -r F
do
    {

	# Extract the file name
	prefix="root://cmsxrootd.fnal.gov/"
	G=${F#"$prefix"}
	
	H="${G##*/}"
	I="${H%.root}"
	echo ${I}

	# Make a temporary .py to call the NanoAODTools
	TEMP="TEMP_${I}_postproc.py"
	cp postproc_template.py ${TEMP}
	grep -rl 'in.root' ${TEMP} | xargs sed -i "s|in.root|$F|g"

	python ${TEMP}

	echo "Done running ${TEMP}, now moving the output file"
	mv ${I}_Skim.root /eos/user/s/skkwan/postproc/sync/
    } &
done < ${SAMPLES}
