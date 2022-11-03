
import pandas as pd
import numpy as np
import datetime as dt

def preprocess_stats(df): 
    df = df.drop(['pos', 'comment'],  axis = 1)
    df = df[df['min'] != '0:00']
    df = df.dropna()
    
    df['min'] = df['min'].str.split(':')
    df['min'] = df['min'].apply(lambda x: dt.timedelta(minutes = int(x[0]), seconds = int(x[1])))
    df['min'] = df['min'].dt.total_seconds()/60
    
    return df
