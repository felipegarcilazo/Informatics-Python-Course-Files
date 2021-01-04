##sum_inp = 0
##while True:
##    usr_inp = input("Please enter a number or Stop:")
##    if usr_inp.upper() == "STOP":
##        print("The Total Sum is:", sum_inp)
##        break
##    sum_inp += int(usr_inp)
##
##
##sum_inp = int(0)
##usr_inp = input("Please enter a number or Stop:")
##while usr_inp != "STOP":
##    sum_inp += int(usr_inp)
##    usr_inp = input("Please enter a number or Stop:")
##print("The Total Sum is:", sum_inp)

##even_lst = []
##odd_lst = []
##others = []
##for i in range(10):
##    usr_inp = eval(input("Please enter a number: "))
##    if usr_inp % 2 == 0:
##        even_lst.append(usr_inp)
##    elif usr_inp % 2 == 1:
##        odd_lst.append(usr_inp)
##    else:
##        others.append(usr_inp)
##print("The Results are:\nEvens:", even_lst, "\nOdds:", odd_lst, "\nOthers", others)

scores = {
    "Dave": 125,
    "Abby": 100,
    "Carrie": 275,
    "Ben": 150,
    }
print("Current Players:\n")
for name in sorted(scores.keys()):
    print(name, end=" ")
name = input("Please enter a Player Name: ")
print("The score for ", name, "is", scores.get(name, "not found")+".")
