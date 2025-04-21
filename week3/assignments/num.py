import numpy as np

serial_number, list_year, town, assessed_value, sale_amount = np.genfromtxt(
    "python_repo/week3/assignments/Real_Estate_Sales_2001-2022_GL-Short.csv",
    delimiter=",",
    unpack=True,
    dtype=None,
    skip_header=1,
    usecols=(0, 1, 3, 5, 6),
    invalid_raise=False,
)

print("The sale amount is : ", sale_amount)
print("The serial number is : ", serial_number)
print("The list year is : ", list_year)
print("The town is : ", town)
print("The assessed value is : ", assessed_value)




# 2. Perform following operation on array of ““Sale Amount”:
# As identified in theory at notes here:
# https://github.com/ShahzadSarwar10/AI-ML￾Explorer/blob/main/Week2/Artificial%20Intelligence%20(Machine%20Learning%20%26%20Dee
# p%20Learning)-Week2-Day4nDay5-Descriptive%20Statistics%20and%20Probability￾Notes_Rev1.pdf
# sequentially and one by one- ALL operations like MODE, MEDIAN, SD and Print it.
# ALL Please. Verify that all stats calculation – are covered.

from scipy import stats

# Mode
mode_sale_amount = stats.mode(sale_amount, keepdims=True)
print(f"Mode: {mode_sale_amount.mode[0]}")

# Median
median_sale_amount = np.median(sale_amount)
print(f"Median: {median_sale_amount}")

# Standard Deviation
std_sale_amount = np.std(sale_amount)
print(f"Standard Deviation: {std_sale_amount}")



# Perform following operation on array of “Assessed Value”:
# As identified in theory at notes here:
# https://github.com/ShahzadSarwar10/AI-ML￾Explorer/blob/main/Week2/Artificial%20Intelligence%20(Machine%20Learning%20%26%20Dee
# p%20Learning)-Week2-Day4nDay5-Descriptive%20Statistics%20and%20Probability￾Notes_Rev1.pdf
# sequentially and one by one- ALL operations like MODE, MEDIAN, SD – and Print it.
# ALL Please. Verify that all stats calculation – are covered.
# Mode
mode_assessed_value = stats.mode(assessed_value, keepdims=True)
print(f"Mode: {mode_assessed_value.mode[0]}")

# Median
median_assessed_value = np.median(assessed_value)
print(f"Median: {median_assessed_value}")

# Standard Deviation
std_assessed_value = np.std(assessed_value)
print(f"Standard Deviation: {std_assessed_value}")


# Perform following operations on - array of [array of ““Sale Amount”] and [array of “Assessed 
# Value”]
# Addition [ via both operator “+” and method “Add”] - Print it.
# Substrat [ via both operator “-” and method “sub”] - Print it.
# Mulitply [ via both operator “*” and method “multi”] - Print it.
# Addition
addition_operator = sale_amount + assessed_value
addition_function = np.add(sale_amount, assessed_value)

# Subtraction
subtraction_operator = sale_amount - assessed_value
subtraction_function = np.subtract(sale_amount, assessed_value)

# Multiplication
multiplication_operator = sale_amount * assessed_value
multiplication_function = np.multiply(sale_amount, assessed_value)


# 5. Create a “2D array” based on array of [array of ““Sale Amount”] and [array of “Assessed Value”]
# Print it.
two_d_array = np.column_stack((sale_amount, assessed_value))
print(two_d_array)



# 6. Create a “3D array” based on array of [array of ““Sale Amount”] and [array of “Assessed Value”]
# and [array of “List Year”]
three_d_array = np.stack((sale_amount, assessed_value, list_year), axis=-1)
print(three_d_array)


# 7. Iterate the array - of [array of ““Sale Amount”]
# With function of “np.nditer(“
# Print each item.
# Understand it.
for value in np.nditer(sale_amount):
    print(value)



# 8. Iterate the array - of [array of ““Sale Amount”]
# With function of “np.ndenumerate(“
# Print each item.
# Understand it.
for index, value in np.ndenumerate(sale_amount):
    print(f"Index: {index}, Value: {value}")


# 9. Use 7 common properties of array - of [array of ““Sale Amount”].
# Ndim , shape , size……..use command 7 in code – print them
print(f"Number of Dimensions: {sale_amount.ndim}")
print(f"Shape: {sale_amount.shape}")
print(f"Size: {sale_amount.size}")
print(f"Data Type: {sale_amount.dtype}")
print(f"Item Size: {sale_amount.itemsize}")
print(f"Total Bytes: {sale_amount.nbytes}")
print(f"First 5 Elements: {sale_amount[:5]}")

# 10. Slice array of [Question 5, as - “2D array” based on array of [array of “Sale Amount”] and [array 
# of “Assessed Value”] ]
# Ensure the array has enough rows and columns
if two_d_array.shape[0] >= 7 and two_d_array.shape[1] >= 4:
    sliced_array = two_d_array[2:7, 1:4]
    print(sliced_array)
else:
    print("Array dimensions are insufficient for slicing.")



# 11. Slice array of [Question 5, as - “2D array” based on array of [array of “Assessed Value”] and 
# [array of “Assessed Value”] ]
# Create a 2D array by duplicating 'assessed_value'
assessed_value_2d = np.column_stack((assessed_value, assessed_value))

# Ensure the array has enough rows and columns
if assessed_value_2d.shape[0] >= 8 and assessed_value_2d.shape[1] >= 5:
    sliced_assessed_value = assessed_value_2d[1:8, 2:5]
    print(sliced_assessed_value)
else:
    print("Array dimensions are insufficient for slicing.")


# 12. Learn – what are geometric operation in NUMPY.
# np.sin , np.cos
# apply common 6 to - “2D array” based on array of [array of “Assessed Value”] and [array of 
# “Assessed Value”] , created in Question 5.
# Apply sine function
sin_values = np.sin(assessed_value_2d)
print("Sine Values:")
print(sin_values)

# Apply cosine function
cos_values = np.cos(assessed_value_2d)
print("Cosine Values:")
print(cos_values)
