list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

even_counter = 0
odd_counter = 0

for index, value in enumerate(list_):
    if value % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

if even_counter > odd_counter:
    print("Четных чисел больше")
elif even_counter < odd_counter:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")
