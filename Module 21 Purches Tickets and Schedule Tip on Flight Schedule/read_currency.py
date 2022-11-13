import csv

with open('./data/currencyrates.csv','r') as file:
    lines = csv.reader(file)
    for line in lines:
        if 'Bangladesh' in line[0]:
            line[2] = float(line[3]) * 50
            print(line)

with open('./data/currencyrates.csv','r') as file:
    lines = csv.reader(file)
    for line in lines:
        if 'Bangladesh' in line[0]:
            line[3] = float(line[2]) * 5000
            print(line)


# # import csv

# # with open('./data/currencyrates.csv','r') as file, open('./data/currencyrates_new.csv','w') as new_file:
# #     lines = csv.reader(file, delimiter=',')
# #     writer = csv.writer(new_file, delimiter=',')
# #     for line in lines:
# #         if 'Bangladesh' in line[0]:
# #             line[2] = float(line[3]) * 50
# #             writer.writerow(line)
# #             print(line)