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
