# Lab_1: Replace None value with rms value and output renewed bunch

# Initial data
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# using filter to create a new bunch of numbers without None
numbers_without_none = [num for num in numbers if num is not None]

# rms value, round to 2 decimal places
average = round(sum(numbers_without_none) / (len(numbers)), 2)

# get index of None
index_of_none = numbers.index(None)
# renew result using the index
numbers[index_of_none] = average

print("Измененный список:", numbers)
