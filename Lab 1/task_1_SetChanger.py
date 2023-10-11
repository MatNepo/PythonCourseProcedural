# Lab_1: Replace None value with rms value and output renewed bunch

# Initial data
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# using filter to create a new bunch of numbers without None
numbers_without_none = [num for num in numbers if num is not None]

# rms value, round to 2 decimal places
rms_value = sum(numbers_without_none) / len(numbers)

# renew result using conditions
numbers = [num if num is not None else rms_value for num in numbers]

print("Измененный список:", numbers)
