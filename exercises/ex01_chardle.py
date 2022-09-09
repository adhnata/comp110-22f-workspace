"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730616599"

num_match: int = 0
word_choice: str = str(input("Enter a 5-character word: "))


if int(len(word_choice)) > 5:
    print("Error: Word must contain 5 characters")
    exit()

if int(len(word_choice)) < 5:
    print("Error: Word must contain 5 characters")
    exit()

char_choice: str = str(input("Enter a single character: "))

if int(len(char_choice)) > 1:
    print("Error: Character must be a single character.")
    exit()

if int(len(char_choice)) < 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + char_choice + " in " + word_choice)

if char_choice == word_choice[0]:
    print(char_choice + " found at index 0")
    num_match = num_match + 1

if char_choice == word_choice[1]:
    print(char_choice + " found at index 1")
    num_match = num_match + 1

if char_choice == word_choice[2]:
    print(char_choice + " found at index 2")
    num_match = num_match + 1
    
if char_choice == word_choice[3]:
    print(char_choice + " found at index 3")
    num_match = num_match + 1
    
if char_choice == word_choice[4]:
    print(char_choice + " found at index 4")
    num_match = num_match + 1

if num_match ==  0:
    print("No instances of " + char_choice + " found in " + word_choice)

if num_match == 1:
    print(str(num_match) + " instance of " + char_choice + " found in " + word_choice)

if num_match == 2:
    print(str(num_match) + " instances of " + char_choice + " found in " + word_choice)

if num_match == 3:
    print(str(num_match) + " instances of " + char_choice + " found in " + word_choice)

if num_match == 4:
    print(str(num_match) + " instances of " + char_choice + " found in " + word_choice)

if num_match == 5:
    print(str(num_match) + " instances of " + char_choice + " found in " + word_choice)