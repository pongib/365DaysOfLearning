# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9

# Rename 'F' in column names with 'C': temps_c.columns
# It very trick for change via str function and can use all str function can do.
temps_c.columns = temps_c.columns.str.replace('F', 'C')

# Print first 5 rows of temps_c
print(temps_c.head())

import pandas as pd

# Read 'GDP.csv' into a DataFrame: gdp
# Need parse_dates=True when use with data index.
gdp = pd.read_csv('GDP.csv', index_col='DATE', parse_dates=True)
# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp.loc['2008':]

# Print the last 8 rows of post2008
print(post2008.tail(8))

# Resample post2008 by year, keeping last(): yearly
# Resample is just like groupby with select date time.
# A is anually, can be 3D mean select every 3 day of data from date.
# it combine with stat function like mean.
# Ref: https://www.w3resource.com/pandas/series/series-resample.php
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)

# Compute percentage growth of yearly: yearly['growth']
# show change every value
yearly['growth'] = yearly.pct_change() * 100

#               VALUE    growth
# DATE                         
# 2008-12-31  14549.9       NaN
# 2009-12-31  14566.5  0.114090
# 2010-12-31  15230.2  4.556345
# 2011-12-31  15785.3  3.644732
# 2012-12-31  16297.3  3.243524
# 2013-12-31  16999.9  4.311144
# 2014-12-31  17692.2  4.072377
# 2015-12-31  18222.8  2.999062
# 2016-12-31  18436.5  1.172707

# Print yearly again
print(yearly)

# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv', parse_dates=True, index_col='Date')

# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv', parse_dates=True, index_col='Date')

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open', 'Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
# It better than * only because it more control with axis to calculate
# dataframe.multiply(series)

pounds = dollars.multiply(exchange['GBP/USD'], axis='rows', fill_value=0)
# normally it should same column for * to work.
# Can do with only series but can't with df.
pounds = dollars['Close'] * exchange['GBP/USD']

# fill_value=0 in multiply will replace NaN with 0
# NaN will show if index key from 2 df is not the same.
# See slide "MERGING DATAFRAMES WITH PANDAS" in arithmetic section for example .

# Print the head of pounds
print(pounds.head())