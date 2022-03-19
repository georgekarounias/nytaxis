cd map
faas-cli build -f taximapq1.yml
value=`cat taximapq1.yml`
if [[ "$value" != *"environment"* ]]; then
	sed -i "    environment:\n      bucketinput: \"commoninput\"\n      bucketoutput: \"map1output\"" >> taximapq1.yml
fi
faas-cli build -f taximapq1.yml
faas-cli deploy -f taximapq1.yml

cd ../reduce
faas-cli build -f taxireduceq1.yml
value=`cat taxireduceq1.yml`
if [[ "$value" != *"environment"* ]]; then
	sed -i "    environment:\n      bucketinput: \"map1output\"\n      bucketoutput: \"result1\"" >> taxireduceq1.yml
fi

faas-cli build -f taxireduceq1.yml
faas-cli deploy -f taxireduceq1.yml
cd ..

