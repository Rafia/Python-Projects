import random

options = ['r', 'p', 's']
print("ROCK PAPER SCISSORS GAME"
      "\nType R, P or S"
      "\nLets Play")

while True:
    computer_choice = random.choice(options)
    user_choice = input("> ")

    print("You Chose:", user_choice,
          "Computer Chose:", computer_choice)

    if user_choice.lower() == computer_choice.lower():
        print("Its a tie...")

    elif user_choice.lower() == 'r':
        if computer_choice.lower() == 'p':
            print("Paper beats Rock"
                  "\nYou Lose")
        else:
            print("Rock beats Scissor"
                  "\nYou Won!!!")

    elif user_choice.lower() == 'p':
        if computer_choice.lower() == 'r':
            print("Rock beats Paper"
                  "\nYou Won!!!")
        else:
            print("Scissor cuts Paper"
                  "\nYou Lose")

    elif user_choice.lower() == 's':
        if computer_choice.lower() == 'p':
            print("Scissor cuts Paper"
                  "\nYou Win!!!")
        else:
            print("Rock beats Scissor"
                  "\nYou Lose")

    else:
        print("Wrong Value Entered")

    play = input("Continue (y/n): ")
    if play.lower() == 'y':
        continue
    else:
        print("Thanks for playing")
        break
