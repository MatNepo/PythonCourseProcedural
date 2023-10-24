from random import choice

HEADS = "Орел"
TAILS = "Решка"

coin = [HEADS, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    """Find the frequency for each count in counts that and return the "fairness" of the coin"""
    # create new list, filled with values from coin[], list has size of counts[count]
    coin_tosses = [choice(coin) for _ in range(count)]
    # count amount of HEADS | TAILS
    heads = len(list(filter(lambda item: item == HEADS, coin_tosses)))
    tails = len(list(filter(lambda item: item == TAILS, coin_tosses)))

    # fill new list with the "fairness" of the coins
    list_freq.append(min(heads, tails) / max(heads, tails))

print(list_freq)
