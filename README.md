# Python Logic Projects 🐍

Welcome to my learning journey! This repository contains small projects and exercises where I practice Python fundamentals.

## 🕹️ Project 1: Guess the Number Game
A classic interactive game where the computer thinks of a secret number and the user has limited attempts to find it.

### Key Learnings:
- **Control Flow:** Using `if/elif/else` for game logic.
- **Loops:** Implementing `while` loops for continuous gameplay.
- **Library Integration:** Using `randint` from the `random` module.
- **User Input:** Validating and processing data from the console.

### How to run:
```bash
python guess_the_number.py



#####################################################
PROJECT 2




## 🎮 Project 2: Hangman Game (El Ahorcado)
This is my own version of the classic Hangman game! The script chooses a random word from a list, and the player has 6 lives to guess it. 

I am really proud of this one because it has some cool logic inside.

### What I practiced in this project:
- **Input Validation:** I wrote a condition to check if the user types a real letter, and I also check if they already used that letter before. 
- **The `enumerate()` function:** I used this to find the exact position (index) of the letter inside the secret word.
- **Lists:** I used a list to keep track of the `used_letters` and to show the `hidden_word` with underscores (`_`).
- **While-Else loop:** A nice Python trick to print the "Game Over" message only if the loop finishes because you lost all your lives.



#####################################################
PROJECT 3


## 📁 Project 3: Recipe Manager (File Handling)
This was my first large script! It's a console-based application to manage text files representing recipes. I built this after learning how to open, edit, and close files in Python.

### What I practiced in this project:
- **`pathlib` & `os` modules:** I used these to navigate directories, create folders, and read/write `.txt` files. 
- **Relative Paths:** I learned to use relative paths instead of my local absolute path so the code works on any machine.
- **Handling empty states:** I added a bug fix to prevent the app from crashing if a user tries to read or delete a recipe from an empty category folder.
- **Functions:** I separated the logic into smaller functions (`show_categories`, `create_recipe`, etc.) to keep the main `while` loop clean.




#####################################################
PROJECT 4



# 🏦 OOP Banking System (Python)
This is the final project of Day 7 of my Python learning journey! 

Until now, I was writing simple scripts, but in this project, I leaped into **Object-Oriented Programming (OOP)**. It's a terminal-based banking app where I built my first classes and objects from scratch.

### Concepts I learned and applied:
- **Classes and Objects:** Creating blueprints for a `Person` and a `Customer`.
- **Inheritance (`super()`):** Passing the name attributes from the Person class down to the Customer class without repeating code.
- **Encapsulation:** Managing the account balance purely through internal methods (`deposit` and `withdraw`), keeping the logic secure.
- **Magic Methods:** Overriding the `__str__` method to create a nice, readable dashboard for the customer's account.
- **Terminal UI:** Integrating `os.system('clear')` and input pauses to make the console app actually usable and clean.

I'm really happy with how the architecture turned out. It was a great challenge to put all these new concepts together!
