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
