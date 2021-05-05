#Add dependencies
import csv
import os
#Assign variable to load file
file_to_load=os.path.join("resources","election_results.csv")
#Assign variable to save file
file_to_save=os.path.join("analysis","election_analysis.txt")
#Add vote counter variable
total_votes = 0
#create a candidate list variable
candidate_options = []
#create dictionary to hold candidate votes
candidate_votes={}
#create a variable to hold empy string for winning candidate
winning_candidate=""
#winning vote count variable
winning_count=0
#winning percentage variable
winning_percentage=0
#Open results and read file
with open(file_to_load) as election_data:

        #to do: read and analyze data
        #Read the file object with reader function
        file_reader=csv.reader(election_data)

        #Read header row
        headers=next(file_reader)
        
        #print rows in CSV
        for row in file_reader:
            #Add to total votes count
            total_votes += 1
            #print candidate name for each row
            candidate_name=row[2]
            #If candidate does not match any existing candidates
            if candidate_name not in candidate_options:
                #add it to the list of candidates
                candidate_options.append(candidate_name)
                #track candidate's vote count
                candidate_votes[candidate_name]=0
            #add votes for each candidate
            candidate_votes[candidate_name]+=1
            #determine % of votes each candidate received
            #go through candidate list
        for candidate_name in candidate_votes:
            #retrieve count for each candidate
            votes=candidate_votes[candidate_name]
            #calculate % of votes
            vote_percentage=float(votes)/float(total_votes)*100
            #to do: print out each candidates name, vote count, and percentage of votes
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #determine winning count and candidate
            #determing if votes is greater than winning count
            if (votes>winning_count) and (vote_percentage>winning_percentage):
                #if true, set winning_count = votes and winning_perecent = vote_percentage
                winning_count=votes
                winning_percentage=vote_percentage
                #set winning_candidate equal to candidates name
                winning_candidate=candidate_name
            winning_candidate_summary=(
                f"------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"------------------\n")
            print(winning_candidate_summary)