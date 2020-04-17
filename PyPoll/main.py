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
#print(tot_votes_cast)

#set command will make new list of all unique inputs

can_list = set(candidate)
can_or = sorted(can_list)
print(can_or)
# def unique(sequence):
#     seen = set(candidate)
#     return [x for x in sequence if not (x in seen or seen.add(x))]
#     print(x)

#can_list=set(candidate)
#print(can_list)
# candidate_1 = candidate[0]
# print(candidate_1)
# for row in candidate:
#     if row != str(candidate_1)
#     candidate_2 = row
#     print(candidate_2)