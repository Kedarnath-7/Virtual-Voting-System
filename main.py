import string
import secrets
import pandas as pd

print("Voting System")
print("===================")

actions = ["Voter ID Registration", "Voters list", "Vote", "Results", "Exit"]
actions_ask1 = ["Go Back to main menu", "Exit"]

Name = []
Age = []
Aadhar = []
Locality = []
Voters = []
Voted = []
Parties = ["NCP", "BJP", "TDP", "YSRCP", "JSP"]
NCP = 0
BJP = 0
TDP = 0
YSRCP = 0
JSP = 0

running = True

while running:
    print("\n")
    i = 0
    for action in actions:
        print(str(i + 1) + ".", actions[i])
        i += 1
    choice1 = int(input("Choose action: "))
    if choice1 == 1:
        print("\nRegistration")
        print("============")

        number = int(input("Enter no. of registrations: "))

        for n in range(0, number):
            age = int(input("Enter your AGE: "))
            if age < 18:
                print("YOU'RE NOT ELIGIBLE TO VOTE!!")
                continue
            Age.append(age)
            name = input("Enter your NAME: ")
            Name.append(name)
            aadhar = int(input("Enter your AADHAR NUMBER: "))
            proxy = 0
            for a in range(0, len(Aadhar)):
                if aadhar == Aadhar[a]:
                    print("ALREADY REGISTRATED!!")
                    proxy = 1
            if proxy == 1:
                Age.remove(Age[n])
                Name.remove(Name[n])
                continue
            Aadhar.append(aadhar)
            locality = input("Enter your LOCALITY: ")
            Locality.append(locality)
            S = 10
            voter_id_str = ''.join(secrets.choice(string.ascii_uppercase) for x in range(3))
            voter_id_num = ''.join(secrets.choice(string.digits) for x in range(7))
            voter_id = voter_id_str + voter_id_num
            Voters.append(str(voter_id))
            print("\nYOUR REGISTRATION IS SUCCESSFUL!!\n")
            print("Your Voter ID is: " + voter_id)
            print('\n"PLEASE NOTE DOWN YOUR VOTER ID!!"\n')

        voters_dict = {'Name': Name, 'Age': Age, 'Aadhar Number': Aadhar, 'Locality': Locality, 'Voter ID': Voters}
        label = []
        for j in range(1, len(Name) + 1):
            label.append(j)
        voters_list = pd.DataFrame(voters_dict, index=label)
        voters_data = pd.DataFrame(voters_dict, index=Voters)

        print("\n")

        k = 0
        for action in actions_ask1:
            print(str(k + 1) + ".", actions_ask1[k])
            k += 1
        # Input further action from user
        choice2 = int(input("Choose action: "))
        if choice2 == 1:
            continue
        elif choice2 == 2:
            running = False

        continue

    elif choice1 == 2:
        print("\nVoters list")
        print("===========")
        if len(Name) == 0:
            print("NO RECORDS FOUND!!")
            continue
        else:
            print(voters_list)
        continue

    elif choice1 == 3:
        print("\nVote")
        print("=====")

        ask_voter_id = input("Enter your VOTER ID: ")

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

        p = 0
        for p in range(len(Parties)):
            print(str(p + 1) + ".", Parties[p])

        user_vote = int(input("Choose your VOTE: "))

        print("\nTHANK YOU FOR VOTING, YOUR VOTE IS REGISTERED.")

        if user_vote == 1:
            NCP += 1
        elif user_vote == 2:
            BJP += 1
        elif user_vote == 3:
            TDP += 1
        elif user_vote == 4:
            YSRCP += 1
        elif user_vote == 5:
            JSP += 1

        Votes = [NCP, BJP, TDP, YSRCP, JSP]

        Votes_dict = {'Party': Parties, 'Votes': Votes}

        Votes_data = pd.DataFrame(Votes_dict)



    elif choice1 == 4:
        print("\nResults")
        print("=======")
        blankIndex = [''] * len(Votes_data)
        Votes_data.index = blankIndex
        print(Votes_data)

        continue

    elif choice1 == 5:
        running = False
