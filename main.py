import random

print("Welcome to the Guessing Game!")

# Introduction
print("\nHello, human! Let's see if I can beat you to it... Are you ready? 😏")
print("Alright, think of a number between 1 and 100... but don't you dare tell me! 😈")
print("I'm going to try to guess it!")
print("Shall we begin?")

# Get user confirmation with proper input validation
while True:
    start = input("\nType 'yes' to begin or 'no' to chicken out🫢: ").strip().lower()

    if start == 'yes':
        break  # Proceed with the game if the user says 'yes'
    elif start == 'no':
        print("Aww, maybe next time then. I'll be here, waiting for you!...")
        exit()  # Exit the game if the user says 'no'
    else:
        print("Hmm, I didn't understand that. Please type 'yes' to start or 'no' to quit.")

# Game logic after confirmation    
low = 1
high = 100
correct = False
attempts = 0  # Track the number of attempts
    
for attempt in range(1, 6):  # Max 5 tries
    guess = random.randint(low, high)
    print(f"\nAttempt {attempt}: I think the number is {guess}.")
    
    response = input("Is that your number?🤔 (Respond with 'high', 'low', or 'correct'): ").strip().lower()

    attempts += 1  # Increment attempts after each try

    if response == "correct":
        print(f"\nYes! I won in {attempts} {'try' if attempts == 1 else 'tries'}! 🎉")
        correct = True
        break
    elif response == "low":
        low = guess + 1
    elif response == "high":
        high = guess - 1
    else:
        print("Hmm, I didn't understand that. Please say 'high', 'low', or 'correct'.")
        continue

# Final message if computer didn't guess correctly after 5 attempts 
if not correct:
    print(f"\nAw man, I couldn't guess it in {attempts} tries. Better luck next time! 😥")

# Ask for another round
while True:
    play_again = input("\nwanna give it another try? (yes/no): ").strip().lower()

    if play_again == 'yes':
        print("Starting a new game...")
        low = 1
        high = 100
        correct = False
        attempts = 0 # Reset attempts for new game
        for attempt in range(1, 6):
            guess = random.randint(low, high)
            print(f"\nAttempt {attempt}: I think the number is {guess}.")
            response = input("Is that your number?🤔 (Respond with 'high', 'low', or 'correct'): ").strip().lower()

            attempts += 1 # Increment attempts after each try

            if response == "correct":
                print(f"\nYes! I won in {attempts} {'try' if attempts == 1 else 'tries'}! 🎉")
                correct = True
                break
            elif response == "low":
                low = guess + 1
            elif response == "high":
                high = guess - 1
            else:
                print("Hmm, I didn't understand that. Please say 'high, 'low', or 'correct'.")
                continue
        # Final message if computer didn't guess correctly after 5 attempts
        if not correct:
            print(f"\nAw man, I couldn't guess it in {attempts} tries. Better luck next time! 😥")

        elif play_again == 'no':
            print("Thanks for playing! See you next time! 👋")
            exit() # Exit the game if the user doesn't want to play again
        else:
            print("Hmm, I didn't understand that. Please type 'yes' to play again or 'no' to quit.")
