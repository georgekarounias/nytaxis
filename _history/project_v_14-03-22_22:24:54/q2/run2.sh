cd map
faas-cli build -f taximapq2.yml
faas-cli deploy -f taximapq2.yml
cd ../reduce
faas-cli build -f reduce/taxireduceq2.yml
faas-cli deploy -f reduce/taxireduceq2.yml
cd ..
