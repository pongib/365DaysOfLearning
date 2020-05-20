### SLICE

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])

# Try to subset rows from Lahore to Moscow
# This is wrong but beware np isn't throw error on data that doesn't make sense
# This case is try to use inner index as key to slice for outter index
print(temperatures_srt.loc['Lahore':'Moscow'])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan', 'Lahore'):('Russia', 'Moscow')])



# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'avg_temp_c'])
 
### USE WITH DATE TIME
# The important thing to remember is to keep your dates in ISO 8601 format, that is, yyyy-mm-dd

# _Note that because the date isn't set as an index, a condition that contains only a year, 
# such as df['date'] == '2009', will check if the date is equal to the first day of the first month of the year (e.g. 2009-01-01), 
# rather than checking whether the date occurs within the given year.

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
c2010 = (temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2010-12-31')
c2011 = (temperatures['date'] >= '2011-01-01') & (temperatures['date'] <= '2011-12-31')
print(temperatures[c2010 | c2011])

# Set date as an index
temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
# Slice all year
print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08-01':'2011-02-28'])

## iloc

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22,1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])


## PIVOT SLICE

# Add a year column to temperatures
# dataframe["column"].dt.component. 
# For example, the month component is dataframe["column"].dt.month, and the year component is dataframe["column"].dt.year
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=['country', 'city'], columns='year')

# See the result
print(temp_by_country_city_vs_year)

# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc['Egypt':'India'])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi')])

# Subset in both directions at once
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi'), '2005':'2010'])


# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis='index')

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')


# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])