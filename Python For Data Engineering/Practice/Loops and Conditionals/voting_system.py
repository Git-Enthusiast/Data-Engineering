print("Indian Voting System. Here You will have \
to Enter two candidate names and choose between them.\n")

cand_1 = input("Enter the name of the first Candidate: ")
cand_2 = input("Enter the name of the second Candidate: ")

print("\nSetup Completed. Voting Started!\n")

already_voted = []
cand_1_vote_count = 0
cand_2_vote_count = 0
valid_voters = [101, 102, 103, 104, 105, 106]

while len(already_voted) < len(valid_voters):
    try:
        voterId = int(input("Please Enter Your VoterID: "))
    except ValueError:
        print("Invalid input. Enter a number.\n")
        continue

    if voterId not in valid_voters:
        print("You are not a Valid Voter.\n")
        continue

    if voterId in already_voted:
        print("You already Voted.\n")
        continue

    print(f"1. for {cand_1}")
    print(f"2. for {cand_2}")
    
    while True:
        choice = input("Enter Your Choice: ")
        if choice == "1":
            cand_1_vote_count += 1
            print(f"You voted {cand_1}\n")
            break
        elif choice == "2":
            cand_2_vote_count += 1
            print(f"You voted {cand_2}\n")
            break
        else:
            print("Invalid Choice. Try again.")

    already_voted.append(voterId)

# Voting results
print("\nVoting Completed!\n")
print(f"Votes for {cand_1}: {cand_1_vote_count}")
print(f"Votes for {cand_2}: {cand_2_vote_count}")

if cand_1_vote_count == cand_2_vote_count:
    print("Equal Votes: Tie")
elif cand_1_vote_count > cand_2_vote_count:
    print(f"{cand_1} is the Winner.")
else:
    print(f"{cand_2} is the Winner.")