import csv
import json
from os import close

INPUT_FILENAME = "C:\Пользователи\win11\Downloads\input1.csv"
OUTPUT_FILENAME = "output.json"




def task() -> None:
    data = []
    with open(r"input.csv", 'r', encoding='utf-8') as f:
        x = csv.DictReader(f, delimiter=',', lineterminator='\n')

        for row in x:
            data.append(row)

    with open(OUTPUT_FILENAME, 'w') as f:
        json_data = json.dumps(data, indent= 4, ensure_ascii= False)
        f.write(json_data)

    return json_data




if __name__ == '__main__':
    task()
    # Нужно для проверки



    with open(OUTPUT_FILENAME,  mode = 'r') as output_f:
        for line in output_f:
            print(line, end="")