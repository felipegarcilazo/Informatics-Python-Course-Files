import random
txt_file = open('top100moviesAFI.txt', 'r')
content = txt_file.readlines()
txt_file.close()
txt_file2 = open('top100moviesrt.txt', 'r')
content2 = txt_file2.readlines()
txt_file2.close()
num_movies = int(input("How many movies in your marathon? "))
list_movies = list(set(content) | set(content2))
random.shuffle(list_movies)
print("Your custom", num_movies, " movies marathon: ")

for i in range(num_movies):
    print(list_movies[i].strip())

    

#print("\tWelcome to 'Guess My Number'!\nI'm thinking of a number between 1 and",
#      "100.\nTry to guess it in as few attempts as possible.")
#comp_num = random.randrange(1, 101)
#counter = 0
#user_guess = random.randrange(1, 101)
#while True:
#    counter += 1
#    user_guess = int(input("Take a Guess: "))
#    if user_guess == comp_num:
#        print("You guessed it! The number was", comp_num, "\nAnd it only took"\
#              "you", counter, "tries!")
#        break
#    elif user_guess > comp_num:
#        print("Lower...")
#    else:
#        print("Higher...")
    





#txt_file = open('top100moviesAFI.txt', 'r')
#content = txt_file.readlines()
#txt_file.close()
#txt_file2 = open('top100moviesrt.txt', 'r')
#content2 = txt_file2.readlines()
#txt_file2.close()
#for i in range(len(content)):
#    content[i] = content[i].strip()
#for i in range(len(content2)):
#    content2[i] = content2[i].strip()
#print("The Movies on both lists are")
#for line in sorted(set(content) & set(content2)):
#      print(line)
