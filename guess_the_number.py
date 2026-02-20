from random import randint # Importing specific function for better memory efficiency

# Configuration and initial state
# Using randint to generate a truly random number between 1 and 100
secret_number = randint(1, 100)
attempts_allowed = 8
attempts_count = 0

# User interaction: Setup phase
user_name = input("Hi! What is your name? ")
print(f"Well {user_name}, I am thinking of a number between 1 and 100.")
print(f"You have {attempts_allowed} attempts to guess it. Good luck!")

# Main game loop
while attempts_count < attempts_allowed:
    user_guess = int(input("\nEnter your guess: "))
    attempts_count += 1
    
    # Validation logic: Check if the guess is within the allowed range
    if user_guess < 1 or user_guess > 100:
        print("Out of bounds! Please stay between 1 and 100.")
    
    # Core game logic: Compare guess with secret number
    elif user_guess < secret_number:
        print("Incorrect! The secret number is higher.")
        
    elif user_guess > secret_number:
        print("Incorrect! The secret number is lower.")
        
    else:
        # Success condition: User guessed the right number
        print(f"Congratulations! You guessed it in {attempts_count} attempts.")
        break

# Game over condition: Triggers if the loop finishes without a 'break'
else:
    print(f"\nGame Over! You've reached the limit of {attempts_allowed} attempts.")
    print(f"The secret number was: {secret_number}")
