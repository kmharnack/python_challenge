import os
import csv

csvpath = os.path.join('resources/election_data.csv')

totalVotes=0
candidateVotes = []
khanCount=0
correyCount=0
liCount=0
OtoolCount=0


with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    next(csvreader)
     
 
    for row in csvreader:
        totalVotes=totalVotes+1
        
        if row[2] == "Khan":
            khanCount += 1
        
        if row[2] == "Correy":
            correyCount += 1
        
        if row[2] == "Li":
            liCount += 1
        
        if row[2] == "O'Tooley":
            OtoolCount += 1
        
        totalCounts=[khanCount, correyCount,liCount,OtoolCount]            

winner=max(totalCounts)
if winner == khanCount:
    winner = "Khan"
if winner == correyCount:
    winner = "Correy"
if winner == liCount:
    winner = "Li"
if winner == OtoolCount:
    winner = "O'Tooley"


output=f'''
Election Results
 -------------------------
Total Votes: {totalVotes}
 -------------------------
 Khan: {(khanCount/totalVotes)*100:.3f}%  {khanCount}
 Correy: {(correyCount/totalVotes)*100:.3f}%  {correyCount}
 Li: {(liCount/totalVotes)*100:.3f}% {liCount}
 O'Tooley: {(OtoolCount/totalVotes)*100:.3f}% {OtoolCount}
 -------------------------
 Winner: {winner}
 -------------------------'''
print(output)

with open('analysis/pypoll_output.txt', 'w') as outputfile:
    outputfile.write(output)

