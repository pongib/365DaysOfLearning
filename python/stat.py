# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

print(sales.describe())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())

# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

# It calculate per function in agg list and return df
#         temperature_c  fuel_price_usd_per_l  unemployment
# iqr            16.583                 0.073         0.565
# median         16.967                 0.743         8.099


# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date', ascending=True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

sales_1_1['cum_min_sales'] = sales_1_1['weekly_sales'].cummin()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales", 'cum_min_sales']])


## COUNT

# Count the number of stores of each type
store_counts = stores['store_type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = stores['store_type'].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = departments['department_num'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = departments['department_num'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

## Drop duplicate

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset='store')
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Print date col of holiday_dates
print(holiday_dates['date'])


### PIVOT
# Import NumPy as np
import numpy as np

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')

# Print mean_sales_by_type
print(mean_sales_by_type)

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='weekly_sales', index='department', columns='type', fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))


#### Group by

### Classic way without group by
# Calc total weekly sales
sales_all = sales['weekly_sales'].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales['type'] == 'B']['weekly_sales'].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales['type'] == 'C']['weekly_sales'].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)


#### Group by

# Group by type; calc total weekly sales
sales_by_type = sales.groupby('type')['weekly_sales'].sum()
# Get proportion for each type
sales_propn_by_type = [sales_by_type['A'], sales_by_type['B']] / sales_by_type.sum()
print(sales_propn_by_type)

# Import NumPy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)


# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)


# type  is_holiday
# A     False         2.337e+08
#       True          2.360e+04
# B     False         2.318e+07
#       True          1.621e+03
# Name: weekly_sales, dtype: float64

# # For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


# unemployment                      fuel_price_usd_per_l                     
#              amin   amax   mean median                 amin   amax   mean median
# type                                                                            
# A           3.879  8.992  7.973  8.067                0.664  1.107  0.745  0.735
# B           7.170  9.765  9.279  9.199                0.760  1.108  0.806  0.803

# try to fill all I learn today at once.
allgroup = sales.groupby(['type', 'is_holiday'])[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])
print(allgroup)
print(allgroup.shape) # (4, 8)
#                                      unemployment                      fuel_price_usd_per_l                     
#                         amin   amax   mean median                 amin   amax   mean median
# type is_holiday                                                                            
# A    False             3.879  8.992  7.973  8.067                0.664  1.107  0.744  0.735
#      True              5.143  8.992  7.835  7.925                0.673  1.077  0.815  0.814
# B    False             7.170  9.765  9.281  9.199                0.760  1.108  0.806  0.803
#      True              7.874  9.199  8.537  8.537                0.782  0.993  0.888  0.888

print(allg.iloc[1,0]) # 5.143
# label multiple group by column use tuple as key can know by use allgroup.index for column is allgroup.columns
print(allg.loc[('A', True), ('unemployment', 'amin')]) # 5.143