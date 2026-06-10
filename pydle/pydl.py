the_word = "wordl"

my_guess = input("guess: ")

if len(my_guess) == 5:
    print("checking guess...")
    for i in the_word:
        print(i)
else:
    print("invalid")