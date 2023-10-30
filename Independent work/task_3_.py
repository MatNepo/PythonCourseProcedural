def delete(list_, index=None):
    if index is None:
        index = -1
    elif index > len(list_):
        index = index % len(list_)

    if index < 0:  # этот блок рассматривается отдельно, а не в elif, т.к. нужно учесть index = None
        index = len(list_) + index
    return list_[:index] + list_[index + 1:]


print(delete([0, 1, 2], index=1))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
