last_message = input("Please enter a message: ")
for i in range(len(last_message)):
    print(last_message[0:i+1])


message = input("Please enter a message: ")
lst_message = message.split(" ")
print("That message has", str(len(lst_message)), "words.")
longest_word = ""
for word in lst_message:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
        



# set up the mad lib with placeholders marked with "_"
mad_lib = """
In the book War of the _noun1_, the main character is an anonymous _occupation_
who records the arrival of _animals_ in _place_. Needless to say, havoc reigns as
the _animals_ continue to _verb_ everything in sight, until they are killed by
the common _noun2_.
"""

# get input from the user - tell them what it needs to be!

noun = input("Please enter a plural noun: ")
occupation = input("Please enter an occupation: ")
plural_animal = input("Please enter a plural word for an animal: ")
place = input("Please enter a place: ")
verb = input("Please enter a verb: ")
sec_noun = input("Please enter a second noun: ")

# replace all of the placeholders with user input.
# the first noun and the place need to have their
# first letters capitalized

noun_one = noun.title()
place = place.title()

mad_lib = mad_lib.replace("_noun1_", noun_one)
mad_lib = mad_lib.replace("_occupation_", occupation)
mad_lib = mad_lib.replace("_animals_", plural_animal)
mad_lib = mad_lib.replace("_place_", place)
mad_lib = mad_lib.replace("_verb_", verb)
mad_lib = mad_lib.replace("_noun2_", sec_noun)

# print the resulting mad lib
print("-" * 50)
print(mad_lib)
print("-" * 50)
