# John Sweeney
# Eleventh Hour Games

# Version 1.0
# Go through list of orders, create list of people with completed orders


import csv

with open('1_ExportedOrderInformation.csv', 'r') as the_input, open('2_SanitizedOrderInformation.csv', 'w', newline='') as the_output:

    reader = csv.reader(the_input, skipinitialspace=True)
    writer = csv.writer(the_output, delimiter=',')

    writer.writerow(next(reader))

    for row in reader:
        order_status = row[0]
        if order_status == "wc-completed":
            writer.writerow(row)