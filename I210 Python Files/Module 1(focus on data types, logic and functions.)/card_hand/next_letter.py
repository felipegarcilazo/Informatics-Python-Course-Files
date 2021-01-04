import cards

def make_hand(num):
    hand = []
    
    for i in range(num):
        new_card = cards.get_card()
        hand += new_card
    return hand

print(make_hand(5))
