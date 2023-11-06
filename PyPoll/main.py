import os
import csv

# Set path for file
election_filePath = os.path.join( "Resources", "election_data.csv")

# setting empty list and variables
count = 0
candidate_list =[]
totalCandVotes =[]
votesByCandidates =[]
votepercentageByCandidate =[]
candicount =0

# Open the CSV using the UTF-8 encoding
with open(election_filePath, encoding='UTF-8') as csvfile:    
    csvreader = csv.reader(csvfile,delimiter = ",")
    #setting header
    csvheader = next(csvreader)
    for row in csvreader:
        count = count + 1
        totalCandVotes.append(row[2])
        if(row[2] not in candidate_list):
          candidate_list.append(row[2])
        candicount = len(candidate_list)  
        #print(candidate_list)
        #print(count)
    for c in candidate_list:
      votesByCandidates.append(totalCandVotes.count(c))
      #votepercentageByCandidate.append(round((totalCandVotes.count(c)/count)*100,2))  
      votepercentageByCandidate.append(totalCandVotes.count(c)/count)
    winnerIndex = votesByCandidates.index(max(votesByCandidates))    
    #print(votesByCandidates)
    #print(votepercentageByCandidate)
    #print(candidate_list[winnerIndex])

# Print the results to terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {count:,}")
print("----------------------------")
for k in range(0,candicount): 
  print(f"{candidate_list[k]}: {votepercentageByCandidate[k]:.3%} ({votesByCandidates[k]:,})")
print("----------------------------")
print(f"Winner: {candidate_list[winnerIndex]}")
print("----------------------------")
    

# Print the results to "PyPoll.txt" file
file = open("output.txt", "w")
file.write("Election Results" + "\n")
file.write("...................................................................................." + "\n")

file.write(f"Total Votes: {count:,}"+ "\n")

for k in range(0,candicount): 
  file.write(f"{candidate_list[k]}: {votepercentageByCandidate[k]:.3%} ({votesByCandidates[k]:,})" +'\n')
file.write("...................................................................................." + "\n")
file.write(f"Winner: {candidate_list[winnerIndex]}" +"\n")

file.write("----------------------------" + "\n")

file.close()

    
    
    