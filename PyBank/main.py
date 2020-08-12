import os
import csv
import sys
csvpath = os.path.join('resources/budget_data.csv')

totalMonths=0
totalProfit=0.00
profit =0
increase = 0
greatestIncrease=""
decrease= sys.maxsize
greatestDecrease=""
change_values=[]


with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile)
    
    next(csvreader)
    row1=next(csvreader)
    totalProfit=totalProfit-float(row1[1])
    totalMonths+= 1
    previousMonth=float(row1[1])
    
    for row in csvreader:
        totalMonths=totalMonths+1
        
        profit=float(row[1])
        totalProfit=totalProfit+profit
        change= profit -previousMonth
        previousMonth=profit
        change_values.append(change)      
        
        if change > increase:
            increase = change
            greatestIncrease = row[0]
        if change < decrease:
            decrease = change
            greatestDecrease = row[0]
            
average_change=sum(change_values)/len(change_values)   
        
output= f'''
 Financial Analysis
 ----------------------------
    Total Months: ${totalMonths}
    Total: ${totalProfit:.0f}
    Average  Change: ${average_change:.2f}
    Greatest Increase in Profits: {greatestIncrease} (${increase:.0f})
    Greatest Decrease in Profits: {greatestDecrease} (${decrease:.0f})'''

print(output)

with open('analysis/pybank_output.txt', 'w') as outputfile:
    outputfile.write(output)