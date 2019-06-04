# John Sweeney
# Eleventh Hour Games

# Version 1.0
# Go through list of orders, create list of people entitled to t-shirts


import csv

with open('2_SanitizedOrderInformation.csv', 'r') as the_input, open('3_TshirtOrderInformation.csv', 'w', newline='') as the_output:

    reader = csv.reader(the_input, skipinitialspace=True)
    writer = csv.writer(the_output, delimiter=',')

    writer.writerow(next(reader))

    int_paid = 0

    for row in reader:
        amount_paid = row[12]
        int_paid = int(amount_paid)
        try:
            if int_paid > 150:
                writer.writerow(row)
        except ValueError:
            print(row)