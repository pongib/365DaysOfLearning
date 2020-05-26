# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index(['city'])

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))



# Make a list of cities to subset on
cities = ['Moscow', 'Saint Petersburg']

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

#                        date country  avg_temp_c
# city                                           
# Moscow           2000-01-01  Russia      -7.313
# Moscow           2000-02-01  Russia      -3.551
# Moscow           2000-03-01  Russia      -1.661
# Moscow           2000-04-01  Russia      10.096
# Moscow           2000-05-01  Russia      10.357
# ...                     ...     ...         ...
# Saint Petersburg 2013-05-01  Russia      12.355
# Saint Petersburg 2013-06-01  Russia      17.185
# Saint Petersburg 2013-07-01  Russia      17.234
# Saint Petersburg 2013-08-01  Russia      17.153




# Multi level index

# Indexes can also be made out of multiple columns, forming a multi-level index (sometimes called a hierarchical index). There is a trade-off to using these.

# The benefit is that multi-level indexes make it more natural to reason about nested categorical variables. For example, in a clinical trial you might have control and treatment groups. Then each test subject belongs to one or other group, and we can say that test subject is nested inside treatment group. Similarly, in the temperature dataset, the city is located in the country, so we can say city is nested inside country.

# The main downside is that the code for manipulating indexes is different to the code for the manipulating columns, so you have to learn two syntaxes, and keep track of how your data is represented.


# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])
#                               date  avg_temp_c
# country  city                                 
# Brazil   Rio De Janeiro 2000-01-01      25.974
#          Rio De Janeiro 2000-02-01      26.699
#          Rio De Janeiro 2000-03-01      26.270
#          Rio De Janeiro 2000-04-01      25.750
#          Rio De Janeiro 2000-05-01      24.356
# ...                            ...         ...
# Pakistan Lahore         2013-05-01      33.457
#          Lahore         2013-06-01      34.456
#          Lahore         2013-07-01      33.279
#          Lahore         2013-08-01      31.511
#          Lahore         2013-09-01         NaN

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=['country', 'city'], ascending=[True, False]))


# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

# Print the head of medals
print(medals.head())


# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())




# Import pandas
import pandas as pd

# year is ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# weather1 index is Index(['Apr', 'Jan', 'Jul', 'Oct'], dtype='object', name='Month')
# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)
#               Mean TemperatureF
# Month                   
# Jan            32.133333
# Feb                  NaN
# Mar                  NaN
# Apr            61.956044
# May                  NaN
# Jun                  NaN
# Jul            68.934783
# Aug                  NaN
# Sep                  NaN
# Oct            43.434783
# Nov                  NaN
# Dec                  NaN

# Print weather2
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()

#           Mean TemperatureF
# Month                   
# Jan            32.133333
# Feb            32.133333
# Mar            32.133333
# Apr            61.956044
# May            61.956044
# Jun            61.956044
# Jul            68.934783
# Aug            68.934783
# Sep            68.934783
# Oct            43.434783
# Nov            43.434783
# Dec            43.434783

# Print weather3
print(weather3)


# Import pandas
import pandas as pd

# how to read csv
# names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
# use name and gender as index


# Shape of names_1981 DataFrame: (19455, 1)
# Shape of names_1881 DataFrame: (1935, 1)

# Reindex names_1981 with index of names_1881: common_names
# It like join names_1981 column with names_1881 column
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)
# (1935, 1) It like names_1981 RIGHT JOIN names_1881 index from names_1881 but value is from names_1981
# and row that didn't have value in names_1981 will result to NaN


# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)
# (1587, 1) So it mean names_1881 have index that does exist in names_1981 because some value are NaN