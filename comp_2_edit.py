import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

Energy_census = pd.read_csv('data/Energy Census and Economic Data US 2010-2014.csv')
df = pd.read_csv('data/cleaned_climate_zones.csv')
#df['State'].map(abv_state)

zone1 = [] #1-2
zone2 = [] #2-3
zone3 = [] #3-4
zone4 = [] #4-5

for ind, row in df.iterrows():
    if 4 < row['CBECS Climate Zone'] <= 5:
        zone4.append(row['State'])
    if 3 < row['CBECS Climate Zone'] <= 4:
        zone3.append(row['State'])
    if 2 < row['CBECS Climate Zone'] <= 3:
        zone2.append(row['State'])
    elif 1 <= row['CBECS Climate Zone'] <= 2:
        zone1.append(row['State'])

merger = pd.DataFrame([])

for ind,row in Energy_census.iterrows():
    if row['StateCodes'] in zone1:
        merger = merger.append(pd.DataFrame({
            'Zone' : 1,
            'State': row['StateCodes']
        }, index = [0]), ignore_index = True)
    if row['StateCodes'] in zone2:
        merger = merger.append(pd.DataFrame({
            'Zone' : 2,
            'State': row['StateCodes']
        }, index = [0]), ignore_index = True)
    if row['StateCodes'] in zone3:
        merger = merger.append(pd.DataFrame({
            'Zone' : 3,
            'State': row['StateCodes']
        }, index = [0]), ignore_index = True)
    elif row['StateCodes'] in zone4:
        merger = merger.append(pd.DataFrame({
            'Zone' : 4,
            'State': row['StateCodes']
        }, index = [0]), ignore_index = True)

merger = merger.merge(Energy_census, left_on='State', right_on='StateCodes', how='left')
merger = merger.drop(['StateCodes', 'State_x', 'State_y', 'Region', 'Division', 'Coast', 'Great Lakes'], axis=1)
merger = merger.groupby(['Zone']).mean()

print(merger)

