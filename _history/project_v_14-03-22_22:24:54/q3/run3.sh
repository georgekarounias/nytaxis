cd map
faas-cli build -f taximapq3.yml
faas-cli deploy -f taximapq3.yml
cd ../reduce
faas-cli build -f taxireduceq3.yml
faas-cli deploy -f taxireduceq3.yml
cd ..
