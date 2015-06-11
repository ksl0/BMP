# Katie Li
# 06/09/2015
# example use: python3 simple_analysis.py data.csv Testing Time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

## readin arguments from command line
if len(sys.argv) > 3:
  filename = sys.argv[1]
  variable = sys.argv[2]
  graphName = sys.argv[3]
  if len(sys.argv) > 4: 
    units = sys.argv[4] # units are optional
  else:
    units = ""
else: 
  raise Exception("Incorrect number of arguments")

DEFAULT_HEADER =60
df = pd.read_csv(filename, header=DEFAULT_HEADER, delim_whitespace=False)

f =  lambda u: int(str(u)[4:-2]) 
df['month'] = df['Date'].map(f) 
## get rid of missing data for specified variable
df2 = df[['Date', variable,'month']].dropna()
df2['copy_month'] = df2['month']
## average by monthly data
df2 = df2.groupby('month').mean()

## create simple, minimalistic plot
plt.cla()
plt.title("\n".join(wrap("Monthly mean for " + graphName + " 1989 - 2015,  Pomona California", 50)))
plt.xlabel('Time (month)', fontsize=12, color='black')
plt.ylabel(graphName+ " " +  units, fontsize = 12, color='black')
plt.plot(df2['copy_month'], df2[variable], color="#078ccc", marker='o')
plt.xlim([0.5,12.5])
plt.savefig('graphs/'+ graphName + ".png")
plt.cla()
