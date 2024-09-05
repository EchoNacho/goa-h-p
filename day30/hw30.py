def print_even_index_numbers(numbers):
    # Slicing the list to get only the numbers at even indices
    even_index_numbers = numbers[::2]
    print(even_index_numbers)

def replace_games_with_languages(games_list):
    # List of programming languages to replace the game titles
    programming_languages = ["Python", "JavaScript", "Java", "C++", "Ruby"]

    # Replace game titles with programming languages
    new_list = programming_languages
    print(new_list)

def greet_user(name):
    print(f"Hello, {name}!")

# Example usage

# Task 1: Print numbers at even indices
numbers_list = [10, 20, 30, 40, 50, 60]
print_even_index_numbers(numbers_list)

# Task 2: Replace game titles with programming languages
games_list = ["Chess", "Monopoly", "Scrabble", "Uno", "Poker"]
replace_games_with_languages(games_list)

# Task 3: Greet the user
greet_user("Alice")