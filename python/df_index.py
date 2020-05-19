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