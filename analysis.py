# Katie Li
# 06/17/2015

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

## A static function that calcuates the descriptive statistics 
## assumes that all variable in nvar, timeframe are in the dataframe (df)
def analyzeVariables(df, timeFrame, nvar):
  baseList = ['Date', timeFrame, 'copy_' + timeFrame]
  header = list(df.columns)
  for var in nvar: 
    if var in header: 
      baseList.append(var)
    else:
      raise Exception("header var not found")

  df2 = df[baseList]
  ## adds the timeframe for the groupby values
  tempVar = nvar + [timeFrame]
  print(tempVar)
  print(nvar)
  grouped = df2[tempVar].groupby(timeFrame)
  df2 = grouped.agg([np.sum, np.mean, np.std])
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
  FILENAME= "data.csv"
  DEFAULT_HEADER =59
  NVARS= ['Precip', 'Air max', 'Air min', 'ETo']
  df = pd.read_csv(FILENAME, header=DEFAULT_HEADER, delim_whitespace=False)

  TIMEFRAME= ["month","year"]
  f =  lambda u: int(str(u)[4:-2]) #helper functions that get month 
  f2 = lambda u: int(str(u)[:-4])   # and date
  df['month'] = df['Date'].map(f) 
  df['year'] = df['Date'].map(f2) 
  df['copy_month'] = df['month']
  df['copy_year'] = df['year']

  ## create two csv files for each of the timeframes
  for tf in TIMEFRAME:
    result = analyzeVariables(df, tf, NVARS)
    result.to_csv("csv/data-processed-" + tf + ".csv", encoding='utf-8')

  print("Analysis completed")
