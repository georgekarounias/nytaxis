import pandas as pd

size = 100

print("Reading fares.csv file")
df = pd.read_csv (r'./_data/fares.csv')
for i, g in df.groupby(df.index // size):
    print(f"Creating {i} csv file" )
    g.to_csv(f'./_data/batches/output{i}.csv', index=False)
    # csv = pd.read_csv (f'./_data/batches/output{i}.csv')
    # csv.to_json (f'./_data/batches/output{i}.json')
    # os.remove(f'./_data/batches/output{i}.csv')