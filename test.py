# import csv

# with open('survey_results_public_mega_inc.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# gezellig


import csv
with open('survey_results_public_mega_inc.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)