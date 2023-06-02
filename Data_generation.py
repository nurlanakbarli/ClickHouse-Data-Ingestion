


import datetime
from datetime import date
from random import randint
from sqlite3 import Date
import pandas as pd
import numpy as np
import numpy
import random
import requests

my_string ='*** UInt8, **** Array(String)'

fields = []
for elemt in my_string.split(','):
    elemt = elemt.strip('\'').lstrip(' ')
    fields.append(elemt.split(" "))


N = 10
startdate=datetime.date(2022,4,20)
datavec=[]
datevec=[str(startdate-datetime.timedelta(days=i)) for i in range(0,500)]
datavec=[random.sample(datevec, 250) for i in range(2)]
df = pd.DataFrame()



for itt in range(0,3):  
    for elmt in fields[:]:
        if ('scenarioVector' in elmt[0]):
            df[elmt[0]] = [ datavec[0] for i in range(N)]
        if ('scenarioVector' not in elmt[0] and 'String' in elmt[1] and 'Array' in elmt[1]):
            df[elmt[0]] = [[elmt[0]+str(random.randint(3000,5000)) for i in range(10)] for i in range(N)]
    
        if('String' in elmt[1] and 'Array' not in elmt[1]):
            df[elmt[0]] = [elmt[0]+str(random.randint(3000,5000)) for i in range(N)]
            df[elmt[0]] = df[elmt[0]]
        if('String' in elmt[1] and 'Array'  in elmt[1]):
            df[elmt[0]] = [[elmt[0]+str(random.randint(3000,5000)) for i in range(10)] for i in range(N)]

        if ('String' not in elmt[1] and 'Array' not in elmt[1]):
            if('Float' in elmt[1]):
                df[elmt[0]] = np.random.uniform(99.5,399.5,N).tolist()
            if('Int' in elmt[1]):
                df[elmt[0]] = np.random.randint(0,100000,N).tolist()
        if ('String' not in elmt[1] and 'Array' in elmt[1]):
            if ('Float' in elmt[1]):
                df[elmt[0]] = np.random.uniform(99.5,399.5,(N,25)).tolist()
            if('Int' in elmt[1]):
                df[elmt[0]] = np.random.randint(0, 100000, (N,25)).tolist()
        if('Date' in elmt[1] and 'DateTime' not in elmt[1]):
            df[elmt[0]] = [date(2023, 4, 14) for i in range(N)]
        if('DateTime' in elmt[1]):
            df[elmt[0]] = [datetime.datetime.now() for i in range(N)]
        if('Decimal' in elmt[1]):
            df[elmt[0]] = np.around(np.random.uniform(99.5,399.5,N), 2).tolist()
        if('UInt64' in elmt[1]):
                df[elmt[0]] = np.random.randint(0,100000,N).tolist()
    df.to_csv(f"13GapTimeBucket{N}_{itt}.csv",header=False,index=False)

