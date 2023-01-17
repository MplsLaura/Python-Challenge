import os
import csv
import math


csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join("analysis", "results.out")
title = "Financial Analysis"

total_months = 0
total = 0
average_change= 0.00
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""
last_month_value = None
total_profit = 0
value_sum = []

print (os.path.basename(__file__))


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        
        total_months += int(1)
        month = row[0]
        value = int(row[1])
        total += int(value)
        if (last_month_value != None):
            profit = value - last_month_value
            total_profit += profit

            if greatest_increase < profit:
                greatest_increase = profit
                greatest_increase_date = month

            if greatest_decrease > profit:
                greatest_decrease = profit
                greatest_decrease_date = month
        last_month_value = value
    average_change = sum(value_sum)/85

    # The total number of months included in the dataset

    output = "Total Months: " + str(total_months) + "\n"
    # The net total amount of "Profit/Losses" over the entire period
    output += "Total: " + "$" + str(total) + "\n"
    # The values in "Profit/Losses" over the entire period, and then the average of those values
    output += "Average value: " + "$" + format(total_profit / (total_months - 1), ".2f") + "\n"
    # The greatest increase in profits (date and amount) over the entire period
    output += "Greatest Increase in Profits: " + greatest_increase_date + " " + "($" + str(greatest_increase) + ")" + "\n"
    # The greatest decrease in profits (date and amount) over the entire period
    output += "Greatest Decrease in Profits: " + greatest_decrease_date + " " + "($" +str(greatest_decrease) + ")" + "\n"

    print (output)
    fo = open (output_file, "w")
    fo.write (output)
    fo.close()