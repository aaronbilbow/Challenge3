import os
import csv


total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

csv_path = os.path.join('Resources', 'election_data.csv')
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    next(csvreader)
    for row in csvreader:
        candidate_name = row[2]
        total_votes += 1
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

candidate_percentages = {name: (votes / total_votes) * 100 for name, votes in candidates.items()}

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage:.3f}% ({candidates[candidate]})")
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

output_path = "election_analysis_results.txt"
with open(output_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, percentage in candidate_percentages.items():
        output_file.write(f"{candidate}: {percentage:.3f}% ({candidates[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-------------------------\n")

print("Analysis results have been printed and saved to 'election_analysis_results.txt'.")

