import csv
import json

data = []

with open("data.csv") as file:
    csv_reader = csv.DictReader(file) 

    for line in csv_reader:
        data.append(line)

with open('data.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)