import random

def play_game():
    print("\n===== NUMBER GUESSING GAME =====")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too Low! Try Again.\n")

            elif guess > secret_number:
                print("Too High! Try Again.\n")

            else:
                print(f"\n🎉 Congratulations!")
                print(f"You guessed the correct number: {secret_number}")
                print(f"Attempts Taken: {attempts}")
                break

        except ValueError:
            print("Please enter a valid number.")

while True:
    play_game()

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != 'y':
        print("\nThanks for playing!")
        break