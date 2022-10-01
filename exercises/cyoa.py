"""Ex06 - CYOA. What's the point of living if I don't know what UNC building I am????"""

__author__ = "730560370"

from random import randint
player: str = ""
points: int = 0


def main() -> None:
    """The main function of the program. Calls the other functions into action."""
    global player
    global points
    if player == "":
        greet()
    else:
        print(f"\nWelcome back, {player}! Let's play again:")
    PARTY_HAT_EMOJI: str = "\U0001F973"
    BOOKS_EMOJI: str = "\U0001F4DA"
    BURGER_EMOJI: str = "\U0001F354"
    RUN_EMOJI: str = "\U0001F3C3"
    ART_EMOJI: str = "\U0001F3A8"
    q_1_ans: int = question_1()
    q_2_ans: int = question_2()
    q_3_ans: int = question_3()
    q_4_ans: int = question_4()
    q_5_ans: int = question_5()
    q_6_ans: int = question_6()
    q_7_ans: int = question_7()
    verdict: int = 0
    verdict = tracker(q_1_ans, q_2_ans, q_3_ans, q_4_ans, q_5_ans, q_6_ans, q_7_ans)
    print("==========\nThe results are in.....\n.....\n.....\n.....")
    if verdict == 1:
        print(f"You got Frat Court! {PARTY_HAT_EMOJI} {PARTY_HAT_EMOJI} {PARTY_HAT_EMOJI} It's not exactly a building but it's still an iconic part of campus :) This means you're social, exciting, and a party animal! Live it up!")
    elif verdict == 2:
        print(f"You got Wilson Library! {BOOKS_EMOJI} {BOOKS_EMOJI} {BOOKS_EMOJI} You're probably poised, refined, and love to study or read!")
    elif verdict == 3: 
        print(f"You got Chase Dining Hall! {BURGER_EMOJI} {BURGER_EMOJI} {BURGER_EMOJI} You're chill, probably southern, and your love language is spending quality time with someone else.")
    elif verdict == 4:
        print(f"You got Kenan Stadium! {RUN_EMOJI} {RUN_EMOJI} {RUN_EMOJI} You're healthy, active, and probably a gym bro. Gotta get those gains!")
    elif verdict == 5:
        print(f"You got Ackland Art Museum! {ART_EMOJI} {ART_EMOJI} {ART_EMOJI} You're creative, independent, and quirky. Maybe one day you'll be a celebrity artist!")
    points += 1
    play_again = str(input(f"\nYou've only done this quiz {points} time(s).\nWant to play again? Just type 'yes' for a redo!\n"))
    if play_again == "yes" or play_again == "Yes" or play_again == "YES":
        main()
    else:
        return
            

def greet() -> None:
    """A function that greets the user and asks for their name."""
    global player
    player = str(input("Welcome to the quiz! Today, we will determine which UNC building you are most similar to! What is your name? "))
    print(f"Hello, {player}! Nice to meet you! Let's begin:")
    return


def correctness(answer: int) -> int:
    """A function to make sure the user only enters in a single number for their answer."""
    i: int = 0
    while (answer < 1 or answer > 5) and i < 5:
        answer = int(input("Oops! Be sure to enter the number correlated with your answer choice. Try again: "))
        i += 1
    if i == 5:
        random_guess: int = randint(1, 5)
        print(f"\nCan't decide? We'll help you out :) Let's choose.... number {random_guess}!\n")
        return random_guess
    return answer


def question_1() -> int:
    """Question 1."""
    print("==========\nQuestion 1:\nWhich of the following is your favorite comfort activity?\nPlease respond with the number that correlates with your answer\n(1) Partying with friends\n(2) Reading a good book\n(3) Cooking healthy meals\n(4) Going for a run\n(5) Painting/Drawing")
    answer: int = int(input(""))
    correctness(answer)
    return answer


def question_2() -> int:
    """Question 2."""
    print("==========\nQuestion 2:\nChoose a dessert:\nPlease respond with the number that correlates with your answer\n(1) Birthday cake\n(2) Tiramisu\n(3) Pudding\n(4) Peanut butter protein balls\n(5) Rolled ice cream")
    answer: int = int(input(""))
    correctness(answer)
    return answer


def question_3() -> int:
    """Question 3."""
    print("==========\nQuestion 3:\nChoose your best strength:\nPlease respond with the number that correlates with your answer\n(1) Being social\n(2) Being prepared\n(3) Making good choices\n(4) Staying active\n(5) Being creative")
    answer: int = int(input(""))
    correctness(answer)
    return answer


def question_4() -> int:
    """Question 4."""
    print("==========\nQuestion 4:\nChoose a song:\nPlease respond with the number that correlates with your answer\n(1) Shots - LMFAO, Lil Jon\n(2) Nocturne Op. 9 No. 2 - Chopin\n(3) You Belong With Me - Taylor Swift\n(4) Jump Around - House of Pain\n(5) Hard to Believe - Wallows")
    answer: int = int(input(""))
    correctness(answer)
    return answer


def question_5() -> int:
    """Question 5."""
    print("==========\nQuestion 5:\nPick a color:\nPlease respond with the number that correlates with your answer\n(1) Dark Red\n(2) Forest Green\n(3) Yellow\n(4) Sky Blue\n(5) Orange")
    answer: int = int(input(""))
    correctness(answer)
    return answer


def question_6() -> int:
    """Question 6."""
    print("==========\nQuestion 6:\nChoose a bagel:\nPlease respond with the number that correlates with your answer\n(1) Everything\n(2) Sesame\n(3) Plain\n(4) Wheat\n(5) Rainbow")
    answer: int = int(input(""))
    correctness(answer)
    return answer


def question_7() -> int:
    """Question 7."""
    print("==========\nQuestion 7:\nChoose a field:\nPlease respond with the number that correlates with your answer\n(1) Business\n(2) English\n(3) Communications\n(4) Health Education\n(5) Art ")
    answer: int = int(input(""))
    correctness(answer)
    return answer


def tracker(a: int, b: int, c: int, d: int, e: int, f: int, g: int) -> int:
    """A place to keep track of which final answer is most like the user."""
    frat_court: int = 0
    wilson_library: int = 0
    chase_dining_hall: int = 0
    kenan_stadium: int = 0
    ackland_art_museum: int = 0
    if a == 1:
        frat_court += 1
    elif a == 2:
        wilson_library += 1
    elif a == 3:
        chase_dining_hall += 1
    elif a == 4:
        kenan_stadium += 1
    elif a == 5:
        ackland_art_museum += 1
   
    if b == 1:
        frat_court += 1
    elif b == 2:
        wilson_library += 1
    elif b == 3:
        chase_dining_hall += 1
    elif b == 4:
        kenan_stadium += 1
    elif b == 5:
        ackland_art_museum += 1
    
    if c == 1:
        frat_court += 1
    elif c == 2:
        wilson_library += 1
    elif c == 3:
        chase_dining_hall += 1
    elif c == 4:
        kenan_stadium += 1
    elif c == 5:
        ackland_art_museum += 1

    if d == 1:
        frat_court += 1
    elif d == 2:
        wilson_library += 1
    elif d == 3:
        chase_dining_hall += 1
    elif d == 4:
        kenan_stadium += 1
    elif d == 5:
        ackland_art_museum += 1

    if e == 1:
        frat_court += 1
    elif e == 2:
        wilson_library += 1
    elif e == 3:
        chase_dining_hall += 1
    elif e == 4:
        kenan_stadium += 1
    elif e == 5:
        ackland_art_museum += 1

    if f == 1:
        frat_court += 1
    elif f == 2:
        wilson_library += 1
    elif f == 3:
        chase_dining_hall += 1
    elif f == 4:
        kenan_stadium += 1
    elif f == 5:
        ackland_art_museum += 1

    if g == 1:
        frat_court += 1
    elif g == 2:
        wilson_library += 1
    elif g == 3:
        chase_dining_hall += 1
    elif g == 4:
        kenan_stadium += 1
    elif g == 5:
        ackland_art_museum += 1
 
    if frat_court >= wilson_library and frat_court >= chase_dining_hall and frat_court >= kenan_stadium and frat_court >= ackland_art_museum: 
        return 1
    if wilson_library >= frat_court and wilson_library >= chase_dining_hall and wilson_library >= kenan_stadium and wilson_library >= ackland_art_museum: 
        return 2
    if chase_dining_hall >= frat_court and chase_dining_hall >= wilson_library and chase_dining_hall >= kenan_stadium and chase_dining_hall >= ackland_art_museum: 
        return 3
    if kenan_stadium >= frat_court and kenan_stadium >= wilson_library and kenan_stadium >= chase_dining_hall and kenan_stadium >= ackland_art_museum: 
        return 4
    elif ackland_art_museum >= frat_court and ackland_art_museum >= wilson_library and ackland_art_museum >= chase_dining_hall and ackland_art_museum >= kenan_stadium: 
        return 5


if __name__ == "__main__":
    main()