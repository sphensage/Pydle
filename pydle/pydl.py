### INITIALIZATION

import os
import vocab
import random
import time

def pick_word() -> str:
    rand_number = random.randint(1,100)
    the_word = vocab.word_list[rand_number]

    return the_word

def check_guess(wotd=str, guess=str) -> list:
    result = []
    
    for a, b in enumerate(guess, start=0):
        lt_wotd = list(wotd)
        has_looped = False
        start = True
        found = False
        count = 0
        i = 0
        e = 5

        while count < 5:
            count += 1
            if a == 0:
                if b == lt_wotd[0]: # If the starting guess letter is equal to the starting wotd letter
                    found = True
                    break
                elif b != lt_wotd[i]: # If the starting guess letter is equal to other wotd letter
                    e -= 1

            else:
                if (i+a) > 4 and not has_looped: # Check if i has already made it to 5
                    has_looped = True # Let it know that it has looped
                    i = 0 # Reset\

                if start and not has_looped and b == lt_wotd[i+a]:
                    found = True
                    start = False
                    break
                elif not has_looped and b != lt_wotd[i+a]:
                    e -= 1
                elif has_looped and b != lt_wotd[i]:
                    e -= 1

            i+=1
        
        if e == 5 and found:
            result.append(b)
        elif e > 0:
            result.append(b+"*")
        elif e == 0:
            result.append("#")
    
    return result

def win_check(wotd=list, guess=str) -> bool:
    str_wotd = ''.join(wotd)

    if str_wotd == guess:
        return True
    
def get_result(wotd=list) -> str:
    return ' '.join(wotd)
            
def init():
    wotd = pick_word().upper().strip()
    e = 0
    history = []

    while e < 6:
        os.system('cls')
        
        e += 1
        if e > 5:
            choice = input(f"You failed! The word was {wotd}\nTry again? [Y] [N]").upper().strip()
            if choice == "Y":
                history = []
                e = 0
            else: break
        else:
            print(f"ATTEMPT {e}\n=============")

            if e > 1:
                for i in history:
                    print(i)
                print("=============")

            my_guess = input("YOUR WORD: ").upper().strip()
            time.sleep(0.5)

            answer = check_guess(wotd, my_guess)
            result = get_result(answer)
            
            if len(my_guess) == 5:
                print("YOUR GUESS: ", end="")

                for i in my_guess:
                    letter = i.upper()
                    print(letter, end=" ")
                print("\n")

                print("checking...")
                time.sleep(1)
                print("")

                print("RESULT: "+ result, end="\n\n")
                history.append(result)

                if win_check(wotd, my_guess) == True:
                    print("You guessed the word correctly! :D")

                    choice = input("Try again? [Y] [N]").upper().strip()
                    if choice == "Y":
                        history = []
                        e = 0
                    else: break

                time.sleep(1)

            else:
                print("INVALID", end="\n\n")
                e -= 1
                input("Enter to continue")

### START

os.system('cls')
init()