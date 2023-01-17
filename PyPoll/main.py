import os
import csv
import math

csvpath = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join("analysis", "results.out")
title = ("Election Results")

total_votes = 0
winner_votes = 0
winner = ""
candidates = {}

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] += 1
        total_votes += 1

output = title + "\n"
output += "---------------------\n"
output += "Total Votes: " + str(total_votes) + "\n"
output += "---------------------\n"

for candidate in candidates:
    output += candidate + ": " + format(candidates[candidate] / total_votes * 100, ".3f") + "% (" + str (candidates[candidate]) + ")\n"
    if (winner_votes < candidates[candidate]):
        winner_votes = candidates[candidate]
        winner = candidate
output += "---------------------\n"
output += "Winner: " + winner + "\n"
output += "---------------------\n"

print (output)
fo = open (output_file, "w")
fo.write (output)
fo.close()  