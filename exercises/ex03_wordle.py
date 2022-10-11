"""Ex03 - Wordle."""

__author__ = "730560370"


def contains_char(word: str, letter: str) -> bool: 
    """A function for searching a string for any given letter."""
    assert len(letter) == 1
    i: int = 0
    while i < len(word):
        if letter == word[i]:
            return True
        i += 1
    return False                        # checks that any given letter is or isn't somewhere in the program's word


def emojified(guess: str, word: str) -> str:
    """A function to represent correctly placed, wrongly placed, and incorrect letters, as emojis."""
    assert len(guess) == len(word) 
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"   
    white_box: str = "\U00002B1C"               # creating emojis
    i: int = 0
    result: str = ""                            # outputs emojis on the same line
    while i < len(word):
        if contains_char(word, guess[i]) is True:
            if word[i] == guess[i]: 
                result += green_box             # correct letter guess
            else: 
                result += yellow_box            # correct letter, wrong spot
        if contains_char(word, guess[i]) is False:
            result += white_box                 # incorrect letter
        i += 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompts for a user's guess, assures the guess is of the correct length."""
    guess = str(input(f"Enter a {expected_length} character word: "))
    while len(guess) != expected_length:
        guess = (input(f"That wasn't {expected_length} chars! Try again: "))    # ensures the program's word and the user's guess are of equal length
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    word: str = "codes"
    turn_number: int = 1
    correct_guess: bool = False
    while turn_number <= 6 and correct_guess is False:
        print(f"=== Turn {turn_number}/6 ===") 
        guess: str = (input_guess(len(word)))   # guess is of the correct length via input_guess function
        emojified(guess, word)                  # guess correctness is shown in emojis via emojified
        if guess == word:                      
            correct_guess = True
            print(f"You won in {turn_number}/6 turns!")
            return None                          # winning guess, end of program
        turn_number += 1
    if turn_number > 6 and correct_guess is False:  
        print("X/6 - Sorry, try again tomorrow!")
        return None                             # false guess, end of program


if __name__ == "__main__":                      # calls the main function and actually runs the program
    main()