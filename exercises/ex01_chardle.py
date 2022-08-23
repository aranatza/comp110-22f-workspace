"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730560370"

word = str(input("Enter a 5-character word: "))
if len(word) <= 4:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) >= 6:
    print("Error: Word must contain 5 characters")
    exit()

letter = str(input("Enter a single character: "))
if len(letter) == 0:
    print("Error: Character must be a single character.")
    exit()
if len(letter) >= 2:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word)
count = int(0)

if letter == word[0]:
    print(letter + " found at index 0")
    count = count + 1
if letter == word[1]:
    print(letter + " found at index 1")
    count = count + 1
if letter == word[2]:
    print(letter + " found at index 2") 
    count = count + 1
if letter == word[3]:
    print(letter + " found at index 3")
    count = count + 1
if letter == word[4]:
    print(letter + " found at index 4")
    count = count + 1  

if count == int(0):
    print("No instances of " + letter + " found in " + word)
else: 
    if count == int(1):
        print("1 instance of " + letter + " found in " + word)
    else:
        if count == int(2):
            print(str(count) + " instances of " + letter + " found in " + word)
        else: 
            if count == int(3):
                print(str(count) + " instances of " + letter + " found in " + word)
            else:
                if count == int(4):
                    print(str(count) + " instances of " + letter + " found in " + word)
                else:
                    if count == int(5):
                        print(str(count) + " instances of " + letter + " found in " + word)
                    else:
                        if count >= int(6):
                            print("Error.")