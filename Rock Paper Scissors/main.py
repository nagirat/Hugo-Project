import random #librari

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"] #list
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice} #dictionari
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer choice {computer}")
    if player == computer:
        return "it's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smash scissors, you win"
        else:
            return "paper cover rock, you lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper cover rock, you win"
        else:
            return "scissors cut paper, you lose"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cut paper, you win"
        else:
            return "rock smash scissors, you lose"
    

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
