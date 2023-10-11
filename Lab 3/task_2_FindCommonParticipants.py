def find_common_participants(first, second, separator=","):
    set_1 = set(first.split(separator))
    set_2 = set(second.split(separator))
    total_set = set_1.intersection(set_2)
    sorted_set = sorted(list(total_set))
    return sorted_set


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

final_list = find_common_participants(participants_first_group, participants_second_group, "|")
print("Общие участники:", final_list)