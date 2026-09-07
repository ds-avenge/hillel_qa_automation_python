import csv
from pathlib import Path

# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv
base_path = Path(__file__).parent
file_1 = base_path / "random.csv"
file_2 = base_path / "random-michaels.csv"
result_file = base_path / "result_semkov.csv"

def read_csv(file_path):
    with open(file_path, 'r', newline="", encoding="utf-8") as file:
        return {tuple(row) for row in csv.reader(file)}

def remove_duplicates_from_csv(file1, file2, result):
    unique_rows = read_csv(file1) | read_csv(file2)

    with open(result, 'w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(unique_rows)

remove_duplicates_from_csv(file_1, file_2, result_file)
