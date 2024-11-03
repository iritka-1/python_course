def find_common_participants(first_group, second_group, de = ','):
    first_group = set(first_group.split(de))
    second_group = set(second_group.split(de))
    common_element = list(first_group.intersection(second_group))
    common_element.sort()
    return common_element





participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))