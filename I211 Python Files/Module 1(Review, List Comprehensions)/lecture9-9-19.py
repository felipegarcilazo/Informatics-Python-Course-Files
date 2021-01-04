##def valid_pass():
##    usr_pass = input("Please enter a password: ")
##    if len(valid_wrd) < 8:
##        print("That was not valid password, Please try again.")
##        usr_pass = valid_pass()
##    return usr_pass
##
##main
##my_pass = valid_pass()
##print("Your valid passsword is:", my_pass)


def num_counter(num_lst):
    dictionary = {}
    for num in num_lst:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1
    return dictionary

test1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 3, 10, 11, 12, 11, 13]
counts = num_counter(test1)
print("The List is:", test1)
print("Number:", "Count:", sep="\t")
for value in counts.items():
    print(value[0], value[1], sep="\t")



