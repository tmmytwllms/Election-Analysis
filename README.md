# Election-Analysis
Repo for module 3 coursework and challenge.

# Pypoll Challenge 3 Analysis

## Resources
- Data source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Overview of Election Audit
This analysis added onto our previous code for an election audit. Inititially, a Colorado Board of Elections employee gave us these tasks to complete an election audit of a recent local congressional election.

The original code was created to:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

The added code calculates and returns:
1. The number of votes per county.
2. The county with the largest number of votes.
3. The county with the largest percentage of total votes. 
4. The largest county by name, number of votes, and percentage of total votes.

### Election-Audit Results by Candidate
The analysis of the election by candidate shows that:
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham receieved 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane receieved 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
  
### Election-Audit Results by County
The additional analysis of this election shows that:
- There were a total of 369,711 total votes cast in the election.
- The list of counties with votes and percentage of total votes were:
  - Jefferson:38,855 votes, 10.5% of total.
  - Denver: 306,055 votes, 82.8% of total.
  - Arapahoe: 24,801 votes, 6.7% of total.
-The county with the most votes was:
  -Denver, with 306,055 votes, which was 82.8% of the 369,711 total votes.
  
## Election-Audit Summary
This script was very useful in determining the number of counts per candidate and county, percentage of votes for candidate and county based on total votes, and determining the largest county and winning candidate by votes. This script could be use to county votes in virtually any local congressional election, regardless of the number of counties or candidates. 
With some refactoring, this code could also be used in regional, state, and country elections by adding additional lists and dictionaries for states, regions, and cities. This script can also be refactored to, if the data is provided, to give a breakdown of votes by party affiliation.
