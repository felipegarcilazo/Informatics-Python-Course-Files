# Problem 6.28
def translate(dictionary):
# Gets an input from user to input a phrase or words to be translated.
    word = input("Enter a phrase to be translated: ")
    word = word.split()
# Goes through each word and translates it to the associated translated word and
# if it can not find it in the dictionary then it will print _ for each
# character in the word.
    for i in range(len(word)):
        word[i] = dictionary.get(word[i], '_ ' * len(word[i]))
# Returns it back as a string.
    translated = ' '.join(word)
    return translated

# Problem 6.33
import random
def diceprob(r):
# This keeps track of the number of rolls and the number times r is rolled.
    rolls = 0
    rolled_r = 0
# Make sures it is between 2 and 12.
    if r > 12 or r < 2:
        return 'The value must be between 2 and 12'
# Stimulates dice being rolled and tracks until r is rolled 100 times.
    while rolled_r < 100:
        pair_roll = random.randrange(1, 7) + random.randrange(1,7)
        if pair_roll == r:
            rolled_r += 1
        rolls += 1
    return ('It took ' + str(rolls) + ' rolls to get ' + str(rolled_r) +
            ' rolls of ' + str(r))

