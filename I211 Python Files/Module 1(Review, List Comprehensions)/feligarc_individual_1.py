# Felipe Garcilazo
# feligarc

## Question 2.
# Import the random module.
# Display a welcome message with instructions.
# Choose between fire, water, or grass which is the users choice.
# Choose a random option between fire, water, or grass that is assigned to the computer.
# Check if the user chose fire
## If the computer had fire then it is a tied
## If the computer had grass then the user won
## If the computer had water then the user lost
# Check if the user chose water
## If the computer had fire then the user won
## If the computer had grass then the user lost
## If the computer had water then it is a tied
# Check if the user chose grass
## If the computer had fire then the user lost
## If the computer had grass then it is a tied
## If the computer had water then the user won
# Display a message of the outcome of the match.

## Question 3
usr_inpt = input("Enter a string and it will duplicat the characters: ")
doubled_str = ''
for char in usr_inpt:
    doubled_str += char * 2
print("The doubled string is:", doubled_str)

## Question 4
def two_lists(list1, list2):
    items_ocr_bth = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                items_ocr_bth.append(item1)
    return items_ocr_bth

