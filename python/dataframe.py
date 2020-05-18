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




## GET DETAIL
# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)


# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending=False)

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())


# Select multiple column the state and family_members columns
state_fam = homelessness[['state', 'family_members']]

# filter 2 expreestion with & "and" operator don't forget () for each expression.
# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & (homelessness['region'] == 'Pacific')]

# See the result
print(fam_lt_1k_pac)


# Select multiple variable from one column.
# Subset for rows in South Atlantic or Mid-Atlantic regions

south_mid_atlantic = homelessness[(homelessness['region'] == 'South Atlantic') | (homelessness['region'] == "Mid-Atlantic")]

# Short hand to

south_mid_atlantic = homelessness[homelessness['region'].isin(['South Atlantic', 'Mid-Atlantic'])]

# See the result
print(south_mid_atlantic)

##################
# Add new column #
##################

# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Create indiv_per_10k col as homeless individuals per 10k state pop
# WAY to calculate number of homeless individuals per 10,000 people in the state
# face 10000 people will see how many homeless.
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']

# Add p_individuals col as proportion of individuals
homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']

# See the result
print(homelessness)



