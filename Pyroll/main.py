
import os
import csv


csvpath = os.path.join('03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
with open(csvpath) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    total_votes = 0
    candidate_votes = {}
    for row in readCSV:
        if row[0] != 'Voter ID':
            total_votes += 1
            # print(row[0],row[1],row[2])
            if row[2] not in candidate_votes:
                candidate_votes[row[2]] = 0
            candidate_votes[row[2]] += 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for key, val in candidate_votes.items():
    percentage = val/total_votes
    print(f"{key} : {percentage:.3%} ({val})")
print("-------------------------")
winner_list = sorted(candidate_votes.items(), key=lambda x: x[1])[::-1]
winner = winner_list[0][0]
print(f"Winner: {winner}")
