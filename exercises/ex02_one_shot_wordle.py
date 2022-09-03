"""Ex02 - One Shot Wordle."""

__author__ = str(730560370)

word: str = "python"                           # the code is adjusted so any word of any length can be used
guess = str(input(f"What is your {len(word)}-letter guess? "))

while len(guess) != len(word):
    guess = str(input(f"That was not {len(word)} letters! Try again: "))   # so the length of the guess matches the length of the word    

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"                  # turning emojis into variables

index: int = 0 

letter_contained: bool = False
alternate_indeces: int = 0

correct_guesses: int = 0
final_result: str = ""                          # to keep track of the final output

while index < len(word):                        # tests if the given letter is in the correct position
    if word[index] == guess[index]:
        final_result += GREEN_BOX
        correct_guesses += 1
    else:
        alternate_indeces = 0
        while alternate_indeces < len(word):    # tests via loop if the given letter is contained at any index within the word
            if guess[index] == word[alternate_indeces]:   
                letter_contained = True
            alternate_indeces += 1
        if letter_contained:                    # prints if loop is True/if the given letter is contained in the word but not in the correct position
            final_result += YELLOW_BOX   
        if not letter_contained:                # if the letter is not contained in the word at all
            final_result += WHITE_BOX
    letter_contained = False                    # resets the bool, allows the nested loop to run again on the next index if needed
    index += 1                                  # avoids infinite outer loop

if (int(correct_guesses) == len(word)):
    print(final_result + "\nWoo! You got it!") 
else:
    print(final_result + "\nNot quite. Play again soon!")   # the end of the program