import csv
import os
import string
import numpy as np
import statistics

#IMPORT DATA####################################################
#read the csv
path_to_file=os.path.join(".","budget_data.csv")

#initialize lists
date=[]
profit_losses=[]

with open(path_to_file,newline="",encoding="utf8") as csvfile:
    data=csv.reader(csvfile, delimiter=',')

    for row in data:
        #write to lists
        date.append(row[0])
        profit_losses.append(row[1])


#MAIN###########################################################
print("Financial Analysis:")
print("---------------------")

#delete headers in each list
del date[0]
del profit_losses[0]

#TOTAL MONTHS
total_months=len(date)
print(f"Total Months: {total_months}")

#NET TOTAL PROFIT/LOSSES
#convert list of strings to ints
profit_losses_int=profit_losses
profit_losses_int = list(map(int, profit_losses_int))
#sum function of all integers in list
total_profit_losses=sum(profit_losses_int)
print(f"Total: ${total_profit_losses}")

#DIFFERENCE AVERAGES
all_diffs=np.diff(profit_losses_int)
diff_avg=np.mean(all_diffs)
print(f"Average Change: ${round(diff_avg,2)}")

#GREATEST INCREASE/DECREASE IN PROFITS

#find greatest increase value
greatest_inc=np.max(all_diffs)
#find greatest decrease value
lowest_inc=np.min(all_diffs)

#find date of greatest increase
month_max=date[list(all_diffs).index(greatest_inc)+1]
#find date of greatest decrease
month_min=date[list(all_diffs).index(lowest_inc)+1]

print(f"Greatest Increase in Profits: {month_max} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {month_min} (${lowest_inc})")


#EXPORT###########################################################

#lists to export
line1=["Total Months",total_months]
line2=["Total",total_profit_losses]
line3=["Average Change",round(diff_avg,2)]
line4=["Greatest Increase in Profits",f"{month_max}: ${greatest_inc}"]
line5=["Greatest Decrease in Profits",f"{month_min}: ${lowest_inc}"]

#combine all lines to 1
all_lines=zip(line1,line2,line3,line4,line5)

# save the output file path
output_file = os.path.join("financial_analysis.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerows(all_lines)
