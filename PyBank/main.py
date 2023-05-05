import os
import csv
from datetime import datetime
budget_file = os.path.join( "Resources", "budget_data.csv")
budget_write = os.path.join("analysis", "Financial Analysis.txt")

#open and read csv
with open(budget_file) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip Header row
    next(csv_reader)    

    #List variables
    total_months = 0
    total_profit_losses = 0
    previous_profit_loss = 0
    profit_loss_changes = []
    max_increase = {"date": " ", "amount": 0}
    max_decrease = {"date": " ", "amount": 0}

    #Loop through the rows
    for row in csv_reader:
        date = datetime.strptime(row[0], '%b-%y')
        profit_loss = int(row[1])

        #update total months and total profit/loss
        total_months += 1
        total_profit_losses += profit_loss

        #calculate profit/loss change from previous month
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

            #define maximum increase and decrease
            if change > max_increase["amount"]:
                max_increase["date"] = date
                max_increase["amount"] = change
            elif change <max_decrease["amount"]:
                max_decrease["date"] = date
                max_decrease["amount"] = change

        #update the profit/loss
        previous_profit_loss = profit_loss

#calculate average profit/loss change
avg_profit_loss_change = sum(profit_loss_changes) / len(profit_loss_changes)

#Print to console
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Losses: ${total_profit_losses}")
print(f"Average Changes: ${avg_profit_loss_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase['date'].strftime('%b-%Y')} (${max_increase['amount']})") 
print(f"Greatest Decrease in Profits: {max_decrease['date'].strftime('%b-%y')} (${max_decrease['amount']})")
  
#Write to text file
with open(budget_write, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total Profit/Losses: ${total_profit_losses}\n")
    txtfile.write(f"Average Changes: ${avg_profit_loss_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_increase['date'].strftime('%b-%Y')} (${max_increase['amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_decrease['date'].strftime('%b-%y')} (${max_decrease['amount']})\n")
