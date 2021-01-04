users_info = []
for i in range(5):
    question = input("What is your name, age, and hometown? (ex. sam, 5, indy) ")
    name, age, hometown = question.split(sep=", ")
    users_info.append([age, name, hometown])
print("Name\tAge\tHometown\n" + ("-"*32))
users_info.sort()
for i in range(len(users_info)):
    print(users_info[i][1], "\t", users_info[i][0], "\t", users_info[i][2])
