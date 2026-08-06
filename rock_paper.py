import random

while True :
    user_choice =  input("rock , paper or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nyou: {user_choice}\ncomputer: {computer_choice}")

    if user_choice == computer_choice:
        print("tie!")
    elif(user_choice == "rock"  and computer_choice == "scissors") or(user_choice == "paper"  and computer_choice == "rock") or (user_choice == "scissors"  and computer_choice == "paper"):
        print(" you win")
    else:
        print("you lose")


    if input("play agin ? (y/n): ").lower() != "y":
        break