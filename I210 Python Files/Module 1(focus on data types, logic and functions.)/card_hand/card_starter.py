import cards

# this function creates num cards and sorts them into
# alphabetical order (so we can see multiples)
def make_hand(num):
    hand = []
    
    #fill in code here
    for i in range(num):
        new_card = cards.get_card()
        hand += new_card
    hand.sort()

    return hand

# A hand's value is 20 points for a pair (but not 3+ of a kind)
# + 5 points per Jack, Queen, or King,
# + 7 points per Ace.
def hand_value(my_cards):
    total = 0

    #fill in code here
    for letter in my_cards:
        my_cards.count(letter)
        if my_cards.count(letter) == 2:
            total += 10
        if  letter in ("J", "Q", "K"):
            total += 5
        if letter == "A":
            total += 7

    return total


#main - test code (don't change this!)
my_hand = make_hand(5)
print("The hand:", my_hand)
print("Its value:", hand_value(my_hand))
    
