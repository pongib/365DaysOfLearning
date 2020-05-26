# Import pandas
import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())



# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for file in filenames:
    dataframes.append(pd.read_csv(file))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())

# Use list comprehensive
dataframes2 = [pd.read_csv(file) for file in filenames]
print(dataframes2[0].head())