from random import sample


def get_unique_list_numbers() -> list[int]:
    """Fill the list with random values in the range of [-10;10]"""
    return sample(range(-10, 11), 15)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
