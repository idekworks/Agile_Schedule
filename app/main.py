import csv
import os

# CSVデータのパス
INPUT_FILE_PATH = './input_test_data'
OUTPUT_PATH = './output_data/'

TASK_CSV_FILE_NAME = 'task.csv'
SCHEDULE_CSV_FILE_NAME = 'schedule.csv'
OUTPUT_CSV_FILE_NAME = 'output.csv'

# Task CSVファイルの読み込み
def read_task_csv(file_path):
    task_data = []
    with open(os.path.join(INPUT_FILE_PATH, TASK_CSV_FILE_NAME), 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
        for row in csvreader:
            task_data.append({
                'PBI_ID': row['PBI_ID'],
                'PRE_TASK_ID': row['PRE_TASK_ID'] if row['PRE_TASK_ID'] != 'None' else None,
                'TASK_ID': row['TASK_ID'],
                'REQ_TIME': float(row['REQ_TIME']),
                'STREAM_NUM': int(row['STREAM_NUM'])
            })

    return task_data

# Task CSVファイルの読み込み
def read_schedule_csv(file_path):
    schedule_data = []
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        # ヘッダーをスキップ
        header = next(reader)
        
        for row in reader:
            time = row[0]
            values = [int(cell) for cell in row[1:]]
            schedule_data.append([time] + values)
    
    return header, schedule_data

# ファイルパスを適切なものに置き換えてください
header, schedule_data = read_schedule_csv(os.path.join(INPUT_FILE_PATH, SCHEDULE_CSV_FILE_NAME))
task_data = read_task_csv(os.path.join(INPUT_FILE_PATH, TASK_CSV_FILE_NAME))

# 読み込んだデータの表示
for row in schedule_data:
    print(row)


# データの表示（確認用）
for task in task_data:
    print(task)
print(header)

