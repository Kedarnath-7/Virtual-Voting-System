# Importing necessary libraries
import secrets
import string
import tkinter as tk
from tkinter import *
import pandas as pd

# Header
print("Voting System")
print("===================")

# Lists of actions
actions = ["Voter ID Registration", "Voters list", "Vote", "Results", "Exit"]
actions_ask1 = ["Go Back to main menu", "Exit"]

# Creating empty lists
Name = []
Age = []
Aadhar = []
Locality = []
Voters = []
Voted = []

# Defining parties names and their initial votes to zero
Parties = ["NCP", "BJP", "TDP", "YSRCP", "JSP"]
NCP = 0
BJP = 0
TDP = 0
YSRCP = 0
JSP = 0

# Condition for running the loop
running = True

# Running loop
while running:
    print("\n")
    # Asking user to choose action
    i = 0
    for action in actions:
        print(str(i + 1) + ".", actions[i])
        i += 1
    choice1 = int(input("Choose action: "))

    # Registration
    if choice1 == 1:
        print("\nRegistration")
        print("============")

        number = int(input("Enter no. of registrations: "))

        for n in range(0, number):

            # Checking eligibility
            age = int(input("Enter your AGE: "))
            if age < 18:
                print("YOU'RE NOT ELIGIBLE TO VOTE!!")
                continue
            Age.append(age)
            name = input("Enter your NAME: ")
            Name.append(name)

            # Checking for proxy
            aadhar = int(input("Enter your AADHAR NUMBER: "))
            proxy = 0
            for a in range(0, len(Aadhar)):
                if aadhar == Aadhar[a]:
                    print("ALREADY REGISTERED!!")
                    proxy = 1
            if proxy == 1:
                Age.remove(Age[n])
                Name.remove(Name[n])
                continue
            Aadhar.append(aadhar)

            locality = input("Enter your LOCALITY: ")
            Locality.append(locality)

            # Generating and storing VOTER ID
            S = 10
            voter_id_str = ''.join(secrets.choice(string.ascii_uppercase) for x in range(3))
            voter_id_num = ''.join(secrets.choice(string.digits) for x in range(7))
            voter_id = voter_id_str + voter_id_num
            Voters.append(str(voter_id))
            print("\nYOUR REGISTRATION IS SUCCESSFUL!!\n")
            print("Your Voter ID is: " + voter_id)
            print('\n"PLEASE NOTE DOWN YOUR VOTER ID!!"\n')

        # Defining dictionary of voters data
        voters_dict = {'Name': Name, 'Age': Age, 'Aadhar Number': Aadhar, 'Locality': Locality, 'Voter ID': Voters}
        label = []
        for j in range(1, len(Name) + 1):
            label.append(j)

        # Defining DataFrame of voters data
        voters_list = pd.DataFrame(voters_dict, index=label)
        voters_data = pd.DataFrame(voters_dict, index=Voters)

        print("\n")

        # Input further action from user
        k = 0
        for action in actions_ask1:
            print(str(k + 1) + ".", actions_ask1[k])
            k += 1
        choice2 = int(input("Choose action: "))
        if choice2 == 1:
            continue
        elif choice2 == 2:
            running = False
        continue

    elif choice1 == 2:
        print("\nVoters list")
        print("===========")

        # Showing empty records
        if len(Name) == 0:
            print("NO RECORDS FOUND!!")
            continue
        else:
            print(voters_list)
        continue

    elif choice1 == 3:
        print("\nVote")
        print("=====")

        # Input Voter id from user
        ask_voter_id = input("Enter your VOTER ID: ")

        # Cross-checking from records
        check = 0
        status = 0
        for voter in Voters:
            if ask_voter_id == voters_data['Voter ID'][voter]:
                print("Your details:\n")
                print(voters_data.loc[voter])

            else:
                check += 1

        if check == len(Name):
            print("NO RECORDS FOUND!!")

        # Checking status of VOTE
        for z in range(0, len(Voted)):
            if ask_voter_id == Voted[z]:
                status = 1
                break
            else:
                status = 0

        if status == 0:
            print("\nStatus of VOTE: NOT VOTED\n")
            Voted.append(ask_voter_id)
        elif status == 1:
            print("\nStatus of VOTE: VOTED\n")
            continue

        # Create the main window
        window = tk.Tk()
        window.geometry("200x200")

        def show():
            label.config(text="You choose " + selected_option.get())

        # Defining a list of options
        options = ['NCP', 'BJP', 'TDP', 'JSP', 'YSRCP']

        # Creating a variable to store the selected option
        selected_option = tk.StringVar(window)

        # Setting the initial text
        selected_option.set("Choose your VOTE")

        # Creating the dropdown list
        dropdown = tk.OptionMenu(window, selected_option, *options)

        # Adding the dropdown list to the main window
        dropdown.pack()

        # Creating the submit button
        button = tk.Button(window, text = "VOTE", command = show)
        button.pack()

        # Creating Label
        label = Label(window, text=" ")
        label.pack()

        # Starting the main loop
        window.mainloop()
        Vote = selected_option.get()

        # Confirmation message
        print("\nTHANK YOU FOR VOTING, YOUR VOTE IS REGISTERED.")

        # Counting the votes
        if selected_option.get() == 'NCP':
            NCP += 1
        elif selected_option.get() == 'BJP':
            BJP += 1
        elif selected_option.get() == 'TDP':
            TDP += 1
        elif selected_option.get() == 'YSRCP':
            YSRCP += 1
        elif selected_option.get() == 'JSP':
            JSP += 1

        # Defining list, dictionary and dataframe of VOTES
        Votes = [NCP, BJP, TDP, YSRCP, JSP]

        Votes_dict = {'Party': Parties, 'Votes': Votes}

        Votes_data = pd.DataFrame(Votes_dict)

    elif choice1 == 4:

        # Showing the voting results
        print("\nResults")
        print("=======")
        blankIndex = [''] * len(Votes_data)
        Votes_data.index = blankIndex
        print(Votes_data)
        continue

    elif choice1 == 5:

        # Condition for stopping the loop
        running = False
