import json

# TODO решите задачу
def task() -> float:
    values = []
    multis = []
    with open('input.json', 'r') as f:
        list_ = json.load(f)

    for i in range(len(list_)):
        for key, value in list_[i].items():
            values.append(value)

    for i in range(0, len(values), 2):

        if i + 1 < len(values):
            pair = round(values[i] * values[i + 1], 3)
            multis.append(pair)

    return sum(multis)







print(task())