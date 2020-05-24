# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar', title='Number of bar')

# Show the plot
plt.show()


# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x='date', y='nb_sold', kind='line', rot=34)

# Show the plot
plt.show()


# Scatter plots are ideal for visualizing relationships between numerical variables. In this exercise, you'll compare the number of avocados sold to average price and see if they're at all related. If they're related, you may be able to use one number to predict the other.

# Scatter plot of nb_sold vs avg_price with title
avocados.plot(kind='scatter', x='nb_sold', y='avg_price', title='Number of avocados sold vs. average price')

# Show the plot
plt.show()




# Histogram of conventional avg_price 
avocados[avocados['type'] == 'conventional']['avg_price'].hist()

# Histogram of organic avg_price
avocados[avocados['type'] == 'organic']['avg_price'].hist()

# Add a legend
# plt.legend(____)
plt.legend(['conventional', 'organic'])

# Show the plot
plt.show()

# Modify histogram transparency to 0.5 
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()


# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5,bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()



# With fill NaN value



# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
# Show column that have NaN or not
print(avocados_2016.isna().any())

# date               False
# avg_price          False
# total_sold         False
# small_sold          True
# large_sold          True
# xl_sold             True
# total_bags_sold    False
# small_bags_sold    False
# large_bags_sold    False
# xl_bags_sold       False


# Will sum NaN in each column
avocados_2016.isna().sum()

# date               0
# avg_price          0
# total_sold         0
# small_sold         6
# large_sold         6
# xl_sold            4
# total_bags_sold    0
# small_bags_sold    0
# large_bags_sold    0
# xl_bags_sold       0

# Bar plot of missing values by variable
# Can plot graph from sum data
avocados_2016.isna().sum().plot(kind='bar', rot=35)


# Show plot
plt.show()

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Remove specific rows with missing values
avocados_complete = avocados_2016.dropna(subset=['small_sold', 'large_sold'])



# Check if any columns contain missing values
print(avocados_complete.isna().any())

# List the columns with missing values
cols_with_missing = list(map(lambda x: x[0], filter(lambda x: x[1] == True, avocados_2016.isna().any().items())))
# Equal to cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()