"""EX06 - Create Your Own Adventure - Number Guessing Game"""

__author__ = "730616599"
 
from random import randint

points: int = 0
player: str = ""
NAMED_CONSTANT: str = "\U0000F642"
def main() -> None:
    """Main function for all other functions to interact in."""
    global points
    global player
    print(greet())
    play: str = input(f"Do you want to play, {player} Y or N:")
    while play == "Y":
        print(create_secret)
        print(guess_num(points, create_secret))
        play = input(f"Do you want to end the game or keep going {player} Y or N: ")
        if play == "N":
            print(f"Good Bye {NAMED_CONSTANT}, here's the number of tries you took so far: {points}")
        else:
            print(f"Here's the number of tries you tooks so far: {points}")
    
    return None


def greet() -> None:
    """Greeting function that offers context on porgram and records user name."""
    print("Hello, the objective of this game is to guess the random number in the least amount of tries.")
    global player
    
    player = input("What is your name?: ")
    
    return None

def create_secret() -> int:
    """Allows for player change secret integer."""
    secret: int = 0
    answer: str = input(f"Hey {player}, do you want to change the secret number? If you do, it counts as a guess. Y or N: ")
    smallest: int = 0
    biggest: int = 0
    global points
    if answer == "Y":
        smallest = input("Give me the smallest integer you'd use for the secret: ")
        biggest = input("Give me the biggest integer you'd use: ")
        secret = randint(smallest, biggest)
        points += 1
    
    if answer == "N":
        secret = randint(1, 10)
    
    return secret

def guess_num(playpoints: int, secguess: int) -> int:
    """Game part of the program. User guesses the secret integer."""
    answer: str = input(f"Hey {player} do you want to guess the number? Y or N: ")
    player_guess: int = 0
    
    if answer == "Y":
        player_guess = input("What is your integer guess?: ")
        if player_guess == secguess:
            playpoints += 1
            print(f"Congrats!!! {NAMED_CONSTANT} Here's how many tries it took: {playpoints}")
            return playpoints
        else:
            playpoints+= 1
            return playpoints
        
    if answer == "N":
        return playpoints

if __name__ == "__main__":
    main()
    