import pandas as pd
import numpy as np
from pandas import DataFrame
import datetime
from datetime import datetime

#Load csv into Dataframe
landslides = pd.read_csv('SLOPE.csv')
noslides = pd.read_csv('NOSLIDE_SLOPE.csv')
#Convert Date column to datetime
landslides['DATE'] = pd.to_datetime(landslides['DATE'])

#initialize date column to appened to noslides dataframe
date = DataFrame(index = np.arange(1418),columns = ['DATE'])
#initialize counter
i = 0
#Loop through noslides dataframe to find closest landslide and get its date
for lat, lon in zip(noslides['Lat'],noslides['Long']):
    diff = DataFrame(index = np.arange(1418),columns = ['Diff'])
    j = 0
    #create dataframe of differences in distance from slope
    for lat_test, lon_test in zip(landslides['Lat'],landslides['Long']):
        diff['Diff'][j] = abs(lat - lat_test) + abs(lon - lon_test)
        j+=1
    #fin index of minimum distance
    diff_index = diff['Diff'].idxmin(axis=1)
    #add date to weather dataframe
    date['DATE'][i] = landslides['DATE'][diff_index]
    if i % 100 == 0:
        print(i)
    i += 1


#add date dataframe onto noslides dataframe
lands = [noslides,date]
noslides = pd.concat(lands,axis=1)

#save dataframe to csv
noslides.to_csv('NOSLIDE_LIST.csv')
