from random import choice

# --- Configuration & State Initialization ---
word_list = ["manzana", "acemuk", "futbol", "pelota", "trofeo"]
secret_word = choice(word_list)

# Creating the hidden word representation (e.g., ['_', '_', '_'])
hidden_word = []
for n in secret_word:
    hidden_word.append("_")

# User's initial state
lives = 6
used_letters = []

# --- Main Game Loop ---
# The game continues as long as the user has lives and there are letters to guess
while lives >= 1 and "_" in hidden_word:
        
        # Prompt user for input and normalize to lowercase
        user_guess = input('\nIntroduzca una letra: ').lower()
        letter_found = False

        # Input Validation: Must be a single alphabetical character and not already guessed
        if len(user_guess) != 1 or not user_guess.isalpha() or user_guess in used_letters:
            print("Entrada inválida o letra ya usada. ¡Intenta de nuevo!")
            continue

        # Core Logic: Iterate through the secret word to find matches
        for index, letter in enumerate(secret_word):
            if letter == user_guess:
                hidden_word[index] = letter
                letter_found = True

        # State Update: Penalize if the letter was not found
        if not letter_found:
            lives -= 1
            
        used_letters.append(user_guess)
        
        # Display current game state
        print(" ".join(hidden_word))
        print(f"Vidas restantes: {lives}")
        print(f"Letras usadas: {used_letters}")

        # Win Condition Check
        if "_" not in hidden_word:
            print("\n🎉🎉🎉 ¡Ganaste el juego!!! 🎉🎉🎉")
            break

# Loss Condition: Triggers when the while loop finishes without a 'break'
else:
    print(f"\n💀💀💀💀 ¡Perdiste el juego!! La palabra era '{secret_word}' 💀💀💀")
