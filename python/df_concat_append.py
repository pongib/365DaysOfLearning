# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv', parse_dates=True, index_col='Date')

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv', parse_dates=True, index_col='Date')

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv', parse_dates=True, index_col='Date')

# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']

# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']

# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']

# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)


# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015': 'mar 7, 2015'])

# Compute & print total sales in quarter1
print(quarter1.sum())

# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units)

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])



# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981

# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981, ignore_index=True)
# or use 
combined_names = names_1881.append(names_1981).reset_index(drop=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

# Print all rows that contain the name 'Morgan'
print(combined_names[combined_names['name'] == 'Morgan'])


# Create a list of weather_max and weather_mean
weather_list = [weather_max, weather_mean]

# Concatenate weather_list horizontally
weather = pd.concat(weather_list, axis=1)

# Print weather
print(weather)



''#Initialize an empyy list: medals
medals =[]

for medal in medal_types:
    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    # Create list of column names: columns
    columns = ['Country', medal]
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)
    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals_df
medals_df = pd.concat(medals, axis='columns')

# Print medals_df
print(medals_df)


for medal in medal_types:

    file_name = "%s_top5.csv" % medal
    
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')
    
    # Append medal_df to medals
    medals.append(medal_df)
    
# Concatenate medals: medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'])

# Print medals in entirety
print(medals)


#                         Total
#        Country               
# bronze United States   1052.0
#        Soviet Union     584.0
#        United Kingdom   505.0
#        France           475.0
#        Germany          454.0
# silver United States   1195.0
#        Soviet Union     627.0
#        United Kingdom   591.0
#        France           461.0
#        Italy            394.0
# gold   United States   2088.0
#        Soviet Union     838.0
#        United Kingdom   498.0
#        Italy            460.0
#        Germany          407.0



# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)


# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# # Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# # Print all the data on medals won by the United Kingdom
# use for select inner level key
print(medals_sorted.loc[idx[:, 'United Kingdom'], :])

#                        Total
#        Country              
# bronze United Kingdom  505.0
# gold   United Kingdom  498.0
# silver United Kingdom  591.0

# Concatenate dataframes: february
february = pd.concat(dataframes, axis=1, keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
# Can select inner level on columns
slice_2_8 = february.loc['Feb 2,2015':'Feb 8,2015', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)


#                             Hardware         Software Service
#                              Company          Company Company
# Date                                                         
# 2015-02-02 08:33:01              NaN            Hooli     NaN
# 2015-02-02 20:54:49        Mediacore              NaN     NaN
# 2015-02-03 14:14:18              NaN          Initech     NaN
# 2015-02-04 15:36:29              NaN        Streeplex     NaN
# 2015-02-04 21:52:45  Acme Coporation              NaN     NaN
# 2015-02-05 01:53:06              NaN  Acme Coporation     NaN
# 2015-02-05 22:05:03              NaN              NaN   Hooli
# 2015-02-07 22:58:10  Acme Coporation              NaN     NaN


# Make the list of tuples: month_list
# Can use with dict
month_list = [('january', jan), ('february', feb), ('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict, axis=0)

# Print sales
print(sales)

#                           Units
#          Company               
# february Acme Coporation     34
#          Hooli               30
#          Initech             30
#          Mediacore           45
#          Streeplex           37
# january  Acme Coporation     76
#          Hooli               70
#          Initech             37
#          Mediacore           15
#          Streeplex           50
# march    Acme Coporation      5
#          Hooli               37
#          Initech             68
#          Mediacore           68
#          Streeplex           40

# Print all sales by Mediacore

idx = pd.IndexSlice
print(sales.loc[idx[:,'Mediacore'], :])

#                     Units
#          Company         
# february Mediacore     45
# january  Mediacore     15
# march    Mediacore     68



# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, keys=['bronze', 'silver', 'gold'], axis=1, join='inner')

# Print medals
print(medals)



# sample data 

#             China
# Year                 
# 1961-01-01  49.557050
# 1962-01-01  46.685179
# 1963-01-01  50.097303
# 1964-01-01  59.062255
# 1965-01-01  69.709153
#              
#             US
# Year             
# 1947-04-01  246.3
# 1947-07-01  250.1
# 1947-10-01  260.3
# 1948-01-01  266.2
# 1948-04-01  272.9

# Resample and tidy china: china_annual
# Use offset that calculate from 10 year data it same as 10A
# in final resample for correct compare value.
china_annual = china.resample('A').last().pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').last().pct_change(10).dropna()


# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual, us_annual], axis=1, join='inner')


# Resample gdp and print
print(gdp.resample('10A').last())

#                China        US
# Year                          
# 1971-12-31  0.988860  1.052270
# 1981-12-31  0.972048  1.750922
# 1991-12-31  0.962528  0.912380
# 2001-12-31  2.492511  0.704219
# 2011-12-31  4.623958  0.475082
# 2021-12-31  3.789936  0.361780