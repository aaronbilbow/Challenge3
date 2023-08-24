import os
import csv

total_months=0
months = []
Total = []
Change = []


csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    # skip first row
    first_row = next(csvreader)
    total_months += 1
    prev_pl = int(first_row[1])
    Total += prev_pl

    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(i)
        month = row[0]
        months.append(month)
        total_months += 1 # total_months = total_months + 1

        Total.append(int(row[1]))
        # change = calc difference between current pl and prev_pl

        # add change to your list of changes

        # set prev_pl = int(row[1])
        
        Change.append(month)


print(f' Total Months {total_months}')
#print(f' Total Months {len(months)}')
print(f' Total $ {sum(Total)}')

