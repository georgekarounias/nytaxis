cd _history
foldername=`date +"project_v_%d-%m-%y_%T"`
mkdir $foldername
cd ..
cp -aR q1 q2 q3 _history/$foldername
echo "Project files: (q1 q2 q3) backed up in _history/"$foldername
