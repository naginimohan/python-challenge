# Modules
import os
import csv

# Set path for file
budget_filePath = os.path.join( "Resources", "budget_data.csv")
# setting empty list and variables
months =[]
total = 0
net_Total =[]
revenue_change =[]
revenue_average = 0
greatest_profits = 0
least_profits = 0
date_monthList =[]
# Open the CSV using the UTF-8 encoding
with open(budget_filePath, encoding='UTF-8') as csvfile:     
    csvreader = csv.reader(csvfile, delimiter=",")
    #setting header
    header = next(csvreader)
    #iterating the rows
    for row in csvreader:
      # List of dates with months
      date_monthList.append(row[0])
      date_List = row[0].split("-")
      months.append(date_List[0])
      # List of profit/Losses
      net_Total.append(row[1])
      #calculating the total net profit
      total = total + int(row[1])
    for t in range(1,len(net_Total)):
     revenue_change.append((int(net_Total[t])-int(net_Total[t-1])))
    # calculate average revenue change
    revenue_average = round(sum(revenue_change) / len(revenue_change),2)
    #calculate  the maximum revenue change
    greatest_profits = max(revenue_change)
    # calculate the minimum revenue change
    least_profits = min(revenue_change)
#Printing the results in console
print("Financial Analysis")

print("....................................................................................")

print("Total months: " + str(len(months)))

print("Total: " + "$" + str(total))

print("Average change: " + "$" + str(revenue_average))

print("Greatest Increase in Profits: " + str(date_monthList[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_profits) +")")

print("Greatest Decrease in Profits: " + str(date_monthList[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(least_profits) +")")
#Adding the results to textfile by opening and writing into the file
file = open("output.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("...................................................................................." + "\n")

file.write("Total months: " + str(len(months)) + "\n")

file.write("Total: " + "$" + str(total) + "\n")

file.write("Average change: " + "$" + str(revenue_average) + "\n")

file.write("Greatest Increase in Profits: " + str(date_monthList[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_profits) + "\n")

file.write("Greatest Decrease in Profits: " + str(date_monthList[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(least_profits) + "\n")

file.close()
