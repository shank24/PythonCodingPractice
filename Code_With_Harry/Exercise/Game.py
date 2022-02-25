import random

print(f"welcome to this fun loving game STONE, PAPER and SCISSOR:")
print(f"Choose from the following list:\n1) st for Stone\n2) p for Paper\n3) sc for Scissor")

lst = ['st','p','sc']

Max_Limit = 10
Human_point = 0
Computer_point = 0
i = 1

while i <= Max_Limit:
    Human_choice = input(f"Enter your Choice number {i} :")
    Computer_choice = random.choice(lst)

    if Human_choice == 'st' and Computer_choice == 'p':
        Computer_point += 1

    elif Human_choice == 'st' and Computer_choice == 'sc':
        Human_point += 1

    elif Human_choice == 'p' and Computer_choice == 'sc':
        Computer_point += 1

    elif Human_choice == 'p' and Computer_choice == 'st':
        Human_point += 1

    elif Human_choice == 'sc' and Computer_choice == 'st':
        Computer_point += 1

    elif Human_choice == 'sc' and Computer_choice == 'p':
        Human_point += 1

    print(f"\ncomputer choice in round number {i} is {Computer_choice}")
    print(f"\n\nyour points after round {i} are {Human_point}\n and computer points are {Computer_point}")
    if Human_point > Computer_point:
        print(f"\nyou wins in this round")
    elif Computer_point > Human_point:
        print(f"\ncomputer wins in this round")
    else:
        print(f"\nRound tied")

    i = i+1

if Human_point > Computer_point:
        print(f"you wins with {Human_point} points")
elif Computer_point > Human_point:
    print(f"computer wins with {Computer_point} points")
else:
    print(f"Match Tied with Human has {Human_point} points and computer has {Computer_point} points")

