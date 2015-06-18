# Katie Li
# 06/17/2015

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

## get rid of missing data for specified variable

def analyzeVariables(df, timeFrame, nvar):
  baseList = ['Date', timeFrame, 'copy_' + timeFrame]
  header = list(df.columns)
  for var in nvar: 
    if var in header: 
      baseList.append(var)
    else:
      print("header var not found")

  df2 = df[baseList]
  print(baseList)
  print(df2.info())
  ## adds the timeframe for the groupby values
  nvar.append(timeFrame)
  print("okay")
  grouped = df2[nvar].groupby(timeFrame)
  df2 = grouped.agg([np.sum, np.mean, np.std])
  print("finished 1")
  return df2

## create simple, minimalistic plot
def createPlot(timeFrame, plotTitle, variable, units, df2):
  plt.cla()
  plt.title("\n".join(wrap(" Mean for each " + timeFrame + " , "+ plotTitle + \
            " 1989 - 2015,  Pomona California", 50)))
  plt.xlabel('Time '+ timeFrame, fontsize=12, color='black')
  plt.ylabel(plotTitle+ " " +  units, fontsize = 12, color='black')
  plt.plot(df2['copy_' + timeFrame], df2[variable], color="#078ccc", marker='o')
  plt.savefig('graphs/'+ plotTitle+ timeFrame + ".png")
  plt.cla()

## process data and create a csv from timeframe
if __name__ == '__main__': 
  filename = "data.csv"
  DEFAULT_HEADER =59
  df = pd.read_csv(filename, header=DEFAULT_HEADER, delim_whitespace=False)

  timeframe = ["month","year"]
  f =  lambda u: int(str(u)[4:-2]) 
  f2 = lambda u: int(str(u)[:-4])
  df['month'] = df['Date'].map(f) 
  df['year'] = df['Date'].map(f2) 
  df['copy_month'] = df['month']
  df['copy_year'] = df['year']

  nvars= ['Precip', 'Air max']

  for tf in timeframe:
    result= analyzeVariables(df, tf, nvars)
    result.to_csv("csv/data-processed" + tf + ".csv", encoding='utf-8')

  print("Done")
