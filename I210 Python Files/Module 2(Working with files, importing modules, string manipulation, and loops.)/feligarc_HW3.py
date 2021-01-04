import random

# Problem 3.44
def distance(time_elapse_sec):
    sound_meters = 3
    strike_dist = (time_elapse_sec * 340.29)/ 1000
    return strike_dist


# Random Cinema Problem
words = eval(input("Please enter a list of words['x', 'y', 'z']: "))
num_movie = int(input("Please enter a number of movies you'd like to generate: "
                      ))
print("Welcome to Randoplex! Currently playing movies are:")

def rand_cinema(lst_words, number):
    for i in range(number):
        print(random.choice(lst_words), random.choice(lst_words),
              random.choice(lst_words))

rand_cinema(words, num_movie)
