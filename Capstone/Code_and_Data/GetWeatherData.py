import pandas as pd
from pandas import DataFrame
import datetime
from datetime import datetime
import time
import urllib
from urllib import urlopen
import json

#Load csv into Dataframe
landslides = pd.read_csv('landslide_short.csv')
print(list(landslides))
#Convert Date column to datetime
landslides['DATE'] = pd.to_datetime(landslides['DATE'])

#Define weather DataFrame
weather = DataFrame(columns = [u'coolingdegreedays',
 u'coolingdegreedaysnormal',
 'date.hour',
 'date.mday',
 'date.min',
 'date.mon',
 'date.pretty',
 'date.tzname',
 'date.year',
 u'fog',
 u'gdegreedays',
 u'hail',
 u'heatingdegreedays',
 u'heatingdegreedaysnormal',
 u'humidity',
 u'maxdewpti',
 u'maxdewptm',
 u'maxhumidity',
 u'maxpressurei',
 u'maxpressurem',
 u'maxtempi',
 u'maxtempm',
 u'maxvisi',
 u'maxvism',
 u'maxwspdi',
 u'maxwspdm',
 u'meandewpti',
 u'meandewptm',
 u'meanpressurei',
 u'meanpressurem',
 u'meantempi',
 u'meantempm',
 u'meanvisi',
 u'meanvism',
 u'meanwdird',
 u'meanwdire',
 u'meanwindspdi',
 u'meanwindspdm',
 u'mindewpti',
 u'mindewptm',
 u'minhumidity',
 u'minpressurei',
 u'minpressurem',
 u'mintempi',
 u'mintempm',
 u'minvisi',
 u'minvism',
 u'minwspdi',
 u'minwspdm',
 u'monthtodatecoolingdegreedays',
 u'monthtodatecoolingdegreedaysnormal',
 u'monthtodateheatingdegreedays',
 u'monthtodateheatingdegreedaysnormal',
 u'monthtodatesnowfalli',
 u'monthtodatesnowfallm',
 u'precipi',
 u'precipm',
 u'precipsource',
 u'rain',
 u'since1jancoolingdegreedays',
 u'since1jancoolingdegreedaysnormal',
 u'since1julheatingdegreedays',
 u'since1julheatingdegreedaysnormal',
 u'since1julsnowfalli',
 u'since1julsnowfallm',
 u'since1sepcoolingdegreedays',
 u'since1sepcoolingdegreedaysnormal',
 u'since1sepheatingdegreedays',
 u'since1sepheatingdegreedaysnormal',
 u'snow',
 u'snowdepthi',
 u'snowdepthm',
 u'snowfalli',
 u'snowfallm',
 u'thunder',
 u'tornado'])

#initialize counter
i = 0
print('Start Weather Collection...')
#Loop through landslide dataframe to find weather data at location and time
for lat, lon, day in zip(landslides['Lat'],landslides['Long'],landslides['DATE']):
    #Put date into string for api call
    if day.month < 10 and day.day < 10:
        date = str(day.year)+'0'+str(day.month)+'0'+str(day.day)
    elif day.month < 10 and day.day >= 10:
        date = str(day.year)+'0'+str(day.month)+str(day.day)
    elif day.month >= 10 and day.day < 10:
        date = str(day.year)+str(day.month)+'0'+str(day.day)
    else:
        date = str(day.year)+str(day.month)+str(day.day)
    print(date)
    print(lat)
    print(lon)
    #get json data for the day and time from weather underground
    f = urlopen('http://api.wunderground.com/api/a84d24bae894ca8e/history_{2}/geolookup/q/{0},{1}.json'.format(str(lat),str(lon),str(date)))
    json_string = f.read()
    parsed_json = json.loads(json_string)
    #transform the json file into dataframe
    date_sum = pd.io.json.json_normalize(parsed_json['history']['dailysummary'])
    #add date and location to weather dataframe
    frames = [weather,date_sum]
    weather = pd.concat(frames,ignore_index=True)
    f.close()
    if i % 100 == 0:
        weather.to_csv('weather_40.csv')
        print(i)
    #pause code to allow only 10 calls per minute (per api key requirements)
    time.sleep(0.6)
    i += 1
print('End of Collection')
#add weather dataframe onto landslides dataframe
#lands = [landslides,weather]
#landslides = pd.concat(lands,axis=1)
weather.to_csv('weather_40.csv')
#save dataframe to csv
#landslides.to_csv('landslides_weather.csv')
