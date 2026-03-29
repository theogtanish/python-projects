import secrets
import string


def ask_yes_no(question):
    answer = input(question).strip().lower()
    return answer == "y" or answer == "yes"


def build_character_pool(use_letters, use_numbers, use_symbols):
    pool = ""

    if use_letters:
        pool += string.ascii_letters
    if use_numbers:
        pool += string.digits
    if use_symbols:
        pool += "!@#$%^&*()_+-=[]{}|;:,.?/"

    return pool


def generate_password(length, pool):
    password = ""
    for _ in range(length):
        password += secrets.choice(pool)
    return password


def main():
    print("====================")
    print("Password Generator")
    print("====================")

    try:
        length = int(input("Enter password length: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    if length <= 0:
        print("Length must be greater than 0.")
        return

    use_letters = ask_yes_no("Include letters? (y/n): ")
    use_numbers = ask_yes_no("Include numbers? (y/n): ")
    use_symbols = ask_yes_no("Include symbols? (y/n): ")

    pool = build_character_pool(use_letters, use_numbers, use_symbols)
    if not pool:
        print("You must include at least one character type.")
        return

    password = generate_password(length, pool)

    print("\nYour password is:")
    print(password)


if __name__ == "__main__":
    main()