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

