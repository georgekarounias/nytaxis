1. Create buckets (manually, see BucketNames.txt)
2. Create Functions
3. Create Webhooks (with script ./create-webhooks.sh)
4. Build-Deploy functions (with script ./run.sh)
5. Assign Webhooks to buckets (manually)
	a) preprocess -> preprocess(put)
	b) commoninput -> taximapq1(put)
	c) commoninput -> taximapq2(put)
	d) commoninput -> taximapq3(put)
	e) map1output -> taxireduce1(put)
	f) map2output -> taxireduce2(put)
	g) map3output -> taxireduce3(put)
6. Add fares.csv to _data folder 
6. Run readData.py to create batches of 100 records
7. Upload a batch(_data/batches) to preprocess bucket
8. See results 

**** NOTE ****
Do not run create.sh
