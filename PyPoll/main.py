import os
import csv

# path to read and write files
read_path = os.path.join('Resources', 'election_data.csv')
write_path = os.path.join('analysis', 'output.txt')

# creating and assigning variables needed for calculating 
candidate_dict = dict()
winner_perc = 0
winner_name =''
#opening csv file to parse and perform calculations
with open(read_path) as csvfile:
    # reading the file an assigning "," as the delimeter
    csvreader = csv.reader(csvfile, delimiter = ',')

    # getting rid of the header names
    csv_header = next(csvreader)

    # iterating over the file 
    for row in csvreader:
        #setting the candidate of the current row to a variable
        current_row_candidate = row[2]
        
        # if the candidate is not in the dictionary, make a new key with their name
        # and number of votes as the value for the dictionary
        if current_row_candidate not in candidate_dict.keys():
            candidate_dict[current_row_candidate] = 1
        else:
            candidate_dict[current_row_candidate] += 1
# count the number of total votes by adding all the values in the dictionary
total_votes = sum(candidate_dict.values())

# print the values in the format specified 
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

# iterate over the dictionary to print each candidate's results
for key, value in candidate_dict.items():
    
    #calculate the percentage of votes for each candidate
    percentage_of_votes = round(100 * (value / total_votes),3)
    
    # find the candidate with the highest percentage of votes 
    # and assign it to the winner_name variable
    if winner_perc < percentage_of_votes:
        winner_perc = percentage_of_votes
        winner_name = key
    print(f"{key}: {percentage_of_votes}% ({value})")
print("----------------------------")
print(f"Winner: {winner_name}")
print("----------------------------")


# export the calculated values to a txt file in the format specified
with open(write_path, "w") as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    
    # iterate over the dictionary to write each candidate's results
    for key, value in candidate_dict.items():
        percentage_of_votes = round(100 * (value / total_votes),3)
        txtfile.write(f"{key}: {percentage_of_votes}% ({value})")
        txtfile.write("\n")
    
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {winner_name}")
    txtfile.write("\n")
    txtfile.write("----------------------------")

    

