import csv
import os
import pandas as pd

#IMPORT DATA####################################################
#read the csv
path=os.path.join(".","budget_data.csv")

#import data as csv
data=pd.read_csv(path)

#MAIN###########################################################
print("Financial Analysis:")
print("---------------------")

#TOTAL MONTHS
total_months=data.shape[0]
print(f"Total Months: {total_months}")

#NET TOTAL PROFIT/LOSSES
#sum function of all integers in list
total_profit_losses=data["Profit/Losses"].sum()
print(f"Total: ${total_profit_losses}")

#DIFFERENCE AVERAGES
all_diffs=data['Profit/Losses']
all_diffs=all_diffs.diff()
diff_avg=all_diffs.mean()
print(f"Average Change: ${round(diff_avg,2)}")

#GREATEST INCREASE/DECREASE IN PROFITS

#find greatest increase value
greatest_inc=all_diffs.max()
#find greatest decrease value
lowest_inc=all_diffs.min()

#find date of greatest increase
date=data["Date"]
month_max=date[list(all_diffs).index(greatest_inc)]
#find date of greatest decrease
month_min=date[list(all_diffs).index(lowest_inc)]

print(f"Greatest Increase in Profits: {month_max} (${int(greatest_inc)})")
print(f"Greatest Decrease in Profits: {month_min} (${int(lowest_inc)})")

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

