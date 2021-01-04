## Felipe Garcilazo
## Team 15
## Question 1
secret = "mysterious".upper()
revealed_let = []
wrong_num = 0
while wrong_num < 6:
    guess = input("Guess a letter: ").upper()
    if guess in secret:
        revealed_let += guess
    else:
        wrong_num += 1
    empty_str = ''
    for let in secret:
        if let == guess:
            empty_str += let
        else:
            empty_str += "_"
    print("Placement of letter in word is", empty_str)
print("You have guessed the following correct letters:\n", revealed_let,
      "\nWith", wrong_num, "number of wrong guesses. While, the secret word being:", secret)

## Question 2
import random
poke_lst = ["fire", "water", "grass"]
usr_typ = input("Welcome to Pokemon. Select a type(Either fire, water, or grass):")
cpu_typ = random.choice(poke_lst)
if usr_typ == "fire":
    if cpu_typ == "fire":
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore it is a tied.")
    elif cpu_typ == "water":
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore you have lost the match.")
    else:
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore you have won the match.")
elif usr_typ == "water":
    if cpu_typ == "fire":
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore you have won the match.")
    elif cpu_typ == "water":
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore it is a tied.")
    else:
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore you have lost the match.")
else:
    if cpu_typ == "fire":
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore you have lost the match.")
    elif cpu_typ == "water":
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore you have won the match.")
    else:
        print("You chose", usr_typ, "vs.", cpu_typ + ". Therefore it is a tied.")
