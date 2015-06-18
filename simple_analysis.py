# Katie Li
# 06/09/2015
# example use: python3 simple_analysis.py data.csv Testing Time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

filename = input("data file to read from:" ) 
DEFAULT_HEADER =60
df = pd.read_csv(filename, header=DEFAULT_HEADER, delim_whitespace=False)

f =  lambda u: int(str(u)[4:-2]) 
f2 = lambda u: int(str(u)[:-4])
df['month'] = df['Date'].map(f) 
df['year'] = df['Date'].map(f2) 
df['copy_month'] = df['month']
df['copy_year'] = df['year']
## get rid of missing data for specified variable

def analyzeOneVariable(df, timeFrame, variable):
  df2 = df[['Date', variable,timeFrame, 'copy_' + timeFrame]].dropna()
  df2 = df2.groupby(timeFrame).mean()
  df2['std_'+ variable] = df2[variable].std() 
  df2[variable+ "_Ustd"] = df2[variable] + df2['std_'+ variable] 
  df2[variable+ "_Dstd"] = df2[variable] - df2['std_'+ variable] 
  return df2

## create simple, minimalistic plot
def createPlot(timeFrame, plotTitle, variable, units, df2):
  plt.cla()
  plt.title("\n".join(wrap(" Mean for each " + timeFrame + " , "+ plotTitle + \
            " 1989 - 2015,  Pomona California", 50)))
  plt.xlabel('Time '+ timeFrame, fontsize=12, color='black')
  plt.ylabel(plotTitle+ " " +  units, fontsize = 12, color='black')
  plt.plot(df2['copy_' + timeFrame], df2[variable], color="#078ccc", marker='o')
  plt.plot(df2['copy_' + timeFrame], df2[variable +"_Ustd"], color="#000000")
  plt.plot(df2['copy_' + timeFrame], df2[variable + "_Dstd"], color="#000000")
  print(df2[[str('copy_'+ timeFrame),variable]])
  print(df2.index)
  plt.savefig('graphs/'+ plotTitle+ timeFrame + ".png")
  plt.cla()

if __name__ == '__main__': 
  df2 = analyzeOneVariable(df, "month", "Precip")
  createPlot("month", "Precipitation", "Precip", "", df2) 
  df2.to_csv("csv/MonthlyPrecip.csv", encoding='utf-8')

  df2 = analyzeOneVariable(df, "year", "Precip")
  createPlot("year", "Precipitation", "Precip", "(inches)", df2) 
  df2.to_csv("csv/YearlyPrecip.csv", encoding='utf-8')

  df2 = analyzeOneVariable(df, "year", "Air_max")
  createPlot("year", "Maximum temperature", "Air_max", "(F)", df2) 
  df2.to_csv("csv/MaxYearlyTemp.csv", encoding='utf-8')

  df2 = analyzeOneVariable(df, "month", "Air_max")
  createPlot("month", "Maximum temperature", "Air_max", "(F)", df2) 
  df2.to_csv("csv/MaxMonthlyTemp.csv", encoding='utf-8')



  print("Done")
