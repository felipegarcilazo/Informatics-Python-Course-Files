import random

# This module allows you to generate random cards.

# When called, get_card returns a value that is one of the ranks
# a playing card could have.
def get_card():

    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    card = random.choice(ranks)

    return card
    
