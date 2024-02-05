#Importing packages

import random as r

#Importing tabulate package for table format

from tabulate import tabulate 

#User puts number of desired ticket as input

num_tickets = int(input("How many tickets would you like? "))
print()
print("My {} Mega Millions ticket:".format(num_tickets))
print()

#Empty list to store tickets

tickets_data = []

#Constructing the loop for user input

for n in range(num_tickets):
    lottoNumbers = [] #initializing a empty list
    while len(lottoNumbers) < 5: 
        lottoNumber = r.randint(1, 76) #Random num generation
        if lottoNumber not in lottoNumbers: #Repeat check
            lottoNumbers.append(lottoNumber)
            
    #Generating random megaball number
            
    megaBallNumber = r.randint(1,25)

    #Sorting

    lottoNumbers.sort()

    tickets_data.append([n+1] + lottoNumbers + [megaBallNumber]) #

#Creating list with col names
    
col_heading = ['Ticket', 'Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5', 'Mega Ball']

#Display table: simple

print(tabulate(tickets_data, col_heading, tablefmt="simple"))




