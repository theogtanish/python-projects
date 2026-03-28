import random

CHOICES = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}


def show_header() -> None:
    print("===================")
    print("Rock Paper Scissors")
    print("===================")
    print("1. ✊ Rock")
    print("2. ✋ Paper")
    print("3. ✌️ Scissors")


def get_player_choice() -> int:
    while True:
        raw = input("Choose your number (1-3): ").strip()
        if not raw.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        player_choice = int(raw)
        if player_choice in CHOICES:
            return player_choice

        print("Invalid choice! Please choose 1, 2, or 3.")


def decide_winner(player_choice: int, computer_choice: int) -> str:
    if player_choice == computer_choice:
        return "It's a tie!"

    winning_pairs = {(1, 3), (2, 1), (3, 2)}
    if (player_choice, computer_choice) in winning_pairs:
        return "You win!"

    return "Computer wins!"


def play_round() -> None:
    player_choice = get_player_choice()
    computer_choice = random.randint(1, 3)

    print(decide_winner(player_choice, computer_choice))
    print(
        f"You chose: {CHOICES[player_choice]} ({player_choice}), "
        f"Computer chose: {CHOICES[computer_choice]} ({computer_choice})"
    )


def play_again_prompt() -> bool:
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print("Please answer with yes/y or no/n.")


def main() -> None:
    show_header()

    while True:
        play_round()
        print("Thank you for playing!")

        if not play_again_prompt():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()