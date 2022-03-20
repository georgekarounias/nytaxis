cd map
faas-cli build -f taximapq3.yml
faas-cli deploy -f taximapq3.yml
value=`cat taximapq3.yml`
if [[ "$value" != *"environment"* ]]; then
echo -e " environment:\n bucketinput: \"commoninput\"\n bucketoutput: \"map3output\"" >> taximapq3.yml
fi



cd ../reduce
faas-cli build -f taxireduceq3.yml
faas-cli deploy -f taxireduceq3.yml
value=`cat taxireduceq3.yml`
if [[ "$value" != *"environment"* ]]; then
echo -e " environment:\n bucketinput: \"map3output\"\n bucketoutput: \"result3\"" >> taxireduceq3.yml
fi
cd ..
