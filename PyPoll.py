# The data we ned to retrieve
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

# Print the file object.
    #  print(election_data)

# To do: perform analysis.

#1. The total numer of votes cast
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 # Read and print the header row.
    headers = next(file_reader)
    # print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
         candidate_name = row[2]
         total_votes += 1
         #2. A complete list of candidates who received votes
         # If the candidate does not match any existing candidate...
         if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
             # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
         candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]   
#3. The percentage of votes each candidate won
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          # Print each candidate, their voter count, and percentage to the terminal.
        # print(candidate_results)
# 

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
         # To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
# print(winning_candidate_summary)
# 3. Print the total votes.
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)


#4. The total number of votes each candidate won
#5. The winner of the election basen on popular votes 
# Close the file.
# election_data.close()

# Using the open() function with the "w" mode we will write data to the file.

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
 # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
# Write some data to the file.
#     txt_file.write('Election Results\n')
#     txt_file.write("-------------------------\n")
#     txt_file.write('Total Votes: ', total_votes)
#     txt_file.write("-------------------------\n")
#     txt_file.write(winning_candidate_summary)
#     txt_file.write("-------------------------\n")
# #  # Write three counties to the file.
#     txt_file.write("Arapahoe\nDenver\nJefferson\n")
# Close the file
