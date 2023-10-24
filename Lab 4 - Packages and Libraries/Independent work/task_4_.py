from typing import List


def remove(list_: list[int], value: int) -> List:
    """Function finds and removes the most recent search value in the list"""
    try:
        index = len(list_) - list_[::-1].index(value) - 1  # go through the reverse list to find the last value
        list_.pop(index)
        return list_
    except ValueError:  # if no such a value -> exception
        raise ValueError(f"value {value} not found")


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
# print(remove([0, 1, 2, 3, 4], 12))  # ValueError
