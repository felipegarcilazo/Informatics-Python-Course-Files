txt_file = open('INFOcourses.txt', 'r')
contents = txt_file.readlines()
txt_file.close()
dictionary = {}
for line in contents:
    key, value = line.split(', ')
    dictionary[key] = value.strip()
print(dictionary)
while True:
    usr_input = input('What would you course would you like to see: ')
    if usr_input == 'stop':
        break
    print('this course is called', dictionary.get(usr_input, 'not a course'))

    
    










#scores = {"Dan": 125, "Abby": 100, "Carrie": 275, "Ben": 150}
#print("Current players:")

# How could we get this to print out without the [ ] and '' ?
#players = sorted(scores.keys())
#for name in players:
#    print(name, end = ' ')

# Ask the user for a name
#usr_name = input('\nPlease enter a Player Name: ')
#print('The score for', usr_name, scores.get(usr_name, 'not found'))







#python_words = {"string": "a sequence of characters", \
#                   "int": "a whole number (integer) "}

#add your code here
#while True:
#    key = input("What is the key: ")
#    if key == 'Stop':
#        break
#    if key not in python_words:
#        print('Not Found')
#        defin = input('What is the definition of the', key)
#        python_words[key] = defin
#    print('The definition of the', key, 'is', python_words[key])
