cd map
faas-cli build -f taximapq1.yml
faas-cli deploy -f taximapq1.yml
cd ../reduce
faas-cli build -f reduce/taxireduceq1.yml
faas-cli deploy -f reduce/taxireduceq1.yml
cd ..
