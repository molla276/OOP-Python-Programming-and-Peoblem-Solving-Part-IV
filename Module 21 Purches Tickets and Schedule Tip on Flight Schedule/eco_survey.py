import csv

with open('./data/economic-survey-of-manufacturing-june-2022-csv.csv','r') as f:
    lines = csv.reader(f)
    header = next(lines)
    for line in lines:
        print(line)
    print(header)