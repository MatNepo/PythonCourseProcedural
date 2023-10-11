def insert(list_, value, index=0):

    # result = insert(list_, value, index)

    first_part = list_[:index]
    second_part = list_[index:]
    result = first_part + [value] + second_part

    return result


print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]
