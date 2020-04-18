### PyPoll Analysis

#impor libraries to use
import csv
import pathlib


# Set path for locating csv file

csv_loc = pathlib.Path('Resources/election_data.csv')

# Create my lists to store data
voter_id=[]
county=[]
candidate =[]
can_list = []
winner = []
winner_state = []
# Open csv file and read
with open(csv_loc) as csv_file:
    csv_data = csv.reader(csv_file)

    #Use next command to skip header.  I did save in case needed later, but next is critical part of this
    csv_header = next(csv_data)

    for row in csv_data:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Calculate total votes, complete list, other request, etc... 
tot_votes_cast=len(voter_id)
print("'''text")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {tot_votes_cast} ")
print("-------------------------")
#set command will make new list of all unique inputs
can_list = set(candidate)
# use sorted command to give consistent order to list
can_ord = sorted(can_list)
## Recieved help from Hunter Carlisle on code below starting at can_vots ie. can_tallies
can_votes  = [0 for can in can_ord]  
can_per = [0 for can in can_ord]
# create loop to associate each candidate in list of candidates the index value my ordered candidate list
# tally votes each candidate by index
for can in candidate:
    can_ord_ind = can_ord.index(can)
    can_votes[can_ord_ind] += 1
    #Just for my own testing below
    #can_votes[can_ord_ind] = can_votes[can_ord_ind] + 1

## End help on first loop.

## Start help from Hunter Carlisle on second loop
# create loop to print out results and determine winner
for votes in can_votes:
    can_ord_ind_v=can_votes.index(votes)
    can = can_ord[can_ord_ind_v]
    can_perc = round(((votes/tot_votes_cast)* 100), 2)
    print(f'Candidate {can}: Recieved {can_perc}% of the vote with ({votes}) total votes')
## End help from Hunter Carlisle.   
    if votes == max(can_votes):
        winner.append(f'Winner: {can}')
print("-------------------------")
print(winner)
print("-------------------------")

# Create Output
output_path = pathlib.Path('Analysis/Results.txt') 

# Write output
with open(output_path, 'w') as output:
    output.write("'''text \n")
    output.write("Election Results \n")
    output.write("------------------------- \n")
    output.write(f"Total Votes: {tot_votes_cast}  \n")
    output.write("------------------------- \n")
    for votes in can_votes:
        can_ord_ind_v=can_votes.index(votes)
        can = can_ord[can_ord_ind_v]
        can_perc = round(((votes/tot_votes_cast)* 100), 2)
        output.write(f'Candidate {can}: Recieved {can_perc}% of the vote with ({votes}) total votes \n')
    output.write("------------------------- \n")
    output.write(f'{winner} \n')
    output.write("------------------------- \n")
    output.write("'''" )