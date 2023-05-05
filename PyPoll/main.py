import os
import csv

#Set up the file path
file_path = os.path.join("Resources", "election_data.csv")
file_write= os.path.join("analysis", "election_results.txt")

#Setup variables
total_votes = 0
candidates = []
candidate_votes = {}

#Read CSV file
with open(file_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skip header
    header = next(csvreader)

    #Loop through each row
    for row in csvreader:

        #Sum of total numbers of votes
        total_votes += 1

        #Candidates name
        candidate_name = row[2]

        #Add the candidate to the list of candidates
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #Add candidates vote count
        candidate_votes[candidate_name] += 1

#print out results
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")
for candidate in candidates:
    percentage = round(candidate_votes[candidate] / total_votes * 100, 3)
    print(f"{candidate}: {percentage}% ({candidate_votes[candidate]})")
print("-------------------------")
winner= max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")

#Write to text file
with open(file_write, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")          
    txtfile.write("------------------------\n")
    for candidate in candidates:  
        percentage = round(candidate_votes[candidate] / total_votes * 100, 3)
        txtfile.write(f"{candidate}: {percentage}% ({candidate_votes[candidate]})\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("------------------------------\n")









