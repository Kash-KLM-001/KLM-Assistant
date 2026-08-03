import random
def rcp():
    klm_choice = random.randint(1,3)
    user = input('> ')
    if user == "rock" or user == "Rock" or user == "r":
        user = 1
    elif user == "paper" or user == "Paper" or user== "p":
        user = 2
    elif user == "scissors" or user == "Scissors" or user == "s":
        user = 3
    else:
        print("Invalid input")
    if klm_choice == user:
        return "tie"
    elif klm_choice == 1 and user == 2:
        print(f"KLM: Rock!\n{name}: Paper")
        return "win"
    elif klm_choice == 1 and user == 3:
        print(f"KLM: Rock!\n{name}: Scissors")
        return "lose"
    elif klm_choice == 2 and user == 1:
        print(f"KLM: Paper!\n{name}: Rock")
        return "lose"
    elif klm_choice == 2 and user == 3:
        print(f"KLM: Paper!\n{name}: Scissors")
        return "win"
    elif klm_choice == 3 and user == 1:
        print(f"KLM: Scissors!\n{name}: Rock")
        return "win"
    elif klm_choice == 3 and user == 2:
        print(f"KLM: Scissors!\n{name}: Rock")
        return "lose"