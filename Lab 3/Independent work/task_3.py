def count(list_, char_):

    # counter = list_.count(char_)

    list_1 = list(list_)
    counter = 0
    for index in range(len(list_)):
        if char_ == list_1[index]:
            counter += 1

    return counter


list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
