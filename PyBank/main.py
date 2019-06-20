
import csv

with open('/Users/heather/Downloads/03-Python_Homework_PyBank_Resources_budget_data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    months = []
    profits_losses = []
    monthly_net = []

    for row in csv_reader:
        months.append(str(row[0]))
        profits_losses.append(int(row[1]))

    for i in range(len(profits_losses) - 1):
        change = profits_losses[i + 1] - profits_losses[i]
        monthly_net.append(change)
        increase_month = row[0]
        decrease_month = row[0]

    total = sum(profits_losses)
    total_months = len(months)
    average_change = (sum(monthly_net)) / (len(monthly_net))

print('''Financial Analysis
----------------------''')

print("Total Months: " + str(total_months))

print("Total: $" + str(total.__format__(",")))

print("Average Change: $" + str(round(average_change, 2)))

print("Greatest Increase in Profits: $" + str(max(monthly_net)))

print("Greatest Decrease in Profits: $" + str(min(monthly_net)))
