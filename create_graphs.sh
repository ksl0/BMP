## Creates 4 graphs: temperature min, temperature max, precipitation, and evapotranspiration
mkdir graphs
python3 simple_analysis.py data.csv Air_max 'Maximum Temperature'  Fahrenheit
python3 simple_analysis.py data.csv Air_min 'Minimum Temperature'  Fahrenheit
python3 simple_analysis.py data.csv Precip Precipitation inches 
python3 simple_analysis.py data.csv "ETo" "Reference evapotranspiration  Inches" inches 

