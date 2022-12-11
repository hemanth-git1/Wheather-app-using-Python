### We will now use our weather tracker to decide where to go on a holiday for a week.

#### In our second milestone, using OIKO as a the weather tracker, we want to compare 2 cities for a given week. We want to select that city whose variance is the least.

import json
import pandas as pd
import requests
import datetime


def get_temperature_variance(city, start_date, end_date):
    URL='https://api.oikolab.com/weather'
    OKIO_KEY='794af116d28b4baf86e9fb4ea4a42fc6'
    resp=requests.get(URL,
                     params={
                         'param':['temperature'],
                         'start':start_date,
                         'location' :city,
                         'end':end_date,
                         'api-key':OKIO_KEY,
                         'freq':'D'
                       }
    )

    print(resp.json())
    weather_data = json.loads(weather_data)
    df=pd.DataFrame(index=pd.to_datetime(weather_data['index'],unit='s'),
                    data=weather_data['data'],
                    columns=weather_data['columns'])
    variance = df['temperature (degC)'].var()
    return variance

city1 = input()
city2 = input()
start_date = input()
start_date = start_date.split('-')
obj1 = datetime.datetime(int(start_date[0]), int(start_date[1]),int(start_date[2]))
obj2 = obj1 + datetime.timedelta(days=7)

start_date = obj1.strftime('%y-%m-%d')
end_date = obj2.strftime('%y-%m-%d')

var1 = get_temperature_variance(city1, start_date, end_date)
var2 = get_temperature_variance(city2, start_date, end_date)

if var1<var2:
    print(f"We choose {city1} because of less temperature variance")
else:
    print(f"We choose {city2} because of less temperature variance")
    
