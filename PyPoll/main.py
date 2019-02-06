import csv
import os
import pandas as pd

#IMPORT DATA####################################################

#read the csv
path=os.path.join(".","election_data.csv")

#import data as csv
data=pd.read_csv(path)

#MAIN###########################################################

#total number of votes cast
total_votes=data.shape[0]                 

#array candidate names
names=data["Candidate"].unique()

print("ELECTION RESULTS:")
print(f"Total Votes: {total_votes}")
print("---------------------")

#number of votes for each candidate
candidate_num=data["Candidate"].value_counts()

#for loop to print out summary statistics
for i in range(len(names)):
    print(f"{names[i]}: {round(candidate_num[i]/total_votes*100,2)}% ({candidate_num[i]})")

print("---------------------")
#print winner
print(f"Winner: {candidate_num.idxmax()}")

#EXPORT###########################################################

#lists to export
votes=["Total Votes",total_votes,"","",""]
winner=["Winner",candidate_num.idxmax(),"","",""]
blank=["","","","",""]
line1=["Candidate Name"]
line2=["Vote Percentage"]
line3=["Number of Votes"]

for i in range(len(names)):
    line1.append(names[i])
    line2.append(f"{round(candidate_num[i]/total_votes*100,2)}%")
    line3.append(candidate_num[i])

#combine all lines to 1
all_lines=zip(votes,winner,blank,line1,line2,line3)


# save the output file path
output_file = os.path.join("election_results.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(all_lines)

