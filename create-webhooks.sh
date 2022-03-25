myIP=$(hostname -I | awk '{print $1}')
printf "%s\n" "$myIP"

cd 
./mc admin config set minio notify_webhook:"preprocess" queue_limit="1000" endpoint="http://$myIP:8080/function/preprocess" queue_dir=""

./mc admin config set minio notify_webhook:"taximapq1" queue_limit="1000" endpoint="http://$myIP:8080/function/taximapq1" queue_dir=""

./mc admin config set minio notify_webhook:"taxireduce1" queue_limit="1000" endpoint="http://$myIP:8080/function/taxireduceq1" queue_dir=""


./mc admin config set minio notify_webhook:"taximapq2" queue_limit="1000" endpoint="http://$myIP:8080/function/taximapq2" queue_dir=""

./mc admin config set minio notify_webhook:"taxireduce2" queue_limit="1000" endpoint="http://$myIP:8080/function/taxireduceq2" queue_dir=""


./mc admin config set minio notify_webhook:"taximapq3" queue_limit="1000" endpoint="http://$myIP:8080/function/taximapq3" queue_dir=""

./mc admin config set minio notify_webhook:"taxireduce3" queue_limit="1000" endpoint="http://$myIP:8080/function/taxireduceq3" queue_dir=""
./mc admin service restart minio

