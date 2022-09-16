"""EX03 - Structured Wordle - Now use loops and add more structure to the wordle."""

__author__ = "730616599"
from platform import python_branch

def contains_char(any_length: str, single_char: str) -> bool:
    """This function checks for the any of the characters of the long string matching that of the single string specified in the parameters"""
    assert len(single_char) == 1
    
    in_the_string: bool = False
    check: int = 0
    while in_the_string == False and check < len(any_length):
         
         if single_char == any_length[check]:
             in_the_string = True
         else:
             check = check + 1
    
    if in_the_string == True:
        return True
    else:
        return False         
            

            
def emojified(guess: str, secret: str) -> str:
    """This function will take two strings of equal length and return a string of emoji that represent which letters they share and how the locations correspond. """
    assert len(guess) == len(secret)
    emoji: str = ""
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while i < len(secret):
        if secret[i] == guess[i]:
            emoji = emoji + GREEN_BOX
            i = i + 1
        else:
            double_check: bool = contains_char(secret, guess[i])
            if double_check == True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
            i = i + 1
            
    return emoji
    
    
def input_guess(expected_length: int) -> str:
    """This function will use the input of the expected length to check the length of the string input until both are matched."""
    given_guess: str = input(f"Enter a {expected_length} character word: ")
    
    while expected_length != len(given_guess):
        given_guess = str(input(f"That wasn't {expected_length} chars! Try again: "))
    
    return given_guess
    
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    i: int = 0
    won: bool = False
    number_of_turns: int = 1
    
    while i < 6 and won == False:
        
        print(f"=== Turn {number_of_turns}/6 ===")
        new_guess: str = input_guess(5)
        new_emoji: str = emojified(new_guess, secret_word)
        print(new_emoji)
        
        if new_guess == secret_word:
            print(f"You won in {number_of_turns}/6 turns!")
            won = True
        else:
            i = i + 1
            number_of_turns = number_of_turns + 1
    if won == False:
        print("X/6 - Sorry, try again tomorrow!")
            
                
if __name__ == "__main__":
    main()

