# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])


### Select only row

# Print out first 3 observations
print(cars[0:3])

## Row only

# Print out observation for Japan
print(cars.loc['JPN'])
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])



# ROW and COLUMN

# Print out drives_right value of Morocco
print(cars.loc[['MOR'], ['drives_right']])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

## Use with slice

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])



### filter data
# step
# 1. get column to series.
# 2. do a condition expresstion like >, <, logical_and, logical_or.
# 3. subset df, apply that expresstion to dataframe to get only data that meet condition.
# Example
# cpc = cars['cars_per_cap']
# between = np.logical_and(cpc > 10, cpc < 80)
# medium = cars[between]

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars['cars_per_cap'] > 500]

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)]

# Print car_maniac
print(car_maniac)


# All different type
# Dataframe
In[4]: cars.loc[['US'], ['cars_per_cap']]
Out[4]: 
    cars_per_cap
US           809
# Series
In [5]: cars.loc[['US'], 'cars_per_cap']
Out[5]: 
US    809
Name: cars_per_cap, dtype: int64
# Numpy int64 it return that data type.
In [6]: cars.loc['US', 'cars_per_cap']
Out[6]: 809

In [7]: type(cars.loc['US', 'cars_per_cap'])
Out[7]: numpy.int64

In [8]: type(cars.loc[['US'], 'cars_per_cap'])
Out[8]: pandas.core.series.Series

In [9]: type(cars.loc[['US'], ['cars_per_cap']])
Out[9]: pandas.core.frame.DataFrame

In [10]: type(cars.loc['US', ['cars_per_cap']])
Out[10]: pandas.core.series.Series




# Use loop through dataframe
# And add column to df.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use normal for and row is series
# access row['country'] return string.
# access row['cars_per_cap'] return <class 'numpy.int64'> for digit.
# access row['drives_right'] return <class 'numpy.bool_'> for boolean.
# Below is example of Dataframe.
#      cars_per_cap   country  drives_right COUNTRY
# US    809    United States     True   UNITED STATES
# This cars.loc[lab, "COUNTRY"] will create new column string.
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Use .apply(str.upper) without for loop.
# This is faster than for loop because it not create series everytime
# it apply str.upper on each element and return array that store to series in one time.
cars['COUNTRY'] = cars['country'].apply(str.upper)

# Can loop through series object.
for c in cars['country']:
    print(c)
    # it print each country from series
    # United States
    # Australia
    # Japan
    # India
    # Russia
    # Morocco
    # Egypt

print(cars)

# THIS IS cars after add column
#     cars_per_cap        country  drives_right        COUNTRY
# US            809  United States          True  UNITED STATES
# AUS           731      Australia         False      AUSTRALIA
# JPN           588          Japan         False          JAPAN
# IN             18          India         False          INDIA
# RU            200         Russia          True         RUSSIA
# MOR            70        Morocco          True        MOROCCO
# EG             45          Egypt          True          EGYPT