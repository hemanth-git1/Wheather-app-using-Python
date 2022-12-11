## As we build our weather tracker, our first task will be to accurately get the temperatures and weather condition of given locations.

## In our first milestone, using OIKO as a the weather tracker, we want to find out the temperature of a given city at a given time.

##Input Format
##The first line contains the name of the first city
##The second line contains the date in the format YYYY-MM-DD.
##You need to print the temperature of the given city at the particular date.

###Check the examples for the required format

import json
import pandas as pd
import requests


city=input()
date=input()
url='https://api.oikolab.com/weather'
OKIO_KEY='b4c6e07e3a854aaa8166cb54f60cab8b'
resp= requests.get('https://api.oikolab.com/weather',
                   params={'param':['temperature'],
                           'start':date,
                           'end':date,
                           'location':city,
                           'api-key':OKIO_KEY,
                           'freq':'D'})




weather_data = resp.json()['data']
weather_data = json.loads(weather_data)
df=pd.DataFrame(index=pd.to_datetime(weather_data['index'],unit='s'),
                data=weather_data['data'],
                columns=weather_data['columns'])
temp=int(df.iloc[0,4])
print(f"Temperature for {city} on {date} = {temp}C")




