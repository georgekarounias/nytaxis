myIP=$(hostname -I | awk '{print $1}')
printf "%s\n" "$myIP"

cd 
./mc admin config set minio notify_webhook:1 queue_limit="1000" endpoint="http://$myIP:8080/function/taximapq1" queue_dir=""
./mc admin service restart minio
./mc admin config set minio notify_webhook:2 queue_limit="1000" endpoint="http://$myIP:8080/function/taxireduceq1" queue_dir=""
./mc admin service restart minio

./mc admin config set minio notify_webhook:3 queue_limit="1000" endpoint="http://$myIP:8080/function/taximapq2" queue_dir=""
./mc admin service restart minio
./mc admin config set minio notify_webhook:4 queue_limit="1000" endpoint="http://$myIP:8080/function/taxireduceq2" queue_dir=""
./mc admin service restart minio

./mc admin config set minio notify_webhook:5 queue_limit="1000" endpoint="http://$myIP:8080/function/taximapq3" queue_dir=""
./mc admin service restart minio
./mc admin config set minio notify_webhook:6 queue_limit="1000" endpoint="http://$myIP:8080/function/taxireduceq3" queue_dir=""
./mc admin service restart minio

