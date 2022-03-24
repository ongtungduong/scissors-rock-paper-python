import random

def welcome_screen():
    print("Welcome to Scissors, Rock, Paper game")
    print("-------------------------------------")
    print("Press 0 to choose Scissors")
    print("Press 1 to choose Rock")
    print("Press 2 to choose Paper")
    print("Press 3 to Exit")
    print("-------------------------------------")

def play():
    computer = random.choice([0, 1, 2])
    result = player - computer
      
    if (player > 3):
        print("Wrong number, please read the instruction")
        print("-------------------------------------")
    else:
        selection = ["Scissors", "Rock", "Paper"]
        print(f"You choose {selection[player]}")
        print(f"Computer chooses {selection[computer]}")
        
        if ((result + 1) % 3 == 0):
            print("You lose")
            print("-------------------------------------")
            
        if ((result - 1) % 3 == 0):
            print("You win")
            print("-------------------------------------")
            
        if (result == 0):
            print("Draw")
            print("-------------------------------------")
        
        input("Press Enter to continue...")

while True:
    welcome_screen()
    print("Your selection is ")
    player = int(input())
    if (player == 3):
        print("Good bye")
        break  
    play()    