import csv
import os

csvpath = os.path.join('..','PyBank','budget_data.csv')

with open(csvpath) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    month_delta = 0
    greatest_increase_month = ''
    greatest_decrease_month = ''
    greatest_increase_profit = 0
    greatest_decrease_profit = 0

    last_month_profit = 0
    last_month = ''
    total = 0
    total_month = 0
    total_change = 0
    for row in readCSV:
        if row[0] != 'Date':
            # print(row[0],row[1])
            current_month = row[0]
            current_profit = int(row[1])
            total += current_profit
            total_month += 1
            profit_change = current_profit - last_month_profit
            total_change += profit_change
           
            if profit_change > greatest_increase_profit:
                greatest_increase_profit = profit_change
                greatest_increase_month = current_month
            if profit_change < greatest_decrease_profit:
                greatest_decrease_profit = profit_change
                greatest_decrease_month = current_month
            last_month_profit = current_profit
            last_month = current_month
            
            
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Month:{total_month}")
    print(f"Total:{total}")               
    print(f"Average change:{total_change/(total_month-1)}")       
    print(f"Greatest Increase in Profits:{greatest_increase_month} ({greatest_increase_profit})")
    print(f"Greatest Decrease in Profits:{greatest_decrease_month} ({greatest_decrease_profit})")

   
    



  







