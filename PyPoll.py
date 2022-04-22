# The data we ned to retrieve
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

# Print the file object.
    #  print(election_data)

# To do: perform analysis.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 # Read and print the header row.
    headers = next(file_reader)
    print(headers)
 # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
#1. The total numer of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election basen on popular votes 
# Close the file.
# election_data.close()

# Using the open() function with the "w" mode we will write data to the file.

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
 # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson\n")
# Close the file
