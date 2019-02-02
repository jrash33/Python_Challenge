import csv
import os
import numpy as np

#IMPORT DATA####################################################
#read the csv
path_to_file=os.path.join(".","election_data.csv")

#create lists to fill
voterid=[]
county=[]
candidate=[]

with open(path_to_file,newline="",encoding="utf8") as csvfile:
    data=csv.reader(csvfile, delimiter=',')

    for row in data:
        #write to lists
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#delete headers in each list
del voterid[0]
del county[0]
del candidate[0]

#MAIN###########################################################

#total number of votes cast
total_votes=len(voterid)

#array candidate names
names=np.unique(candidate)

#convert list to numpy array
candidate_array=np.asarray(candidate)

#initialize list of number of votes for each candidate
candidate_num=[]

print("ELECTION RESULTS:")
print(f"Total Votes: {total_votes}")
print("---------------------")

#for loop to output a summary of each candidate in the list
for i in range(len(names)):
    candidate_num.append(len(np.where(candidate_array == names[i])[0]))
    print(f"{names[i]}: {round(candidate_num[i]/total_votes*100,2)}% ({candidate_num[i]})")

print("---------------------")
#print winner
print(f"Winner: {names[candidate_num.index(np.max(candidate_num))]}")


#EXPORT###########################################################

#lists to export
votes=["Total Votes",total_votes,"","",""]
winner=["Winner",names[candidate_num.index(np.max(candidate_num))],"","",""]
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

