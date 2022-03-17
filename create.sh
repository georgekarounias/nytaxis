cd _history
foldername=`date +"project_v_%d-%m-%y_%T"`
mkdir $foldername
cd ..
cp -aR q1 q2 q3 _history/$foldername
echo "Project backed up in _history/"$foldername
cd q1
./create1.sh
cd ../q2
./create2.sh
cd ../q3
./create3.sh
cd ..

