import os
from pathlib import Path

# Setting terminal environment (useful for clearing the screen on some Macs)
os.environ["TERM"] = "xterm"

# I changed my absolute Mac path to a relative path so anyone downloading this can run it!
# It assumes there is a folder called 'Recetas' in the same directory as this script.
base_path = Path('Recetas')

print("Welcome to the Recipe Manager (Day 6 Project)!")
print(f"The path we are using is: {base_path.absolute()}")

# Counting all .txt files in the directory and subdirectories using glob
total_files = len(list(base_path.glob("**/*.txt")))
print(f"You currently have {total_files} recipes saved.")

def show_categories(path):
    # Iterate through the directory to find folders (categories)
    categories = []
    for folder in path.iterdir():
        if folder.is_dir():
            categories.append(folder.name)
    return categories

def choose_category(categories_list):
    choice = 0
    # Enumerate helps me print a numbered list starting from 1
    for index, folder in enumerate(categories_list, 1):
        print(f"{index} - {folder}")

    while choice not in categories_list:
        user_input = int(input("Choose a category (number): "))
        
        # Simple validation to avoid index out of range errors
        if 1 <= user_input <= len(categories_list):
            return categories_list[user_input - 1]
        else:
            print("Invalid number. Try again.")

def show_recipes(category_path):
    recipes_list = []
    # Using glob to find only text files inside the selected category
    for recipe in category_path.glob('*.txt'):
        recipes_list.append(recipe.name)
    return recipes_list

def choose_recipe(recipes_list):
    choice = 0
    for index, recipe in enumerate(recipes_list, 1):
        print(f"{index} - {recipe}")

    while choice not in recipes_list:
        user_input = int(input("Choose a recipe (number): "))

        if 1 <= user_input <= len(recipes_list):
            return recipes_list[user_input - 1]
        else:
            print("Invalid number.")

def read_recipe(recipe_path):
    # Pathlib makes it really easy to read file contents
    print(recipe_path.read_text())

def create_recipe(category_path):
    recipe_name = input("Enter a name for the new recipe: ")
    content = input("Type the recipe content: ")
    
    # Creating the new path and writing the file
    new_path = Path(category_path / (recipe_name + ".txt"))
    new_path.write_text(content)
    print("Recipe created successfully!")

def create_category(path):
    category_name = input("Enter the name of the new category: ")
    category_path = Path(path / category_name)
    category_path.mkdir()
    print("Category created!")

def delete_recipe(recipe_path):
    recipe_path.unlink()
    print(f"Recipe {recipe_path.name} deleted!")

def delete_category(category_path):
    category_path.rmdir()
    print(f"Category {category_path.name} deleted!")

# --- MAIN MENU LOOP ---
menu_option = 0

while menu_option != 6:
    # Clear the screen at the start of each loop
    os.system('clear')

    print("\n" + "*" * 20)
    print("RECIPE MENU")
    print("1. Read Recipe")
    print("2. Create Recipe")
    print("3. Create Category")
    print("4. Delete Recipe")
    print("5. Delete Category")
    print("6. Exit")
    print("*" * 20 + "\n")

    menu_option = int(input("Choose an option: "))

    if menu_option == 1:
        my_categories = show_categories(base_path)
        chosen_cat = choose_category(my_categories)
        chosen_cat_path = base_path / chosen_cat
        my_recipes = show_recipes(chosen_cat_path)

        # Bug fix: Check if the category is empty before trying to choose a recipe
        if len(my_recipes) < 1:
            print("\n❌ There are no recipes in this category yet.")
        else:
            chosen_rec = choose_recipe(my_recipes)
            chosen_rec_path = chosen_cat_path / chosen_rec
            read_recipe(chosen_rec_path)
            
        input("\nPress Enter to return to the main menu...")

    elif menu_option == 2:
        my_categories = show_categories(base_path)
        chosen_cat = choose_category(my_categories)
        chosen_cat_path = base_path / chosen_cat
        create_recipe(chosen_cat_path)
        input("\nPress Enter to return to the main menu...")

    elif menu_option == 3:
        create_category(base_path)
        input("\nPress Enter to return to the main menu...")

    elif menu_option == 4:
        my_categories = show_categories(base_path)
        chosen_cat = choose_category(my_categories)
        chosen_cat_path = base_path / chosen_cat
        my_recipes = show_recipes(chosen_cat_path)

        if len(my_recipes) < 1:
            print("\n❌ No recipes to delete in this category.")
        else:
            chosen_rec = choose_recipe(my_recipes)
            recipe_to_delete = chosen_cat_path / chosen_rec
            delete_recipe(recipe_to_delete)
            
        input("\nPress Enter to return to the main menu...")

    elif menu_option == 5:
        my_categories = show_categories(base_path)
        chosen_cat = choose_category(my_categories)
        chosen_cat_path = base_path / chosen_cat
        delete_category(chosen_cat_path)
        input("\nPress Enter to return to the main menu...")

    elif menu_option == 6:
        print("Closing the Recipe Manager. Bye!")
        break
