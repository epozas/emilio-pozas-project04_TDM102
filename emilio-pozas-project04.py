import pandas as pd
myDF= pd.read_csv("/anvil/projects/tdm/data/noaa/1880.csv",header=None,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
for index, row in myDF.iterrows():
    if row['element_code'] == "PRCP":
        if row["value"] >= 1200:
            print(row['date'])
myDF[(myDF.element_code == 'PRCP') & (myDF.value >= 1200)]['date']

from pathlib import Path
for year in range(1800,1851):
    file_path = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myDF = pd.read_csv(file_path,header=None,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    prcp_avg = myDF[myDF['element_code']=='PRCP']['value'].mean()
    print(f'The average precipation is {prcp_avg} for the year {year}')
    
prcp_avg = 0
year = 1800
while prcp_avg <= 22 and year <= 1850:
    file_path = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myDF = pd.read_csv(file_path,header=None,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    prcp_avg = myDF[myDF['element_code']=='PRCP']['value'].mean()
    print(f'The average precipation is {prcp_avg} for the year {year}')
    year += 1
    
myDF[myDF['element_code'] == 'PRCP'].groupby('id')['value'].mean().sort_values()
myDF[myDF['element_code'] == 'PRCP'].groupby('id')['value'].mean().sort_values()['USC00288878']

myDF[myDF['element_code'] == 'PRCP'].groupby('id')['value'].mean().sort_values().to_dict()

for year in range(1800,1811):
    file_path = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myDF1 = pd.read_csv(file_path,header=None,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    value_avg = myDF1['value'].mean()
    print(f'The value is {value_avg} for the year {year}')
    
value_avg = 0
year = 1800
while year <= 1810:
    file_path = Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myDF2 = pd.read_csv(file_path,header=None,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
    value_avg = myDF2['value'].mean()
    print(f'The average value is {value_avg} for the year {year}')
    year += 1