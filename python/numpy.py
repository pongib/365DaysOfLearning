# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light]) == print(bmi[bmi < 21])


# type in array must be same type, 
# finally numpy will type coercion to make every element in same type.
np.array([True, 1, 2]) + np.array([3, 4, False]) == np.array([4, 5, 2])


######### 2D Array #########

# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# print Shape
print(np_baseball.shape)

# Print out the 50th row of np_baseball
print(np_baseball[:51])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,1])


import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2

array([[ 2,  4],
       [ 6,  8],
       [10, 12]])

np_mat + np.array([10, 10])
# array([[11, 12],
#        [13, 14],
#        [15, 16]])
np_mat + np_mat

# array([[ 2,  4],
#        [ 6,  8],
#        [10, 12]])



# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion use to change to meter unit m and kg
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)



## BASIC STAT PART

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

## USE condition expresstion to filter data
np_positions = ['GK', 'A', 'MF', 'GK', 'A']
np_heights = [198, 180, 185, 191, 160]

(np_positions == 'GK') == [True, False, False, True, False]

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

## AND and OR

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house >= 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))


##### 
# LOOP over numpy
#####

# Import numpy as np
import numpy as np

# For loop over np_height
# it simple 1D array
for height in np_height:
    print(str(height)+" inches")

# np_baseball is 
# array([[ 74, 180],
#        [ 74, 215],
#        [ 72, 210],
#        ...,
#        [ 75, 205],
#        [ 75, 190],
#        [ 73, 195]])

# For loop over np_baseball
# it will loop through first column untill finish then to second column
# it will print 74,72,72,...,75,75,73 then print 180,215,210,...,205,190,195
for x in np.nditer(np_baseball):
    print(x)