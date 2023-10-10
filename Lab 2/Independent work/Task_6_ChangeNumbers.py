list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Инициализируем переменные для индексов последнего максимального элемента и последнего элемента
max_index = None
last_index = len(list_numbers) - 1

# Ищем последний максимальный элемент и его индекс
for i, value in enumerate(list_numbers):
    if max_index is None or value >= list_numbers[max_index]:
        max_index = i

# Меняем местами последний максимальный и последний элементы
list_numbers[max_index], list_numbers[last_index] = list_numbers[last_index], list_numbers[max_index]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
