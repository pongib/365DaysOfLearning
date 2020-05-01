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
