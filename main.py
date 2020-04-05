import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import os
import seaborn as sns
from scipy import stats
import urllib.request
import math
import statistics

def df_cleanup(df_raw):
    df_clean = pd.DataFrame()
    for region in df_raw['Country/Region'].unique():
        # df_tmp = df_raw_confirmed.loc[df_raw_confirmed['Country/Region'] == region].sum().drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
        df_tmp = df_raw.loc[df_raw['Country/Region'] == region].sum()
        df_clean[region] = pd.Series(df_tmp)
    df_clean = df_clean.drop(['Province/State', 'Country/Region', 'Lat', 'Long'], axis = 0)
    return df_clean

def find_highest(df):
    highest = df.iloc[-1].sort_values(ascending=False)[:10].index
    return highest

def plot(df, regions, xlabel, ylabel, title, x_size=25, y_size=8, log_scale='off'):
    plt.figure(figsize=(x_size, y_size))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid()
    # plt.gca().set_yticks(np.arange(0, df.max().max(), df.max().max()/25))
    plt.rc('grid', linestyle=":", color='grey')
    for region in regions:
        x = df.index
        y = df[region]
        legend = df_confirmed.iloc[0].index
        plt.plot(x, y, marker='o', label=region)
    if 'on' in log_scale:
        plt.yscale("log")
    plt.legend(loc="upper left", ncol=3, title="Legend", fancybox=True)
    plt.savefig(title)
    plt.show()

# Data import
confirmed_name = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
death_name = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
recovered_name = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

# DataFrame cleanup
df_confirmed = df_cleanup(pd.read_csv(confirmed_name))
df_death = df_cleanup(pd.read_csv(death_name))
df_recovered = df_cleanup(pd.read_csv(recovered_name))

# Top countries are selected
top_countries = find_highest(df_confirmed)

# Plot of top countries
title = ["Confirmed", "Death", "Recovered"]
xlabel = ["Data", "Data", "Data"]
ylabel = ["Persone", "Persone", "Persone"]
picname = [title[0]+".jpg", title[1]+".jpg", title[2]+".jpg"]
df = [df_confirmed, df_death, df_recovered]

for i in range(len(title)):
    plot(df[i], top_countries, xlabel[i], ylabel[i], title[i])