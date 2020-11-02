import csv
import pandas as pd

folder_path = 'data/'
lapTimes = pd.read_csv(folder_path + 'lapTimes.csv', encoding='latin-1')
races = pd.read_csv(folder_path + 'races.csv', encoding='latin-1')
drivers = pd.read_csv(folder_path + 'drivers.csv', encoding='latin-1')
results = pd.read_csv(folder_path + 'results.csv', encoding='latin-1')
circuits = pd.read_csv(folder_path + 'circuits.csv', encoding='latin-1')
status = pd.read_csv(folder_path + 'status.csv', encoding='latin-1')
top_100 = pd.read_csv(folder_path + 'top_100_score.csv', encoding='latin-1', index_col = False)
top_100 = top_100.drop(['year'], axis=1)
print(top_100)

#print(results[results['raceId'] == 973][['resultId', 'raceId', 'driverId','grid', 'position', 'statusId']])

#print(status[status['statusId'].isin([131, 4, 130])])