#Add dependencies
import csv
import os
#Assign variable to load file
file_to_load=os.path.join("resources","election_results.csv")
#Assign variable to save file
file_to_save=os.path.join("analysis","election_analysis.txt")

#Open results and read file
with open(file_to_load) as election_data:

        #to do: read and analyze data
        #Read the file object with reader function
        file_reader=csv.reader(election_data)

        #Print rows in CSV
        headers=next(file_reader)
        print(headers)