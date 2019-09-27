# Import Modules/Dependencies
import os
import csv


# Define Variables & Set Initial Values
Total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0


# Set Relative Path to CSV File
pypoll_csv = os.path.join('..', 'Data_Files','pypoll_election_data.csv')

# Open & Read CSV File with Specified Delimiter
with open(pypoll_csv, newline='', encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip Header Row when Reading CSV File
    csv_header = next(csvfile)

    # Read & Iterate Through Each Row of Data
    for row in csvreader:

        #Determine the Total Number of Votes
        Total_votes += 1

        #Determine the Total Number of Votes per Candidate
        if (row[2] == "Khan"):

            Khan_votes += 1

        elif (row[2] == "Correy"):

            Correy_votes += 1

        elif (row[2] == "Li"):

            Li_votes += 1

        elif (row[2] == "O'Tooley"):

            Otooley_votes += 1


#Determine the Percentage of Total Votes for Each Candidate
Khan_percentage = Khan_votes / Total_votes

Correy_percentage = Correy_votes / Total_votes

Li_percentage = Li_votes / Total_votes

Otooley_percentage = Otooley_votes / Total_votes


#Determine the Winning Candidate Based on Candidate with Max Number of Votes
Winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)

#Assign Winning Candidates Name to the Winner_name Variable
if Winner == Khan_votes:

    Winner_name = "Khan"

elif Winner == Correy_votes:

    Winner_name = "Correy"

elif Winner == Li_votes:

    Winner_name = "Li"

elif Winner == Otooley_votes:

    Winner_name = "O'tooley"


# Print Election Results Table in Terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {Total_votes}")
print("--------------------------\n")
print(f"Khan: {Khan_percentage:.3%} ({Khan_votes})")
print(f"Correy: {Correy_percentage:.3%} ({Correy_votes})")
print(f"Li: {Li_percentage:.3%} ({Li_votes})")
print(f"O'Tooley: {Otooley_percentage:.3%} ({Otooley_votes})\n")
print("--------------------------")
print(f"Winner: {Winner_name}")
print("--------------------------")


# Set Relative Path to Output Text File
output_file = os.path.join("..", "Output_Files", "Election_Results.text")

# Open and Write to Text File
with open(output_file, "w") as txtfile:

    # Write Election Results Table in Text File
    txtfile.write("Election Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Votes: {Total_votes}\n")
    txtfile.write("--------------------------\n\n")
    txtfile.write(f"Khan: {Khan_percentage:.3%} ({Khan_votes})\n")
    txtfile.write(f"Correy: {Correy_percentage:.3%} ({Correy_votes})\n")
    txtfile.write(f"Li: {Li_percentage:.3%} ({Li_votes})\n")
    txtfile.write(f"O'Tooley: {Otooley_percentage:.3%} ({Otooley_votes})\n\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Winner: {Winner_name}\n")
    txtfile.write("--------------------------")