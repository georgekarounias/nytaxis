cd map
faas-cli build -f taximapq2.yml
faas-cli deploy -f taximapq2.yml
value=`cat taximapq2.yml`
if [[ "$value" != *"environment"* ]]; then
	echo -e "    environment:\n      bucketinput: \"commoninput\"\n      bucketoutput: \"map2output\"" >> taximapq2.yml
fi

cd ../reduce
faas-cli build -f taxireduceq2.yml
faas-cli deploy -f taxireduceq2.yml
value=`cat taxireduceq2.yml`
if [[ "$value" != *"environment"* ]]; then
	echo -e "    environment:\n      bucketinput: \"map2output\"\n      bucketoutput: \"result2\"" >> taxireduceq2.yml
fi
cd ..
