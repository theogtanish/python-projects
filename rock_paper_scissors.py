import random

print("===================")
print("Rock Paper Scissors")
print("===================")

play_again = "yes"

while play_again == "yes" or play_again == "y":
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    player_choice = input("Choose your number (1-3): ")

    if player_choice != "1" and player_choice != "2" and player_choice != "3":
        print("Invalid choice! Please choose 1, 2, or 3.")
    else:
        computer_choice = str(random.randint(1, 3))

        if player_choice == "1":
            player_word = "Rock"
        elif player_choice == "2":
            player_word = "Paper"
        else:
            player_word = "Scissors"

        if computer_choice == "1":
            computer_word = "Rock"
        elif computer_choice == "2":
            computer_word = "Paper"
        else:
            computer_word = "Scissors"

        print("You chose:", player_word)
        print("Computer chose:", computer_word)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "1" and computer_choice == "3":
            print("You win!")
        elif player_choice == "2" and computer_choice == "1":
            print("You win!")
        elif player_choice == "3" and computer_choice == "2":
            print("You win!")
        else:
            print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()

print("Goodbye!")