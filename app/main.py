import csv
import os

from config import INPUT_FILE_PATH, TASK_CSV_FILE_NAME, SCHEDULE_CSV_FILE_NAME, OUTPUT_FILE_PATH, OUTPUT_CSV_FILE_NAME
from csv_reader import read_task_csv, read_schedule_csv 

# ファイルパスを適切なものに置き換えてください
schedule_header, schedule_data = read_schedule_csv(os.path.join(INPUT_FILE_PATH, SCHEDULE_CSV_FILE_NAME))
task_data = read_task_csv(os.path.join(INPUT_FILE_PATH, TASK_CSV_FILE_NAME))

output_path = os.path.join(OUTPUT_FILE_PATH, OUTPUT_CSV_FILE_NAME)
def calculate_schedule(schedule_header, schedule_data, task_data, output_path):
    return []

# 読み込んだデータの表示
for row in schedule_data:
    print(row)

# データの表示（確認用）
for task in task_data:
    print(task)
print(schedule_header)

