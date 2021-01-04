# Problem 5.39
def exclamation(string):
    mod_string = ''
# Looks at every character and checks if it is a vowel and alters the message.
    for letter in string:
        mod_string += letter
        if letter in ('a', 'e', 'i', 'o', 'u'):
            mod_string += 3 * letter
# Adds the exclamation mark at the end of the sentence
    mod_string += '!'
    return mod_string


# Problem 5.43
def evenrow(twod_list):
    for j in twod_list:
# Loops inside of the loops to look at the rows and tracks the sum of the rows
        print(j)
        row_sum = 0
        for x in j:
            row_sum += x
# This says if the sum is odd then it will return false and end the for loop
# else it will return true once done with the loop as it found the sum for each
# loop to be even.
        if row_sum % 2 == 1:
            return False
    return True
