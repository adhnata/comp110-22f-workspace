"""EX02 - One Shot Wordle - A little more in-depth version of Wordle."""

__author__ = "730616599"

from platform import python_branch


secret: str = "python"
word_guess: str = (input("What is your 6-letter guess? "))

while len(secret) != len(word_guess):
    word_guess = str(input("That was not 6 letters! Try again: "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""

in_the_word: bool = False
check: int = 0
i: int = 0
while i < 6:
    if secret[i] == word_guess[i]:
        emoji = emoji + GREEN_BOX
        i = i + 1
    else:
        while in_the_word == False and check < 6:
            
            if word_guess[i] == secret[check]:
                in_the_word = True
            else:
              check = check + 1
        
        if in_the_word == True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        
        i = i + 1
        
        
print(emoji)

if word_guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
    
